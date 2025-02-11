# **Diabetes Prediction**  
This project predicts the likelihood of diabetes in individuals based on key health parameters using a machine learning model. A user-friendly Streamlit web application is deployed to make predictions accessible and interactive.

---
## **Overview**  
Diabetes is a chronic condition that affects millions worldwide. Early detection can significantly improve management and outcomes. This project uses machine learning to predict diabetes risk based on health data, providing an accessible solution for healthcare providers and individuals alike.

---
### **Features**  
The dataset includes property attributes such as:  

- Pregnancies  
- Glucose  
- BloodPressure  
- SkinThickness  
- Insulin  
- BMI  
- DiabetesPedigreeFunction  
- Age

---
### Key Steps:

1. **Data Preprocessing:**
   - Checked for any null values in the dataset.
   - Imputed or removed null values if present to ensure data integrity.

2. **Exploratory Data Analysis (EDA):**
   - Extracted useful insights using statistical methods.
   - Checked the distribution of diabetic and non-diabetic groups using a pie chart.
   - Used a correlation matrix to analyze the relationship between features.

3. **Feature Scaling:**
   - Applied the **StandardScaler** function to transform the data using the formula:

4. **Modeling:**
   - Used a **Support Vector Classifier (SVC)** to build the predictive model.
   - Achieved:
     - **Training Accuracy:** 78.34%
     - **Test Accuracy:** 77.92%

5. **Deployment:**
   - Deployed the project as a **Streamlit web application** for user interaction.

---
# **Getting Started**

 - Deployed using Streamlit as a web-application   
 - Clone the repo and install dependencies.  
 - Run the python file and try it yourself!  

---
you need to run the following commands in the terminal  
- **cd Diabetes**  
- **streamlit run app.py**
