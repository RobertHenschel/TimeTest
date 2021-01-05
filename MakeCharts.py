#!/usr/bin/env python3

import pandas as pd
import plotly.express as px
import plotly.io as pio
from datetime import date, datetime

dfTime = pd.read_excel('test.xlsx', sheet_name='Today', usecols = 'A:C', skiprows = 1, nrows = 30)

# This is ideally what I would like to do to calculate the total time
# dfTime['TotalTime']=dfTime["Time1"] + dfSteps["Time2"]


# As an example, I am charting "Time1" here, but I would rather like to chart "TotalTime"

# I am doing this conversrion, as I was not able to chart it without doing this first
dfTime['Time1'] = pd.to_datetime(dfTime.Time1, format='%H:%M:%S')

ceiling=datetime(1900, 1, 1,10,0)
floor=datetime(1900, 1, 1,0,0)
fig = px.line(dfTime, x = 'Date', y = 'Time1', title='Total Time Chart')
fig.update_xaxes(autorange="reversed")
fig.update_yaxes(range=[floor, ceiling])
# I found the following yaxis format to be particular troublesome,
# but I really really really like to have the y-axis show only hours and minutes, no seconds
fig.update_layout(yaxis={'type': 'date','tickformat': '%H:%M'})
fig.update_layout(xaxis={'tickformat': '%a %b %d %Y'})
pio.kaleido.scope.default_format = "png"
pio.kaleido.scope.default_width = 1200
pio.kaleido.scope.default_height = 900
fig.write_image("Time.png")
