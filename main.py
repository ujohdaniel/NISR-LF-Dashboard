import streamlit as sl
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Import the datasets
df2 = pd.read_csv('maps.csv')
df3 = pd.read_csv('LF_Year_Summary.csv')
df4 = pd.read_csv('Population_Data.csv')
df5 = pd.read_csv('Economic_activities.csv')

# Page configuations
sl.set_page_config(page_title= "NISR Labour Force Dashboard",
                    page_icon= ":bar_chart:",
                    layout= "wide")

print("working")
# ----SIDEBAR----

with open("styles.css", "r") as f:
    sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# ----MAIN PAGE----

# Title
sl.title(':bar_chart: NISR LABOR FORCE UNDERUTILIZATION DASHBOARD')
sl.markdown(':grey[Exploring Labor Force Underutilization in Rwanda with Reference to the "Labour Market Trend Analysis Brief 2016-2020" ]')


#----------
# Section 1
# Top KPI's
sl.markdown("##")
sl.markdown("#### :red[Labor Underutilization]")

kpi1 = df3.loc[(df3["Year"] == 2019) & (df3["Indicators"] == "LU4 - Composite measure of labour underutilization(%)"), "Total"].values[0]
kpi2 = df3.loc[(df3["Year"] == 2021) & (df3["Indicators"] == "LU4 - Composite measure of labour underutilization(%)"), "Total"].values[0]
kpi3 = df3.loc[(df3["Year"] == 2022) & (df3["Indicators"] == "LU4 - Composite measure of labour underutilization(%)"), "Total"].values[0]

kpi1_col, kpi2_col, kpi3_col = sl.columns(3)

kpi1_col.metric(label="2019", value= f"{kpi1}%")
kpi2_col.metric(label="2021", value= f"{kpi2}%")
kpi3_col.metric(label="2022", value= f"{kpi3}%")

sl.divider()
sl.markdown("##")

#----------
# Sidebar
col1, col2 = sl.columns([1, 3])

col1.markdown("##")
col1.caption('Labor Underutilization categories:')

selected_chart = col2.selectbox(" ", ["Potential Labour Force", "Time Related Underemployment Rate", "Unemployment Rate"])

sl.markdown("##")

# Filter data based on the selected chart
if selected_chart == "Potential Labour Force":

    # Potential Labour Force
    sl.markdown("#### :red[Potential Labour Force by Year]")
    sl.caption('What has happened since the recommendations were made? Has it gotten better or worse?')

    # Filter data for the specific indicator
    potential_lf = df3[(df3["Indicators"] == "Potential labour force")]

    # Create a line chart using Plotly Express
    chart2 = px.bar(potential_lf, x="Year", y="Total", text='Total', orientation='v',
                height= 500, title="Potential labor force Over Years (millions)")

    chart2.update_xaxes(tickmode='linear', dtick=1)
    chart2.update_traces(textposition='outside')
    chart2.update_layout(xaxis_title="Year", yaxis_title="Potential labour force  (millions)")

    # Display the chart using Streamlit
    sl.plotly_chart(chart2)

    sl.caption('The overall decline in the potential labor force from 2019 - 2022 could have either a positive or negative outlook depending on Rwanda\'s Economic Goals and on the cause of the decline, which could be as a result of retirement, demographic shifts and more.')

elif selected_chart == "Time Related Underemployment Rate":

    # Time related underemployment rate
    sl.markdown("#### :red[Time related underemployment rate(%) by Year]")
    sl.caption('What has happened since the recommendations were made? Has it gotten better or worse?')

    # Filter data for the specific indicator
    timerelated_ur = df3[(df3["Indicators"] == "Time related underemployment rate(%)")]

    # Create a line chart using Plotly Express
    chart3 = px.bar(timerelated_ur, x="Year", y="Total", text='Total', orientation='v',
                height= 500, title="Time related underemployment rate(%) Over Years")
    chart3.update_xaxes(tickmode='linear', dtick=1)
    chart3.update_traces(textposition='outside')
    chart3.update_layout(xaxis_title="Year", yaxis_title="Time related underemployment rate(%)")

    # Display the chart using Streamlit
    sl.plotly_chart(chart3)

    sl.caption('This illustrates the fraction of the employed working population willing to take up more working hours. With an increase from 2019 - 2020, the potential culprit could be the availabilty of full-time employment. In addition to this, the 2020 market brief underscores limited market and a general perception that farming is unprofitable and unattractive, and not desirable for those with higher education levels, among others (RDB, 2020).')


