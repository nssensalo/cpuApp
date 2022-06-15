from tkinter import *
from matplotlib.style import available
from psutil import cpu_count
import psutil
import math
import speedtest
from PIL import Image,ImageTk
from sympy import imageset

def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count,image=tk_image,compound='center',fg='#00ffff')

    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage,image=tk_image,compound='center',fg='#00ffff')
    cpu_usage_label.after(100,usage)

    ram_count = math.floor(psutil.virtual_memory()[0]/1000000000)
    ram_count_text = str(ram_count) + "GB"
    ram_count_label.config(text=ram_count_text,image=tk_image,compound='center',fg='#00ffff')

    # ram usage
    ram_usage = psutil.virtual_memory()[2]
    ram_usage_text = str(ram_usage)+ "%"
    ram_usage_label.config(text=ram_usage_text,image=tk_image,compound='center',fg='#00ffff')
    
    #available ram
    available_ram = math.floor(psutil.virtual_memory()[1]/1000000000)
    available_ram_text = str(available_ram)+ "GB"
    ram_available_label.config(text=available_ram_text,image=tk_image,compound='center',fg='#00ffff')

def internet_speed():
    st = speedtest.Speedtest()
    download_speed = str(math.floor(st.download()/1000000))+"Mb/s"
    upload_speed = str(math.floor(st.upload()/1000000))
    ping_to_round = round((st.results.ping),2)
    ping =  str(ping_to_round) + "MS"
    download_label.config(text=download_speed)
    upload_label.config(text=upload_speed)
    ping_label.config(text=ping)

root = Tk()
root.config(bg='black')
image = Image.open('single.png')
tk_image = ImageTk.PhotoImage(image)

root.geometry("1800x1080")
root.title("CPU Status")


#code for cpu count
cpu_count_label = Label(root,font=("Orbitron",40,"bold"),text="0",bd=-2)
cpu_count_label.grid(row=0,column=0)
L1 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="CPUs")
L1.grid(row=1,column=0)

#cpu_usage
cpu_usage_label = Label(root,font=("Orbitron",40,"bold"),text="0",bd=-2)
cpu_usage_label.grid(row=0,column=1)
L2 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="CPU Usage In % ")
L2.grid(row=1,column=1)

#Total ram
ram_count_label = Label(root,font=("Orbitron",40,"bold"),text="0",bd=-2)
ram_count_label.grid(row=0,column=2)
L3 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="Total RAM")
L3.grid(row=1,column=2)

#ram % usage
ram_usage_label = Label(root,font=("Orbitron",40,"bold"),text="0",bd=-2)
ram_usage_label.grid(row=0,column=3)
L4 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="RAM Usage In %")
L4.grid(row=1,column=3)

#Available ram
ram_available_label = Label(root,font=("Orbitron",40,"bold"),text="0",bd=-2)
ram_available_label.grid(row=0,column=4)
L5 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="Available RAM") 
L5.grid(row=1,column=4)

speed_button = Button(root,text="Test Internet Speed", command=internet_speed, width=15,height=2,font=("Orbitron",10,"bold"))
speed_button.grid(row=3,column=0)

download_label = Label(root,font=("Orbitron",30,"bold"),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-2)
download_label.grid(row=3,column=1)
L6 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="Download Speed")
L6.grid(row=4,column=1)

upload_label = Label(root,font=("Orbitron",30,"bold"),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-2)
upload_label.grid(row=3,column=2)
L7 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="Upload Speed")
L7.grid(row=4,column=2)

ping_label = Label(root,font=("Orbitron",30,"bold"),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-2)
ping_label.grid(row=3,column=3)
L8 = Label(root,font=("Orbitron",20,"bold"),bg='black', fg='#fcba03',text="Ping")
L8.grid(row=4,column=3)

usage()

#label should be right before main loop
root.mainloop()



