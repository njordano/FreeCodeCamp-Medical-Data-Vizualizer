# Medical Data Visualizer

This project is part of the FreeCodeCamp Data Analysis with Python certification. It analyzes medical examination data and visualizes health indicators, helping to understand patterns and correlations among key health metrics.

# Project Overview:

The dataset contains medical examination data including height, weight, blood pressure, cholesterol, glucose levels, smoking and alcohol habits, and physical activity. This project:

- Calculates a BMI-based overweight column.

- Cleans the data by filtering out invalid or extreme values.

- Generates a categorical bar plot to compare health features across patients with or without cardiovascular disease.

- Creates a heatmap to show correlations among health indicators.

# Features:

- Overweight Calculation: Uses BMI formula to determine if a patient is overweight.

- Data Cleaning: Filters data for invalid blood pressure readings and extreme height/weight values.

- Categorical Plot: Displays counts of health features across cardio conditions.

- Heatmap: Visualizes correlations among all numerical variables, masking the upper triangle for clarity.

# Files:

- medical_examination.csv – dataset provided by FreeCodeCamp

- medical_data_visualizer.py – main Python script with all analysis and visualization functions

- catplot.png – categorical bar plot

- heatmap.png – correlation heatmap

# How to Run:

1- Install required Python packages: pandas, matplotlib, seaborn, numpy.

2- Place the dataset in the same folder as the script.

3- Run medical_data_visualizer.py.

4- The generated plots will be saved as PNG files in the same folder.

# Acknowledgements:

This project is part of the FreeCodeCamp Data Analysis with Python curriculum, serving as a practical exercise in cleaning, analyzing, and visualizing data using Python.
