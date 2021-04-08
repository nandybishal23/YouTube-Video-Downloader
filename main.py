from pytube import YouTube
from tkinter import*
from tkinter.ttk import*
from tkinter.messagebox import*

Canvas=Tk()


def download_video():
    yt=YouTube(e1.get())
    yt1=yt.streams.get_by_resolution(box.get())
    yt1.download()
    showinfo("Notification","Downloaded")

label0=Label(Canvas,text="YouTube Video Downloader",font="time 50",borderwidth=5, relief="ridge",foreground="white",background="coral")
label0.grid(row=0,column=1,columnspan=3,pady=5)

label1=Label(Canvas,text="Enter Link :",font="poppins 20")
label1.grid(row=1,column=1,pady=5)
label2=Label(Canvas,text="Resolution :",font="poppins 20")
label2.grid(row=2,column=1,pady=5)
e1=Entry(Canvas,width=50)
e1.grid(row=1,column=2)


box=Combobox(Canvas,values=['360p','480p','720p'],width=30)
box.grid(row=2,column=2)

btn=Button(Canvas,text="Download Video",command=download_video,width=40)
btn.grid(row=2,column=3,padx=5)

Canvas.mainloop()
