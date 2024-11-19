import pickle 
import numpy as np
from sklearn.preprocessing import StandardScaler

loaded_model = pickle.load(open('C:/Users/LAKSHYA PALIWAL/.vscode/Deployment/Diabetes/trained_model.sav','rb'))
scaler = pickle.load(open('C:/Users/LAKSHYA PALIWAL/.vscode/Deployment/Diabetes/scaler.sav','rb'))

# Making a predictive System
input_data = (1,89,66,23,94,28.1,0.167,21)

# Changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# Standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = loaded_model.predict(std_data)
print(prediction)

if(prediction[0] == 0):
  print("Person is not Diabetic!!\n")
else:
  print("Person is Diabetic!!\n")
