from tkinter import *

root = Tk()

root.title('Calculator')
root.geometry('300x400')
root.resizable(0,0)
root.configure(background='black')

def get_number(digit):
    current = result_display['text']
    new = current + str(digit)
    result_display.config(text=new) 

def clr_display():
    result_display.config(text='')

def calc_operator(op):
    global number1, operator

    number1 = int(result_display['text'])
    operator = op
    result_display.config(text='')

def calc_result():
    global number1, number2, operator

    number2 = int(result_display['text'])

    if operator == '+':
        result_display.config(text=str(number1 + number2))
    elif operator == '-':
        result_display.config(text=str(number1 - number2))
    elif operator == '*':
        result_display.config(text=str(number1 * number2))
    else:
        if  number2 == 0:
            result_display.config(text='Error')
        else:
            result_display.config(text=str(round(number1 / number2,2)))
    
    


result_display =Label(root, text='',bg='black', fg='white')
result_display.grid(row=0,column=0 ,columnspan=5, sticky='w', pady=(50,25))
result_display.config(font=('arial', 40 ,'italic'))

btn_7 =Button(root, text='7',bg='green',fg='white',width=5,height=2,command= lambda : get_number(7))
btn_7.grid(row=1, column=0)
btn_7.config(font=('arial',14))

btn_8 =Button(root, text='8',bg='green',fg='white',width=5,height=2,command= lambda : get_number(8))
btn_8.grid(row=1, column=1)
btn_8.config(font=('arial',14))

btn_9 =Button(root, text='9',bg='green',fg='white',width=5,height=2,command= lambda : get_number(9))
btn_9.grid(row=1, column=2)
btn_9.config(font=('arial',14))

btn_add =Button(root, text='+',bg='green',fg='white',width=5,height=2, command=lambda : calc_operator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('arial',14))

btn_4 =Button(root, text='4',bg='green',fg='white',width=5,height=2,command= lambda : get_number(4))
btn_4.grid(row=2, column=0)
btn_4.config(font=('arial',14))

btn_5 =Button(root, text='5',bg='green',fg='white',width=5,height=2,command= lambda : get_number(5))
btn_5.grid(row=2, column=1)
btn_5.config(font=('arial',14))

btn_6 =Button(root, text='6',bg='green',fg='white',width=5,height=2,command= lambda : get_number(6))
btn_6.grid(row=2, column=2)
btn_6.config(font=('arial',14))

btn_sub =Button(root, text='-',bg='green',fg='white',width=5,height=2,command=lambda : calc_operator('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('arial',14))

btn_1 =Button(root, text='1',bg='green',fg='white',width=5,height=2,command= lambda : get_number(1))
btn_1.grid(row=3, column=0)
btn_1.config(font=('arial',14))

btn_2 =Button(root, text='2',bg='green',fg='white',width=5,height=2,command= lambda : get_number(2))
btn_2.grid(row=3, column=1)
btn_2.config(font=('arial',14))

btn_3 =Button(root, text='3',bg='green',fg='white',width=5,height=2,command= lambda : get_number(3))
btn_3.grid(row=3, column=2)
btn_3.config(font=('arial',14))

btn_mult =Button(root, text='*',bg='green',fg='white',width=5,height=2, command=lambda : calc_operator('*'))
btn_mult.grid(row=3, column=3)
btn_mult.config(font=('arial',14))

btn_clr =Button(root, text='C',bg='green',fg='white',width=5,height=2,command= lambda : clr_display())
btn_clr.grid(row=4, column=0)
btn_clr.config(font=('arial',14))

btn_0 =Button(root, text='0',bg='green',fg='white',width=5,height=2,command= lambda : get_number(0))
btn_0.grid(row=4, column=1)
btn_0.config(font=('arial',14))

btn_equal =Button(root, text='=',bg='green',fg='white',width=5,height=2,command=calc_result)
btn_equal.grid(row=4, column=2)
btn_equal.config(font=('arial',14))

btn_div =Button(root, text='/',bg='green',fg='white',width=5,height=2,command=lambda : calc_operator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('arial',14))

root.mainloop()
