#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import folium


# In[ ]:


def coverage (X,Y, my_map):
# X = [latitude, longitude, radio in meters] - This vector defines the points that will be plotted.
# Y = This vector defines the label of the plotted points. All the positions must be correspondent to X vector
# my_map = map previously created, with the function folium.Maps. For Example: mapa = folium.Map(location=[-19.916667,-43.933333],zoom_start=4)
    
    for i in X:
        folium.Circle(
        location=[i[0],i[1]],
        radius=i[2],
        color='#3186cc',
        fill=True,
        fill_color='#3186cc',
        popup=Y[i[3]]
        ).add_to(my_map)
        
    return

