import tkinter.messagebox
from tkinter import *
import random
import collections
scoree = 0 
dontRepeat = []
mapp = {
    1: ["ehy","hey"],
    2: ["bmhule","humble"],
    3: ["yrpai","priya"],
    4: ["wenswmoen", "newswomen"],
    5: ["aph","hap"],
    6: ["aituch" ,"chaitu"],
    7: ["bbbyo","bobby"],
    8: ["uitgra" ,"guitar"],
    9: ["aaannt" ,"ananta"],
    10:["anshuka" ,"anushka"],
    11:["gphicra" ,"graphic"],
    12: ["arredrnh","harendra"],
    13: ["dnillaah","allahdin"],
    14: ["atruim","maitru"],
    15:["gganstre","gangster"],
    16:["Kraabhmaigd","dimagKharab"],
    17:["MROGARP","PROGRAM"],
    18:["MDNOIAUH","HUMANOID"],
    19:["INGNETORCOI","RECOGNITION"],
    20:["ETCPRMUO","COMPUTER"],
    21:["IAIARIFTCL","ARTIFICIAL"]
}

def answer():
    
    global scoree 
    scoree -= 1
    entry.insert(0,mapp[randd][1])
    
def reset():
    randomO()
    entry.delete(0,'end')
def delteAll():
    entry.delete(0,'end')

def randomO():
    global key , randd
    randd = random.randrange(1,21 , 1)
    while randd in dontRepeat and len(dontRepeat) != len(mapp):
        print(len(dontRepeat))
        randd = random.randrange(1,21 , 1)
        
        
    label.configure(text = mapp[ randd ][0])
    dontRepeat.append(randd)
def checkEntry():
    global input ,scoree
   
    input = entry.get()
    if( input == ""):
        messagebox.showinfo("Faggot!","Atleast Try")
        return 
    if( input.lower() == mapp[randd][1].lower() ) :
        messagebox.showinfo("HORRAYY!","You Passed")
        reset()
        scoree += 1 
        score.configure( text = "Score: {0}".format(scoree  ) ) 
        
    else:
        messagebox.showerror("OOPS!","You Failed")

root = Tk()
root.configure(background = "#000000")
root.title("Jumbled Game")
root.geometry("350x380+400+300")

score = Label( root , text = "Score: {0}".format(scoree) , font = ("Verdana",10) )
score.pack()

label = Label( root , text = "you are here" , font = ("Verdana", 18 ) ,fg = "white" ,bg ="#000000")
label.pack(pady = 30 ,ipadx = 10,ipady = 10)

entry = Entry( root ,font =("Verdana",16) )
entry.pack(ipadx = 2 , ipady = 5)

b1 = Button(root , text = "Submit: " , bg = "#4C4B4B" ,  font = ("Comic sans ms", 14) ,fg = "#6ab04c", relief = GROOVE , command = lambda : checkEntry() )
b1.pack(pady = 30)

b2 = Button(root ,width = 10, text = "Reset: " , bg = "#4C4B4B" ,  font = ("Comic sans ms", 10),  fg = "#74B9FF" ,command = lambda : delteAll() )
b2.pack()

b4 = Button(root , text = "Answer: " ,width = 10, bg = "#4C4B4B" ,  font = ("Comic sans ms", 10),  fg = "#3498DB" ,command = lambda : answer() )
b4.pack()

b3 = Button(root , text = "Too Hard: ",width = 10 , bg = "#4C4B4B" ,  font = ("Comic sans ms", 10),  fg = "#EA425C" ,command = lambda : reset() )
b3.pack()

randomO()
root.mainloop()
