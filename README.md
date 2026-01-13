# Teacher Evaluation Prediction using Concrete ML (Homomorphic Encryption)

## Project Overview
Privacy-preserving prediction of teacher performance using **Fully Homomorphic Encryption** via **Concrete ML**.  
We use synthetic educational data (teacher profiles, current semester assignments, students, and student feedback ratings) to train/predict overall teaching effectiveness without exposing sensitive data.

## Key Features & Constraints
- 5-year engineering programmes (Data Science, AI & ML, Software Systems)
- Teachers teach only within their assigned programme
- No teacher teaches multiple subjects to the same student year/batch
- Only even semesters active (II, IV, VI, VIII, X)
- Class sizes fixed per programme + year (50–60 students)
- Sensitive feedback ratings (Likert 1–5) — perfect for demonstrating HE privacy

## Dataset Files (in /data/)
- `teachers.csv` — Teacher profiles
- `subjects.csv` — Teaching assignments (current even semester)
- `students.csv` — Anonymized students (5 per class)
- `student_feedbacks.csv` — End-of-semester student ratings

## How to Generate/Reproduce the Data
Run the scripts in this order (in your virtual env):
1. `teachers_gen.py`
2. `subjects_gen.py`
3. `students_gen.py`
4. `student_feedbacks_gen.py`

## Next Steps / To-Do
- Exploratory Data Analysis → `/EDA/` folder (add notebooks soon)
- Data Preparation: Join tables → Features (teacher exp, ratings avg, etc.) + Target (Overall_Teaching_Effectiveness)
- Concrete ML Integration: Quantize model → Compile FHE circuit → Train/infer on encrypted feedback data
- Client-server simulation: Encrypt → Compute → Decrypt → Compare accuracy

## Tech Stack
- Python, Pandas (data gen)
- Concrete ML (homomorphic encryption & ML)