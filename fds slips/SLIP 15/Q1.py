
import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'DBMS', 'AI', 'Cloud']
marks = [85, 75, 90, 80, 70]

plt.figure(figsize=(6, 5))
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Subject-wise Marks - Pie Chart")
plt.show()

plt.figure(figsize=(6, 5))
plt.bar(subjects, marks, color='skyblue', edgecolor='black')
plt.title("Subject-wise Marks - Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
