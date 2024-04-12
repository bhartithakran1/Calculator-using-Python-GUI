from tkinter import *
first_number=second_number=third_number=None
def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text= new)
def clear():
    result_label.config(text='' )

def get_operator(op):
    global first_number, operator
    first_number=int(result_label["text"])
    operator=op
    result_label.config(text='')




def get_result():
    global first_number,second_number,operator
    second_number=int(result_label["text"])
    if operator=="+":
        result_label.config(text=first_number+second_number)
    elif operator == "-":
        result_label.config(text=first_number - second_number)
    elif operator == "*":
        result_label.config(text=first_number * second_number)
    elif operator == "/":
        if second_number==0:
            result_label.config(text="error")
        else:
            result_label.config(text=first_number / second_number)



root= Tk()
root.title("Calculator")
root.geometry("280x380")
root.resizable(0,0)
root.configure(background="black")
root.iconbitmap("calcuLATOR.jpg")

result_label=Label(root,text='',bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=20 ,pady=(50,25),sticky='e')
result_label.config(font=("calbri",30,"bold"))


btn7=Button(root,text="7",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('calbri',14 ))

btn8=Button(root,text="8",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('calbri',14 ))

btn9=Button(root,text="9",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('calbri',14))

btn_add=Button(root,text="+",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('calbri',14 ))

btn4=Button(root,text="4",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('calbri',14 ))

btn5=Button(root,text="5",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('calbri',14 ))

btn6=Button(root,text="6",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('calbri',14 ))

btn_sub=Button(root,text="-",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('calbri',14 ))

btn1=Button(root,text="1",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('calbri',14 ))

btn2=Button(root,text="2",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('calbri',14 ))

btn3=Button(root,text="3",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('calbri',14 ))

btn_mul=Button(root,text="*",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('calbri',14 ))




btn_clr=Button(root,text="CLR",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('calbri',14 ))

btn0=Button(root,text="0",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('calbri',14 ))

btn_equals=Button(root,text="=",fg="white",bg="#D3D3D3",height=2,width=5,command= lambda:get_result())
btn_equals.grid(row=4,column=2)
btn_equals.config(font=('calbri',14 ))

btn_div=Button(root,text="/",fg="white",bg="#D3D3D3",height=2,width=5,command=lambda:get_operator('/'))
btn_div.grid(row=4,column=3 )
btn_div.config(font=('calbri',14 ))


root.grid_size()

root.mainloop()

