from numpy import linspace, cos, pi, arange, zeros

'''
Some window functions for DFT spectra. Some were taken from
http://edoc.mpg.de/395068
'''

def weighted_cosine_window(N, *coeffs):
    z = 2*pi*arange(N)/N
    r = zeros(N)
    for i in range(len(coeffs)):
        r += coeffs[i]*cos(i*z)
    return r

def FTSRS(N):
    return weighted_cosine_window(N, 1., -1.93, 1.29, -0.388, 0.028)

def HFT116D(N):
    return weighted_cosine_window(N, 1., -1.9575375, 1.4780705, -0.6367431, 0.1228389, -0.0066288)
