import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import folium
import plotly.express as px
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import json
from branca.colormap import linear

# Set the page configuration to wide mode
st.set_page_config(layout="wide")


st.subheader('ROOFTOP SOLAR')
#st.sidebar.image("streamlit_app/data/ceed logo.png")

with open(r'streamlit_app/data/jhnew.geojson') as f:
    geojson_data = json.load(f)

dfall = pd.read_csv(r'streamlit_app/data/All_Total_.csv')

# Function to customize tooltip
color_scale = linear.Greens_09.scale(dfall['Privatesolartotalcapacity'].min(), dfall['Privatesolartotalcapacity'].max())
def style_function(feature):
    return {
        'fillColor':color_scale(feature['properties']['PRIVATE_SOLAR(19-20)']),
        'color': 'black',
        'weight':0.5,
        'dashArray': '4, 4',
        'fillOpacity': 3.0,
    }
m = folium.Map(location=[23.6345, 85.3803], zoom_start=7, tiles='CartoDB Positron',min_zoom =7,max_zoom=7,control_scale= True)
folium.GeoJson(
    geojson_data,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['dtname','PRIVATE_SOLAR(19-20)','PRIVATE_SOLAR_ROOFTOP'], aliases=['District:','PRIVATE INSTALLATIONS SOLAR ROOFTOP(19-20)','PRIVATE INSTALLATIONS SOLAR ROOFTOP(20-21)'])
).add_to(m)
color_scale.caption = 'Installed Capacity (kwp)'
color_scale.add_to(m)
folium.LayerControl().add_to(m)
# Lock the zoom level
m.options['scrollWheelZoom'] = False
#folium_static(m,width=600,height=400)



dfSRFY=pd.read_csv(r'streamlit_app/data/All_Total.csv')
#Grid Connected Solar Rooftop Financial year wise counts in Jharkhand
dfSRFY_sorted = dfSRFY.sort_values(by='PRIVATE_SOLAR_ROOFTOP(19-20)', ascending=True)
fig1 = px.bar(dfSRFY_sorted, y='District', x=['PRIVATE_SOLAR_ROOFTOP(19-20)','PRIVATE_SOLAR_ROOFTOP(21-22)'],
             title='Private Solar Rooftop Installation (Nos.) in Jharkhand',
             labels={'value': 'Installation Counts','variable': 'Financial Years'},
             template='plotly_dark',
             width=700, height=500)

fig1.update_xaxes(showgrid=True)
fig1.update_yaxes(showgrid=True)
fig1.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})
fig1.update_yaxes(tickmode='array', tickvals=dfSRFY_sorted['District'], ticktext=dfSRFY_sorted['District'])
#fig1.show()
#st.plotly_chart(fig1) 

row1, row2 = st.columns(2)
with row1:
    folium_static(m,width=600,height=500)
with row2:
    st.plotly_chart(fig1)

st.header('SOLAR PUMPS')
color_scale = linear.Greens_09.scale(dfall['Count_solar_pump_installed'].min(), dfall['Count_solar_pump_installed'].max())
def style_function(feature):
    return {
        'fillColor': color_scale(feature['properties']['State_Solarpump_counts']),
        'color': 'black',
        'weight':0.5,
        'dashArray': '4, 4',
        'fillOpacity': 3.0,
    }
m = folium.Map(location=[23.6345, 85.3803], zoom_start=6, tiles='CartoDB Positron',min_zoom =7,max_zoom=7)
folium.GeoJson(
    geojson_data,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['dtname','State_Solarpump_counts'], aliases=['District:','Solar Pumps Count:'])
).add_to(m)
folium.LayerControl().add_to(m)
# Lock the zoom level
m.options['scrollWheelZoom'] = False
color_scale.caption = 'Installed Counts'
color_scale.add_to(m)


#dfall = dfall.sort_values(b ascending=True)


dfSSL=pd.read_csv(r'streamlit_app/data/Solar_Water_Pumps.csv')
#Grid Connected Solar Rooftop Financial year wise counts in Jharkhand
dfSSL_sorted = dfSSL.sort_values(by='2021-22', ascending=True)
fig3 = px.bar(dfSSL_sorted, y='District', x=['2016-17','2018-19','2019-20_&_2020-21','2021-22',],
             title='Solar Pump Installations in Jharkhand',
             labels={'value': 'Installation Counts','variable': 'Financial Years'},
             template='plotly_dark',
             width=700, height=500)
fig3.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})
fig3.update_yaxes(tickmode='array', tickvals=dfSSL_sorted['District'], ticktext=dfSSL_sorted['District'])
#fig1.show()


row1, row2 = st.columns(2)
with row1:
    folium_static(m,width=600,height=500)
with row2:
    st.plotly_chart(fig3) 



st.header('Ground Mounted (Utility Grade Solar)')
color_scale = linear.Greens_09.scale(dfall['SGM_Capacity'].min(), dfall['SGM_Capacity'].max())
def style_function(feature):
    return {
        'fillColor': color_scale(feature['properties']['SGM_Capacity']),
        'color': 'black',
        'weight':0.5,
        'dashArray': '4, 4',
        'fillOpacity': 3.0,
    }
m = folium.Map(location=[23.6345, 85.3803], zoom_start=6, tiles='CartoDB Positron',min_zoom =7,max_zoom=7)
folium.GeoJson(
    geojson_data,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['dtname','SGM_Capacity'], aliases=['District:','Solar Ground Mounted Capacity(kWp):'])
).add_to(m)
folium.LayerControl().add_to(m)

color_scale.caption = 'Installed Capacity(kWp)'
color_scale.add_to(m)
# Lock the zoom level
m.options['scrollWheelZoom'] = False
#folium_static(m,width=600,height=400)



dfSGM_sorted = dfall.sort_values(by='SGM_Capacity', ascending=True)
fig4 = px.bar(dfSGM_sorted, y='District', x='SGM_Capacity',
             title='Solar Ground Mounted Capacity(kWp)',
             text='SGM_Capacity',
             template='plotly_dark',
             width=700, height=550)

fig4.update_layout(
    xaxis_title='Capacity (kWp)',
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)

row1, row2 = st.columns(2)
with row1:
    folium_static(m,width=600,height=500)
with row2:
    st.plotly_chart(fig4)  








