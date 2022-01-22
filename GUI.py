from lib2to3.pgen2.token import RIGHTSHIFT
from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0, 0)

temp_text = StringVar()
temp_text.set('')
temp_result = DoubleVar()
temp_result.set(0)
temp_ans = StringVar()
temp_ans.set('')
factors = []
actions = []
result = 0

def get_next_var(text):
    temp_val = ''
    sign = ''
    for i in range(1,len(text)+1):
        if text[-i] == '+' or text[-i] == '*' or text[-i] == '/':
            break
        elif text[-i] == '-':
            sign = '-'
            break
        else: 
            temp_val = temp_val + text[-i] + sign
    if temp_val == '':
        temp_val = 0
        return temp_val
    temp_val = float(temp_val[::-1])
    return temp_val

def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x,y):
    if y == 0:
        return 'error'
    else:
        return x/y

def calculating(factors, actions):
    temp = temp_text.get()
    if temp[0] == '-':
        factors[0] = factors[0]*(-1)
    res = factors[0]
    if actions.count('*'):
        while(actions.count('*')):
            x = actions.index('*')
            res = multiply(factors[x], factors[x+1])
            factors.pop(x)
            factors.pop(x)
            actions.pop(x)
            factors.insert(x+1, res)
        res = factors[0]
    if actions.count('/'):
        while(actions.count('/')):
            x = actions.index('/')
            res = divide(factors[x], factors[x+1])
            if res == 'error':
                return res
            factors.pop(x)
            factors.pop(x)
            actions.pop(x)
            factors.append(res)
        res = factors[0]
    for i in range(len(factors)):
        if actions[i] == 'plus':
            res = sum(res, factors[i+1])
        if actions[i] == 'minus':
            res = subtract(res, factors[i+1])
    return res

def clear_ops():
    factors.clear()
    actions.clear()

def click(sign):
    temp = temp_text.get()
    temp += sign
    temp_text.set(temp)

def click_ans():
    if str(temp_ans.get()) == 'error':
        temp_text.set('')
    temp = temp_text.get() + str(temp_result.get())
    temp_text.set(temp)

def click_AC():
    temp_text.set('')
    temp_result.set(0)
    temp_ans.set('')

def click_C():
    temp_text.set('')

def click_DEL():
    temp = temp_text.get()
    temp = temp[0:-1:1]
    temp_text.set(temp)

def click_equal():
    temp = get_next_var(temp_text.get())
    factors.append(float(temp))
    actions.append('equal')
    result = round(calculating(factors, actions), 5)
    clear_ops()
    if result == 'error':
        return temp_ans.set(result)
    temp_ans.set(temp_text.get() + ' = ' + str(result))
    temp_text.set('')
    temp_result.set(result)     
    
def click_plus():
    temp = temp_text.get()
    factors.append(get_next_var(temp))
    actions.append('plus')
    temp += '+'
    temp_text.set(temp)

def click_minus():
    temp = temp_text.get()
    factors.append(get_next_var(temp))
    actions.append('minus')
    temp += '-'
    temp_text.set(temp)

def click_multiply():
    temp = temp_text.get()
    factors.append(get_next_var(temp))
    actions.append('*')
    temp += '*'
    temp_text.set(temp)

def click_divide():
    temp = temp_text.get()
    factors.append(get_next_var(temp))
    actions.append('/')
    temp += '/'
    temp_text.set(temp)




top_frame = Frame(root)

top_but_frame = Frame(top_frame)
but_ans = Button(top_but_frame, text = 'ANS', width = 6, height = 1, command=click_ans)
but_AC = Button(top_but_frame, text = 'AC', width = 7, height = 1, command=click_AC)
but_C = Button(top_but_frame, text = 'C', width = 6, height = 1, command=click_C)
but_DEL = Button(top_but_frame, text = 'DEL', width = 6, height = 1, command=click_DEL)

com_frame = Frame(root)

result_field = Label (com_frame,  height = 2, textvariable = temp_ans, width = 25, borderwidth = 2, relief = "sunken")
enter_field = Label(com_frame, width = 25, height = 2, bg = "#ffffff", borderwidth = 2, relief = "sunken", textvariable = temp_text, justify = RIGHT)

calc_frame = Frame(root)
but1 = Button(calc_frame, text = '1', width = 5, height = 3, command = lambda: click('1'))
but2 = Button(calc_frame, text = '2', width = 5, height = 3, command = lambda: click('2'))
but3 = Button(calc_frame, text = '3', width = 5, height = 3, command = lambda: click('3'))
but4 = Button(calc_frame, text = '4', width = 5, height = 3, command = lambda: click('4'))
but5 = Button(calc_frame, text = '5', width = 5, height = 3, command = lambda: click('5'))
but6 = Button(calc_frame, text = '6', width = 5, height = 3, command = lambda: click('6'))
but7 = Button(calc_frame, text = '7', width = 5, height = 3, command = lambda: click('7'))
but8 = Button(calc_frame, text = '8', width = 5, height = 3, command = lambda: click('8'))
but9 = Button(calc_frame, text = '9', width = 5, height = 3, command = lambda: click('9'))
but0 = Button(calc_frame, text = '0', width = 5, height = 3, command = lambda: click('0'))
but_comma = Button(calc_frame, text = '.', width = 5, height = 3, command = lambda: click('.'))
but_equal = Button(calc_frame, text = '=', width = 5, height = 3, command = click_equal)
but_plus = Button(calc_frame, text = '+', width = 5, height = 3, command = click_plus)
but_minus = Button(calc_frame, text = '-', width = 5, height = 3, command = click_minus)
but_multiply = Button(calc_frame, text = '*', width = 5, height = 3, command = click_multiply)
but_divide = Button(calc_frame, text = '/', width = 5, height = 3, command = click_divide)

