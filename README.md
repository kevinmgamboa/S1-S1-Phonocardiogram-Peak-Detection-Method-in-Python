# S1-S1-Phonocardiogram-Peak-Detection-Method-in-Python
Prerequisites
* In order to make the code work correctly we need to have the library PeakUtils install. You can find this at https://pypi.python.org/pypi/PeakUtils/1.0.0
* Additionally we need matplotlib, numpy, scipy

## Description of main files
* "SS_phonocardiogram_peak_detection.py" contains the main code which shows an example using a heart sound signal or PCG store in a .wav file
* "mdatabase.m" contains the PCG data vector and its information (fs, etc.)
* "Filters1.mat" contains the coeficients of a filter 

## Peak-Detection Method
The first derivative gives the slope of a signal at each point (That’s a fact!). In a sound file (heart sound signal for example) when we calculate the first derivate of the vector the set of values of the growing part of the signal results in a positive slope and the set of values of the decreasing part results in negative slope. As a peak happens when the trend change from upward to downward (top of the fig. 1st vector, position 136), we can also think that a peak is going to happen when the values change from positive to negative (top of the fig. 2nd vector, position 136) as its showed below :

![img1](https://user-images.githubusercontent.com/15948497/47213034-b4182500-d391-11e8-928e-009f8b61bf86.png)
Figure 1.

Figure 1 also show at the top that each peak is represented as the first negative value of the derivative vector. Therefore, to get the set of all peaks we can just take the positives values or the greater than zero from the derivative vector ‘Derivative’. As a result we will get a logic vector ‘Positives’ with zeros when the value is low than zero and ones when is greater. We will need to transform this vector from logic values to doubles (due in matlab). Finally we will make a “for loop” that give us a peak when the actual value (i) is one and the next one (i+1) is zero in the derivative vector as we show below. The resultant vector when we do a derivative is going to have a length (i-1) that the length of the principal vector. In order to fix this problem we might add (i+1) to the resultant vector. Figure 2 shows how we can show this result.

![image](https://user-images.githubusercontent.com/15948497/47213598-6bfa0200-d393-11e8-9579-3a6ac0982d3a.png)
Figure 2.

Finally, we can make use of the PeakUtils library to select the peaks we need according to a distance between them. The result of this will be as shown in figure 3. 

![image](https://user-images.githubusercontent.com/15948497/47214257-4110ad80-d395-11e8-9875-d72145d4e2c6.png)
Figure 3.


