import numpy as np
import streamlit as st
import pickle
import os

# Load the model
working_dir = os.path.dirname(os.path.abspath(__file__)) 
loaded_model = pickle.load(open(f'{working_dir}/trained_model.sav','rb'))
scaler = pickle.load(open(f'{working_dir}/scaler.sav','rb'))


# Function for prediction
def make_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(std_data)

    if prediction[0] == 1:
        return 'Person is Diabetic!'
    else:
        return 'Person is not Diabetic!'

def main():
    st.title('Diabetes Prediction')

    # Getting input from user with numeric inputs
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
    Glucose = st.number_input('Glucose Level', min_value=0)
    BloodPressure = st.number_input('Blood Pressure value', min_value=0)
    SkinThickness = st.number_input('Skin Thickness value', min_value=0)
    Insulin = st.number_input('Insulin Level', min_value=0)
    BMI = st.number_input('BMI', min_value=0.0, format="%.1f")
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.3f")
    Age = st.number_input('Age of the person', min_value=0, step=1)

    # Code for prediction
    diagnosis = ''  # This will store the prediction result

    # Creating a button for prediction
    if st.button('Result'):
        diagnosis = make_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)  # Displaying the result

if __name__ == '__main__':
    main()

