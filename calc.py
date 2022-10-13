from tkinter import *
import math

tk_calc = Tk()
tk_calc.title("Calculator")

calc_operator = ""
textin = StringVar()
ans = Entry(tk_calc, textvar=textin, width = 50, borderwidth=5)
ans.grid(row=0, column=0, columnspan=5)

def cl(c):
    global calc_operator
    calc_operator += str(c)
    textin.set(calc_operator)

def clear_all():
    global calc_operator
    calc_operator = ""
    textin.set("")

def delete():
    global calc_operator
    dell = calc_operator[:-1]
    calc_operator = dell
    textin.set(dell)

def sins():
    global calc_operator
    var = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = var
    textin.set(var)

def cosin():
    global calc_operator
    var = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = var
    textin.set(var)

def tg():
    global calc_operator
    var = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = var
    textin.set(var)

def ctg():
    global calc_operator
    var = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = var
    textin.set(var)

def square_root():
    global calc_operator
    if float(calc_operator)>=0:
        s = str(eval(calc_operator+'**(1/2)'))
        calc_operator = s
    else:
        s = "ERROR"
    textin.set(s)

def percent():
    global calc_operator
    p = str(eval(calc_operator+'/100'))
    calc_operator = p
    textin.set(p)

def equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    textin.set(temp_op)
    calc_operator = temp_op

log, ln = math.log10, math.log

sinus = Button(tk_calc,  text='sin', command=sins).grid(row=2, column=0, sticky="nsew")
cosinus = Button(tk_calc,  text='cos', command=cosin).grid(row=2, column=1, sticky="nsew")
tangent = Button(tk_calc,  text='tan', command=tg).grid(row=2, column=2, sticky="nsew")
cotangent = Button(tk_calc, text='cot', command=ctg).grid(row=2, column=3, sticky="nsew")
pishka = Button(tk_calc, text='pi', command=lambda:cl(str(math.pi))).grid(row=2, column=4, sticky="nsew")
second_power = Button(tk_calc, text='x^2', command=lambda:cl('**2')).grid(row=3, column=0, sticky="nsew")
expon = Button(tk_calc, text='e', command=lambda:cl(str(math.exp(1)))).grid(row=3, column=1, sticky="nsew")
npower = Button(tk_calc, text='x^n', command=lambda:cl('**')).grid(row=3, column=2, sticky="nsew")
tenp = Button(tk_calc, text='10^x', command=lambda:cl('10**')).grid(row=3, column=4, sticky="nsew")
sqroot = Button(tk_calc,  text='x^(1/2)', command=square_root).grid(row=3, column=3, sticky="nsew")
log_10 = Button(tk_calc, text='log', command=lambda:cl('log(')).grid(row=4, column=3, sticky="nsew")
ln_e = Button(tk_calc,  text='ln', command=lambda:cl('ln(')).grid(row=4, column=4, sticky="nsew")
l_b = Button(tk_calc,  text='(', command=lambda:cl('(')).grid(row=4, column=1, sticky="nsew")
r_b = Button(tk_calc,  text=')', command=lambda:cl(')')).grid(row=4, column=2, sticky="nsew")  
procent = Button(tk_calc, text='%', command=percent).grid(row=5, column=3, sticky="nsew")
ex = Button(tk_calc, text='e^x', command=lambda:cl(str(math.exp^()))).grid(row=5, column=4, sticky="nsew")
button_7 = Button(tk_calc, text='7', command=lambda:cl('7')).grid(row=7, column=0, sticky="nsew")
button_8 = Button(tk_calc, text='8', command=lambda:cl('8')).grid(row=7, column=1, sticky="nsew")
button_9 = Button(tk_calc, text='9', command=lambda:cl('9')).grid(row=7, column=2, sticky="nsew")
delete_1 = Button(tk_calc, text='DEL', command=delete, bg='red').grid(row=8, column=3, sticky="nsew")
delete_all = Button(tk_calc, text='AC', command=clear_all, bg='red').grid(row=8, column=4, sticky="nsew")
button_4 = Button(tk_calc, text='4', command=lambda:cl('4')).grid(row=6, column=0, sticky="nsew")
button_5 = Button(tk_calc,  text='5', command=lambda:cl('5')).grid(row=6, column=1, sticky="nsew")
button_6 = Button(tk_calc, text='6', command=lambda:cl('6')).grid(row=6, column=2, sticky="nsew")
mult = Button(tk_calc, text='*', command=lambda:cl('*')).grid(row=7, column=3, sticky="nsew")
div = Button(tk_calc,text='/', command=lambda:cl('/')).grid(row=7, column=4, sticky="nsew")
button_1 = Button(tk_calc, text='1', command=lambda:cl('1')).grid(row=5, column=0, sticky="nsew")
button_2 = Button(tk_calc,  text='2', command=lambda:cl('2')).grid(row=5, column=1, sticky="nsew")
button_3 = Button(tk_calc, text='3', command=lambda:cl('3')).grid(row=5, column=2, sticky="nsew")
add = Button(tk_calc, text='+', command=lambda:cl('+')).grid(row=6, column=3, sticky="nsew")
min = Button(tk_calc,  text='-', command=lambda:cl('-')).grid(row=6, column=4, sticky="nsew")
button_0 = Button(tk_calc, text='0', command=lambda:cl('0')).grid(row=8, column=0, sticky="nsew")
p = Button(tk_calc, text='.', command=lambda:cl('.')).grid(row=4, column=0, sticky="nsew")
equal = Button(tk_calc, text='=', command=equal).grid(row=8, columnspan=2, column=1, sticky="nsew")

tk_calc.mainloop()
