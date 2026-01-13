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
subjects_with_year = subjects_df[['Semester_ID', 'Subject_Code', 'Student_Year_Taught', 'Programme', 'Teacher_ID']].copy()

# Merge to find valid student-subject combinations
# Students can only give feedback for subjects in their own Programme and their current Student_Year
valid_combinations = pd.merge(
    students_df[['Student_ID', 'Student_Year', 'Programme', 'Department', 'Gender']],
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

# Pre-assign traits to teachers for realism (randomly, but consistent per teacher)
# Traits: 'gender_bias' ('favor_girls', 'favor_boys', 'none')
# 'knowledge_style' ('strong_knowledge', 'weak_knowledge_good_teaching', 'none')
teacher_traits = {}
for teacher_id in teachers_df['Teacher_ID'].unique():
    gender_bias = random.choices(['favor_girls', 'favor_boys', 'none'], weights=[0.2, 0.2, 0.6], k=1)[0]
    knowledge_style = random.choices(['strong_knowledge', 'weak_knowledge_good_teaching', 'none'], weights=[0.3, 0.3, 0.4], k=1)[0]
    teacher_traits[teacher_id] = {'gender_bias': gender_bias, 'knowledge_style': knowledge_style}

# Generate realistic feedback: one row per student per subject they are taking this semester
feedback_data = []
feedback_id_counter = 1

for _, row in valid_combinations.iterrows():
    student_id = row['Student_ID']
    subject_code = row['Subject_Code']
    semester_id = row['Semester_ID']
    student_gender = row['Gender']
    
    # Get teacher details
    teacher_id = row['Teacher_ID']
    teacher_exp = teachers_df.loc[teachers_df['Teacher_ID'] == teacher_id, 'Years_of_Experience'].values[0]
    teacher_cert = teachers_df.loc[teachers_df['Teacher_ID'] == teacher_id, 'Certification_Status'].values[0]
    traits = teacher_traits[teacher_id]
    
    # Base weights: Heavily biased toward 4 and 5
    base_weights = [1, 2, 4, 8, 10]
    
    # Adjust for experience: Higher exp → more positive
    if teacher_exp > 15:
        base_weights = [1, 1, 3, 8, 12]  # Even more positive
    elif teacher_exp > 10:
        base_weights = [1, 2, 4, 9, 11]  # Slightly more positive
    elif teacher_exp < 5:
        base_weights = [2, 4, 6, 6, 4]   # Slightly lower
    
    # Adjust for certification: Certified → slight boost
    if teacher_cert == 'Certified':
        base_weights = [w * 0.8 if i < 3 else w * 1.2 for i, w in enumerate(base_weights, 1)]  # Reduce low, increase high
    
    # Group ratings into categories for realism
    # Teaching-related: Clarity, Engagement, Participation, Classroom_Management, Pacing, Encouragement_Critical_Thinking, Adjustment_Confusion
    # Knowledge-related: Subject_Knowledge, Relevance_Material
    # Fairness/Availability: Fairness_Grading, Timely_Feedback, Availability_Doubts
    # Tech/Inclusive: Use_Teaching_Aids, Respectful_Inclusive
    
    # Apply knowledge_style trait
    knowledge_weights = base_weights.copy()
    teaching_weights = base_weights.copy()
    if traits['knowledge_style'] == 'strong_knowledge':
        knowledge_weights = [w * 0.5 if i < 3 else w * 1.5 for i, w in enumerate(knowledge_weights, 1)]  # Boost knowledge
    elif traits['knowledge_style'] == 'weak_knowledge_good_teaching':
        knowledge_weights = [w * 1.5 if i < 3 else w * 0.5 for i, w in enumerate(knowledge_weights, 1)]  # Lower knowledge
        teaching_weights = [w * 0.5 if i < 3 else w * 1.5 for i, w in enumerate(teaching_weights, 1)]  # Boost teaching
    
    # Apply gender bias: Favor one gender by shifting weights
    if traits['gender_bias'] == 'favor_girls' and student_gender == 'Male':
        base_weights = [w * 1.2 if i < 3 else w * 0.8 for i, w in enumerate(base_weights, 1)]  # Slightly lower for boys
    elif traits['gender_bias'] == 'favor_boys' and student_gender == 'Female':
        base_weights = [w * 1.2 if i < 3 else w * 0.8 for i, w in enumerate(base_weights, 1)]  # Slightly lower for girls
    
    # Now generate ratings using appropriate weights
    # Teaching-related use teaching_weights
    clarity = random.choices(ratings, weights=teaching_weights, k=1)[0]  # Teaching
    engagement = random.choices(ratings, weights=teaching_weights, k=1)[0]  # Teaching
    participation = random.choices(ratings, weights=teaching_weights, k=1)[0]  # Teaching
    classroom_management = random.choices(ratings, weights=teaching_weights, k=1)[0]  # Teaching
    pacing = random.choices(ratings, weights=teaching_weights, k=1)[0]  # Teaching
    critical_thinking = random.choices(ratings, weights=teaching_weights, k=1)[0]  # Teaching
    adjustment = random.choices(ratings, weights=teaching_weights, k=1)[0]  # Teaching
    
    # Knowledge-related use knowledge_weights
    knowledge = random.choices(ratings, weights=knowledge_weights, k=1)[0]  # Knowledge
    relevance = random.choices(ratings, weights=knowledge_weights, k=1)[0]  # Knowledge
    
    # Fairness/Availability use base_weights (general)
    fairness = random.choices(ratings, weights=base_weights, k=1)[0]
    timely_feedback = random.choices(ratings, weights=base_weights, k=1)[0]
    availability = random.choices(ratings, weights=base_weights, k=1)[0]
    
    # Tech/Inclusive use base_weights (could be influenced by modern teaching)
    tech_use = random.choices(ratings, weights=base_weights, k=1)[0]
    inclusive = random.choices(ratings, weights=base_weights, k=1)[0]
    
    # Compute Overall_Teaching_Effectiveness logically: Average of all other ratings, rounded to nearest 1-5, with small random variation (±0.5)
    all_ratings = [clarity, knowledge, engagement, participation, fairness, timely_feedback, availability, tech_use,
                   classroom_management, pacing, relevance, critical_thinking, inclusive, adjustment]
    avg_rating = sum(all_ratings) / len(all_ratings)
    variation = random.uniform(-0.5, 0.5)  # Small noise for realism (students' holistic view may differ slightly)
    overall_raw = avg_rating + variation
    overall = max(1, min(5, round(overall_raw)))  # Clamp to 1-5
    
    feedback_id = f"F{feedback_id_counter:04d}"
    
    feedback_data.append([
        feedback_id, subject_code, student_id, semester_id,
        clarity, knowledge, engagement, participation, fairness,
        timely_feedback, availability, tech_use, classroom_management,
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