# Hot Loud Dusty Server

To sync data

        rsync -azP pi@192.168.43.233:/home/pi/hotlouddusty/data/*.csv data/

## Timeseries

        docker-compose run --rm scripts/write_plot_data.py 

## Map

To create geojson for the [Leaflet.timeline earthquakes.html example (which I forked to slightly change so it reads from a local file](https://github.com/ssuffian/Leaflet.timeline)
        
        docker-compose run --rm python scripts/make_geojsonp.py

Which creates a file called data.geojsonp. Move this file to the Leaflet.timeline/examples folder. Then:

        cd Leaflet.timeline
        npm run start

And go to the earthquakes.html page.

# Thanks to:
[GeoJson Time Series](https://github.com/skeate/Leaflet.timeline)
[d3 Brush and Zoom](https://bl.ocks.org/mbostock/34f08d5e11952a80609169b7917d4172)
