import folium

myMap4 = folium.Map(location=[34.0881, 74.0340], zoom_start=12)
folium.Marker(location=[34.0881, 74.0340], popup='Uri, J&K', icon=folium.Icon(color='green')).add_to(myMap4)

folium.Marker(location=[34.0881, 74.0340], popup='Uri, J&K', icon=folium.Icon(color='green')).add_to(myMap4)

folium.PolyLine(locations=[(34.0881, 74.0340), (34.0881, 74.0340), (34.0881, 74.0340)], color='red', weight=5, opacity=0.8)

myMap4.save("myMap4.html")
myMap4
