import csv
import matplotlib.pyplot as plt

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

students = []

with open("student_grades.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Student"]
        score = int(row["Score"])
        grade = letter_grade(score)

        students.append({
            "Student": name,
            "Score": score,
            "Grade": grade
        })

scores = [student["Score"] for student in students]

average = sum(scores) / len(scores)
highest = max(students, key=lambda student: student["Score"])
lowest = min(students, key=lambda student: student["Score"])

print("STUDENT GRADE ANALYZER")
print("------------------------------")
print("Students analyzed:", len(students))
print(f"Class average: {average:.2f}")
print(f"Highest score: {highest['Student']} ({highest['Score']})")
print(f"Lowest score: {lowest['Student']} ({lowest['Score']})")

with open("grade_results.csv", "w", newline="") as file:
    fieldnames = ["Student", "Score", "Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("Results saved to grade_results.csv")

names = [student["Student"] for student in students]
scores = [student["Score"] for student in students]

plt.bar(names, scores)
plt.title("Student Grade Distribution")
plt.xlabel("Student")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grade_distribution.png")

print("Graph saved to grade_distribution.png")