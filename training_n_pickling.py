# Import Packages
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.DataFrame(np.random.randint(0,500,size=(100, 5)), columns= ['A', 'B', 'C', 'D', 'Target']) # Artifically Generate data
X = data[['A', 'B', 'C', 'D']]
y = data['Target']

# Initialize model and fit onthe data
model = LinearRegression().fit(X, y)

# Save the model in pickle format
pickle_handler = open("my_model.pkl", "wb")
pickle.dump(model, pickle_handler)
pickle_handler.close()