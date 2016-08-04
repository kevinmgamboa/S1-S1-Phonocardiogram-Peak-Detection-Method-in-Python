##----------------------------------------------------------------------------
## LYBRARIES:
##----------------------------------------------------------------------------
# # Kevin Machado Gamboa/ Universidad Autonoma de Occidente/Cali/ Colombia
# Numpy Tutorial http://cs231n.github.io/python-numpy-tutorial/#numpy
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt                 # Librery to load .mat files
import peakutils                                # Librery to help in peak detection
from scipy import special

##----------------------------------------------------------------------------
# FUNCTIONS: "execfile"
##----------------------------------------------------------------------------
''' This Function creates a time-vector for any signal given the sampling frequency
    and the duration of a signal'''
def time_vector(sampling_frequency,duration): 
	number_samples= sampling_frequency*duration;
	result=np.arange(1,duration/number_samples,duration-duration/number_samples);

	return result

##----------------------------------------------------------------------------
''' Derivate of an input signal as y[n]= x[n+1]- x[n-1] 
'''
def derivate (x):
	lenght=np.shape(x)				# Get the length of the vector		
	lenght=lenght[0];				# Get the value of the length
	y=np.zeros(lenght);				# Initializate derivate vector
	for i in range(lenght-1):
			y[i]=x[i+1]-x[i];		
	return y

##----------------------------------------------------------------------------
'''To normalized any vector\0-dimentional array in [-1,1] range, by divided the 
   vector by the maximun value of itself, substracting the mean value to the vector
   & dividing each value of the vector by the maximun value of itself 
'''
def vec_nor(x):
	lenght=np.shape(x)				# Get the length of the vector		
	lenght=lenght[0];				# Get the value of the length
	xMax=max(x);					# Get the maximun value of the vector
	nVec=np.zeros(lenght);			        # Initializate derivate vector
	for n in range(lenght):
		nVec[n]=x[n]/xMax;			
	nVec=nVec-np.mean(nVec);
	nVec=np.divide(nVec,np.max(nVec));
	return nVec
##----------------------------------------------------------------------------
'''
  FpassBand is the function that develop a pass band filter of the signal 'x' through the
  discrete convolution of this 'x' first with the coeficients of a High Pass Filter 'hp' and then
  with the discrete convolution of this result with a Low Pass Filter 'lp'
'''
def FpassBand(X,hp,lp):
        llp=np.shape(lp)	  	        # Get the length of the lowpass vector		
        llp=llp[0];				# Get the value of the length
        lhp=np.shape(hp)			# Get the length of the highpass vector		
        lhp=lhp[0];				# Get the value of the length	

        x=np.convolve(X,lp);		        # Disrete convolution 
        x=x[(llp/2):-1-(llp/2)];
        x=x-(np.mean(x));
        x=x/np.max(x);
	
        y=np.convolve(x,hp);			# Disrete onvolution
        y=y[(lhp/2):-1-(lhp/2)];
        y=y-np.mean(y);
        y=y/np.max(y);

        x=np.convolve(y,lp);		        # Disrete convolution 
        x=x[(llp/2):-1-(llp/2)];
        x=x-(np.mean(x));
        x=x/np.max(x);
	
        y=np.convolve(x,hp);			# Disrete onvolution
        y=y[(lhp/2):-1-(lhp/2)];
        y=y-np.mean(y);
        y=y/np.max(y);
        
        y=vec_nor(y);				# Vector Normalizing
        
        return y
        
##----------------------------------------------------------------------------
## Loading Phonocardiogram Signal from Michigan Heart Sound & Murmur Library
## Ref:http://www.med.umich.edu/lrc/psb_open/html/repo/primer_heartsound/primer_heartsound.html
## and Filter made by FDA tools from matlab

datos=sio.loadmat('mdatabase');
filtros=sio.loadmat('Filters1');
## Getting access to variables into 'newSound1' & 'Filters1'
X=datos['x1'];X=X[0];		                # Phonocardigram signal	
Fs=datos['fs'];Fs=Fs[0];#datos['Fs'];#Fs=int(Fs);			# Frecuency of the Phonocardigram signal
#duration=datos['duration'];duration=int(duration); # Duration of the Phonocardigram signal
Fpa20=filtros['Fpa20'];			        # High pass filter
Fpa20=Fpa20[0];					# High pass filter
Fpb100=filtros['Fpb100'];		        # Low-pass Filter
Fpb100=Fpb100[0];				# Low-pass Filter
## ----------------------------------------------------------------------------
# PassBand Filter ... The Original Signal X loose 4 samples after this process

Xf=FpassBand(X,Fpa20,Fpb100); 	                # Apply a passband filter
Xf=vec_nor(Xf);			                # Vector Normalizing

# Derivate of the Signal
dX=derivate(Xf);				# Derivate of the signal
dX=vec_nor(dX);					# Vector Normalizing

# Square of the signal
dy=np.square(Xf);
dy=vec_nor(dy);

## -----------------------------------------------------------------
# Peak Detection Process

size=np.shape(Xf)				# Rank or dimension of the array
fil=size[0];					# Number of rows

positive=np.zeros((1,fil+1));                   # Initializating Positives Values Vector 
positive=positive[0];                           # Getting the Vector

points=np.zeros((1,fil));                       # Initializating the all Peak Points Vector
points=points[0];                               # Getting the point vector

peaks=np.zeros((1,fil));                        # Initializating the s1-s1 Peak Vector
peaks=peaks[0];                                 # Getting the point vector
'''
FIRST! having the positives values of the slope as 1
And the negative values of the slope as 0
'''
for i in range(0,fil):
        if dX[i]>0:
                positive[i]=1;
        else:
                positive[i]=0;
'''
SECOND! a peak will be found when the ith value is equal to 1 &&
the ith+1 is equal to 0
'''
for i in range(0,fil):
        if (positive[i]==1 and positive[i+1]==0):
                points[i]=Xf[i];
        else:
                points[i]=0;

'''
THIRD! Height & Distance Threshold using peakutils function
Reference: https://pypi.python.org/pypi/PeakUtils/1.0.0
'''

indexes=peakutils.indexes(points,thres=0.5/max(points), min_dist=2000);
lenght=np.shape(indexes)			# Get the length of the index vector		
lenght=lenght[0];				# Get the value of the index vector

for i in range(0,lenght):
        p=indexes[i];
        peaks[p]=points[p];
        
n=np.arange(0,fil);                            # Vector to the X axes (Number of Samples)

## -----------------------------------------------------------------
# Graphics
plt.figure(0)
plt.subplot(3,1,1)
plt.plot(n,Xf)
plt.grid(True)
plt.title('Normal Phonocardiogram Signal')
plt.subplot(3,1,2)
plt.plot(n,Xf,'k',n,points,'bo')
plt.grid(True)
plt.title('Phonocardiogram Signal All Peaks Points')
plt.ylabel('Normalized Amplitude',fontsize=12)
plt.subplot(3,1,3)
plt.plot(n,Xf,'k',n,peaks,'bo')
plt.title('Phonocardiogram Signal s1-s1 Peak Detection')
plt.xlabel('Number of Samples',fontsize=12)
plt.grid(True)


plt.figure(1)
plt.plot(n,Xf,'k',n,peaks,'bo')
plt.ylabel('Normalized Amplitude',fontsize=12)
plt.xlabel('Number of Samples',fontsize=12)
plt.title('Phonocardiogram Signal s1-s1 Peak Detection')
plt.grid(True)
plt.show()
