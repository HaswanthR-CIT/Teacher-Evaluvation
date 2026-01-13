import pandas as pd
import random

# For reproducibility (same data every time you run)
random.seed(42)

# Fixed institution name
institution = "Coimbatore Institute of Technology"

# Possible realistic values
genders = ["Male", "Female"]
age_groups = ["25-34", "35-44", "45-54", "55+"]
departments = [
    "M.Sc.",
    "B.E.",
    "B.Tech"
]
programmes = [
    "Data Science",
    "AI & ML",
    "Software Systems"
]
years_experience_options = list(range(2, 25))  # 2 to 24 years
highest_degrees = ["M.Tech", "M.E.", "Ph.D", "M.S."]
cert_status = ["Certified", "Not Certified"]

# Create list for 5 teachers (respecting: each teacher assigned to only ONE programme)
teacher_data = []

# Teacher 1 - Data Science
teacher_data.append({
    "Teacher_ID": "T001",
    "Teacher_Name": "Dr. ABC",
    "Institution": institution,
    "Gender": random.choice(genders),
    "Age_Group": random.choice(age_groups),
    "Department": "M.Sc.",
    "Programme": "Data Science",
    "Years_of_Experience": random.choice(years_experience_options),
    "Highest_Degree_Earned": random.choice(highest_degrees),
    "Certification_Status": "Certified"
})

# Teacher 2 - Also Data Science (multiple teachers can belong to same programme)
teacher_data.append({
    "Teacher_ID": "T002",
    "Teacher_Name": "Dr. DEF",
    "Institution": institution,
    "Gender": random.choice(genders),
    "Age_Group": random.choice(age_groups),
    "Department": "M.Sc.",
    "Programme": "Data Science",
    "Years_of_Experience": random.choice(years_experience_options),
    "Highest_Degree_Earned": random.choice(highest_degrees),
    "Certification_Status": "Certified"
})

# Teacher 3 - AI & ML
teacher_data.append({
    "Teacher_ID": "T003",
    "Teacher_Name": "GHI",
    "Institution": institution,
    "Gender": random.choice(genders),
    "Age_Group": random.choice(age_groups),
    "Department": "M.Sc.",
    "Programme": "AI & ML",
    "Years_of_Experience": random.choice(years_experience_options),
    "Highest_Degree_Earned": random.choice(highest_degrees),
    "Certification_Status": "Certified"
})

# Teacher 4 - Software Systems
teacher_data.append({
    "Teacher_ID": "T004",
    "Teacher_Name": "Dr. JKL",
    "Institution": institution,
    "Gender": random.choice(genders),
    "Age_Group": random.choice(age_groups),
    "Department": "M.Sc.",
    "Programme": "Software Systems",
    "Years_of_Experience": random.choice(years_experience_options),
    "Highest_Degree_Earned": random.choice(highest_degrees),
    "Certification_Status": "Certified"
})

# Teacher 5 - Data Science
teacher_data.append({
    "Teacher_ID": "T005",
    "Teacher_Name": "MNO",
    "Institution": institution,
    "Gender": random.choice(genders),
    "Age_Group": random.choice(age_groups),
    "Department": "M.Sc.",
    "Programme": "Data Science",
    "Years_of_Experience": random.choice(years_experience_options),
    "Highest_Degree_Earned": random.choice(highest_degrees),
    "Certification_Status": "Certified"
})

# Create the DataFrame
teachers_df = pd.DataFrame(teacher_data)

# Optional: Save to CSV
teachers_df.to_csv("teachers.csv", index=False)

# Display the table
print(teachers_df.to_string(index=False))