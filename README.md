# Wildfire_Hackathon_CNN

Predicting wildfire growth using geospatial and weather datasets with advanced machine learning techniques

# Wildfire Prediction Hackathon Project

## Introduction

This project aims to predict future wildfire growth using a variety of geospatial and weather-related datasets. The data includes information on fire growth, fire weather indices, fuels, topography, and general weather conditions. The goal of the project is to utilize these datasets to model and predict the progression of wildfires over time.

## Dataset Description

All the data used in this project is stored in GeoTIFF files, which can be viewed using the `rasterio` library in Python. The data is organized into the following directories:

- **Fire Growth Data (`/fire/`)**: Contains raster data representing the day-to-day growth of wildfires.
- **Fire Weather Index Data (`/fire_weather/`)**: Includes indices related to fire weather, which influence the behavior and intensity of wildfires. More information can be found [here](https://cwfis.cfs.nrcan.gc.ca/background/summary/fwi).
- **Fuels Data (`/fuels/`)**: Data related to the types of fuels present in the area, which can affect fire spread. Detailed descriptions of fuel types can be found [here](https://cwfis.cfs.nrcan.gc.ca/background/fueltypes/c1).
- **Topography Data (`/topography/`)**: Contains information about the landscape, including digital elevation models (DEMs) and slope data.
- **Weather Data (`/weather/`)**: Includes variables such as temperature, humidity, wind speed, and wind direction that influence wildfire behavior. Further details are available [here](https://cfs.nrcan.gc.ca/pubwarehouse/pdfs/29152.pdf).

## Installation

To get started with this project, you'll need to install the following Python libraries:

```bash
pip install rasterio matplotlib geopandas numpy pandas
```

## Base model Code Overview

### Viewing Fire Growth Data

Fire growth data is stored in the `/fire/` directory. The data consists of raster files representing the day-to-day growth of a fire. Below is an example of how to load and visualize the fire growth data:

```python
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show, show_hist

path = "PATH_TO_FILES"
fire_num = 2214
fire = path + f'/Train/fire{fire_num}'
tiff_file = fire + f'/fire/fire{fire_num}.tif'
img = rasterio.open(tiff_file)
img_test = img.read(1)
plt.imshow(img_test)
plt.show()

show_hist(img, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")
```

### Viewing Fire Hotspot Data

Fire hotspot data, collected from VIIRS, IBAND, and MODIS satellite sensors, will be stored in the `/fire_hotspot/` directory. The data is in `.shp` format and can be viewed using `geopandas`:

```python
import geopandas as gpd

shp_file = fp + f'/fire_growth/Hotspots_{fnum}_2018.shp'
shape = gpd.read_file(shp_file)
shape.plot()
```

### Viewing Topography Data

Topography data includes the digital elevation model (DEM) and slope data:

```python
tiff_file = fire + "/topography/dem.tif"
img = rasterio.open(tiff_file)
show(img)

tiff_file = fire + "/topography/slope.tif"
img = rasterio.open(tiff_file)
show(img)
```

### Viewing Fire Weather Index Data

Fire weather indices are critical for understanding fire behavior. The following code snippet shows how to visualize these indices:

```python
tiff_files = [
    fire + f'/fire_weather/build_up_index_day{day}.tif',
    fire + f'/fire_weather/drought_code_day{day}.tif',
    fire + f'/fire_weather/duff_moisture_code_day{day}.tif',
    fire + f'/fire_weather/fine_fuel_moisture_code_day{day}.tif',
    fire + f'/fire_weather/fire_weather_index_day{day}.tif',
    fire + f'/fire_weather/initial_spread_index_day{day}.tif'
]

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
for i in range(len(tiff_files)):
    ax = axs[i // 3][i % 3]
    tiff_file = tiff_files[i]
    with rasterio.open(tiff_file) as raster:
        extent = plotting_extent(raster)
        data = raster.read(1)
        ax.imshow(data, extent=extent)
        ax.set_title(tiff_file.split("/")[-1])
plt.show()
```

### Viewing Weather Data

Weather data, such as temperature and wind speed, plays a crucial role in fire behavior. The following example shows how to load and view weather data:

```python
tiff_files = [
    fire + f'/weather/24hr_max_temperature_day{day}.tif',
    fire + f'/weather/noon_relative_humidity_day{day}.tif',
    fire + f'/weather/noon_temperature_day{day}.tif',
    fire + f'/weather/noon_wind_direction_day{day}.tif',
    fire + f'/weather/noon_wind_speed_day{day}.tif'
]

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
for i in range(len(tiff_files)):
    ax = axs[i // 3][i % 3]
    tiff_file = tiff_files[i]
    with rasterio.open(tiff_file) as raster:
        extent = plotting_extent(raster)
        data = raster.read(1)
        ax.imshow(data, extent=extent)
        ax.set_title(tiff_file.split("/")[-1])
plt.show()
```

## Goals and Challenges

The primary goal of this hackathon project is to predict future fire growth using the provided datasets. Key challenges include handling the diversity and complexity of the data, such as varying resolutions of satellite imagery, and integrating various factors like topography and weather conditions to build robust predictive models.

## Conclusion

This project involves the use of advanced geospatial data processing techniques, machine learning models, and a deep understanding of fire behavior and weather patterns. It provides a comprehensive platform for experimenting with and improving wildfire prediction models.

## References

- [Fire Weather Index System](https://cwfis.cfs.nrcan.gc.ca/background/summary/fwi)
- [Fuel Type Descriptions](https://cwfis.cfs.nrcan.gc.ca/background/fueltypes/c1)
- [Weather Data Source](https://cfs.nrcan.gc.ca/pubwarehouse/pdfs/29152.pdf)

---

This README gives a clear and organized overview of your project, the datasets used, and the goals you aim to achieve. You can further adjust it to fit the specific requirements or add additional sections as needed.
