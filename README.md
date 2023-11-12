# NISR Labour Force Dashboard

This Streamlit dashboard utilizes data from three CSV files originall gotten from the [NISR website]([url](https://www.statistics.gov.rw/publication/2002)): `16+ years_LF_data.csv` and `Labour Force data.csv`. The data provides insights into labor force participation dynamics by different indicator types.

## Data Sources

### 1. 16+ years_LF_data.csv
This dataset includes information related to education, marital status, sex, rural/urban areas, and more. The indicators cover aspects such as labor force participation rate, unemployment rate, and various employment-related metrics.

### 2. Labour Force data.csv
This dataset categorizes information based on the employed and unemployed population, including economic activity, educational level, age groups, employment type, and hours worked. It provides a detailed breakdown of the population in terms of male and female, urban and rural and subsistence agriculture participation and subsistence agriculture non-participation.

## Key Metrics

The dashboard communicates key labor force indicators, including:
- **Labor Force Participation Rate**
- **Labour Underutilization**
- **Time-Related Underemployment**
- **Median Monthly Earnings at Main Job**

## Interacting with the Dashboard

### Filters
1. **Section 1 Filters**
   - Choose a group from the dropdown: Education, Marital Status, Sex_RA (Sex and Regional Area).
   - Select specific indicators related to the chosen group.

2. **Section 2 Filters**
   - Choose a population type filter from the dropdown (Employed & Unemployed).
   - Select a specific indicator based on the chosen data type (economic activity, educational level, age groups, employment type, and hours worked).

### Visualizations

#### 1. Section 1 Visualizations
   a. **Chart 1: Employment to Population Ratio, LF Participation Rate, and Unemployment Rate**
   - Displays trends for selected indicators.
   
   b. **Chart 2: Labour Force, Employed, Out of LF, and Unemployed Stats**
   - Provides insights into the average values for various labor-related metrics.

#### 2. Section 2 Visualizations
   a. **Chart 3: Male and Female Population Comparison**
   - Compares the male and female populations for selected indicators.

   b. **Chart 4: Urban and Rural Population Variation**
   - Illustrates the variation in population between urban and rural areas.

   c. **Chart 5: Subsistence Agriculture Participation**
   - Highlights the participation in subsistence agriculture.

## Running the Dashboard

1. Ensure you have Streamlit installed: `pip install streamlit`.
2. Run the app: `streamlit run main.py`.
3. Interact with the filters and explore the visualizations.

Feel free to explore the labor force data dynamically and gain valuable insights!
