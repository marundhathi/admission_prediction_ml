# Admission Prediction & University Recommendation System

A machine learning web application that predicts whether a student will be admitted to a graduate programme and recommends suitable universities based on their academic profile. Built with Python, Scikit-learn, and deployed as an interactive Streamlit app.

---

## What the App Does

A student enters their academic scores and the app instantly returns:
- **Admission outcome** — Admitted or Not Admitted
- **University recommendations** — a list of universities the student can realistically aim for based on their profile

---


## Input Features

| Feature | Description |
|---|---|
| GRE Score | Graduate Record Examination score |
| TOEFL Score | English proficiency test score |
| CGPA | Undergraduate GPA (10-point scale) |
| JEE Score | Joint Entrance Examination score |

---

## Models Used

| Model | Accuracy |
|---|---|
| Random Forest | 90–94% |
| Gradient Boosting | 90–94% |

Both models were trained and evaluated on 50,000+ student records. The best performing model is served in the Streamlit app.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Scikit-learn | ML model training and evaluation |
| Pandas | Data preprocessing |
| Streamlit | Web app deployment |
| Jupyter Notebook | Exploratory data analysis |

---


## Dataset

- 50,000+ student records
- Public / anonymised dummy dataset
- Features include GRE, TOEFL, CGPA, JEE scores and admission outcomes

---

## Key Learnings

- Handling imbalanced classification problems in admissions data
- Comparing ensemble methods (Random Forest vs Gradient Boosting) for prediction accuracy
- Building an end-to-end ML pipeline from raw data to deployed web app
- Designing a recommendation system based on score thresholds
- Deploying an interactive ML app using Streamlit

---

*Built during Data Analytics Internship at Techolas Technologies · 2025*
