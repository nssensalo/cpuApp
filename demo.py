import psutil
import math
import speedtest 
from tkinter import *

print(psutil.cpu_count())
# while (1):
#     print(psutil.cpu_percent(1))
print('Total system memory is:',math.floor(psutil.virtual_memory()[0]/1000000000))
print('Available memory is:',math.floor(psutil.virtual_memory()[1]/1000000000))
print('Percent system memory is:',psutil.virtual_memory()[2])
print('Used memory is:',math.floor(psutil.virtual_memory()[3]/1000000000))
print('Free memory is:',math.floor(psutil.virtual_memory()[4]/1000000000))

#getting network speed
st = speedtest.Speedtest()
print('Download speed:',math.floor(st.download()/1000000))
print('Upload speed:',math.floor(st.upload()/1000000))
print("Ping is:", st.results.ping)