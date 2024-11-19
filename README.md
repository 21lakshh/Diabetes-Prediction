# **Diabetes Prediction**  
This project predicts the likelihood of diabetes in individuals based on key health parameters using a machine learning model. A user-friendly Streamlit web application is deployed to make predictions accessible and interactive.

## **Overview**  
Diabetes is a chronic condition that affects millions worldwide. Early detection can significantly improve management and outcomes. This project uses machine learning to predict diabetes risk based on health data, providing an accessible solution for healthcare providers and individuals alike.

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
  
#### **Approach**
**Data analysis** : Using heatmap to check correaltion between multiple features, Using pie charts to check people diagnosed with diabetes distribution and pair plot  

**Data Preprocessing** : Standardized numeric values using StandardScaler, data had no missing values to be handled  

**Model Selection**: Tested SVC (Support Vector Classifier)   

**Model Evaluation:**  
- Accuracy on Training Data: 78.43%  
- Accuracy on Testing Data: 77.92%  

##### **Getting Started**
Deployed using Streamlit as a web-application   
Clone the repo and install dependencies.  
Run the python file and try it yourself!
