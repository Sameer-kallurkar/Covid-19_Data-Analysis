# COVID-19 Data Analysis and Visualization

This Python program analyzes and visualizes COVID-19 data using the Pandas, Matplotlib, and Seaborn libraries. The program performs comprehensive data preprocessing, including handling missing values and outliers, and conducts exploratory data analysis (EDA) to derive insights from the data. 

## Data Source
The COVID-19 dataset used in this project is obtained from [source](https://github.com/CSSEGISandData/COVID-19) provided by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University. The dataset provides comprehensive information on confirmed cases, deaths, and recoveries across various countries and regions.

## Libraries Used
- Pandas: For data manipulation and analysis.
- Matplotlib: For creating static, animated, and interactive visualizations in Python.
- Seaborn: For statistical data visualization based on Matplotlib.

## Flow of the Program

### 1. Data Loading and Preprocessing
- The program loads the COVID-19 dataset from a CSV file named "covid_19_clean_complete.csv" into a Pandas DataFrame.
- Data preprocessing steps include converting the 'Date' column to datetime format, handling missing values, and performing feature engineering to calculate the mortality rate.

### 2. Exploratory Data Analysis (EDA)
- Statistical summaries are generated to describe the distribution of COVID-19 cases and deaths.
- Various visualizations, including line plots, bar plots, and pie charts, are created to analyze trends and distribution of COVID-19 cases and deaths.

### 3. Output
- The program generates visualizations depicting the trends and distribution of COVID-19 cases and deaths, providing insights into the global impact of the pandemic.
- Summary statistics are saved to a CSV file named "summary_statistics.csv" for further analysis.

## Running the Program
To run the program:
1. Ensure you have Python installed on your system.
2. Install the required libraries using `pip install pandas matplotlib seaborn`.
3. Download the COVID-19 dataset and save it as "covid_19_clean_complete.csv" in the same directory as the script.
4. Run the Python script.

## Conclusion
This analysis provides valuable insights into the trends and distribution of COVID-19 cases and deaths worldwide. By leveraging comprehensive data preprocessing and exploratory data analysis techniques, we gain a deeper understanding of the global impact of the pandemic.

For further analysis, refer to the summary statistics saved in the "summary_statistics.csv" file.
