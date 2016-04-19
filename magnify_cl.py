from magnify import *

file_in = sys.argv[1]
file_out = file_in.replace(".dat",".ampl.dat")
k = float(sys.argv[2])
width = int(sys.argv[3])
image = load_cube(file_in)
im = magnify_motions_2d(image, k = k, width = width)
save_cube(file_out,im)
