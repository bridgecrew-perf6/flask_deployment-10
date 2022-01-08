import pickle

# Data
data_object_to_pickle = [1,2,3,4,5]

# Save
pickle_handler = open("stored_object.pkl", "wb")
pickle.dump(data_object_to_pickle, pickle_handler)
pickle_handler.close()

# Load
file_to_be_read = open("stored_object.pkl", "rb")
loaded_object = pickle.load(file_to_be_read)
file_to_be_read.close()

print(loaded_object)