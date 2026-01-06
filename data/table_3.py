import pandas as pd
import random

# For reproducibility
random.seed(42)

# Read existing CSVs
teachers_df = pd.read_csv('teachers.csv')
subjects_df = pd.read_csv('subjects.csv')

# Extract unique programme + student_year + department combos from subjects
# Since department is consistent per programme in data
unique_classes = subjects_df[['Programme', 'Student_Year_Taught', 'Department']].drop_duplicates()

# Possible values
genders = ["Male", "Female"]

# Generate students: 5 per unique class (programme + year)
students_data = []
student_id_counter = 1

for _, row in unique_classes.iterrows():
    prog = row['Programme']
    year = row['Student_Year_Taught']
    dept = row['Department']
    for _ in range(5):  # 5 students per class
        student_id = f"STU{student_id_counter:03d}"
        gender = random.choice(genders)
        
        students_data.append({
            'Student_ID': student_id,
            'Student_Year': year,
            'Programme': prog,
            'Department': dept,
            'Gender': gender,
        })
        student_id_counter += 1

# Create DataFrame
students_columns = [
    'Student_ID', 'Student_Year', 'Programme', 'Department', 'Gender'
]
students_df = pd.DataFrame(students_data, columns=students_columns)

# Save to CSV
students_df.to_csv('students.csv', index=False)

# Display the table
print(students_df.to_string(index=False))