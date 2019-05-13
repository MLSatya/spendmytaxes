import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "direction": "counterclockwise", 
  "hole": 0.54, 
  "hoverinfo": "percent+label", 
  "labels": ["Transportation", "Agriculture", "Treasury", "Interior", "Commerce", "Labor", "Defense", "Veterans Affairs", "Health & Human Services", "Education", "Homeland Security", "Housing & Urban Development", "State & International", "Energy", "Justice"], 
  "labelssrc": "mlsatya:15:214ea2", 
  "marker": {"line": {
      "color": "rgb(25, 38, 77)", 
      "width": 1
    }}, 
  "name": "trace1", 
  "pull": 0, 
  "rotation": 0, 
  "showlegend": True, 
  "sort": True, 
  "text": ["Transportation", "Agriculture", "Treasury", "Interior", "Commerce", "Labor", "Defense", "Veterans Affairs", "Health & Human Services", "Education", "Homeland Security", "Housing & Urban Development", "State & International", "Energy", "Justice"], 
  "textfont": {"family": "Droid Sans"}, 
  "textinfo": "percent", 
  "textposition": "middle center", 
  "textsrc": "mlsatya:15:214ea2", 
  "type": "pie", 
  "values": [0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.57, 0.07, 0.05, 0.05, 0.04, 0.04, 0.03, 0.03, 0.02], 
  "valuessrc": "mlsatya:15:d15a17"
}
data = Data([trace1])
layout = {
  "annotations": [
    {"text": "<br>"}
  ], 
  "autosize": True, 
  "legend": {
    "font": {"family": "Droid Sans"}, 
    "xanchor": "auto"
  }, 
  "showlegend": True, 
  "title": {"text": "2020 US Discretionary Budget Request"}, 
  "xaxis": {
    "autorange": True, 
    "range": [-1, 6]
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-1, 4]
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)