import matplotlib.pyplot as plt
import seaborn as sns
from insights import *

# Set Seaborn style
sns.set(style="whitegrid")


# Visualization 1: Pair plot of numerical columns
fig = plt.figure(figsize=(15, 10))
sns.pairplot(data[numerical_cols])
plt.suptitle('Pair Plot of Numerical Columns', y=1.02)
plt.savefig("Visualization_1_Pair_plot_of_numerical_columns.png")

# Visualization 2: Box plot of 'Temperature (C)' by 'Summary'
plt.close()
fig = plt.figure(figsize=(15, 8))
sns.boxplot(x='Summary', y='Temperature (C)', data=data)
plt.title('Box plot of Temperature by Summary')
plt.xticks(rotation=45)

plt.savefig("Visualization_2_Box_plot_of_Temperature_by_Summary.png")

# Visualization 3: Heatmap of Correlation Matrix
plt.close()
fig = plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')

plt.savefig("Visualization_3_Heatmap_of_Correlation_Matrix.png")

# Visualization 4: Distribution of 'Apparent Temperature (C)' by 'Precip Type'
plt.close()
fig = plt.figure(figsize=(15, 8))
sns.violinplot(x='Precip Type', y='Apparent Temperature (C)', data=filtered_data)
plt.title('Distribution of Apparent Temperature by Precipitation Type')

plt.savefig("Visualization_4_Distribution_of_Apparent_Temperature_by_Precip_Type.png")

# Visualization 5: Line plot of Hourly Temperature trend
plt.close()
fig = plt.figure(figsize=(15, 8))
sns.lineplot(x=hourly_temp_trend.index, y=hourly_temp_trend.values)
plt.title('Hourly Temperature Trend')
plt.xlabel('Hour')
plt.ylabel('Average Temperature (C)')

plt.savefig("Visualization_5_Line_plot_of_Hourly_Temperature_trend.png")

# Visualization 6: Scatter plot of 'Temperature (C)' vs 'Humidity'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.scatterplot(x='Temperature (C)', y='Humidity', data=data)
plt.title('Scatter plot of Temperature vs Humidity')

plt.savefig("Visualization_6_Scatter_plot_of_Temperature_vs_Humidity.png")

#_Visualization 7: Bar plot of 'Precip Type' proportions
plt.close()
fig = plt.figure(figsize=(10, 6))
precip_type_proportion.plot(kind='bar')
plt.title('Proportion of Precipitation Types')
plt.xlabel('Precipitation Type')
plt.ylabel('Proportion')

plt.savefig("Visualization_7_Bar_plot_of_Precip_Type_proportions.png")

#_Visualization 8: Line plot of 'Average Temperature by Month'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.lineplot(x=avg_temp_by_month.index, y=avg_temp_by_month.values)
plt.title('Average Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Average Temperature (C)')

plt.savefig("Visualization_8_Line_plot_of_Average_Temperature_by_Month.png")

# Visualization 9: Count plot of 'Summary' values
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.countplot(x='Summary', data=data)
plt.title('Count of Each Weather Summary')
plt.xticks(rotation=45)

plt.savefig("Visualization_9_Count_plot_of_Summary_values.png")

#_Visualization 10: Histogram of 'Humidity'
plt.close()
fig = plt.figure(figsize=(10, 6))
sns.histplot(data['Humidity'], bins=30, kde=True)
plt.title('Distribution of Humidity')
plt.xlabel('Humidity')

plt.savefig("Visualization_10_Histogram_of_Humidity.png")

# Visualization 11: Bar plot of 'Hourly Wind Speed statistics'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.barplot(x=hourly_wind_speed_stats.index, y=hourly_wind_speed_stats['mean'])
plt.title('Hourly Average Wind Speed')
plt.xlabel('Hour')
plt.ylabel('Average Wind Speed (km/h)')

plt.savefig("Visualization_11_Bar_plot_of_Hourly_Wind_Speed_statistics.png")

#_Visualization 12: Scatter plot of 'Temperature (C)' vs 'Apparent Temperature (C)'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.scatterplot(x='Temperature (C)', y='Apparent Temperature (C)', data=data)
plt.title('Scatter plot of Temperature vs Apparent Temperature')

plt.savefig("Visualization_12_Scatter_plot_of_Temperature_vs_Apparent_Temperature.png")

# Visualization 13: Bar plot of 'Pressure (millibars)' variance by 'Summary'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.barplot(x=pressure_variance.index, y=pressure_variance.values)
plt.title('Variance of Pressure by Weather Summary')
plt.xticks(rotation=45)

