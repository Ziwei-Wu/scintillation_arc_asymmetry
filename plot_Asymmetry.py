import numpy as np
import matplotlib.pyplot as plt
import argparse
import warnings
from matplotlib.lines import Line2D


def ignorewarning():
    warnings.simplefilter('ignore', RuntimeWarning)
    warnings.simplefilter('ignore', UserWarning)

def find_center(data):
    lens = len(data)
    middle = int(lens/2.0)
    max = np.argmax(data[middle-20:middle+20])
    max = middle - 20 + max
    
    return max

def standard(args):
    #plot data
    fig = plt.figure(figsize=(8,20))
    marker_list = [1,2,3,4,5,6,7,8,9,10,'o','v','^','<','>','8','s','p','*','h','H','D','d','P','X']

    i=0.0
    j=0
    for file in args.infile:
        print file
        #loading data
        mjd = float(file.split('_')[1])
        full_arr = np.genfromtxt('%s' % file)

        #remove mean value and normalize
        full_arr -= np.min(full_arr)
        full_arr += i
        #full_arr /= np.max(full_arr)
        #full_arr += mjd

        #fing center then align data
        max = find_center(full_arr)
        #createing x-axis
        #1. based on max
        #x_axis = np.arange(-1*int(max),len(full_arr)-int(max), 1)
        
        #createing x-axis
        #2.based on len
        lens = (len(full_arr) + 1)/2
        x_axis = np.arange(-1*lens,lens, 1)     

        #plot data
        #plt.scatter(x_axis[:-1], full_arr, label=str(mjd), s=2, marker=marker_list[j])
        plt.scatter(x_axis[:-1], full_arr, s=2, marker=marker_list[j])
        time=mjd-57000.0
        plt.annotate(str(time), xy=(lens,np.min(full_arr)),xytext=(lens+10,min(full_arr)),fontsize=8)

        i += 1.5
        j += 1


            
    #plt.plot([0,0],[-50,-20])
    plt.xlim(-1990,1990)
    plt.annotate('MJD after 57000', xy=(1200,20),xytext=(1200,20),fontsize=12, color='red' )
    plt.annotate('', xy=(1940,30),xytext=(1940,10), arrowprops=dict(facecolor='black', shrink=0.1) )
    plt.ylim(0,35)
    plt.yticks([])
    plt.xlabel('Bin')
    plt.title('Arc evolution')
    plt.subplots_adjust(bottom=0.05, right=0.99, top=0.95, left=0.01)
    #plt.legend()
    #plt.tight_layout()
    plt.show()
    #plt.savefig('Arc-asymmetry.png')

        
  


if __name__ == '__main__':
    # Using Argument Parser to get the location of image
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='+', help='filename')
    args = parser.parse_args()
  
    ignorewarning()
    standard(args)
