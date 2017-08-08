import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show

csv_file = 'points.csv'
data = pd.read_csv(csv_file)
TOOLS = 'hover,crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select'
picture = figure(width=1000, height=400, tools=TOOLS)
picture.line(data['order'], data['value'], color='blue', alpha=0.5)
output_file('waveform.html', title='waveform')
show(picture)