import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import argparse

# Using Argument Parser to get the location of image
args = argparse.ArgumentParser()
args.add_argument('-i', '--file', required=True, help='Path to image')
arg = args.parse_args()

filename = arg.file
full_arr = np.genfromtxt('%s' % filename)
#plt.imshow(full_arr[:,:],aspect='auto', origin='lower')
#plt.colorbar()
#plt.title('Original image')
#plt.show()
x, y = full_arr.shape
print x,y
 
#1. find the noise level
def findchange(data, start, gap, bin):
    x, y = data.shape
    number = int(x/bin)
    ymean_list = []
    i=0
    while i<number:
        ymean_list.append(np.mean(data[i*bin:(i+1)*bin,start:start+gap]))
        i += 1

    j = 0
    while j<len(ymean_list):
        if ymean_list[j] < np.mean(ymean_list):
            break
        else:
            j += 1

    return ymean_list,j 

ymean_list, start = findchange(full_arr, 0, 20, 1)
#plt.plot(ymean_list)
#plt.plot([0,1000],[np.mean(ymean_list), np.mean(ymean_list)])
#plt.title('determine noise level')
#plt.show()

def get_mean(full, bin):
    x, y = full.shape
    number = int(y/bin)
    print number
    data = full[:,:]
    mean_list = []
    i = 0
    while i<=number:
        mean_list.append(np.mean(data[:,bin*i:bin*(i+1)]))
        i += 1
    return mean_list
    

mean_list = get_mean(full_arr[start:,:], 1)
file_name = '%s_asymmetry.txt' % filename
np.savetxt('%s' % file_name, mean_list[:-1],  fmt='%.5f')  
