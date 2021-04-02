import numpy as np

def curve1(in_array_ ):
    return (in_array_**3) + ((in_array_*.9-4)**2)

def curve2(in_array_ ):
    return (20*np.sin((in_array_)*3+4)+20) + curve1(in_array_ )
