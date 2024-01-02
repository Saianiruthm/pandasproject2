import pandas as pd
import numpy as np

# Assume 'data' is your dataframe

# Load the dataset
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Display basic info about the dataset
print("Dataset info before preprocessing:")
print(data.info())

# Handling missing values
data.dropna(inplace=True)  # Drop rows with missing values, you might want to handle these differently depending on your needs

# Convert 'Formatted Date' column to datetime format
data['Formatted Date'] = pd.to_datetime(data['Formatted Date'], utc=True)
# Extracting date components
data['Year'] = data['Formatted Date'].dt.year
data['Month'] = data['Formatted Date'].dt.month
data['Day'] = data['Formatted Date'].dt.day
data['Hour'] = data['Formatted Date'].dt.hour

# Handle categorical variables (if any)
# Example: Convert 'Precip Type' to numerical values using one-hot encoding
#data = pd.get_dummies(data, columns=['Precip Type'])

# Normalize numerical columns (optional but can be useful for some analyses)
numerical_cols = ['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)', 'Pressure (millibars)']
data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()

# Display basic info after preprocessing
print("\nDataset info after preprocessing:")
print(data.info())

# Save the preprocessed data to a new CSV file
data.to_csv('preprocessed_weather_data.csv', index=False)

#Insights

# 1. Shape of the dataframe
insight_1 = f"Shape of the dataframe: {data.shape}"

# 2. Summary statistics
summary_stats = data.describe()
insight_2 = f"Summary statistics:\n{summary_stats}"

# 3. Checking for missing values
missing_values = data.isnull().sum()
insight_3 = f"Missing values:\n{missing_values}"

# 4. Checking unique values in a column (e.g., 'Summary')
unique_values_summary = data['Summary'].unique()
insight_4 = f"Unique values in 'Summary' column: {unique_values_summary}"

# Numerical columns only
numerical_data = data.select_dtypes(include=[np.number])

# 5. Correlation matrix between numerical columns
correlation_matrix = numerical_data.corr()
insight_5 = f"Correlation matrix:\n{correlation_matrix}"

# 6. Distribution of temperatures
temperature_distribution = data['Temperature (C)'].hist()
insight_6 = "Distribution of temperatures"

# 7. Average humidity by 'Summary'
avg_humidity_summary = data.groupby('Summary')['Humidity'].mean()
insight_7 = f"Average humidity by 'Summary':\n{avg_humidity_summary}"

# 8. Busiest period by 'Formatted Date'
busy_period = data['Formatted Date'].dt.to_period('M').value_counts().idxmax()
insight_8 = f"Busiest period by 'Formatted Date': {busy_period}"

# 9. Variance of 'Pressure (millibars)' across different 'Summary' types
pressure_variance = data.groupby('Summary')['Pressure (millibars)'].var()
insight_9 = f"Variance of 'Pressure (millibars)' by 'Summary':\n{pressure_variance}"

# 10. Top 5 windiest days
top_windiest_days = data.nlargest(5, 'Wind Speed (km/h)')[['Formatted Date', 'Wind Speed (km/h)']]
insight_10 = f"Top 5 windiest days:\n{top_windiest_days}"

# 11. Mean temperature by 'Precip Type'
mean_temp_precip = data.groupby('Precip Type')['Temperature (C)'].mean()
insight_11 = f"Mean temperature by 'Precip Type':\n{mean_temp_precip}"

# 12. Visualizing Humidity vs. Temperature relationship
humidity_temp_relationship = data.plot.scatter(x='Temperature (C)', y='Humidity')
insight_12 = "Humidity vs. Temperature relationship"

# 13. Daily summary with the longest text
max_summary_length = data.loc[data['Daily Summary'].str.len().idxmax(), 'Daily Summary']
insight_13 = f"Daily summary with the longest text:\n{max_summary_length}"

# 14. Day with the highest visibility
max_visibility_day = data.loc[data['Visibility (km)'].idxmax(), 'Formatted Date']
insight_14 = f"Day with the highest visibility: {max_visibility_day}"

# 15. Proportion of different 'Precip Type'
precip_type_proportion = data['Precip Type'].value_counts(normalize=True)
insight_15 = f"Proportion of different 'Precip Type':\n{precip_type_proportion}"


# Collect all insights
insights = [insight_1, insight_2, insight_3, insight_4, insight_5, insight_6,
                insight_7, insight_8, insight_9, insight_10, insight_11, insight_12,
                insight_13, insight_14, insight_15]

# 16. Hourly Temperature trend
hourly_temp_trend = data.groupby('Hour')['Temperature (C)'].mean()
insights.append(hourly_temp_trend)

# 17. Relationship between Temperature and Apparent Temperature
temp_vs_apparent_temp = data.plot.scatter(x='Temperature (C)', y='Apparent Temperature (C)')
insights.append(temp_vs_apparent_temp)

# 18 . Average Temperature by Month
avg_temp_by_month = data.groupby('Month')['Temperature (C)'].mean()
insights.append(avg_temp_by_month)

# 19. Count of different 'Summary' values
summary_counts = data['Summary'].value_counts()
insights.append(summary_counts)

# 20. Maximum Humidity recorded
max_humidity = data['Humidity'].max()
insights.append(max_humidity)

# 21. Distribution of Precipitation Types
precip_type_distribution = data['Precip Type'].value_counts()
insights.append(precip_type_distribution)

# 22. Daily Summary occurrences
daily_summary_counts = data['Daily Summary'].value_counts()
insights.append(daily_summary_counts)

# 23. Monthly average visibility
monthly_avg_visibility = data.groupby('Month')['Visibility (km)'].mean()
insights.append(monthly_avg_visibility)

# 24. Range of Pressure values
pressure_range = data['Pressure (millibars)'].max() - data['Pressure (millibars)'].min()
insights.append(pressure_range)

# 25. Hourly Wind Speed statistics
hourly_wind_speed_stats = data.groupby('Hour')['Wind Speed (km/h)'].describe()
insights.append(hourly_wind_speed_stats)

# 26. Proportion of days with Loud Cover
loud_cover_proportion = (data['Loud Cover'].sum() / len(data)) * 100
insights.append(loud_cover_proportion)

# 27. Summary statistics of Apparent Temperature
apparent_temp_stats = data['Apparent Temperature (C)'].describe()
insights.append(apparent_temp_stats)


# Print or use insights as needed
for i, insight in enumerate(insights, start=1):
    print(f"Insight {i}:")
    print(insight)
    print("\n")
