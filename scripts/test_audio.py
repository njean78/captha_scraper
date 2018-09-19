from scipy.io import wavfile
sampFreq, snd = wavfile.read('prova1.wav')

from numpy import arange, array, int16
timeArray = arange(0, 2641920, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

snd = snd / (2.**15)
s1 = snd[:,0]

import matplotlib.pyplot as plt
plt.plot(timeArray, s1, color='k')
plt.show()


def fil(x):
    if abs(x) < 0.05 :
        return 0
    else :
        return x
aa = [int(fil(x)* (2.**15)) for x in s1]

snd_f = array(aa, dtype = int16)
wavfile.write(data = snd_f,rate = sampFreq, filename = "filtered_prova1.wav")


sox -V3 input.wav output.wav silence 1 3.0 0.1% 1 0.3 0.1% : newfile : restart

## splitting :
len_snd = len(snd_f)
for i, val  in enumerate(snd_f):
    if i < len(snd_f)


http://pst.giustizia.it/PST/pst_2_6_4.wp?regioneRicerca=9&ufficioRicerca=0181770092&registroRicerca=FALL
