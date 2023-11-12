import streamlit as sl
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Import the datasets
df1 = pd.read_csv('16+ years_LF_data.csv')
df2 = pd.read_csv('Labour Force data.csv')
df3 = pd.read_csv('LF Summary Data.csv')


# Page configuations
sl.set_page_config(page_title= "NISR Labour Force Dashboard",
                    page_icon= ":bar_chart:",
                    layout= "wide")


# ----SIDEBAR----


# ----MAIN PAGE----

# Title
sl.title(':bar_chart: NISR LABOR FORCE DASHBOARD')
sl.markdown('### :grey[Labor Force Participation Dynamics by Different Indicator Types]')


#--------
# Top KPI's
lfp = df3.loc[(df3["Indicator type"] == "Summ LF Indicators") & (df3["Indicator"] == "Labour force participation rate(%)"), "Total"].values[0]
lu = df3.loc[(df3["Indicator type"] == "Summ LF Indicators") & (df3["Indicator"] == "LU4 - Composite measure of labour underutilization(%)"), "Total"].values[0]
tru = df3.loc[(df3["Indicator type"] == "Summ LF Indicators") & (df3["Indicator"] == "Time related underemployment rate(%)"), "Total"].values[0]
mme = df3.loc[(df3["Indicator type"] == "Summ LF Indicators") & (df3["Indicator"] == "Median monthly earnings at main job"), "Total"].values[0]
mme = int(mme)

sl.markdown("##")

lfp_metric, lu_metric, tru_metric, mme_metric = sl.columns(4)
lfp_metric.metric(label=":grey[Labor Force Participation]", value="{:.2f}%".format(lfp))
lu_metric.metric(label= ":grey[Labour Underutilization]", value= f"{lu:.2f}%")
tru_metric.metric(label= ":grey[Time Related Underemployment]", value= f"{tru:.2f}%")
mme_metric.metric(label= ":grey[Median Monthly Earnings (at main job)]", value= f"{mme:,}")

sl.divider()
sl.markdown("##")
sl.markdown("##")


#------
# Section 1
# Filter 1 (16+ years_LF_data)
group_indicators = {}
for group, indicators in df1.groupby("Group")["Indicator type"].unique().items():
    group_indicators[group] = indicators.tolist()

text_col1, left_filter1, right_filter1 = sl.columns([1,2,5])
with text_col1:
    sl.markdown("")
    sl.markdown("")
    sl.caption("Filters:")

selected_group1 = left_filter1.selectbox("", 
                                          options=list(group_indicators.keys()))

# Get selected indicators based on the selected group
selected_indicators1 = group_indicators[selected_group1]

# Multi-Select for Indicator Type
selected_indicator1 = right_filter1.multiselect("", 
                                               options=selected_indicators1, 
                                               default=selected_indicators1)

# Filter dataframe based on selected_group and selected_indicator
filtered_df1 = df1[(df1["Group"] == selected_group1) & (df1["Indicator type"].isin(selected_indicator1))]



#--------
# Chart 1 (Employment to Population Ratio, Labour Force Participation Rate, and Unemployment Rate Chart)
# Calculate the average Employment to pop. ratio, LF Participation Rate and Unemployment Rate
average_employment_pop_rate = filtered_df1.groupby('Indicator')['Employment to pop. ratio'].mean().reset_index()
average_lf_participation_rate = filtered_df1.groupby('Indicator')['LF participation rate'].mean().reset_index()
average_unemployment_rate = filtered_df1.groupby('Indicator')['Unemployment rate'].mean().reset_index()

chart1 = px.bar(average_employment_pop_rate, x='Indicator', y="Employment to pop. ratio",
            labels={'Employment to pop. ratio': 'Employment to Population Ratio'},
            height=600, width=500, template='plotly_white')

chart1.update_layout(
                    plot_bgcolor= "rgba(0,0,0,0)",
                    yaxis= (dict(showgrid=False)) 
)

line1_trace = px.line(average_lf_participation_rate, x='Indicator', y=["LF participation rate"]).data[0]
line1_trace.line.color = 'darkblue'

line2_trace = px.line(average_unemployment_rate, x='Indicator', y=["Unemployment rate"]).data[0]
line2_trace.line.color = 'red'

chart1.add_trace(line1_trace)
chart1.add_trace(line2_trace)


#--------
# Chart 2 (Labour force, Employed, Out of LF and Unemployed Stats)
# Calculate the average Labour force, Employed, Out of LF and Unemployed
average_labour_force = filtered_df1.groupby('Indicator')['Labour force'].mean().reset_index()
average_employed = filtered_df1.groupby('Indicator')['Employed'].mean().reset_index()
average_out_of_lf = filtered_df1.groupby('Indicator')['Out of LF'].mean().reset_index()
average_unemployed = filtered_df1.groupby('Indicator')['Unemployed'].mean().reset_index()

