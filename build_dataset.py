import tkinter as tk
from PIL import Image, ImageTk
import cv2
import shutil
import argparse
import os

window = tk.Tk()
window.resizable(0,0)
video_capture = None
count = 1
image_label = None
text_label = None
video = None
key = None
fpsWaitTime = None
image_path = None
# Function to display the selected option

def getNextImage(first_time):
    image_capture(first_time)
    image = Image.open(image_path)
    new_img = ImageTk.PhotoImage(image)
    image_label.configure(image=new_img)
    image_label.image = new_img
    return image_path

def display_option(option):
    if option == 1:
        new_loc = 'pictures/happy'
    elif option == 2:
        new_loc = 'pictures/unknown'
    elif option == 3:
        new_loc = 'pictures/not_happy'
    elif option == 4:
        os.remove(image_path)
        exit(0)
    elif option == 5:
        os.remove(image_path)
        getNextImage(False)
        return
    try:
        shutil.move(image_path, new_loc)
        text_label['text'] = "Move to:" + new_loc + "/" + key + "_" + str(count-1) + ".jpg"
        getNextImage(False)
    except Exception as e:
        print()

def loadWindow():
    # Create a tkinter window
    global image_label
    global text_label
    frame = tk.Frame(master=window)
    frame.grid(row=3, column=0 , columnspan=3)

    # Display the image
    image_label = tk.Label(frame)
    image_label.pack()
    getNextImage(True)

    # Create three buttons for the options
    frame1 = tk.Frame(master=window)
    frame1.grid(row=1, column=0)
    button1 = tk.Button(frame1, width = 10, height = 1,text="Happy (a)", command=lambda: display_option(1))
    button1.pack()

    frame2 = tk.Frame(master=window)
    frame2.grid(row=1, column=1)
    button2 = tk.Button(frame2, width = 10, height = 1,text="UnKnown (s)", command=lambda: display_option(2))
    button2.pack()

    frame3 = tk.Frame(master=window)
    frame3.grid(row=1, column=2)
    button3 = tk.Button(frame3, width = 10, height = 1,text="Not_Happy (d)", command=lambda: display_option(3))
    button3.pack()

    frame4 = tk.Frame(master=window)
    frame4.grid(row=0, column=1)
    button4 = tk.Button(frame4, width = 10, height = 1,text="Exit (e)", command=lambda: display_option(4))
    button4.pack()

    frame5 = tk.Frame(master=window)
    frame5.grid(row=0, column=0)
    button5 = tk.Button(frame5, width = 10, height = 1,text="Next (x)", command=lambda: display_option(5))
    button5.pack()

    frame6 = tk.Frame(master=window)
    frame6.grid(row=2, column=0, columnspan=3)
    text_label = tk.Label(frame6, width = 50, height = 3)
    text_label.pack()

    window.bind('a', lambda event: display_option(1))
    window.bind('d', lambda event: display_option(3))
    window.bind('s', lambda event: display_option(2))
    window.bind('e', lambda event: display_option(4))
    window.bind('x', lambda event: display_option(5))

    # Start the tkinter event loop
    #window.focus_force()

def image_capture(first_time):
    global count
    global image_path
    frame = None
    frame_count = 1
    if (first_time):
        ret, frame = video_capture.read()
    else:
        stop = True
        while (stop):
            ret, frame = video_capture.read()
            if ret:
                if frame_count%fpsWaitTime == 0:
                    stop = False
                frame_count+=1
    image_path = 'pictures/' + key + "_" + str(count) + ".jpg"
    cv2.imwrite(image_path, frame)
    count+=1

def main(video_name, img_prefix):
    global video_capture
    global video
    global key
    global fpsWaitTime
    video = video_name
    key = img_prefix
    video_capture = cv2.VideoCapture(video)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    fpsPerSec = round(fps, 0)
    fpsWaitTime = fpsPerSec * 1
    loadWindow()
    window.mainloop()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True,help="name of the video")
    ap.add_argument("-k", "--key", required=True,help="images key name saved on file system")
    args = vars(ap.parse_args())
    main(args['video'], args['key'])
    

