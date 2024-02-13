import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load COVID-19 dataset
covid_data = pd.read_csv("c19p/covid_19_clean_complete.csv")

# Data preprocessing
# Assuming columns: 'Date', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'WHO Region'
covid_data['Date'] = pd.to_datetime(covid_data['Date'])
covid_data['Month'] = covid_data['Date'].dt.to_period('M')

# Aggregate data by month
covid_data_monthly = covid_data.groupby('Month').agg({
    'Confirmed': 'sum', 
    'Deaths': 'sum', 
    'Recovered': 'sum',
    'Active': 'sum'
}).reset_index()

# Data visualization
plt.figure(figsize=(12, 8))

# Line plot for COVID-19 cases and deaths over time
plt.subplot(2, 2, 1)
plt.plot(covid_data_monthly['Month'].dt.to_timestamp(), covid_data_monthly['Confirmed'], label='Confirmed Cases', color='blue')
plt.plot(covid_data_monthly['Month'].dt.to_timestamp(), covid_data_monthly['Deaths'], label='Deaths', color='red')
plt.plot(covid_data_monthly['Month'].dt.to_timestamp(), covid_data_monthly['Recovered'], label='Recovered', color='green')
plt.title('COVID-19 Cases and Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid(True)

# Bar plot showing distribution of cases and deaths by country
country_data = covid_data.groupby('Country/Region').agg({
    'Confirmed': 'max',
    'Deaths': 'max'
}).reset_index()
country_data = country_data.sort_values(by='Confirmed', ascending=False).head(10)  # Top 10 countries
plt.subplot(2, 2, 2)
sns.barplot(data=country_data, x='Confirmed', y='Country/Region', color='blue', label='Confirmed Cases')
sns.barplot(data=country_data, x='Deaths', y='Country/Region', color='red', label='Deaths')
plt.title('Top 10 Countries by COVID-19 Cases and Deaths')
plt.xlabel('Count')
plt.ylabel('Country/Region')
plt.legend()

# Pie chart illustrating percentage of cases and deaths across different continents
continent_data = covid_data.groupby('WHO Region').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum'
}).reset_index()
plt.subplot(2, 2, 3)
plt.pie(continent_data['Confirmed'], labels=continent_data['WHO Region'], autopct='%1.1f%%', colors=sns.color_palette('viridis', len(continent_data)))
plt.title('Percentage of COVID-19 Cases by Continent')

plt.subplot(2, 2, 4)
plt.pie(continent_data['Deaths'], labels=continent_data['WHO Region'], autopct='%1.1f%%', colors=sns.color_palette('viridis', len(continent_data)))
plt.title('Percentage of COVID-19 Deaths by Continent')

plt.tight_layout()
plt.show()
