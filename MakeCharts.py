#!/usr/bin/env python3

import pandas as pd
import plotly.express as px
import plotly.io as pio
import datetime

dfTime = pd.read_excel('test.xlsx', sheet_name='Today', usecols = 'A:C', skiprows = 1, nrows = 30)

# This is ideally what I would like to do to calculate the total time


# Convert your values to "timedelta".
#  Use datetime.datetime to represent point in time, and datetime.timedelta to represent duration
dfTime.dropna(inplace=True)
dfTime["Time1"] = dfTime["Time1"].apply(lambda x: datetime.timedelta(hours=x.hour, minutes=x.minute, seconds=x.second))
dfTime["Time2"] = dfTime["Time2"].apply(lambda x: datetime.timedelta(hours=x.hour, minutes=x.minute, seconds=x.second))

# You can then do any duration arithmetics
dfTime['TotalTime'] = dfTime["Time1"] + dfTime["Time2"]

# Convert it to the plotly format
# (yes, it's a bit of cheating. Plotly doesn't support durations)
dfTime['TotalTime'] = dfTime['TotalTime'].apply(lambda x: datetime.datetime(2000,1,1) + x)

# As an example, I am charting "Time1" here, but I would rather like to chart "TotalTime"

# I am doing this conversrion, as I was not able to chart it without doing this first

fig = px.line(dfTime, x = 'Date', y = 'TotalTime', title='Total Time Chart')
print(dfTime["TotalTime"])
fig.update_xaxes(autorange="reversed")

# I found the following yaxis format to be particular troublesome,
# but I really really really like to have the y-axis show only hours and minutes, no seconds
fig.update_layout(yaxis={'type': 'date','tickformat': '%H:%M'})
fig.update_layout(xaxis={'tickformat': '%a %b %d %Y'})

#pio.kaleido.scope.default_format = "png"
#pio.kaleido.scope.default_width = 1200
#pio.kaleido.scope.default_height = 900
fig.show()
#fig.write_image("Time.png")
