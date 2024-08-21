dic={"cat":"an animal","dog":"an animal","aadvark":"an African animal with a long snouth","aback":"surprised",
     "abacus":"a frame with beads sliding on wire or rod","abandon":"leave permanantly"}
def check():
    d=0
    word1=word.get()
    a="The meaning of the word "
    b=" is "
    for i in dic:
        if word1.lower()==i:
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
    if d==0:
        Resut=tk.Tk()
        Resut.geometry('500x200')
        Resut.title("Result not found")
        Input.destroy()
        result= tk.Label(Resut,text="No word found")
        result.pack()
        Return=tk.Button(Resut,text="Try again",command=Resut.destroy)
        Return.pack()
import tkinter as tk

Input=tk.Tk()
Input.geometry('500x200')
Input.title("Dictionary")
lab=tk.Label(Input, text='Enter the word:')
lab.pack()
word=tk.Entry(Input, justify="left")
word.pack()
submit=tk.Button(Input,text="Submit",command=check,)
submit.pack()
Input.mainloop()


