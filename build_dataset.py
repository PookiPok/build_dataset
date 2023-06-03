import tkinter as tk
from PIL import Image, ImageTk
import cv2
import shutil
import argparse
import os


# Function to display the selected option
def display_option(option, img,window):
    if option == 1:
        new_loc = 'pictures/happy'
    elif option == 2:
        new_loc = 'pictures/unknown'
    elif option == 3:
        new_loc = 'pictures/not_happy'
    elif option == 4:
        exit(0)
    elif option == 5:
        os.remove(img)
        window.destroy()
        return
    try:
        shutil.move(img, new_loc)
    except Exception as e:
        print()
    window.destroy()

def chooseImage(img):
    # Create a tkinter window
    window = tk.Tk()
    window.resizable(0,0)
    frame = tk.Frame(master=window)
    frame.grid(row=4, column=0 , columnspan=3)
    # Load the image
    image_path = img  # Use the path to your image file
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    # Display the image
    image_label = tk.Label(frame, image=tk_image)
    image_label.pack()

    # Create three buttons for the options
    frame1 = tk.Frame(master=window)
    frame1.grid(row=2, column=0)
    button1 = tk.Button(frame1, width = 10, height = 3,text="Happy (a)", command=lambda: display_option(1,img,window))
    button1.pack()

    frame2 = tk.Frame(master=window)
    frame2.grid(row=2, column=1)
    button2 = tk.Button(frame2, width = 10, height = 3,text="UnKnown (s)", command=lambda: display_option(2,img,window))
    button2.pack()

    frame3 = tk.Frame(master=window)
    frame3.grid(row=2, column=2)
    button3 = tk.Button(frame3, width = 10, height = 3,text="Not_Happy (d)", command=lambda: display_option(3,img,window))
    button3.pack()

    frame4 = tk.Frame(master=window)
    frame4.grid(row=0, column=0,columnspan=3)
    button4 = tk.Button(frame4, width = 50, height = 3,text="Exit (e)", command=lambda: display_option(4,img,window))
    button4.pack()

    frame5 = tk.Frame(master=window)
    frame5.grid(row=1, column=0,columnspan=3)
    button5 = tk.Button(frame5, width = 50, height = 3,text="Next (x)", command=lambda: display_option(5,img,window))
    button5.pack()

    frame6 = tk.Frame(master=window)
    frame6.grid(row=3, column=0,columnspan=3)
    label1 = tk.Label(frame6, width = 50, height = 3,text=str(img))
    label1.pack()


    window.bind('a', lambda event: display_option(1,img,window))
    window.bind('d', lambda event: display_option(3,img,window))
    window.bind('s', lambda event: display_option(2,img,window))
    window.bind('e', lambda event: display_option(4,img,window))
    window.bind('x', lambda event: display_option(5,img,window))

    # Start the tkinter event loop
    window.focus_force()
    window.mainloop()

def image_capture(video, key):
    video_capture = cv2.VideoCapture(video)
    count = 1
    while video_capture.isOpened():
      ret, img = video_capture.read()

      if not ret:
          break
      path = 'pictures/' + key + "_" + str(count) + ".jpg"
      cv2.imwrite(path, img)
      chooseImage(path)
      count+=1

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True,help="name of the video")
    ap.add_argument("-k", "--key", required=True,help="images key name saved on file system")
    args = vars(ap.parse_args())
    image_capture(args['video'], args['key'])

