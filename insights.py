import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'weatherHistory.csv'
data = pd.read_csv(file_path)

# Display basic info about the dataset
print("Dataset info before preprocessing:")
print(data.info())

# Handling missing values
def fill_nan_based_on_datatype(column):
    if column.dtype == 'object':
        return column.fillna('Not available')
    elif column.dtype in ['int64', 'float64', 'int32', 'float32', 'bool']:
        return column.fillna(0)
    else:
        return column


# Convert 'Formatted Date' column to datetime format
data['Formatted Date'] = pd.to_datetime(data['Formatted Date'], utc=True)
# Extracting date components
data['Year'] = data['Formatted Date'].dt.year
data['Month'] = data['Formatted Date'].dt.month
data['Day'] = data['Formatted Date'].dt.day
data['Hour'] = data['Formatted Date'].dt.hour

missing_values = data.isnull().sum()
data = data.apply(fill_nan_based_on_datatype)

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

insights = []

# 1. Shape of the dataframe
insights.append(data.shape)

# 2. Summary statistics
summary_stats = data.describe()
insights.append(summary_stats)

# 3. Checking for missing values
insights.append(missing_values)

# 4. Checking unique values in a column (e.g., 'Summary')
unique_values_summary = data['Summary'].unique()
insights.append(unique_values_summary)

# 5. Correlation matrix between numerical columns
numerical_data = data.select_dtypes(include=[np.number]) # type: ignore
correlation_matrix = numerical_data.corr()
insights.append(correlation_matrix)

# 6. Average humidity by 'Summary'
avg_humidity_summary = data.groupby('Summary')['Humidity'].mean()
insights.append(avg_humidity_summary)

# 7. Busiest period by 'Formatted Date'
busy_period = data['Formatted Date'].dt.to_period('M').value_counts().idxmax()
insights.append(busy_period)

# 8. Variance of 'Pressure (millibars)' across different 'Summary' types
pressure_variance = data.groupby('Summary')['Pressure (millibars)'].var()
insights.append(pressure_variance)

# 9. Top 5 windiest days
top_windiest_days = data.nlargest(5, 'Wind Speed (km/h)')[['Formatted Date', 'Wind Speed (km/h)']]
insights.append(top_windiest_days)

# 10. Mean temperature by 'Precip Type'
mean_temp_precip = data[data['Precip Type']!= 'Not available'].groupby('Precip Type')['Temperature (C)'].mean()
insights.append(mean_temp_precip)

# 11. Daily summary with the longest text
max_summary_length = data.loc[data['Daily Summary'].str.len().idxmax(), 'Daily Summary']
insights.append(max_summary_length)

# 12. Day with the highest visibility
max_visibility_day = data.loc[data['Visibility (km)'].idxmax(), 'Formatted Date']
insights.append(max_visibility_day)

# 13. Proportion of different 'Precip Type'
filtered_data = data[data['Precip Type'] != 'Not available']
precip_type_proportion = filtered_data['Precip Type'].value_counts(normalize=True)
insights.append(precip_type_proportion)

# 14. Hourly Temperature trend
hourly_temp_trend = data.groupby('Hour')['Temperature (C)'].mean()
insights.append(hourly_temp_trend)

# 15 . Average Temperature by Month
avg_temp_by_month = data.groupby('Month')['Temperature (C)'].mean()
insights.append(avg_temp_by_month)

# 16. Count of different 'Summary' values
summary_counts = data['Summary'].value_counts()
insights.append(summary_counts)

# 17. Maximum Humidity recorded
max_humidity = data['Humidity'].max()
insights.append(max_humidity)

# 18. Daily Summary occurrences
daily_summary_counts = data['Daily Summary'].value_counts()
insights.append(daily_summary_counts)

# 19. Monthly average visibility
monthly_avg_visibility = data.groupby('Month')['Visibility (km)'].mean()
insights.append(monthly_avg_visibility)

# 20. Range of Pressure values
pressure_range = data['Pressure (millibars)'].max() - data['Pressure (millibars)'].min()
insights.append(pressure_range)

# 21. Hourly Wind Speed statistics
hourly_wind_speed_stats = data.groupby('Hour')['Wind Speed (km/h)'].describe()
insights.append(hourly_wind_speed_stats)

# 22. Proportion of days with Loud Cover
loud_cover_proportion = (data['Loud Cover'].sum() / len(data)) * 100
insights.append(loud_cover_proportion)

# 23. Summary statistics of Apparent Temperature
apparent_temp_stats = data['Apparent Temperature (C)'].describe()
insights.append(apparent_temp_stats)

insight_descriptions = [
    "Shape of the dataframe",
    "Summary statistics",
    "Missing values",
    "Unique values in 'Summary' column",
    "Correlation matrix",
    "Average humidity by 'Summary'",
    "Busiest period by 'Formatted Date'",
    "Variance of 'Pressure (millibars)' by 'Summary'",
    "Top 5 windiest days",
    "Mean temperature by 'Precip Type'",
    "Daily summary with the longest text",
    "Day with the highest visibility",
    "Proportion of different 'Precip Type'",
    "Mean temperature for each hour of the day",
    "Mean temperature for each month",
    "Number of occurrences for each weather summary",
    "Maximum humidity value in the dataset",
    "Count of occurrences for each daily summary",
    "Mean visibility for each month",
    "Difference between the maximum and minimum pressure values",
    "Descriptive statistics for wind speed grouped by hour",
    "Percentage of days with loud cover",
    "Descriptive statistics for apparent temperature"
]

# Associate insights with their descriptions
insights_with_descriptions = list(zip(insight_descriptions, insights))

for i, (description, insight) in enumerate(insights_with_descriptions, start=1):
    print(f"Insight {i}:{description}")
    print(insight)
    print("\n")