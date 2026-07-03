import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_performance.csv")

# Show first 5 rows
print("----- First 5 Rows -----")
print(df.head())

# Create Total and Average columns
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# 1. Overall average mark
overall_avg = df["Average"].mean()
print("\nOverall Average Mark:", round(overall_avg, 2))

# 2. Top scoring student
topper = df.loc[df["Total"].idxmax()]
print("\n----- Top Scoring Student -----")
print("Name:", topper["Name"])
print("Department:", topper["Department"])
print("Total Marks:", topper["Total"])

# 3. Department-wise average marks
dept_avg = df.groupby("Department")["Average"].mean()
print("\n----- Department-wise Average -----")
print(dept_avg)

# 4. Attendance average
attendance_avg = df["Attendance"].mean()
print("\nAverage Attendance:", round(attendance_avg, 2))

# 5. Students with average above 80
high_scorers = df[df["Average"] > 80][["Name", "Average"]]
print("\n----- Students with Average > 80 -----")
print(high_scorers)

# ---------------------------
# VISUALIZATIONS
# ---------------------------

# Bar chart - Department average
plt.figure(figsize=(6,4))
dept_avg.plot(kind='bar')
plt.title("Department-wise Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Scatter plot - Study hours vs Average
plt.figure(figsize=(6,4))
plt.scatter(df["Study_Hours"], df["Average"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# Histogram - Average marks distribution
plt.figure(figsize=(6,4))
plt.hist(df["Average"], bins=5)
plt.title("Average Marks Distribution")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()
