import numpy as np
from functools import lru_cache

def get_lat_long(dat):
    """find latitude and longitude corresponding to no. of rows and columns in the data
       
       Parameters:
       ----------

       dat : data elements as numpy array

       Return:
       ------

       lat_points, lon_points: vector (list) of latitude and longitude points

    """ 
    ndates, nrows, ncols = dat.shape
    lon_points, dx = np.linspace(-180, 180, ncols, endpoint=False, retstep=True)
    lon_points += dx/2
    lat_points, dx = np.linspace(90, -90, nrows, endpoint=False, retstep=True)
    lat_points += dx/2
    return lat_points, lon_points


@lru_cache()
def load(fname):
    """load file from the directory and do some pre-processing for performance bottleneck
    
    Parameters:
    ----------

    fname: string specifying the name of file present  in the working directory

    Return:
    ------

    data: array of data elements

    """
    data = np.loadtxt(fname)
    data = data[::2, ::2]
    data[data == -9999] = np.nan
    return data
