import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📊 Student Performance Analyzer Dashboard")

# Load data
df = pd.read_csv("student_exam_scores.csv")
df.columns = df.columns.str.strip()

# Ensure numeric
df['previous_scores'] = pd.to_numeric(df['previous_scores'], errors='coerce')
df['exam_score'] = pd.to_numeric(df['exam_score'], errors='coerce')

# Create score difference
df['score_diff'] = df['exam_score'] - df['previous_scores']

# Performance label
def performance_label(row):
    if row['exam_score'] > row['previous_scores']:
        return "Improved"
    elif row['exam_score'] < row['previous_scores']:
        return "Declined"
    else:
        return "No Change"

df['performance'] = df.apply(performance_label, axis=1)

# ----------------------------
# 📊 SECTION 1: OVERALL VISUALS
# ----------------------------

st.subheader("📊 Overall Analysis")

# Scatter plots
fig1, ax1 = plt.subplots()
sns.scatterplot(x='hours_studied', y='exam_score', data=df, ax=ax1)
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.scatterplot(x='previous_scores', y='exam_score', data=df, ax=ax2)
st.pyplot(fig2)

# Attendance grouping
df['attendance_group'] = pd.cut(df['attendance_percent'],
                               bins=[0,50,75,100],
                               labels=['Low','Medium','High'])

fig3, ax3 = plt.subplots()
sns.barplot(x='attendance_group', y='exam_score', data=df, ax=ax3)
st.pyplot(fig3)

# Heatmap
fig4, ax4 = plt.subplots()
sns.heatmap(df.drop(columns=['student_id','attendance_group','performance']).corr(),
            annot=True, ax=ax4)
st.pyplot(fig4)

# Score difference distribution
fig5, ax5 = plt.subplots()
sns.histplot(df['score_diff'], bins=20, kde=True, ax=ax5)
st.pyplot(fig5)

# ----------------------------
# 🎯 SECTION 2: STUDENT SELECTOR
# ----------------------------

st.subheader("🎯 Individual Student Analysis")

student_id = st.selectbox("Select Student ID", df['student_id'])

student = df[df['student_id'] == student_id]

prev = float(student['previous_scores'])
exam = float(student['exam_score'])
diff = float(student['score_diff'])
status = student['performance'].values[0]

st.write(f"📌 Previous Score: {prev}")
st.write(f"📌 Exam Score: {exam}")
st.write(f"📌 Score Difference: {diff}")
st.write(f"📌 Performance: {status}")

# Dynamic conclusion
if status == "Improved":
    st.success("🎉 This student has improved compared to previous performance.")
elif status == "Declined":
    st.error("⚠️ This student's performance has declined.")
else:
    st.info("😐 No change in performance.")