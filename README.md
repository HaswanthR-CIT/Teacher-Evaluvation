# Teacher Evaluation Prediction using Concrete ML (Homomorphic Encryption)

**Objective**: Privacy-preserving prediction of teacher performance scores using Homomorphic Encryption (Concrete ML) on synthetic educational feedback data.

## Dataset Overview
- Synthetic data simulating a 5-year engineering program (even semesters only).
- Constraints enforced:
  - Teachers teach only within their assigned Programme.
  - No teacher teaches multiple subjects to the same student year/batch.
  - Fixed class sizes per programme/year (50-60).
  - Only even semesters active (II, IV, VI, VIII, X).

## Files
- `data/teachers.csv` — Teacher profiles
- `data/subjects.csv` — Current semester teaching assignments
- `data/students.csv` — Anonymized students
- `data/student_feedbacks.csv` — Student feedback ratings (sensitive data)

## How to Generate Data
Run the scripts in order:
1. teachers_gen.py
2. subjects_gen.py
3. students_gen.py
4. student_feedbacks_gen.py

Next: EDA in EDA/ folder → Concrete ML model training & encrypted inference.
