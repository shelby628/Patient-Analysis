# Patient Data Analysis 


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

##Tools used.
- Python (Jupyter Notebook)
- Power BI
- Excel
  
  ##  Process
1. Data Cleaning — handled missing values and removed duplicates  
2. Exploratory Data Analysis (EDA) — visualized distributions and correlations  
3. Visualization — built KPI dashboards in Power BI  
4. Reporting — summarized findings for decision making

  ## QUESTIONS (KPI)
1. Calculating the total number of patients recorded?
2. Evaluating workload distribution and service segmentation.
3. What is the Average rating of patient satisfaction?
4.What is the Mean waiting time before receiving service?
5.  Comparison between weekday and weekend visits.
6.  What is the Correlation between race, age group, and satisfaction?

 ## Key Insights
1-The average satisfaction score of 5.47 indicates room for improvement,
especially given that 75% of patients did not provide ratings,suggesting low engagement in feedback collection.#
2-The average wait time of 35.26 minutes is relatively high and may be negatively influencing satisfaction levels. Operational workflow optimization is likely needed.
3-Patient Volume Growth

Total patients increased from 4,338 in 2019 to 4,878 in 2020, showing a 12% year-over-year growth — a positive indicator of patient trust or expanded services.
4-Age Group Concentration

The Adult category accounts for the majority of patients, suggesting the hospital’s core services are primarily targeted toward adult care rather than pediatrics.
5-Referral Trends

Non-referred patients (59%) outnumber referred patients (41%), implying that most patients are direct visitors, possibly due to general consultations or primary care visits.
6-Satisfaction Disparities Across Demographics

The heatmap analysis reveals that certain racial and age groups show higher satisfaction (darker shades), highlighting potential demographic-driven experience gaps that management should investigate.
  “The analysis reveals strong patient growth but highlights critical opportunities in reducing wait times, improving feedback collection, and addressing satisfaction disparities across demographics.”
  ##Visualisations
##Dashboard overview


<img width="770" height="340" alt="image" src="https://github.com/user-attachments/assets/88d4979d-30ca-4990-8f01-6ba71fd0fb97" />

<img width="759" height="334" alt="image" src="https://github.com/user-attachments/assets/9f6c1f7e-00c8-4f9a-ae4f-b50fab0f517a" />

The Wait Time Probability Predictor is a Streamlit-based machine learning application designed to model the relationship between patient waiting times and satisfaction scores. Using a linear regression algorithm, the app analyzes real-world patient data to generate predictive insights that can guide operational decisions in healthcare management. It features an interactive interface built with Streamlit, enabling real-time input, prediction, and visualization of results. This project demonstrates practical skills in Python, pandas, scikit-learn, data visualization (Matplotlib), and Streamlit deployment, showcasing the ability to translate raw data into actionable intelligence.
<img width="731" height="450" alt="image" src="https://github.com/user-attachments/assets/0c07736c-40ff-4d46-8ee4-971723fdce72" />
<img width="548" height="401" alt="image" src="https://github.com/user-attachments/assets/1a8fa2d1-b7c5-476a-88e4-c4790882314b" />



##  How to Run the miniapp
How to Run the App

Clone the repository

git clone https://github.com/shelby628/<patient data analysis>.git
cd <patient data analysis>


Install dependencies
Make sure you have Python installed, then install the required libraries:

pip install streamlit pandas matplotlib scikit-learn


Run the Streamlit application

streamlit run "C:\Users\hp\OneDrive\Desktop\patient data analysis\miniapps\waittime_probability_app.py"

Open in browser
Once the app starts, Streamlit will automatically open it at:
👉 http://localhost:8501
   
##  Conclusion
The analysis of the project proved the potential of analytical tools to transform raw healthcare data into actionable insights that can enhance both operational efficiency and quality of care.
## Author
**Shelby Adede**  
- Data Analyst | Machine Learning Enthusiast  
-  shelbyadede@gmail.com  

 






  