chart2 = px.bar(average_labour_force, x='Indicator', y="Labour force",
            labels={'Labour force': 'Labour force'},
            height=600, width=500, template='plotly_white'
            )

chart2.update_layout(
                    plot_bgcolor= "rgba(0,0,0,0)",
                    yaxis= (dict(showgrid=False)) 
                    )

chart2_line1_trace = px.line(average_employed, x='Indicator', y=["Employed"]).data[0]
chart2_line1_trace.line.color = 'darkblue'

chart2_line2_trace = px.line(average_out_of_lf, x='Indicator', y=["Out of LF"]).data[0]
chart2_line2_trace.line.color = 'orange'

chart2_line3_trace = px.line(average_unemployed, x='Indicator', y=["Unemployed"]).data[0]
chart2_line3_trace.line.color = 'red'

chart2.add_trace(chart2_line1_trace)
chart2.add_trace(chart2_line2_trace)
chart2.add_trace(chart2_line3_trace)

# Diplay Charts in 2 columns
left, right = sl.columns(2)
# Filter dataframe based on selected_group and selected_indicator
filtered_df1 = df1[(df1["Group"] == selected_group1) & (df1["Indicator type"].isin(selected_indicator1))]

with left:
    sl.plotly_chart(chart1)

with right:
    sl.plotly_chart(chart2)



#-----
# Section 2
sl.markdown("##")
sl.divider()
sl.markdown("##")

# Filter 2 (Labour Force data)
datatype_indicators = {}
for data_type, indicator_types in df2.groupby("Data type")["Indicator type"].unique().items():
    datatype_indicators[data_type] = indicator_types.tolist()

text_col2, left_filter2, right_filter2 = sl.columns([1,2,5])
with text_col2:
    sl.markdown("")
    sl.markdown("")
    sl.caption("Filters:")

selected_group2 = left_filter2.selectbox("", 
                                          options=list(datatype_indicators.keys()))

# Get selected indicators based on the selected group
selected_indicators2 = datatype_indicators[selected_group2]

# Multi-Select for Indicator Type
selected_indicator2 = right_filter2.selectbox("", 
                                               options=selected_indicators2)

# Filter dataframe based on selected_group and selected_indicator
filtered_df2 = df2[(df2["Data type"] == selected_group2) & (df2["Indicator type"] == selected_indicator2)]

#--------
# Chart 3
filtered_df2_sorted_chart3 = filtered_df2.sort_values(by='Male', ascending=True)

chart3 = px.bar(filtered_df2_sorted_chart3, x=['Male', 'Female'], y='Indicator', orientation='h',
             labels={'Male': 'Female', 'Male': 'Female'},
             title='Male and Female Population Comparison',
             barmode='group', width=1200, height=500, template='plotly_white')

chart3.update_layout(
                    plot_bgcolor= "rgba(0,0,0,0)",
                    xaxis= (dict(showgrid=False)) 
)

# Display the chart in Streamlit
sl.plotly_chart(chart3)


#--------
# Chart 4
filtered_df2_sorted_chart4 = filtered_df2.sort_values(by='Urban area', ascending=True)

chart4 = px.bar(filtered_df2_sorted_chart4, x=['Urban area', 'Rural area'], y='Indicator', orientation='h',
             labels={'Urban area': 'Rural area', 'Urban area': 'Rural area'},
             title='Urban and Rural Population Variation',
             barmode='group', width=1200, height=500, template='plotly_white')

chart4.update_layout(
                    plot_bgcolor= "rgba(0,0,0,0)",
                    xaxis= (dict(showgrid=False)) 
)

# Display the chart in Streamlit
sl.plotly_chart(chart4)


#--------
# Chart 5
filtered_df2_sorted_chart5 = filtered_df2.sort_values(by='Subsistence agriculture non-', ascending=True)

chart5 = px.bar(filtered_df2_sorted_chart4, x=['Subsistence agriculture non-', 'Subsistence agriculture participation'], y='Indicator', orientation='h',
             labels={'Subsistence agriculture non-participation': 'Subsistence agriculture participation', 'Subsistence agriculture participation': 'Subsistence agriculture non-'},
             title='Subsistence Agriculture Participation',
             barmode='group', width=1200, height=500, template='plotly_white')

chart5.update_layout(
                    plot_bgcolor= "rgba(0,0,0,0)",
                    xaxis= (dict(showgrid=False)) 
)

# Display the chart in Streamlit
sl.plotly_chart(chart5)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
sl.markdown(hide_st_style, unsafe_allow_html=True)
