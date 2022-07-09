from tkinter import *
class ImageDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Image Demo")
        self.grid()
        self._image=PhotoImage(file="1dpmw.gif")
        self._imageLabel=Label(self,image=self._image)
        self._imageLabel.grid()
        self._textLabel=Label(self,text="umesh")
        self._textLabel.grid()
def main():
    ImageDemo() .mainloop()
main()
