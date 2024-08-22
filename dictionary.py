dic={"cat":"an animal","dog":"an animal","aadvark":"an African animal with a long snouth","aback":"surprised",
     "abacus":"a frame with beads sliding on wire or rod","abandon":"leave permanantly"} #the list of words
def check():  # function when you click search
    d=0
    word1=word.get()
    a="The meaning of the word "
    b=" is "
    for i in dic:
        if word1.lower()==i: # run if word found
            Resut=tk.Tk()
            Resut.geometry('500x200')
            Resut.title("Result found")
            Input.destroy()
            a+=word1
            a+=b
            a+=dic[i]
            meaning=tk.Label(Resut,text=a)
            meaning.pack()
            end=tk.Button(Resut,text="Done",command=Resut.destroy)
            end.pack()

            Resut.mainloop()
           
            
            
            
            d=1
    if d==0: # else
        Resut=tk.Tk()
        Resut.geometry('500x200')
        Resut.title("Result not found")
        Input.destroy()
        result= tk.Label(Resut,text="No word found")
        result.pack()
        Return=tk.Button(Resut,text="Try again",command=Resut.destroy)
        Return.pack()
from PIL import Image, ImageTk
import tkinter as tk

Input=tk.Tk() # input screen
Input.geometry('500x200')
Input.title("Dictionary")
lab=tk.Label(Input, text='Enter the word:')
lab.pack()
word=tk.Entry(Input, justify="left")
word.pack()
photo= ImageTk.PhotoImage(file='school project/search.png')
submit=tk.Button(Input, width=100,height =100,image=photo,command=check,)
submit.pack()
Input.mainloop()


