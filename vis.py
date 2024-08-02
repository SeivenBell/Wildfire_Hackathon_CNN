import pandas as pd

# Load the uploaded CSV file
file_path = 'D:\Projects\Wildfire_Hackathon_Complete\submissionv3.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
data.head()
import matplotlib.pyplot as plt
import numpy as np

# Create a color map based on the values
def value_to_color(val):
    if val == "True":
        return 'red'
    elif val == "False":
        return 'green'
    else:
        return 'white'

# Apply the color map to the dataframe
colored_data = data.applymap(value_to_color)

# Create a plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')
ax.axis('tight')

# Create a table with colors
table = ax.table(cellText=data.values, cellColours=colored_data.values, cellLoc='center', loc='center')

# Adjust the column widths
table.auto_set_column_width(col=list(range(len(data.columns))))

plt.show()