else:

    # Unemployment Rate
    sl.markdown("#### :red[Unemployment Rate by Year]")
    sl.caption('What has happened since the recommendations were made? Has it gotten better or worse?')

    # Filter data for the specific indicator
    unemployment_rate = df3[(df3["Indicators"] == "LU1 - Unemployment rate(%)")]

    # Create a line chart using Plotly Express
    chart1 = px.bar(unemployment_rate, x="Year", y="Total", text='Total', orientation='v',
                height= 500, title="Unemployment rate(%) Over Years")
    chart1.update_xaxes(tickmode='linear', dtick=1)
    chart1.update_traces(textposition='outside')
    chart1.update_layout(xaxis_title="Year", yaxis_title="Unemployment Rate (%)")

    # Display the chart using Streamlit
    sl.plotly_chart(chart1)

    sl.caption('From a distance, the spike in unemployment rate is imperative. Irrespective of strategies and priorities, reducing unemployment is a common goal for most countries, as it contributes to economic stability and social wellbeing. A decline in unemloyment rates in 2022 with respect to 2021, Rwanda\'s road to recovery post Covid-19 is well on track yet much is left to be done. So what is the case with Rwanda\'s unemployment rate?')
    sl.divider()


    sl.markdown("#### :red[Comparing the industries that employ most to the in-demand skills from the labour force]")
    sl.caption('Do graduates still lack skills that are in demad in the job market?')


    # Columns for Economic activity and Skills
    economic_act_col, skills_col = sl.columns([3, 2])

    # Economic activity
    # Filter the data for the specific indicator type and sort the top 5 economic activities for each year
    economic_act = df3[df3["Indicator type"] == "Economic activity"]
    economic_act['Total'] = economic_act['Total'].str.replace(',', '').astype(float)
    top4_activities = economic_act.groupby(["Year", "Indicators"]).sum().reset_index()
    top4_activities = top4_activities.groupby("Year").apply(lambda x: x.nlargest(3, "Total")).reset_index(drop=True)

    # Create a grouped column bar chart using Plotly Express
    chart4 = px.bar(top4_activities, x="Year", y="Total", color="Indicators", text='Total', width=900, height=600, 
                title="Top 3 Economic Activities by Year", barmode="group", labels={"Total": "Total Value", "Indicators": "Economic Activity"})

    # Customize the layout
    chart4.update_layout(xaxis_title="Year", yaxis_title="Value (millions)", legend_title="Economic Activity")
    chart4.update_traces(textposition='outside')

    # Display the chart using Streamlit
    economic_act_col.plotly_chart(chart4)
    sl.divider()


    # Filter for skills
    selected_chart1 = skills_col.selectbox(" ", ["Field of education", "Technical skills"])

    if selected_chart1 == "Field of education":
        # Field of education
        # Filter the data for the specific indicator type
        educational_field = df4[df4["Indicator type"] == "Field of education"]
        educational_field['Total'] = educational_field['Total'].str.replace(',', '').astype(float)

        total_value = educational_field.loc[educational_field['Indicator'] == 'Total', 'Total'].values[0]

        # Drop the "No Education" row
        educational_field = educational_field[(educational_field["Indicator"] != "No Education") & (educational_field["Indicator"] != "Total") & (educational_field["Indicator"] != "General program")]

        # Calculate the percentage of each value in the "Total" column relative to the "Total" row
        educational_field['Total Percentage'] = educational_field['Total'] / total_value * 100

        # Create a donut chart using Plotly Express
        Chart5 = px.pie(
            educational_field, values='Total Percentage', names='Indicator', hole=0.3, title="Percentage Distribution of Educational Fields",
            labels={'Total Percentage': 'Percentage of Total'}, width=600, height=600
        )

        # Display the chart using Streamlit
        skills_col.plotly_chart(Chart5)

    elif selected_chart1 == "Technical skills":
        # Technical skills
        # Filter the data for the specific indicator type
        technical_skills = df4[df4["Indicator type"] == "Technical skills"]
        technical_skills['Total'] = technical_skills['Total'].str.replace(',', '').astype(float)

        total_skills = technical_skills.loc[technical_skills['Indicator'] == 'Total', 'Total'].values[0]

        # Drop the "No Education" row
        technical_skills = technical_skills[technical_skills["Indicator"] != "Total"]

        # Map specific skills to categories
        skill_to_category = {
            "Masonry": "Building and Construction",
            "Carpentry": "Building and Construction",
            "Civil engeneering": "Building and Construction",
            "Industrial electricity": "Building and Construction",
            "Domestic Electricity": "Building and Construction",
            "Welding": "Building and Construction",
            "Plumbing": "Building and Construction",
            "Concrete masonry": "Building and Construction",
            "Automotive technology.": "Automotive",
            "Automotive body repair": "Automotive",
            "Auto- Electricity": "Automotive",
            "Engine mechanics": "Automotive",
            "Motor vehicle engine mechanics": "Automotive",
            "Computer maintenance": "Information Technology",
            "Networking": "Information Technology",
            "Software Development": "Information Technology",
            "Crop production": "Agriculture",
            "Nursery growing": "Agriculture",
            "Horticulture production": "Agriculture",
            "Livestock": "Agriculture",
            "Agri-Business": "Agriculture",
            "Culinary arts": "Food and Beverage",
            "Food processing": "Food and Beverage",
            "Food & Beverage services": "Food and Beverage",
            "Milk processig": "Food and Beverage",
            "Animal health": "Health and Beauty",
            "Hairdressing": "Health and Beauty",
            "Manicure and Pedicure": "Health and Beauty",
            "Beauty therapy": "Health and Beauty",
            "Sport and Medical Massage": "Health and Beauty",
            "NCDs and Palliative Care Community Health": "Health and Beauty",
            "Crochet embroidery": "Art and Design",
            "Pottery": "Art and Design",
            "Painting and decoration": "Art and Design",
            "Multimedia": "Art and Design",
            "Screen printing": "Art and Design",
            "Leather craft": "Art and Design",
            "Biding and Jewelries": "Art and Design",
            "Film making": "Art and Design",
            "Colleography": "Art and Design",
            "Typing(dactilographie)": "Art and Design",
            "Tailoring": "Art and Design",
            "Music": "Others",
            "Networking": "Others",
            "Front office": "Others",
            "House keeping": "Others",
            "Driving": "Others",
            "Other": "Others"
        }

        # Add a new column 'Category' based on the mapping
        technical_skills['Category'] = technical_skills['Indicator'].map(skill_to_category)
        print(technical_skills['Category'])

        # Calculate the percentage of each value in the "Total" column relative to the "Total" row
        technical_skills['Total Percentage'] = technical_skills['Total'] / total_skills * 100

        # Create a donut chart using Plotly Express
        Chart6 = px.pie(
            technical_skills, values='Total Percentage', names='Category', hole=0.3, labels={'Total Percentage': 'Percentage of Total'}, 
            title= "Percentage Distribution of Technical Skills by Category", width=500, height=500
        )

        # Display the chart using Streamlit
        skills_col.plotly_chart(Chart6)

    sl.caption("The 2022 market brief highlights the lack of market relevance skills possesed by Upper Secondary and University Students as one of the causes of unemployment. To this end, exploring the top 3 employment activities in relation to the education and training received, agriculture despite being the activity with the most employment, remains the least studied course/training. However without a proper understanding of the agricultural sector much is left unanswered.")
    sl.divider()


    # Informal and Formal Sectors
    sl.markdown("#### :red[Formal and Informal employment by Economic activities]")
    sl.caption('What are the dynamics of the Economic activities and how can they influece unemployment?')

    sector = df5.sort_values(by='Informal employment', ascending=True)
    sector['Formal employment'] = sector['Formal employment'].str.replace(',', '').astype(float)
    sector['Informal employment'] = sector['Informal employment'].str.replace(',', '').astype(float)

    # Drop the "Total" row
    sector = sector[sector["Economic activity"] != "Total"]

    chart7 = px.bar(sector, x=['Formal employment', 'Informal employment'], y='Economic activity', orientation='h',
                labels={'Formal employment': 'Informal employment', 'Formal employment': 'Informal employment'},
                title='Formal employment and Informal employment Population Comparison',
                barmode='group', width=1200, height=500, template='plotly_white')

    chart7.update_layout(xaxis_title="Value (millions)", yaxis_title="Economic activities",
                        plot_bgcolor= "rgba(0,0,0,0)",
                        xaxis= (dict(showgrid=False)) 
    )

    # Display the chart in Streamlit
    sl.plotly_chart(chart7)

    sl.caption(f"According to the graph above, over 90\% of employment in agriculture falls in the informal sector. This leaves the question, how can we drive formal employment in agriculture?")
    sl.divider()


    # Informal and Formal Sectors
    sl.markdown("#### :red[Geographical representation of employment in the agriculture]")
    sl.caption('How can we create specific policies for different districts in Rwanda to mordernize agriculture and improve the perception around agriculture?')

    sl.markdown("##")
    sl.markdown("##### Coming soon...")
