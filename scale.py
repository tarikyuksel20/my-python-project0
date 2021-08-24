from tkinter import *

def submit():
    if scale.get() >= 50:
        print("The temperature is: "+ str(scale.get()) + " celsius.The weather is hot.")
    elif scale.get() < 50 and scale.get() > 20:
        print("The temperature is: "+ str(scale.get()) + " celsius.The weather is warm.")
    else:
        print("The temperature is: "+ str(scale.get()) + " celsius.The weather is cold.")


window = Tk()
hotImage = PhotoImage(file="img_1.png")
hotlabeL = Label(image=hotImage)
hotlabeL.pack()

window.geometry("820x820")
window.title("Scale")

scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval = 10,
              resolution = 1,
              troughcolor="white",
              fg = "#FF1C00",
              )
scale.pack()

coldImage = PhotoImage(file="img.png")
coldlabeL = Label(image=coldImage)
coldlabeL.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()