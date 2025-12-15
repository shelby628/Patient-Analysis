import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -----------------------------
# Load your dataset
# -----------------------------
df = pd.read_csv("patients.csv")  # CSV must be in the same folder
df = df.dropna(subset=['patient_waittime', 'patient_sat_score'])  # Remove missing values

# -----------------------------
# Train linear regression model
# -----------------------------
X = df[['patient_waittime']]      # Feature
y = df['patient_sat_score']       # Target

model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Patient Wait Time → Satisfaction Predictor")

# User input
wait_time = st.number_input(
    "Enter wait time in minutes:",
    min_value=int(df['patient_waittime'].min()),
    max_value=int(df['patient_waittime'].max()),
    value=int(df['patient_waittime'].mean())
)

# Predict satisfaction score
pred_score = model.predict(pd.DataFrame([[wait_time]], columns=['patient_waittime']))[0]
st.success(f"Predicted Satisfaction Score: {pred_score:.2f} / 10")

# Show wait time distribution
fig, ax = plt.subplots()
ax.hist(df['patient_waittime'], bins=20, color='skyblue', edgecolor='black')
ax.axvline(wait_time, color='red', linestyle='dashed', linewidth=2, label='Your input')
ax.set_xlabel("Wait Time (minutes)")
ax.set_ylabel("Number of Patients")
ax.set_title("Distribution of Patient Wait Times")
ax.legend()
st.pyplot(fig)
