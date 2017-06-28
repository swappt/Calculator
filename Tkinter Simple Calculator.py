from tkinter import *
from tkinter import ttk

def operation():
    if option.get() == "-":
        minus()
    elif option.get() == "+":
        addition()
    elif option.get() == "/":
        divide()
    elif option.get() == "*":
        multiply()


def addition(*args):
    try:
        valueF1 = float(value1.get())
        valueF2 = float(value2.get())
        total = (valueF1 + valueF2)

        answer_s = str(total) # turn the float into a string
        answer_l = answer_s.split('.') # split the string into 2 lists either side of the decimal place

        if answer_l[1] == '0':
            answer.set(answer_l[0])
        else:
            answer.set(total)

    except ValueError:
        pass

def minus(*args):
    try:
        valueF1 = float(value1.get())
        valueF2 = float(value2.get())
        total = (valueF1 - valueF2)
        print (total)

        answer_s = str(total) # turn the float into a string
        answer_l = answer_s.split('.') # split the string into 2 lists either side of the decimal place

        if answer_l[1] == '0':
            answer.set(answer_l[0])
        else:
            answer.set(total)
            
    except ValueError:
        pass

def multiply(*args):
    try:
        valueF1 = float(value1.get())
        valueF2 = float(value2.get())
        total = (valueF1 * valueF2)
        print (total)

        answer_s = str(total) # turn the float into a string
        answer_l = answer_s.split('.') # split the string into 2 lists either side of the decimal place

        if answer_l[1] == '0':
            answer.set(answer_l[0])
        else:
            answer.set(total)
            
    except ValueError:
        pass

def divide(*args):
    try:
        valueF1 = float(value1.get())
        valueF2 = float(value2.get())
        total = (valueF1 / valueF2)
        print (total)

        answer_s = str(total) # turn the float into a string
        answer_l = answer_s.split('.') # split the string into 2 lists either side of the decimal place

        if answer_l[1] == '0':
            answer.set(answer_l[0])
        else:
            answer.set(total)
            
    except ValueError:
        pass


    
root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

value1 = StringVar()
value2 = StringVar()
answer = StringVar()

value1_entry = ttk.Entry(mainframe, width=5, textvariable=value1)
value1_entry.grid(column=2, row=1)




option_selection = StringVar()
option_value = StringVar()
option = ttk.Combobox(mainframe, textvariable=option_value, state='readonly')
option['values'] = ('+', '-', '/', '*')
option.bind("<<ComboboxSelected>>")
option.current(1)
option.grid(column=3, row=1)

value2_entry = ttk.Entry(mainframe, width=5, textvariable=value2)
value2_entry.grid(column=4, row=1)


ttk.Button(mainframe, text="Calculate", command=operation).grid(column=5, row=3)

ttk.Label(mainframe, text="=").grid(column=1, row=2, sticky=E)

ttk.Label(mainframe, textvariable=answer).grid(column=2, row=2, sticky=E)

value1_entry.focus()
root.bind('<Return>', addition)

root.mainloop()

restart = True





