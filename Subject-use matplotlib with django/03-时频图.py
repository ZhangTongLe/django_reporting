import numpy as np
import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure

data = pd.read_csv('tf_stft.csv')

value = np.array(data['value'])
d = np.reshape(value, (338, 124))
d = np.transpose(d)

TOOLS = "hover,crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select"
p = figure(x_range=(0, 62), y_range=(0, 169), tools=TOOLS)
p.image(image=[d], x=0, y=0, dw=62, dh=169, palette="Viridis256")
output_file("image.html", title="image.py example")
show(p)