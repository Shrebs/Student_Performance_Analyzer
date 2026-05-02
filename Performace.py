from google.colab import files
uploaded = files.upload()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/content/student_exam_scores.csv')
df.head()


df.isnull().sum()

df.describe()

print(df.columns)
df.columns= df.columns.str.strip()

print(df.columns.tolist())

df.columns=df.columns.str.strip()

sns.scatterplot(x='hours_studied',y='exam_score',data=df)
plt.show()

sns.scatterplot(x='previous_scores',y='exam_score',data=df)
plt.show()

df['attendanc_group']=pd.cut(df['attendance_percent'],bins=[0,50,75,100],labels=['low','medium','high'])


sns.barplot(x='attendanc_group',y='exam_score',data=df)
plt.show()


import numpy as np
sns.heatmap(df.drop(columns=['student_id', 'attendanc_group']).corr(), annot=True)
plt.show()


#overall comparision
# Create difference column
df['score_diff'] = df['exam_score'] - df['previous_scores']

# Average comparison
prev_avg = df['previous_scores'].mean()
exam_avg = df['exam_score'].mean()

print("Average Previous Score:", prev_avg)
print("Average Exam Score:", exam_avg)

if exam_avg > prev_avg:
    print("Overall Performance: Improved 📈")
elif exam_avg < prev_avg:
    print("Overall Performance: Declined 📉")
else:
    print("Overall Performance: No Change 😐")

# Count categories
improved = (df['score_diff'] > 0).sum()
declined = (df['score_diff'] < 0).sum()
same = (df['score_diff'] == 0).sum()

print("\nNumber of Students Improved:", improved)
print("Number of Students Declined:", declined)
print("Number of Students Same:", same)


#overall comparision
# Create difference column
df['score_diff'] = df['exam_score'] - df['previous_scores']

# Average comparison
prev_avg = df['previous_scores'].mean()
exam_avg = df['exam_score'].mean()

print("Average Previous Score:", prev_avg)
print("Average Exam Score:", exam_avg)

if exam_avg > prev_avg:
    print("Overall Performance: Improved 📈")
elif exam_avg < prev_avg:
    print("Overall Performance: Declined 📉")
else:
    print("Overall Performance: No Change 😐")

# Count categories
improved = (df['score_diff'] > 0).sum()
declined = (df['score_diff'] < 0).sum()
same = (df['score_diff'] == 0).sum()

print("\nNumber of Students Improved:", improved)
print("Number of Students Declined:", declined)
print("Number of Students Same:", same)


#individual student comparison
# Label performance for each student
def performance_label(row):
    if row['exam_score'] > row['previous_scores']:
        return "Improved"
    elif row['exam_score'] < row['previous_scores']:
        return "Declined"
    else:
        return "No Change"

df['performance'] = df.apply(performance_label, axis=1)

# Show sample
print(df[['student_id', 'previous_scores', 'exam_score', 'score_diff', 'performance']].head(10))


#summary
print("\nPerformance Summary:")
print(df['performance'].value_counts())


print("\nAverage Factors by Performance:")
print(df.groupby('performance')[['hours_studied', 'sleep_hours', 'attendance_percent']].mean())



# 1. Check raw values
print("FIRST 10 ROWS:")
print(df[['previous_scores', 'exam_score']].head(10))

# 2. Check min/max
print("\nMIN/MAX VALUES:")
print("Previous -> min:", df['previous_scores'].min(), "max:", df['previous_scores'].max())
print("Exam     -> min:", df['exam_score'].min(), "max:", df['exam_score'].max())

# 3. Check if ANYONE improved
print("\nNumber of students who improved:")
print((df['exam_score'] > df['previous_scores']).sum())

# 4. Check difference values directly
df['score_diff'] = df['exam_score'] - df['previous_scores']
print("\nScore diff sample:")
print(df['score_diff'].head(10))