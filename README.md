# COVID-19 Data Analysis and Visualization

This Python program analyzes and visualizes COVID-19 data using the Pandas, Matplotlib, and Seaborn libraries. The program performs data preprocessing, aggregates data, and generates various visualizations to understand the trends and distribution of COVID-19 cases and deaths.

## Data Source
The COVID-19 dataset used in this project is obtained from [source](https://github.com/CSSEGISandData/COVID-19) provided by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University. The dataset is regularly updated and provides comprehensive information on confirmed cases, deaths, and recoveries across various countries and regions.

## Libraries Used
- Pandas: For data manipulation and analysis.
- Matplotlib: For creating static, animated, and interactive visualizations in Python.
- Seaborn: For statistical data visualization based on Matplotlib.

## Flow of the Program

### 1. Data Loading
The program loads the COVID-19 dataset from a CSV file named "covid_19_clean_complete.csv" into a Pandas DataFrame.

### 2. Data Preprocessing
- The 'Date' column is converted to datetime format.
- A new column 'Month' is created by extracting the month from the 'Date' column.
- The data is aggregated monthly, summing up the columns 'Confirmed', 'Deaths', 'Recovered', and 'Active'.

### 3. Data Visualization
The program generates various visualizations to analyze the COVID-19 data:

#### Line Plot (COVID-19 Cases and Deaths Over Time)
- Plots the total number of confirmed cases, deaths, and recoveries over time.
- X-axis: Date
- Y-axis: Count
- Each line represents the trend of confirmed cases, deaths, and recoveries over time.

#### Bar Plot (Top 10 Countries by COVID-19 Cases and Deaths)
- Shows the distribution of COVID-19 cases and deaths for the top 10 countries with the highest confirmed cases.
- X-axis: Count
- Y-axis: Country/Region
- Two bars are plotted for each country, representing confirmed cases and deaths.

#### Pie Chart (Percentage of COVID-19 Cases and Deaths by Continent)
- Illustrates the percentage distribution of COVID-19 cases and deaths across different continents.
- Two pie charts are plotted, one for cases and one for deaths.
- Each slice of the pie represents a continent, and its size represents the percentage of cases or deaths.

## Running the Program
To run the program:
1. Ensure you have Python installed on your system.
2. Install the required libraries using `pip install pandas matplotlib seaborn`.
3. Download the COVID-19 dataset and save it as "covid_19_clean_complete.csv" in the same directory as the script.
4. Run the Python script.

## Output
The program generates visualizations depicting the trends and distribution of COVID-19 cases and deaths, providing insights into the global impact of the pandemic.

