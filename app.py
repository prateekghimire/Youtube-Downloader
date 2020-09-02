from flask import Flask,render_template,request
from pytube import YouTube



app=Flask(__name__)


@app.route('/')

def home():
    link="https://www.youtube.com/watch?v=SmTDwsomYno"

    yt=YouTube(link)

    print(yt.title)

    print(yt.rating)

    ys=yt.streams.get_highest_resolution()

    print("*****Downloading******")
    ys.download()

    return 'Youtube downloaded'

#app.run(debug=True,port=0000)
    
