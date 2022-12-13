from tkinter import *

def btn_press(num):
    global eqn_text
    eqn_text = eqn_text+str(num)
    eqn_label.set(eqn_text)

def clear():
    global eqn_text
    eqn_label.set("")
    eqn_text=""
def equals():
    global eqn_text
    try:
        total= str(eval(eqn_text))
        eqn_label.set(total)
        eqn_text = total
    except ZeroDivisionError:
        eqn_label.set("Arithmetic error")
        eqn_text=""
    except SyntaxError:
        eqn_label.set("syntax error")
        eqn_text=""
        
window=Tk()
window.title("calculator")
window.configure(bg="orange")
eqn_text=""
eqn_label=StringVar()

label=Label(window,textvariable=eqn_label,font=("Arial",20),
            width=25,height=2,relief=RAISED,bg="yellow")
label.pack()

frame=Frame(window)
frame.pack()

btn1=Button(frame,text=1,height=3,width=7,activebackground="orange",font =10,command=lambda:btn_press(1))
btn1.grid(row=0,column=0)

btn2=Button(frame,text=2,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(2))
btn2.grid(row=0,column=1)

btn3=Button(frame,text=3,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(3))
btn3.grid(row=0,column=2)

btn4=Button(frame,text=4,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(4))
btn4.grid(row=1,column=0)

btn5=Button(frame,text=5,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(5))
btn5.grid(row=1,column=1)

btn6=Button(frame,text=6,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(6))
btn6.grid(row=1,column=2)

btn7=Button(frame,text=7,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(7))
btn7.grid(row=2,column=0)

btn8=Button(frame,text=8,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(8))
btn8.grid(row=2,column=1)

btn9=Button(frame,text=9,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(9))
btn9.grid(row=2,column=2)

btn0=Button(frame,text=0,height=3,width=7,activebackground="orange",font=10,command=lambda:btn_press(0))
btn0.grid(row=3,column=0)

btn11=Button(frame,text=".",height=3,width=7,font=10,command=lambda:btn_press("."))
btn11.grid(row=3,column=1)

btn16=Button(frame,text="%",height=3,width=7,font=10,command=lambda:btn_press("%"))
btn16.grid(row=3,column=2)

btn12=Button(frame,text="+",height=3,width=7,font=10,command=lambda:btn_press("+"))
btn12.grid(row=3,column=3)

btn13=Button(frame,text="-",height=3,width=7,font=10,command=lambda:btn_press("-"))
btn13.grid(row=2,column=3)

btn14=Button(frame,text="*",height=3,width=7,font=10,command=lambda:btn_press("*"))
btn14.grid(row=1,column=3)

btn15=Button(frame,text="/",height=3,width=7,font=10,command=lambda:btn_press("/"))
btn15.grid(row=0,column=3)

btn17=Button(frame,text="(",height=3,width=7,font=10,command=lambda:btn_press("("))
btn17.grid(row=4,column=0)

btn18=Button(frame,text=")",height=3,width=7,font=10,command=lambda:btn_press(")"))
btn18.grid(row=4,column=1)

btn19=Button(frame,text="AC",height=3,width=7,font=10,command=clear)
btn19.grid(row=4,column=2)

btn20=Button(frame,text="=",height=3,width=7,font=10,activebackground="blue",bg="#0000ff",command=equals)
btn20.grid(row=4,column=3)

window.mainloop()
