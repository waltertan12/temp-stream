import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import os
import time
import datetime
import temp

username = os.environ['PLOTLY_USERNAME']
api_key = os.environ['PLOTLY_API_KEY']
stream_token = os.environ['PLOTLY_STREAM_TOKEN']

py.sign_in(username, api_key)

trace1 = Scatter(
	x=[],
	y=[],
	stream=dict(
		token=stream_token,
		maxpoints=200
	)
)

layout = Layout(
	title = 'Raspberry Pi Temperature Log'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Temperature Stream')

stream = py.Stream(stream_token)
stream.open()

while True:
	stream.write({'x': datetime.datetime.now(), 'y': temp.toF(temp.readTemp())})
	time.sleep(60)
