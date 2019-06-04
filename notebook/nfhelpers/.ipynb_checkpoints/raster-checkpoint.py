# Structure to rasters
class Raster():
    def __init__(self, data_name, data, file_info):
        self.data_name = data_name # Name of data property
        self.data = data           # Raw data points
        self.file_info = file_info # File metadata