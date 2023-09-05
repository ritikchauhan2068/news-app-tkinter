# Library
import io
import os
import webbrowser
from tkinter import *
import requests
from urllib.request import urlopen
from PIL import ImageTk,Image

class News:
    def __init__(self):
        self.data=requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=bac9390071ad4026be75e1edbd9ac72b').json()
        self.root=Tk()
        self.root.title('News')
        self.root.configure(bg='black')
        self.root.geometry('350x800')
        self.news(0)
        self.root.mainloop()


    def news(self,index):
        self.clear()


        heading1=Label(self.root,text= self.data['articles'][index]['title'],bg='black',fg='Red',wraplength=300,justify='center')
        heading1.pack(pady=(10, 20))
        heading1.config(font=('verdana', 15))


        img_url = self.data['articles'][index]['urlToImage']
        raw_data = urlopen(img_url).read()
        im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=photo)
        label.pack()


        description = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=300,justify='center')
        description.pack(pady=(10, 20))
        description.config(font=('verdana', 15))

        frame = Frame(self.root, bg='black')
        frame.pack(fill=BOTH)
        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.news(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.news(index + 1))
            next.pack(side=LEFT)

# Clear the screen
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def open_link(self, url):
        webbrowser.open(url)




News_day=News()
