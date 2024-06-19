from django.shortcuts import render
from analysis.models import WaterData,WaterData2
from analysis.forms import DateForm
import plotly.express as px

def analysis1(request):
    waterData = WaterData.objects.all()

    fig = px.line(
        x=[c.date for c in waterData],
        y=[c.BOD for c in waterData],
        title="Biological Oxygen Demand PPM",
        labels={'x': 'Date', 'y': 'BOD PPM'}
    )

    chart = fig.to_html()

    context = {'chart': chart, 'form': DateForm()}
    return render(request, "visualization/core/chart.html", context)


def analysis2(request):
    waterData2 = WaterData2.objects.all()
    fig = px.line(
        x=[c.month for c in waterData2],
        y=[c.COD for c in waterData2],
        title="Chemical Oxygen Demand PPM",
        labels={'x': 'Month', 'y': 'COD PPM'}
    )

    chart = fig.to_html()

    context = {'chart': chart, 'form': DateForm()}
    return render(request, "visualization/core/chart2.html", context)