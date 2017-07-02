
# DTCWT based motion magnification
Motion magnication acts like a microscope for low amplitude motions in image sequences, i.e. imaging data cubes or videos. It articially amplifies small displacements making them detectable by eye or some automated technique. The code provided here  is based on the two-dimensional Dual Tree Complex Wavelet Transform (DTCWT) and  allows for magnifying transverse quasi-periodic motions of contrast features in image sequences. 

The algorithm is designed to work with Extreme Ultraviolet imaging observations of the Sun made with [Atmospheric Imaging Assembly](http://aia.lmsal.com) onboard [Solar Dynamics Observatory](http://sdo.gsfc.nasa.gov), but can be applied to any time sequence of images, i.e. an imaging data cube.

If you use my motion magnification code in your research, please, let [me](mailto:sergey.istp@gmail.com) know and cite [the paper](http://adsabs.harvard.edu/doi/10.1007/s11207-016-1013-z) describing it.

## Dependences
The  code is implemented in [Python 3](https://www.python.org) and requires [NumPy](http://www.numpy.org) and  [SciPy](http://scipy.org). The easiest way to get full scientific Python environment is to install the Python  3 version of [Anaconda](https://www.continuum.io/downloads), which is available for Windows, Mac, and Linux. 
You also will need to install [Dual-Tree Complex Wavelet Transform library for Python](https://github.com/rjw57/dtcwt)

## Usage
### From Python
```python
from magnify import *
result = magnify_motions_2d(input_data, k, width)
```
Variable input_data must a 3D NumPy double array with the shape of `[nt, ny, nx]`. Where `nt`  is total number of images, `nx` and `ny` are spatial dimentions. Due to the restrictions of the underlying DTCWT library,  `nx` and `ny` dimensions must be even numbers. Result will be returned in the same format. `k` is the magnification factor and `width` is the phase smothing width, which must be larger than the time scale of the motion to be magnified. 

 
### From IDL
```idl
data_amplified = magnify_2d(data, k, width)
```
Variable `data` must be a 3D double array with the size of `[nx, ny, nt]`,  where `nx`,  `ny`  are dimensions of a single image and `nt` is the number of images. Due to the restrictions of the underlying DTCWT library,  `nx` and `ny` dimensions must be even numbers. The result will be returned in the same format. `k` is the magnification factor and `width` is the phase smothing width, which must be larger than the time scale of the motion to be magnified. 