plt.savefig("Visualization_13_Bar_plot_of_Pressure_variance_by_Summary.png")

# Visualization 14: Box plot of 'Visibility (km)' by 'Month'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.boxplot(x='Month', y='Visibility (km)', data=data)
plt.title('Visibility Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Visibility (km)')

plt.savefig("Visualization_14_Box_plot_of_Visibility_by_Month.png")

# Visualization 15: Scatter plot of 'Wind Speed (km/h)' vs 'Humidity'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.scatterplot(x='Wind Speed (km/h)', y='Humidity', data=data)
plt.title('Scatter plot of Wind Speed vs Humidity')

plt.savefig("Visualization_15_Scatter_plot_of_Wind_Speed_vs_Humidity.png")

#_Visualization 16: Line plot of 'Monthly Average Visibility'
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.lineplot(x=monthly_avg_visibility.index, y=monthly_avg_visibility.values)
plt.title('Monthly Average Visibility')
plt.xlabel('Month')
plt.ylabel('Average Visibility (km)')

plt.savefig("Visualization_16_Line_plot_of_Monthly_Average_Visibility.png")

# Visualization 17: Bar plot of 'Daily Summary' occurrences
plt.close()
fig = plt.figure(figsize=(15, 8))
daily_summary_counts.head(10).plot(kind='bar')
plt.title('Top 10 Daily Summary Occurrences')
plt.xlabel('Daily Summary')
plt.ylabel('Occurrences')

plt.savefig("Visualization_17_Bar_plot_of_Daily_Summary_occurrences.png")

# Visualization 18: Histogram of 'Pressure (millibars)'
plt.close()
fig = plt.figure(figsize=(10, 6))
sns.histplot(data['Pressure (millibars)'], bins=30, kde=True)
plt.title('Distribution of Pressure')
plt.xlabel('Pressure (millibars)')

plt.savefig("Visualization_18_Histogram_of_Pressure.png")

# Visualization 19: Pie chart of 'Precip Type' proportions
plt.close()
fig = plt.figure(figsize=(8, 8))
plt.pie(precip_type_proportion, labels=precip_type_proportion.index, autopct='%1.1f%%', startangle=140) # type: ignore
plt.title('Proportion of Precipitation Types')

plt.savefig("Visualization_19_Pie_chart_of_Precip_Type_proportions.png")

# Visualization 20: Box plot of 'Apparent Temperature (C)' by 'Month'
plt.close()
fig = plt.figure(figsize=(15, 8))
sns.boxplot(x='Month', y='Apparent Temperature (C)', data=data)
plt.title('Apparent Temperature Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Apparent Temperature (C)')

plt.savefig("Visualization_20_Box_plot_of_Apparent_Temperature_by_Month.png")

# Advanced Visualizations

# Visualization 21: Pairplot of Numerical Columns with Hue based on 'Precip Type'
    # Add 'Precip Type' to numerical_data temporarily for visualization
numerical_data_with_precip = numerical_data.join(filtered_data['Precip Type'])
plt.close()
fig = plt.figure(figsize=(20, 15))
sns.pairplot(data=numerical_data_with_precip, hue='Precip Type')
plt.suptitle('Pair Plot of Numerical Columns with Hue by Precipitation Type', y=1.02)

plt.savefig("Visualization_21_Pairplot_of_Numerical_Columns_with_Hue_based_on_Precip_Type.png")

# Visualization 22: Boxplot of 'Apparent Temperature (C)' by 'Month' and 'Precip Type'
plt.close()
fig = plt.figure(figsize=(15, 10))
sns.boxplot(x='Month', y='Apparent Temperature (C)', hue='Precip Type', data=filtered_data)
plt.title('Apparent Temperature by Month and Precipitation Type')
plt.xlabel('Month')
plt.ylabel('Apparent Temperature (C)')

plt.savefig("Visualization_22_Boxplot_of_Apparent_Temperature_by_Month_and_Precip_Type.png")

# Visualization 23: Heatmap of Hourly Wind Speed statistics by Month and Hour
plt.close()
fig = plt.figure(figsize=(15, 10))
hourly_wind_speed_pivot = hourly_wind_speed_stats.unstack().fillna(0)['mean']
hourly_wind_speed_pivot = hourly_wind_speed_pivot.reset_index().pivot(index='Hour', columns='Month', values='mean')
sns.heatmap(hourly_wind_speed_pivot, cmap='coolwarm', annot=True, fmt=".2f")
plt.title('Hourly Wind Speed by Month and Hour')
plt.xlabel('Month')
plt.ylabel('Hour')

