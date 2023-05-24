import pandas as pd

# Assuming you have an array of dictionaries
data = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 28, 'City': 'London'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Paris'}
]

# Convert the array into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as JSON
df.to_json('data.json', orient='records')
