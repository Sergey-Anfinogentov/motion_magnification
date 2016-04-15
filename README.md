# DTCWT based motion magnification
Motion magnication acts like a microscope for low amplitude motions in image sequences, i.e. imaging data cubes or videos. It articially amplifies small displacements making them detectable by eye or some automated technique. The code provided here  is based on the two-dimensional Dual Tree Complex Wavelet Transform (DTCWT) and  allows for magnifying transverse quasi-periodic motions of contrast features in image sequences. 

The algorithm is designed to work with Extreme Ultraviolet imaging observations of the Sun made with [Atmospheric Imaging Assembly](http://aia.lmsal.com) onboard [Solar Dynamics Observatory](http://sdo.gsfc.nasa.gov), but can be applied to any time sequence of images, i.e. an imaging data cube.

##Dependences
The  code is implemented in [Python 3](https://www.python.org) and requires [NumPy](http://www.numpy.org) and  [SciPy](http://scipy.org). The easiest way to get full scientific Python environment is to install the Python  3 version of [Anaconda](https://www.continuum.io/downloads), which is available for Windows, Mac, and Linux. 
You also will need to install [Dual-Tree Complex Wavelet Transform library for Python](https://github.com/rjw57/dtcwt).
##Usage
###From Python
###From IDL
