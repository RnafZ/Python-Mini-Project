import tkinter as tk

window = tk.Tk()
window.title('Calculator')

def click(button):
    value = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,value+button)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,'Error')

def clear():
    entry.delete(0,tk.END)

def backspace():
    value = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,value[:-1])

entry = tk.Entry(window,width=16,font=('Arial',24),bd=10,relief='ridge',justify='right')
entry.grid(row=0,columnspan=4)

button = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('**',4,2),('+',4,3),
]

for (text,row,column) in button:
    if text in ['**','+','-','*','/']:
        tk.Button(window,width=5,height=3,text=text,font=('Arial',18),bg='cyan',command=lambda t=text : click(t)).grid(row=row,column=column)
    else:
        tk.Button(window,width=5,height=3,text=text,font=('Arial',18),bg='lightblue',command=lambda t=text : click(t)).grid(row=row,column=column)

equal_button = tk.Button(window,width=11,height=2,text='=',font=('Arial',18),bg='blue',command=calculate)
equal_button.grid(row=5,column=0,columnspan=2)

clear_button = tk.Button(window,width=5,height=2,text='C',font=('Arial',18),bg='yellow',command=clear)
clear_button.grid(row=5,column=2)

backspace_button = tk.Button(window,width=5,height=2,text='<<<',font=('Arial',18),bg='red',command=backspace)
backspace_button.grid(row=5,column=3)

window.mainloop()