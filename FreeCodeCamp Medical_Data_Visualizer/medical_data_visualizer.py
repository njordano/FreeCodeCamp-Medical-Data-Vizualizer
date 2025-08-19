import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#
# Read the CSV first:
medical_data = pd.read_csv('medical_examination.csv')
#
# Elaborate a small function to define "overweight" column, which will be used later
def bmi(person, col1, col2):
    # Make sure no bugs will happen due to a TypeError:
    if not isinstance(col1,str) or not isinstance(col2, str):
        raise TypeError('col1 and col2 must be a string type representing the column names')
    # The function must determine whether the person is overweight or not based on their height and weight. 
    # 1 means overweight; 0 means NOT overweight
    if person[col1]/((person[col2]/100)**2) > 25:
        return 1
    else:
        return 0
#
# Create the 'overweight' column:
medical_data['overweight'] = medical_data.apply(lambda person: bmi(person,'weight','height'),axis=1)
#
# Adjust the Cholesterol and Glucose columns by set 0 (healthy) for those with normal levels (1), or 1 (unhealthy)
# for those with above-normal levels (2 or 3):
medical_data[['cholesterol','gluc']] = medical_data[['cholesterol','gluc']].map(
    lambda person: 0 if person == 1 else 1
    )
#
# Create the draw_cat_plot fundtion:
def draw_cat_plot():
    # Create a DataFrame for the cat plot
    # using values from cholesterol, gluc, smoke, alco, active,
    # and overweight in the df_cat variable.
    df_cat = medical_data.melt(id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # Group it so it can be properly understood by sns.catplot()
    df_cat = df_cat.groupby(['cardio','variable','value']).size()
    df_cat = df_cat.reset_index(name='total')
    # Create the chart
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
        )
    # Save the figure
    fig.savefig('catplot.png')
    return fig
#
# Draw the heat map:
def draw_heat_map():
    # Clean the data  by filtering out the following patient segments that represent incorrect data:
    # -Diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    # -Height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    # -Height is more than the 97.5th percentile
    # -Weight is less than the 2.5th percentile
    # -Weight is more than the 97.5th percentile
    pressure_mask = medical_data['ap_lo'] <= medical_data['ap_hi'] # Here, I have decided to make masks, in order for readability
    short_height_mask = medical_data['height'] >= medical_data['height'].quantile(0.025)
    tall_height_mask = medical_data['height'] <= medical_data['height'].quantile(0.975)
    light_weight_mask = medical_data['weight'] >= medical_data['weight'].quantile(0.025)
    heavy_weight_mask = medical_data['weight'] <= medical_data['weight'].quantile(0.975)
    # Apply the masks:
    df_heat = medical_data[
        pressure_mask &
        short_height_mask &
        tall_height_mask &
        light_weight_mask &
        heavy_weight_mask
    ]
    # Elaborate the correlation matrix:
    correlation = df_heat.corr(method='pearson')
    # Create a mask to apply on sns.heatmap()
    uppr_trngl_msk = np.triu(np.ones_like(correlation, dtype=bool))
    # Set up the heatmap:
    fig, ax = plt.subplots(figsize=(12,10))
    sns.heatmap(correlation,annot=True, fmt='.1f', center=0, square=True, mask=uppr_trngl_msk, ax=ax)  
    # Save the figure
    fig.savefig('heatmap.png')
    return fig
#
# Test the functions:
draw_cat_plot()
draw_heat_map()