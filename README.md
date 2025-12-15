
## Part 1: Patient Data Analysis & Visualization


## Table of Contents
1. [Overview](#overview)
2. [Data Sources](#data-sources)
3. [Tools Used](#tools-used)
4. [Process](#process)
5.  [QUESTIONS (KPI)](#QUESTIONS (KPI))
6. [Key Insights](#key-insights)
7. [Visualizations](#visualizations)
8. [How to Run](#how-to-run)
9. [Conclusion](#conclusion)
10. [Author](#author)




## OVERVIEW / OBJECTIVES
The objective of this project is to analyze patient data to uncover patterns in demographics, referral sources, visit trends, and patient satisfaction. 
The analysis aims to identify areas for improving service delivery, reducing wait times, and enhancing overall patient experience across different departments and age groups."

## Data Sources
- `Patient` — Visits  that occured throughout the year.    
- Data sourced from a public healthcare dataset in Kaggle

## Tools used.
- Python (Jupyter Notebook)
- Power BI
- Excel
  
  ##  Process
1. Data Cleaning — handled missing values and removed duplicates  
2. Exploratory Data Analysis (EDA) — visualized distributions and correlations  
3. Visualization — built KPI dashboards in Power BI  
4. Reporting — summarized findings for decision making

  ## Key Questions (KPIs)
1. What is the total number of patients recorded?
2. What is the average patient satisfaction score?
3. What is the mean waiting time before receiving service?
4. How do weekday and weekend visits compare?
5. Is there a relationship between race, age group, and satisfaction?

## Key Insights
- **Patient Satisfaction:** The average satisfaction score of **5.47** indicates room for improvement. Notably, **75% of patients did not provide ratings**, suggesting low engagement in feedback collection.
- **Waiting Time:** The average wait time of **35.26 minutes** is relatively high and likely contributes to lower satisfaction levels, indicating a need for operational workflow optimization.
- **Patient Volume Growth:** Total patients increased from **4,338 in 2019 to 4,878 in 2020**, representing a **12% year-over-year growth**, which may reflect increased patient trust or expanded services.
- **Age Group Concentration:** The adult category accounts for the majority of patients, suggesting the hospital’s core services are primarily focused on adult care rather than pediatrics.
- **Referral Trends:** Non-referred patients (**59%**) outnumber referred patients (**41%**), implying that most visits are direct and likely driven by general consultations or primary care needs.
- **Satisfaction Disparities Across Demographics:** Heatmap analysis reveals variations in satisfaction levels across race and age groups, highlighting potential demographic-driven experience gaps that management should further investigate.


  ## Visualisations
## Dashboard overview
### Power BI Dashboard Overview

<img width="770" height="340" alt="image" src="https://github.com/user-attachments/assets/88d4979d-30ca-4990-8f01-6ba71fd0fb97" /> <br>

<img width="759" height="334" alt="image" src="https://github.com/user-attachments/assets/9f6c1f7e-00c8-4f9a-ae4f-b50fab0f517a" /> <br>

## Conclusion
The analysis reveals strong patient growth while highlighting critical opportunities to reduce wait times, improve feedback collection, and address satisfaction disparities across demographics. <br>  <br>  <br> 


## Part 2: Wait Time Probability Predictor (ML Mini-App)

### Mini App: Wait Time Probability Predictor
The *Wait Time Probability Predictor* is a Streamlit-based machine learning application that models the relationship between patient waiting times and satisfaction scores. Using a linear regression algorithm, the app analyzes real-world patient data to generate predictive insights that support operational decision-making in healthcare management.

The application features an interactive Streamlit interface that allows users to input values, generate predictions, and visualize results in real time. This mini app demonstrates practical skills in Python, pandas, scikit-learn, data visualization with Matplotlib, and Streamlit deployment, showcasing the ability to convert raw data into actionable insights.

<br> 

<img width="731" height="450" alt="image" src="https://github.com/user-attachments/assets/0c07736c-40ff-4d46-8ee4-971723fdce72" />
<br> 

<img width="548" height="401" alt="image" src="https://github.com/user-attachments/assets/1a8fa2d1-b7c5-476a-88e4-c4790882314b" />

<br> 

##  How to Run the miniapp
How to Run the App

Clone the repository

git clone https://github.com/shelby628/<patient data analysis>.git
cd <patient data analysis>


Install dependencies
Make sure you have Python installed, then install the required libraries:

pip install -r requirements.txt



Run the Streamlit application

streamlit run waittime_probability_app.py


Open in browser
Once the app starts, Streamlit will automatically open it at:
👉 http://localhost:8501
   
##  Conclusion
The analysis of the project proved the potential of analytical tools to transform raw healthcare data into actionable insights that can enhance both operational efficiency and quality of care.
## Author
**Shelby Adede**  
- Data Analyst | Machine Learning Enthusiast  
-  shelbyadede@gmail.com  

 






  
