def generate_recommendation(branch, career, company_type=None):

    recommendations = []

    # SOFTWARE PATH
    if career == "Software":

        recommendations.append("Master Data Structures and Algorithms")
        recommendations.append("Build 3-4 strong real-world projects")
        recommendations.append("Strong knowledge in Python or Java or C++")
        recommendations.append("Good understanding of DBMS, OS, and CN")
        recommendations.append("Stay Updated with Latest Tech Trends that needs in industry")
        if company_type == "Product":
            recommendations.append("LeetCode Rating Target: 1700+")
            recommendations.append("CodeChef Rating Target: 1500+")
            recommendations.append("Solve 400+ DSA problems")
            recommendations.append("Learn System Design Basics")
            recommendations.append("Participate in coding contests regularly")

        elif company_type == "Service":
            recommendations.append("Focus on Aptitude Preparation")
            recommendations.append("Prepare HR Interview Questions")
            recommendations.append("Practice basic coding questions")
            recommendations.append("Improve Communication Skills")

    # CORE PATH
    elif career == "Core":

        if branch == "ECE":
            recommendations.append("Focus on VLSI and Embedded Systems")
            recommendations.append("Learn MATLAB and PCB Design")
            recommendations.append("Strengthen Digital Electronics")

        elif branch == "EEE":
            recommendations.append("Power Systems and Electrical Machines")
            recommendations.append("Learn ETAP Software")
            recommendations.append("Understand Control Systems")

        elif branch == "MECH":
            recommendations.append("Learn CAD, SolidWorks, ANSYS")
            recommendations.append("Focus on Thermodynamics")
            recommendations.append("Understand Manufacturing Processes")

        elif branch == "CIVIL":
            recommendations.append("Learn AutoCAD and STAAD Pro")
            recommendations.append("Focus on Structural Engineering")
            recommendations.append("Understand Construction Planning")

        elif branch == "CSE":
            recommendations.append("Focus on Core CS Subjects (OS, DBMS, CN)")
            recommendations.append("Learn Backend Development")
            recommendations.append("Build System-Level Projects")
        elif branch == "CSE-AIML":
            recommendations.append("Focus on Machine Learning and AI Concepts And Advanced Technologies")
            recommendations.append("Learn Python Libraries (TensorFlow, PyTorch)")
            recommendations.append("Build AI/ML Projects")
        elif branch == "CSE-DS":
            recommendations.append("Focus on Data Science and Analytics")
            recommendations.append("Learn Python Libraries (Pandas, NumPy, Scikit-learn)")
            recommendations.append("Build Data Science Projects")
        elif branch == "CSE-IT":
            recommendations.append("Focus on Information Technology Concepts")
            recommendations.append("Learn Web Development and Cloud Computing")
            recommendations.append("Build IT Projects")
        elif branch == "CHEMICAL ENGINEERING":
            recommendations.append("Focus on Process Engineering")
            recommendations.append("Learn Aspen HYSYS Software")
            recommendations.append("Understand Chemical Reaction Engineering")
        elif branch == "MRB":
            recommendations.append("Focus on Material Science and Metallurgy")
            recommendations.append("Learn Material Testing Methods")
            recommendations.append("Understand Corrosion and Failure Analysis")
    return recommendations