import numpy as np
import pickle
import sqlite3
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, session

# Import recommendation logic
from recommendation import generate_recommendation

app = Flask(__name__, template_folder="templates")
app.secret_key = "supersecretkey"


# ------------------ DATABASE INITIALIZATION ------------------ #
def init_db():
    conn = sqlite3.connect('career_lens.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            branch TEXT,
            career TEXT,
            company_type TEXT,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()


# ------------------ LOAD MODELS ------------------ #
model = pickle.load(open('model.pkl', 'rb'))
model1 = pickle.load(open('model1.pkl', 'rb'))


# ------------------ HOME ROUTES ------------------ #
@app.route('/')
def h():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def home():
    return render_template('index.html')


# ------------------ PREDICTION ROUTE ------------------ #
@app.route('/predict', methods=['GET'])
def predict():

    cgpa = request.args.get('cgpa', 0)
    projects = request.args.get('projects', 0)
    workshops = request.args.get('workshops', 0)
    mini_projects = request.args.get('mini_projects', 0)
    skills = request.args.get('skills', "")
    communication_skills = request.args.get('communication_skills', 0)
    internship = request.args.get('internship', 0)
    hackathon = request.args.get('hackathon', 0)
    tw_percentage = request.args.get('tw_percentage', 0)
    te_percentage = request.args.get('te_percentage', 0)
    backlogs = request.args.get('backlogs', 0)
    name = request.args.get('name', "Student")

    # Count skills
    s = skills.count(',') + 1 if skills else 0

    # Placement Prediction
    arr = np.array([cgpa, projects, workshops, mini_projects, s,
                    communication_skills, internship, hackathon,
                    tw_percentage, te_percentage, backlogs], dtype=float)

    output = model.predict([arr])[0]
    p = 1 if output == 'Placed' else 0

    # Salary Prediction
    arr1 = np.array([cgpa, projects, workshops, mini_projects, s,
                     communication_skills, internship, hackathon,
                     tw_percentage, te_percentage, backlogs, p], dtype=float)

    salary = model1.predict([arr1])[0]
    formatted_salary = "{:,.0f}".format(salary)

    if output == 'Placed':
        out = f'Congratulations {name} !! You have high chances of getting placed!!!'
        out2 = f'Your Expected Salary will be INR {formatted_salary} per annum'
    else:
        out = f'Sorry {name} !! You have low chances of getting placed. All the best!!!!'
        out2 = 'Improve your skills to increase placement chances.'

    return render_template('output.html', output=out, output2=out2)


# ------------------ RECOMMENDATION ROUTE ------------------ #
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():

    if request.method == 'POST':

        branch = request.form.get('branch')
        career = request.form.get('career')
        company_type = request.form.get('company_type')

        # Generate recommendations
        recommendations = generate_recommendation(
            branch,
            career,
            company_type
        )

        # ---------------- SAVE TO DATABASE ---------------- #
        conn = sqlite3.connect('career_lens.db')
        c = conn.cursor()

        c.execute('''
            INSERT INTO history (branch, career, company_type, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (branch, career, company_type, datetime.now()))

        conn.commit()
        conn.close()
        # -------------------------------------------------- #

        # Store in session (PRG pattern)
        session['recommendations'] = recommendations

        return redirect(url_for('recommend'))

    recommendations = session.pop('recommendations', None)

    return render_template(
        "recommendation.html",
        recommendations=recommendations
    )


# ------------------ HISTORY ROUTE ------------------ #
@app.route('/history')
def history():

    conn = sqlite3.connect('career_lens.db')
    c = conn.cursor()

    c.execute('''
        SELECT id, branch, career, company_type, timestamp
        FROM history
        ORDER BY id DESC
        LIMIT 10
    ''')

    records = c.fetchall()
    conn.close()

    return render_template('history.html', records=records)
@app.route('/delete/<int:record_id>')
def delete_record(record_id):

    conn = sqlite3.connect('career_lens.db')
    c = conn.cursor()

    c.execute("DELETE FROM history WHERE id = ?", (record_id,))

    conn.commit()
    conn.close()

    return redirect(url_for('history'))

# ------------------ RUN APP ------------------ #
if __name__ == "__main__":
    app.run()