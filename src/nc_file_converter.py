import pandas as pd
import netCDF4
import numpy as np
from netCDF4 import Dataset

nc = netCDF4.Dataset(
    "data\download\BERKEARTH_mean_temperature-anomaly_day_1x1_global_2018_v1.0.nc")

time = nc.variables['time']

print(time.shape)
print(time.dimensions)
print(time)

print(time[:])
