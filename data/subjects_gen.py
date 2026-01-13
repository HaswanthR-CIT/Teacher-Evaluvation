import pandas as pd
import random

# For reproducibility
random.seed(42)

# Read teachers.csv (assume it exists from previous generation)
teachers_df = pd.read_csv('teachers.csv')

# Extract unique programmes from teachers
programmes = teachers_df['Programme'].unique()

# Group teachers by programme
teachers_by_programme = teachers_df.groupby('Programme')['Teacher_ID'].apply(list).to_dict()

# Fixed even semesters mapping
year_to_sem = {
    '1st Year': 'II',
    '2nd Year': 'IV',
    '3rd Year': 'VI',
    '4th Year': 'VIII',
    '5th Year': 'X'
}
student_years = list(year_to_sem.keys())

# Realistic subject names by programme
subject_names = {
    'Data Science': [
        'Introduction to Data Science', 'Statistics for Data Analysis', 'Python Programming',
        'Machine Learning Basics', 'Data Visualization', 'Big Data Technologies',
        'Advanced Machine Learning', 'Deep Learning', 'Natural Language Processing',
        'Data Mining', 'Time Series Analysis', 'Cloud Computing for Data Science',
        'AI Ethics', 'Capstone Project in Data Science'
    ],
    'AI & ML': [
        'Artificial Intelligence Fundamentals', 'Neural Networks', 'Reinforcement Learning',
        'Computer Vision', 'AI Algorithms', 'Machine Learning Models',
        'Expert Systems', 'Robotics and AI', 'Predictive Analytics',
        'AI in Healthcare', 'Generative AI', 'AI Security',
        'Advanced AI Topics', 'ML Project'
    ],
    'Software Systems': [
        'Software Engineering Principles', 'Database Management Systems', 'Operating Systems',
        'Web Development', 'Software Testing', 'Object-Oriented Programming',
        'Distributed Systems', 'Mobile App Development', 'Software Architecture',
        'DevOps Practices', 'Cybersecurity Basics', 'Enterprise Software',
        'Software Project Management', 'Emerging Technologies in Software'
    ]
}

# Class sizes fixed per programme per year
class_sizes = {}
for prog in programmes:
    for year in student_years:
        class_sizes[(prog, year)] = random.randint(50, 60)

# Columns with duplicate 'Semester_ID' as per spec
subjects_columns = [
    'Semester_ID', 'Subject_Code', 'Subject_Name', 'Teacher_ID', 'Course_Credits',
    'Semester', 'Student_Year_Taught', 'Programme', 'Department', 'Class_Size'
]

# Generate subjects data as list of lists
subjects_data = []
sem_id_counter = 1

for prog in programmes:
    prog_teachers = teachers_by_programme[prog]
    num_teachers = len(prog_teachers)
    for year in student_years:
        available_teachers = prog_teachers.copy()
        random.shuffle(available_teachers)
        avail_sub_names = random.sample(subject_names[prog], k=num_teachers)
        for i in range(num_teachers):
            sem_id = f"S{sem_id_counter:03d}"
            subject_code = f"{prog[:2].upper()}{random.randint(100, 999)}"
            subject_name = avail_sub_names[i]
            teacher_id = available_teachers[i]
            course_credits = random.randint(1, 3)
            semester = year_to_sem[year]
            student_year_taught = year
            teacher_row = teachers_df[teachers_df['Teacher_ID'] == teacher_id].iloc[0]
            programme = teacher_row['Programme']
            department = teacher_row['Department']
            class_size = class_sizes[(prog, year)]
            
            # Append as list matching columns
            subjects_data.append([
                sem_id, subject_code, subject_name, teacher_id, course_credits,
                semester, student_year_taught, programme, department, class_size
            ])
            sem_id_counter += 1

# Create DataFrame with specified columns (duplicates allowed)
subjects_df = pd.DataFrame(subjects_data, columns=subjects_columns)

# Save to CSV
subjects_df.to_csv('subjects.csv', index=False)

# Display the table
print(subjects_df.to_string(index=False))