# CHATBOT

from tkinter import *

root = Tk()
def send():

    send ="Me:"+e.get()
    txt.insert(END, "\n"+send)
    if(e.get() == "Hello"):
        txt.insert(END, "\n"+"Bot: Hi")
    elif (e.get() == "Hi"):
        txt.insert(END, "\n" + "Bot: Hello")
    elif (e.get() == "How are you?"):
        txt.insert(END, "\n" + "Bot: Fine and you")
    elif (e.get() == "Fine"):
        txt.insert(END, "\n" + "Bot: Nice to Hear")
    elif (e.get() == "What is your name?"):
        txt.insert(END, "\n" + "Bot:I'm Machine Learning,conversational Dialog engine")
    elif (e.get() == "Who created you?"):
        txt.insert(END, "\n" + "Bot: I was created by Rutika")
    else:
        txt.insert(END, "\n" + "Bot: Sorry I did'nt get it")
    e.delete(0, END)

txt = Text(root)

txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("CHATBOT")
root.mainloop()