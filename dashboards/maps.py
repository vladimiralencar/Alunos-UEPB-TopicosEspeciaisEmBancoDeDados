#token = open(".mapbox_token").read() # you will need your own token

token = "pk.eyJ1IjoidmFsZW5jYXIiLCJhIjoiY2tzYm9kc2x0MDhxMTJzb21ld2h0eXpoYyJ9.a9IcXbiO88uu-QdDcatixw"


from urllib.request import urlopen
import json
#with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
with open('Brasil.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("covid_estados_12_ago_2021.csv") #,
                   #dtype={"fips": str})
print(df)
import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.state, z=df.last_available_confirmed,
                                    colorscale="Viridis", zmin=0, zmax=12, marker_line_width=0))
fig.update_layout(mapbox_style="light", mapbox_accesstoken=token,
                  mapbox_zoom=3, mapbox_center = {"lat": -15.77972, "lon":  -47.92972})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

