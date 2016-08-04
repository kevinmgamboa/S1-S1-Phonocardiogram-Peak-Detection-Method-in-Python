% Code to show some signals from Michigan Heart Sounds Database 
% by: Kevin Machado
% Ref: http://www.med.umich.edu/lrc/psb_open/html/repo/primer_heartsound/primer_heartsound.html
% -------------------------------------------------------------------------
clc;clear all;close all;
load('mDatabase');              % Loading the MHS Database
% Reduction of samples for practice porpose
x1=x1(1:200000);
x8=x8(1:200000);
x13=x13(1:200000);
x17=x17(1:200000);
% Start time measure
tic
[y1,y1peak]=fPeak(x1);          % Getting the peaks of x1
[y8,y8peak]=fPeak(x8);          % Getting the peaks of x9
[y13,y13peak]=fPeak(x13);       % Getting the peaks of x13
[y17,y17peak]=fPeak(x17);       % Getting the peaks of x17

ev1=sEnergy(x1,y1peak);         % Getting the energy of x1
%ev1=ev1./(max(ev1));           % Amplitude normalization of x1
ev8=sEnergy(x8,y8peak);         % Getting the energy of x9
%ev9=ev9./max(ev9);             % Amplitude normalization of x9
ev13=sEnergy(x13,y13peak);      % Getting the energy of x13
%ev13=ev13./max(ev13);          % Amplitude normalization of x3
ev17=sEnergy(x17,y17peak);      % Getting the energy of x17
%ev17=ev17./max(ev17);          % Amplitude normalization of x17
% Ends time measure
toc
% -------------------------------------------------------------------------
% Plots and Comments
figure(1)
subplot(4,1,1),plot(x1);title('Single S1 S2 - Supine, Apex A.','fontsize',10);
hold on
plot(y1peak,'--rs')
subplot(4,1,2),plot(x8);title('Late Systolic Murmur, Apex A. Supine, Bell - Supine, Apex A.','fontsize',10);
hold on
plot(y8peak,'--rs')
subplot(4,1,3),plot(x13);title('Systolic & Diastolic Murmur - Sitting, Aortic A.','fontsize',10);
hold on
plot(y13peak,'--rs')
subplot(4,1,4),plot(x17);title('Mitral Opening Snap & Diastolic Murmur - Left Decubitus, Apex A.','fontsize',10);
hold on
plot(y17peak,'--rs')
figure(2)
subplot(4,1,1),bar(ev1);title('Energy Single S1 S2 - Supine, Apex A.','fontsize',10);
subplot(4,1,2),bar(ev8);title('Energy Late Systolic Murmur - Supine, Apex A.','fontsize',10);
subplot(4,1,3),bar(ev13);title('Energy Systolic & Diastolic Murmur - Sitting, Aortic A.','fontsize',10);
subplot(4,1,4),bar(ev17);title('Mitral Opening Snap & Diastolic Murmur - Left Decubitus, Apex A.','fontsize',10);


p1=0;
for i=2:6
    p1=p1+ev1(1,i); 
end