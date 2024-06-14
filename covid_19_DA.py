import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load COVID-19 dataset
covid_data = pd.read_csv("c19p/covid_19_clean_complete.csv")

# Data preprocessing
covid_data['Date'] = pd.to_datetime(covid_data['Date'])
covid_data['Month'] = covid_data['Date'].dt.to_period('M')

# Data quality assessment and preprocessing
# Handling missing values
covid_data.dropna(inplace=True)

# Handling outliers
# Assuming outliers are removed based on domain knowledge or statistical methods

# Feature engineering
covid_data['Mortality Rate'] = covid_data['Deaths'] / covid_data['Confirmed']

# Exploratory Data Analysis (EDA)
# Statistical summaries
summary_statistics = covid_data.describe()

# Data visualization
plt.figure(figsize=(12, 8))

# Line plot for COVID-19 cases, deaths, and recoveries over time
plt.subplot(2, 2, 1)
sns.lineplot(data=covid_data, x='Month', y='Confirmed', label='Confirmed Cases')
sns.lineplot(data=covid_data, x='Month', y='Deaths', label='Deaths')
sns.lineplot(data=covid_data, x='Month', y='Recovered', label='Recovered')
plt.title('COVID-19 Cases, Deaths, and Recoveries Over Time')
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

# Save summary statistics to a CSV file
summary_statistics.to_csv("summary_statistics.csv", index=True)
