__author__="Antigoni-K"
__description__="Simple, beginner-friendly video player using tkVideoPlayer. Please install tkVideoPlayer: py -m pip install --no-deps tkvideoplayer --upgrade. Press the play button after you've selected a video."


from tkinter import *
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
import datetime


window=Tk()
window.title('Video Player')
window.state("zoomed")



def loopvideo(event):
    bgvideo.play()

def selectvideo():
    
    def playpause():
        if videoplayer.is_paused():
            videoplayer.play()
            playpausebutton["text"]=" ⏸ "
        else:
            videoplayer.pause()
            playpausebutton["text"]=" ⏵ "
    def seek():
        videoplayer.seek(int(value))
    def updateduration(event):
        duration=videoplayer.video_info()["duration"]
        endtime["text"]=str(datetime.timedelta(seconds=duration))
        progressslider["to"]=duration
    def updatescale(event):
        progressvalue.set(videoplayer.current_duration())
    def videoended(event):
        progressslider.set(progressslider["to"])
        playpausebutton["text"]=" ⏵ "
        progressslider.set(0)
        
    filename=filedialog.askopenfilename(title="Select Video", filetypes=(("mp4 files", "*.mp4"),))

    bgvideo.destroy()
    vplabel.destroy()
    descriptionlabel.destroy()
    viewvideobutton.destroy()

    videoplayer=TkinterVideo(scaled=True, master=window)
    videoplayer.pack(expand=True, fill=BOTH)


    playpausebutton=Button(window, text=" ⏵ ", command=playpause)
    playpausebutton.pack()

    starttime=Label(window, text=str(datetime.timedelta(seconds=0)))
    starttime.pack(side="left")

    progressvalue=IntVar(window)
    progressslider=Scale(window, variable=progressvalue, from_=0, to=0, orient="horizontal", command=seek)
    progressslider.pack(side="left", fill="x", expand=True)

    endtime=Label(window, text=str(datetime.timedelta(seconds=0)))
    endtime.pack(side="left")

    videoplayer.bind("<<Duration>>", updateduration)
    videoplayer.bind("<<SecondChanged>>", updatescale)
    videoplayer.bind("<<Ended>>", videoended)

    if filename:
        videoplayer.load(filename)
        progressslider.config(to=0, from_=0)
        playpausebutton["text"]=" ⏵ "
        progressvalue.set(0)



#Menu Background Video
bgvideo=TkinterVideo(window, scaled=True)
bgvideo.load(r"https://videos.pexels.com/video-files/2915051/2915051-hd_1280_720_25fps.mp4")
bgvideo.grid(column=0, row=0)
bgvideo.pack(expand=True, fill=BOTH)
bgvideo.play()
bgvideo.bind('<<Ended>>', loopvideo)


#Menu Labels and Button
vplabel=Label(window, text="             Video Player             ", fg="#17967f", bg="white", font="Corbel 48 bold")
vplabel.place(relx=.5, rely=.37, anchor="c")

descriptionlabel=Label(window, text="A simple, beginner-friendly video player using tkVideoPlayer.", bg="#17967f", fg="white", font="Corbel 11 bold")
descriptionlabel.place(relx=.5, rely=.433, anchor="c")

viewvideobutton=Button(window, text="view videos", font="Corbel 28", bd=0, width=15, bg="#17967f", fg="white", relief="groove", command=selectvideo)
viewvideobutton.place(relx=.5, rely=.65, anchor="c")


window.mainloop()
