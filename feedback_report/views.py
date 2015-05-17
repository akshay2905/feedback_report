# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
import random
import datetime
import time
import MySQLdb
import json
import models
from .models import feedback_student_info

from .models import course, batch, section_info, Question, infrastructure_support_info, feedback_student_info, subject, faculty_table, time_table, academic_assessment_info

from .models import feedback_student_info
from django_pandas.io import read_frame
import pandas.io.sql as sql
from django_pandas.managers import DataFrameManager
from pandas import DataFrame
from django.http import JsonResponse
#qs=academic_assessment_info.objects.all()

#df = read_frame(qs)
#d_frame = to_dataframe(qs)
qs = academic_assessment_info.objects.all()
db= MySQLdb.connect(host="localhost", user="root", passwd="nano@2406",db="feedback_system")

df = sql.read_frame(str(qs.query), db)

def home(request):
    """
    home page
    """
    return render_to_response('home.html')


def demo_piechart(request):
    """
    pieChart page
    """
    xdata=["Parameter 1","Parameter 2","Parameter 3","Parameter 4","Parameter 5","Parameter 6","Parameter 7","Parameter 8","Parameter 9","Parameter 10"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    color_list = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e', '#a4c639',
                  '#b2beb5', '#8db600', '#7fffd4', '#ff007f', '#ff55a3', '#5f9ea0']
    extra_serie = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "color_list": color_list
    }
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('piechart.html', data)





def demo_linewithfocuschart(request):
    """
    linewithfocuschart page
    """
    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 5) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "The Total Ratings - ", "y_end":""},
                   "date_format": tooltip_date}

    chartdata = {
        'x': xdata,
        'name1': 'Teacher 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'Teacher 2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'Teacher 3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'Teacher 4', 'y4': ydata4, 'extra4': extra_serie
    }
    charttype = "lineWithFocusChart"
    chartcontainer = 'linewithfocuschart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': True,
        }
    }
    return render_to_response('linewithfocuschart.html', data)


def demo_multibarchart(request):
    """
    multibarchart page
    """
    nb_element = 5
    xdata = ["Teacher 1","Teacher 2","Teacher 3","Teacher 4","Teacher 5"]
    ydata = [random.randint(1, 5) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}

    chartdata = {
        'x': xdata,
        'name1': 'Parameter  1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'Parameter  2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'Parameter  3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'Parameter  4', 'y4': ydata4, 'extra4': extra_serie
    }

    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}

    date_chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
    }

    charttype = "multiBarChart"
    chartcontainer = 'multibarchart_container'  # container name
    chartcontainer_with_date = 'date_multibarchart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
        'chartdata_with_date': date_chartdata,
        'chartcontainer_with_date': chartcontainer_with_date,
        'extra_with_date': {
            'name': chartcontainer_with_date,
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %d',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('multibarchart.html', data)


def demo_stackedareachart(request):
    """
    stackedareachart page
    """
    nb_element = 100
    xdata = range(nb_element)
    xdata = map(lambda x: 100 + x, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}
    extra_serie2 = {"tooltip": {"y_start": "", "y_end": " calls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2,
    }
    charttype = "stackedAreaChart"
    chartcontainer = 'stackedareachart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('stackedareachart.html', data)


def demo_multibarhorizontalchart(request):
    """
    multibarhorizontalchart page
    """
    nb_element = 10
    xdata = range(nb_element)
    ydata = [ random.randint(0, 5) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 1, ydata)
    ydata3=["Parameter 1","Parameter 2","Parameter 3","Parameter 4","Parameter 5","Parameter 6","Parameter 7","Parameter 8","Parameter 9","Parameter 10"]
    extra_serie = {"tooltip": {"y_start": "was rated ", "y_end": " mins"}}

    chartdata = {
        'x': xdata,

        'name1': 'Teacher 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'Teacher 2', 'y2': ydata2, 'extra2': extra_serie,
    }

    charttype = "multiBarHorizontalChart"
    chartcontainer = 'multibarhorizontalchart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('multibarhorizontalchart.html', data)





def demo_cumulativelinechart(request):
    """
    cumulativelinechart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 100
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " calls"},
                    "date_format": tooltip_date}
    extra_serie2 = {"tooltip": {"y_start": "", "y_end": " min"},
                    "date_format": tooltip_date}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2,
    }

    charttype = "cumulativeLineChart"
    chartcontainer = 'cumulativelinechart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('cumulativelinechart.html', data)



def demo_discretebarchart_with_date(request):
    """
    discretebarchart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 10

    xdata = list(range(nb_element))
    xdata = [start_time + x * 1000000000 for x in xdata]
    ydata = [i + random.randint(1, 5) for i in range(nb_element)]

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {
        'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
    }
    charttype = "discreteBarChart"
    chartcontainer = 'discretebarchart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d-%b',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('discretebarchart_with_date.html', data)



def infra(request):
    """
    multibarchart page
    """
    nb_element = 1
    xdata=["Infrastructure Support","Parameter 2","Parameter 3","Parameter 4","Parameter 5","Parameter 6","Parameter 7","Parameter 8","Parameter 9","Parameter 10"]
    ydata = [random.randint(1, 5) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)
    ydata5 = map(lambda x: x * 3, ydata)
    ydata6 = map(lambda x: x * 3.5, ydata)
    ydata7 = map(lambda x: x * 4.5, ydata)
    ydata8 = map(lambda x: x * 2, ydata)
    

    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}

    chartdata = {
        'x': xdata,
        'name1': 'Parameter  1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'Parameter  2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'Parameter  3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'Parameter  4', 'y4': ydata4, 'extra4': extra_serie,

        'name5': 'Parameter  5', 'y5': ydata5, 'extra1': extra_serie,
        'name6': 'Parameter  6', 'y6': ydata6, 'extra2': extra_serie,
        'name7': 'Parameter  7', 'y7': ydata7, 'extra3': extra_serie,
        'name8': 'Parameter  8', 'y8': ydata8, 'extra4': extra_serie,
    }

    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}

    date_chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
    }

    charttype = "multiBarChart"
    chartcontainer = 'multibarchart_container'  # container name
    chartcontainer_with_date = 'date_multibarchart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
        'chartdata_with_date': date_chartdata,
        'chartcontainer_with_date': chartcontainer_with_date,
        'extra_with_date': {
            'name': chartcontainer_with_date,
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %d',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('infra.html', data)
