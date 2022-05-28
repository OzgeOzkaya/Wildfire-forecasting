import cdsapi

c = cdsapi.Client()

c.retrieve(
    'insitu-gridded-observations-global-and-regional',
    {
        'format': 'zip',
        'origin': 'berkearth',
        'region': 'global',
        'variable': 'temperature_anomaly',
        'statistic': 'mean',
        'time_aggregation': 'daily',
        'horizontal_aggregation': '1_x_1',
        'year': '2018',
        'version': 'v1.0',
    },
    'download.zip')
