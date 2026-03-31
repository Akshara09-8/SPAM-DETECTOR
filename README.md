# Spam Detection Project
## Student Information
**Name:** Akshara Sharma<br>
**Registration no:** 25BCE10666<br>

##  Course Information
**Course:** Fundamentals of AI and ML  
**Course Code:** CSA2001

##  Motivation

This project was developed as part of the **Bring Your Own Project (BYOP)** requirement for the *Fundamentals of AI and ML* course.

The goal of this assignment is to move beyond guided exercises and engage in real-world problem solving by:

- Identifying a meaningful problem from daily life, environment, or community
- Applying concepts, tools, and techniques learned during the course
- Designing and implementing a complete solution independently
- Demonstrating understanding through practical execution

This project reflects an effort to:
- Apply machine learning concepts in a practical setting  
- Build a complete end-to-end solution  
- Gain hands-on experience with real-world data and workflows  
- Strengthen problem-solving and implementation skills  

---

##  Approach

The project follows a structured machine learning workflow:

1. Data Collection  
2. Data Preprocessing  
3. Feature Extraction  
4. Model Training  
5. Model Evaluation  
6. Prediction / Testing  

---

##  Tech Stack

- Python<br>
- Scikit-learn<br> 
- Pandas<br>  
- NumPy<br>  
- Matplotlib / Seaborn (for visualization)<br>  

---
## Setup / Installation

- Download the code
Click Code → Download ZIP on GitHub, or clone the repository:

git clone https://github.com/your-username/your-repo-name.git

- Navigate to the project folder

cd your-repo-name

Install dependencies

- Make sure you have Python installed (Python 3.7+ recommended). Then install required packages:
pip install pandas numpy scikit-learn joblib
----

## How to Run
-Open your terminal in the project folder.
-Run the main script:
  python your_script_name.py

This will:

1.Train the model on sample messages.<br>
2.Test the model on a sample message.<br>
3.Print whether the test message is SPAM or HAM (Legit).<br>
4.You can also change the test_msg variable in the script to test your own messages.<br>

## Usage Example
Testing Message: 'Claim your free prize now by clicking here!'
Prediction: SPAM

## Files
- your_script_name.py — Main Python script that trains and tests the model.<br>
- spam_model.pkl — Saved Naive Bayes model (created after running the script).<br>
- vectorizer.pkl — Saved CountVectorizer (created after running the script).<br>
