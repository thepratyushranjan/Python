# Pickling
# Definition: Pickling is the process of converting a Python object into a byte stream (serialization).
# This byte stream can then be written to a file, sent over a network, or stored in a database for later use.
#Use Case: You use pickling when you want to save the state of an object (like a dictionary, list, or custom object) to a file or transfer it between processes.
#Module: The pickle module in Python provides functions like pickle.dump() and pickle.dumps() for pickling objects.

# Example:-
import pickle

# Example object (dictionary)
data = {"name": "Alice", "age": 25, "city": "New York"}

# Pickle the object and write to a file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
# Explanation: The pickle.dump() function writes the pickled byte stream of the object data to a file named data.pkl. The file is opened in binary write mode ("wb").

# Unpickling
# Definition: Unpickling is the process of converting a byte stream back into a Python object (deserialization). This is useful for reading stored objects from a file or retrieving them from a network transmission.
# Use Case: You use unpickling when you need to load the previously stored object back into memory.
# Module: The pickle module provides functions like pickle.load() and pickle.loads() for unpickling objects.
# Example:-
import pickle

# Unpickle the object from a file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Explanation: The pickle.load() function reads the byte stream from the file and converts it back into a Python object, restoring it to its original form.

