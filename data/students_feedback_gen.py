import pandas as pd
import random
from datetime import datetime, timedelta

# For reproducibility
random.seed(42)

# Read existing tables
teachers_df = pd.read_csv('teachers.csv')
subjects_df = pd.read_csv('subjects.csv')
students_df = pd.read_csv('students.csv')

# Merge subjects with student year and programme to match students
subjects_with_year = subjects_df[['Semester_ID', 'Subject_Code', 'Student_Year_Taught', 'Programme']].copy()

# Merge to find valid student-subject combinations
# Students can only give feedback for subjects in their own Programme and their current Student_Year
valid_combinations = pd.merge(
    students_df[['Student_ID', 'Student_Year', 'Programme']],
    subjects_with_year,
    left_on=['Student_Year', 'Programme'],
    right_on=['Student_Year_Taught', 'Programme'],
    how='inner'
)

# Columns for feedback table
feedback_columns = [
    'Feedback_ID', 'Subject_Code', 'Student_ID', 'Semester_ID',
    'Clarity_of_Explanation', 'Subject_Knowledge_of_Teacher', 'Engagement_in_Class',
    'Encouragement_of_Participation', 'Fairness_in_Grading', 'Timely_Feedback_on_Assignments',
    'Availability_for_Doubts_Outside_Class', 'Use_of_Teaching_Aids_Technology',
    'Classroom_Management', 'Pacing_of_Course', 'Relevance_of_Course_Material',
    'Encouragement_of_Critical_Thinking', 'Respectful_and_Inclusive_Environment',
    'Adjustment_to_Student_Confusion', 'Overall_Teaching_Effectiveness'
]

# Likert scale ratings (1-5)
ratings = [1, 2, 3, 4, 5]

# Generate realistic feedback: one row per student per subject they are taking this semester
feedback_data = []
feedback_id_counter = 1

for _, row in valid_combinations.iterrows():
    student_id = row['Student_ID']
    subject_code = row['Subject_Code']
    semester_id = row['Semester_ID']
    
    # Generate realistic ratings: slightly biased toward positive (common in student feedback)
    # Teachers with more experience tend to get slightly higher average ratings
    teacher_id = subjects_df.loc[subjects_df['Subject_Code'] == subject_code, 'Teacher_ID'].values[0]
    teacher_exp = teachers_df.loc[teachers_df['Teacher_ID'] == teacher_id, 'Years_of_Experience'].values[0]
    
    # Base rating shift based on experience (subtle effect)
    weights = [1, 2, 4, 8, 10]  # Heavily biased toward 4 and 5
    if teacher_exp > 15:
        weights = [1, 1, 3, 8, 12]  # Even more positive for very experienced
    elif teacher_exp < 5:
        weights = [2, 4, 6, 6, 4]   # Slightly lower for new teachers
    
    # Generate each rating
    clarity = random.choices(ratings, weights=weights, k=1)[0]
    knowledge = random.choices(ratings, weights=weights, k=1)[0]
    engagement = random.choices(ratings, weights=weights, k=1)[0]
    participation = random.choices(ratings, weights=weights, k=1)[0]
    fairness = random.choices(ratings, weights=weights, k=1)[0]
    timely_feedback = random.choices(ratings, weights=weights, k=1)[0]
    availability = random.choices(ratings, weights=weights, k=1)[0]
    tech_use = random.choices(ratings, weights=weights, k=1)[0]
    management = random.choices(ratings, weights=weights, k=1)[0]
    pacing = random.choices(ratings, weights=weights, k=1)[0]
    relevance = random.choices(ratings, weights=weights, k=1)[0]
    critical_thinking = random.choices(ratings, weights=weights, k=1)[0]
    inclusive = random.choices(ratings, weights=weights, k=1)[0]
    adjustment = random.choices(ratings, weights=weights, k=1)[0]
    overall = random.choices(ratings, weights=weights, k=1)[0]
    
    feedback_id = f"F{feedback_id_counter:04d}"
    
    feedback_data.append([
        feedback_id, subject_code, student_id, semester_id,
        clarity, knowledge, engagement, participation, fairness,
        timely_feedback, availability, tech_use, management,
        pacing, relevance, critical_thinking, inclusive,
        adjustment, overall
    ])
    
    feedback_id_counter += 1

# Create DataFrame
feedback_df = pd.DataFrame(feedback_data, columns=feedback_columns)

# Save to CSV
feedback_df.to_csv('student_feedbacks.csv', index=False)

# Display first 50 rows and summary
print("=== Student Feedbacks Generated ===")
print(f"Total feedback records: {len(feedback_df)}")
print("\nFirst 30 rows:")
print(feedback_df.head(30).to_string(index=False))

print("\nLast 10 rows:")
print(feedback_df.tail(10).to_string(index=False))

# Optional: Show average overall rating per teacher
print("\n=== Average Overall Teaching Effectiveness by Teacher ===")
feedback_with_teacher = feedback_df.merge(
    subjects_df[['Subject_Code', 'Teacher_ID']],
    on='Subject_Code'
).merge(
    teachers_df[['Teacher_ID', 'Teacher_Name']],
    on='Teacher_ID'
)
avg_rating = feedback_with_teacher.groupby(['Teacher_ID', 'Teacher_Name'])['Overall_Teaching_Effectiveness'].mean().round(2)
print(avg_rating.to_string())