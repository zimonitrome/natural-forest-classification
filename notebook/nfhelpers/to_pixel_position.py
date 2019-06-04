# Converts Sverref (Or any) coords to float positions in the raster (x, y)
def to_pixel_position(coords, geo_info):
    x_coord, y_coord = coords
    x_start = geo_info[0]
    y_start = geo_info[3]
    x_size = geo_info[1]
    y_size = geo_info[5]
    
    x_index = (x_coord - x_start) / x_size
    y_index = (y_coord - y_start) / y_size
    return x_index, y_index