plt.savefig("Visualization_23_Heatmap_of_Hourly_Wind_Speed_statistics_by_Month_and_Hour.png")

# Visualization 24: Pairplot of Temperature, Humidity, Wind Speed, and Pressure by Month
selected_cols = ['Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)', 'Month']
pairplot_filtered = data[selected_cols]
plt.close()
fig = plt.figure(figsize=(15, 10))
sns.pairplot(pairplot_filtered, hue='Month')
plt.suptitle('Pair Plot of Weather Attributes by Month', y=1.02)

plt.savefig("Visualization_24_Pairplot.png")

# Visualization 25: Line plot of Monthly Average Temperature and Humidity
monthly_avg_temp_humidity = data.groupby('Month')[['Temperature (C)', 'Humidity']].mean().reset_index()
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.lineplot(x='Month', y='value', hue='variable', data=pd.melt(monthly_avg_temp_humidity, ['Month']))
plt.title('Monthly Average Temperature and Humidity')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend(['Temperature (C)', 'Humidity'])

plt.savefig("Visualization_25_Line_plot_of_Monthly_Average_Temperature_and_Humidity.png")

# Visualization 26: Scatter plot of Temperature vs Apparent Temperature by Humidity
plt.close()
fig = plt.figure(figsize=(12, 8))
sns.scatterplot(x='Temperature (C)', y='Apparent Temperature (C)', hue='Humidity', data=data)
plt.title('Temperature vs Apparent Temperature colored by Humidity')
plt.xlabel('Temperature (C)')
plt.ylabel('Apparent Temperature (C)')

plt.savefig("Visualization_26_Scatter_plot_of_Temperature_vs_Apparent_Temperature_by_Humidity.png")

# Visualization 27: Violin plot of Apparent Temperature by Summary with Hue by Precip Type
plt.close()
fig = plt.figure(figsize=(15, 8))
sns.violinplot(x='Summary', y='Apparent Temperature (C)', hue='Precip Type', data=filtered_data)
plt.title('Apparent Temperature Distribution by Weather Summary and Precipitation Type')
plt.xticks(rotation=45)

plt.savefig("Visualization_27_Violin_plot_of_Apparent_Temperature_by_Summary_with_Hue_by_Precip_Type.png")

# Visualization 28: Pairplot of Weather Attributes with Hourly Trend
pairplot_hourly_trend = data[selected_cols + ['Hour']]
pairplot_hourly_trend = pairplot_hourly_trend.assign(Hourly_Trend=data.groupby('Hour')['Temperature (C)'].transform('mean'))
plt.close()
fig = plt.figure(figsize=(20, 15))
sns.pairplot(pairplot_hourly_trend, hue='Hour', palette='viridis')
plt.suptitle('Pair Plot of Weather Attributes with Hourly Temperature Trend', y=1.02)

plt.savefig("Visualization_28_Pairplot_of_Weather_Attributes_with_Hourly_Trend.png")

# Visualization 29: Boxplot of Wind Speed by Weather Summary
plt.close()
fig = plt.figure(figsize=(15, 8))
sns.boxplot(x='Summary', y='Wind Speed (km/h)', data=data)
plt.title('Wind Speed Distribution by Weather Summary')
plt.xticks(rotation=45)

plt.savefig("Visualization_29_Boxplot_of_Wind_Speed_by_Weather_Summary.png")

#_Visualization 30: Line plot of Hourly Wind Speed Trend by Month
hourly_wind_speed_month_trend = data.pivot_table(index='Hour', columns='Month', values='Wind Speed (km/h)', aggfunc='mean')
plt.close()
fig = plt.figure(figsize=(15, 8))
sns.lineplot(data=hourly_wind_speed_month_trend, dashes=False)
plt.title('Hourly Wind Speed Trend by Month')
plt.xlabel('Hour')
plt.ylabel('Average Wind Speed (km/h)')
plt.legend(title='Month')

plt.savefig("Visualization_30_Line_plot_of_Hourly_Wind_Speed_Trend_by_Month.png")

#Visualization 31:  Distribution of temperatures
plt.close()
fig = plt.figure(figsize=(10, 6))
sns.histplot(data['Temperature (C)'], bins=30, kde=True)
plt.title('Distribution of Temperature (C)')
plt.xlabel('Temperature (C)')

plt.savefig("Visualisation_31_Temperature_Distribution.png")