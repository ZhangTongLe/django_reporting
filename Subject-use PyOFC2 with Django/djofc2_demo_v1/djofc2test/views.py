from django.http import HttpResponse
from pyofc2  import * 
import random
import time

# def chart_data(request):
#     t = title(text=time.strftime('%a %Y %b %d'))
#     b1 = bar()
#     b1.values = range(9,0,-1)
#     b2 = bar()
#     b2.values = [random.randint(0,9) for i in range(9)]
#     b2.colour = '#56acde'
#     chart = open_flash_chart()
#     chart.title = t
#     chart.add_element(b1)
#     chart.add_element(b2)
#     return HttpResponse(chart.render())


def test_area_line():
    t = title(text="Area Chart")
    a = pyofc2.area_line()
    a.width = 2
    a.dot_size = 4
    a.halo_size = 1
    a.colour = '#C4B86A'
    a.fill_colour = '#C4B8AA'
    a.fill_alpha = 0.7
    a.values = scurve()
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(a)
    y = y_axis()
    y.min, y.max, y.steps = -2, 2, 2
    y.labels = None
    y.offset = False

    x = x_axis()
    x.labels = scurve()
    x.steps = 2
    xlbls = x_axis_labels(steps=4, rotate="vertical")
    x.labels = xlbls

    chart.y_axis = y
    chart.x_axis = x
    return chart
    