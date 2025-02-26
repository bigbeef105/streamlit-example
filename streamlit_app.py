from collections import namedtuple
import altair as alt
import math
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
csv = convert_df(df)

"""
# Welcome Shakira!

The below level one data science dashboard should be compatible with your device files.

"""

number = st.number_input('Define smoothing window size..', value=3)
number2 = st.number_input('Plot window size', value=len(df))


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, skiprows=3)
  df.drop(df.tail(1).index,inplace=True)
  df['Date-Time'] =  pd.to_datetime(df['Date-Time'], format='%m/%d/%y %H:%M:%S.%f')
  csv = convert_df(df)
  st.write(df)

# Add some matplotlib code !
#   df_shortened = df.head(number2)

  fig = px.line(        
        df, #Data Frame
        x = "Date-Time", #Columns from the data frame
        y = "Weight(g)",
        title = "Weight"
    )
  fig.update_traces(line_color = "maroon")
  st.plotly_chart(fig)
#   fig, ax = plt.subplots()
#   df_shortened.plot.line(
#     x="Date-Time",
#     y="Weight(g)",
#     grid=False,
#     figsize=(8, 8),
#     color="#86bf91",
#     ax=ax,
#   )

#   st.write(fig)


if st.button('Smooth Data'):

  df['rolling_mean'] = df['Weight(g)'].rolling(number).mean()
  csv = convert_df(df)
  st.write('Processed Data!') #displayed when the button is clicked
  st.write(df)
  
  # Add some matplotlib code !
#   df_shortened = df.head(number2)

  fig, ax = plt.subplots()
  df.plot.line(
    x="Date-Time",
    y="rolling_mean",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    ax=ax,
  )
  



st.download_button(
   "Press to Download Transformed Data",
   csv,
   "Shakira.csv",
   "text/csv",
   key='download-csv'
)


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))
