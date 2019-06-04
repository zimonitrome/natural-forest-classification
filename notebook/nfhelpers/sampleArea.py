# Structure to hold data (one sample area)
class SampleArea():
    def __init__(self, id, classification, coords=None):
        self.coords = coords
        self.id = id
        self.classification = classification
        
        self.rasters = {}
        
        self.features = {}