# build_dataset
How to download video from YouTube:
  1) open YouTube and find your desire video
  2) right click on the mouse and pree "Copy video URL"
  3) Open https://en.y2mate.is/293/youtube-to-mp4.html
  4) paste YouTube link and press Start, choose which Quality you need and press convert
  5) Move the video to the video directory in build_dataset project

Before we start building the project we will need
  1) Visual Studio Code or PyCharm with Python 3.x extension (you can use the latest python version) - https://www.python.org/downloads/
  2) pip - follow this link: https://nerdschalk.com/how-to-install-pip-on-windows-11/

How to use this project:
you will need to have 
  1) git clone https://github.com/PookiPok/build_dataset.git
  2) pip install -r requirements.txt
  3) run the program: 
      python .\build_dataset.py -v '.\video\10.mp4' -k 'video_name'
