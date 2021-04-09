from tkinter import Canvas, END, StringVar, OptionMenu, Label, Entry, Toplevel, Button, DISABLED, Tk, Listbox, Scrollbar
from enum import Enum
from ComponentDB import ComponentDatabase

# asynchronne programovanie, class
# class - nazov napr. class PCComponent, nejaky konstruktor napr. name = name, type = type, ..., destruktor atd.

class EnumeForButton(Enum):
    first = 1
    second = 2

########################################################################################################################

ComponentDB = ComponentDatabase('store.db')

########################################################################################################################

def whenrun_list():
    component_list.delete(0, END)
    for row in ComponentDB.fetch():
        component_list.insert(END, row)

def asc():
    component_list.delete(0, END)
    for row in ComponentDB.orderbynameasc():
        component_list.insert(END, row)

def desc():
    component_list.delete(0, END)
    for row in ComponentDB.orderbynamedesc():
        component_list.insert(END, row)

def lowest():
    component_list.delete(0, END)
    for row in ComponentDB.orderbypricelowest():
        component_list.insert(END, row)

def highest():
    component_list.delete(0, END)
    for row in ComponentDB.orderbypricehighest():
        component_list.insert(END, row)

def graphic():
    component_list.delete(0, END)
    for row in ComponentDB.choosegraphic():
        component_list.insert(END, row)

def processor():
    component_list.delete(0, END)
    for row in ComponentDB.chooseprocessor():
        component_list.insert(END, row)

def motherboard():
    component_list.delete(0, END)
    for row in ComponentDB.choosemotherboard():
        component_list.insert(END, row)

def add_item():
    if nameofcomponent_text.get() == '' or typeofcomponent_text.get() == '' or priceofcomponent_text.get() == '':
        messagebox.showerror('Requiered Fields', 'Fill all fields')
        return
    ComponentDB.insert(nameofcomponent_text.get(), typeofcomponent_text.get(), priceofcomponent_text.get())
    component_list.delete(0, END)
    component_list.insert(END, (nameofcomponent_text.get(), typeofcomponent_text.get(), priceofcomponent_text.get()))
    clear_text()
    whenrun_list()
    window2.destroy()

def select_item(event):
    try:
        global selected_item
        index = component_list.curselection()[0]
        selected_item = component_list.get(index)
        edit_button['state'] = 'active'
        remove_button['state'] = 'active'
    except IndexError:
        pass

def remove_item():
    ComponentDB.remove(selected_item[0])
    whenrun_list()

def update_item():
    ComponentDB.update(selected_item[0], nameofcomponent_text.get(), typeofcomponent_text.get(),
                       priceofcomponent_text.get())
    whenrun_list()
    window2.destroy()

def clear_text():
    nameofcomponent_entry.delete(0, END)
    typeofcomponent_entry.delete(0, END)
    priceofcomponent_entry.delete(0, END)

########################################################################################################################

def choose(*args):
    global secondchoose
    global thirdchoose
    global variable
    secondchoices = ['A - Z', 'Z - A']
    thirdchoices = ['Lowest', 'Highest']

    variable = StringVar(window3)
    variable.set('Choose')

    if firstvariable.get() == 'Name':
        secondchoose = OptionMenu(window3, variable, *secondchoices)
        secondchoose.grid(row=0, column=1, pady=10, padx=10)
        ok_button['state'] = 'disabled'
        othervariable.set('Choose')
        variable.trace('w', choose2)
        try:
            thirdchoose.destroy()
        except:
            print('Thirdchoose has not been created yet')  # Jedna z moznosti ako vyriesit tuto situaciu je try except
            pass

    elif firstvariable.get() == 'Price':
        thirdchoose = OptionMenu(window3, variable, *thirdchoices)
        thirdchoose.grid(row=0, column=1, pady=10, padx=10)
        ok_button['state'] = 'disabled'
        othervariable.set('Choose')
        variable.trace('w', choose2)
        try:
            secondchoose.destroy()
        except:
            print('Secondchoose has not been created yet')  # Jedna z moznosti ako vyriesit tuto situaciu je try except
            pass

def choose2(*args):
    if variable.get() == 'A - Z':
        ok_button['state'] = 'active'

    elif variable.get() == 'Z - A':
        ok_button['state'] = 'active'

    elif variable.get() == 'Lowest':
        ok_button['state'] = 'active'

    else:
        ok_button['state'] = 'active'

def otherchoose(*args):
    if othervariable.get() == 'All':
        firstvariable.set('Choose')
        ok_button['state'] = 'active'
        try:
            secondchoose.destroy()
            thirdchoose.destroy()  # Znova jedna z moznosti ako vyriesit tuto situaciu
        except:
            print('Secondchoose and Thirdchoose has not been created yet')
            pass

    elif othervariable.get() == 'Graphic Card':
        firstvariable.set('Choose')
        ok_button['state'] = 'active'
        try:
            secondchoose.destroy()
            thirdchoose.destroy()  # Znova jedna z moznosti ako vyriesit tuto situaciu
        except:
            print('Secondchoose and Thirdchoose has not been created yet')
            pass

    elif othervariable.get() == 'Processor':
        firstvariable.set('Choose')
        ok_button['state'] = 'active'
        try:
            secondchoose.destroy()
            thirdchoose.destroy()  # Znova jedna z moznosti ako vyriesit tuto situaciu
        except:
            print('Secondchoose and Thirdchoose has not been created yet')
            pass

    elif othervariable.get() == 'Motherboard':
        firstvariable.set('Choose')
        ok_button['state'] = 'active'
        try:
            secondchoose.destroy()
            thirdchoose.destroy()  # Znova jedna z moznosti ako vyriesit tuto situaciu
        except:
            print('Secondchoose and Thirdchoose has not been created yet')
            pass

def filter_items():
    # Rozhoduje sa na zaklade zvolenej moznosti
    if variable.get() == 'A - Z':
        asc()

    elif variable.get() == 'Z - A':
        desc()

    elif variable.get() == 'Lowest':
        lowest()

    elif variable.get() == 'Highest':
        highest()

    elif othervariable.get() == 'All':
        whenrun_list()

    elif othervariable.get() == 'Graphic Card':
        graphic()

    elif othervariable.get() == 'Processor':
        processor()

    elif othervariable.get() == 'Motherboard':
        motherboard()

    window3.destroy()

def window_close():
    window.destroy()

def another_close():
    window2.destroy()

def filter_close():
    window3.destroy()

########################################################################################################################

def another_gui(button_id):
    global window2
    global nameofcomponent_text
    global nameofcomponent_label
    global nameofcomponent_entry
    global typeofcomponent_text
    global typeofcomponent_label
    global typeofcomponent_entry
    global priceofcomponent_text
    global priceofcomponent_label
    global priceofcomponent_entry

    # Vytvara okno a kontroluje ci nie je otvorene
    try:
        if window2.state() == 'normal':
            window2.focus()
    except:
        window2 = Toplevel()
        window2.title('Another GUI')
        window2.geometry('400x200')

    # Nazov komponentu
    nameofcomponent_text = StringVar()
    nameofcomponent_label = Label(window2, text='Component Name', font=('bold', 10))
    nameofcomponent_label.grid(row=1, column=0, pady=10, padx=10)
    nameofcomponent_entry = Entry(window2, textvariable=nameofcomponent_text)
    nameofcomponent_entry.grid(row=1, column=1)

    # Typ komponentu
    typeofcomponent_text = StringVar()
    typeofcomponent_label = Label(window2, text='Component Type', font=('bold', 10))
    typeofcomponent_label.grid(row=2, column=0, pady=10, padx=10)
    typeofcomponent_entry = Entry(window2, textvariable=typeofcomponent_text)
    typeofcomponent_entry.grid(row=2, column=1)

    # Cena komponentu
    priceofcomponent_text = StringVar()
    priceofcomponent_label = Label(window2, text='Component Price', font=('bold', 10))
    priceofcomponent_label.grid(row=3, column=0, pady=10, padx=10)
    priceofcomponent_entry = Entry(window2, textvariable=priceofcomponent_text)
    priceofcomponent_entry.grid(row=3, column=1)

    # Tlacidla
    if button_id == EnumeForButton.first:
        ok_button = Button(window2, text='OK', width=12, command=add_item)
        ok_button.grid(row=0, column=0, pady=10, padx=10)

        clear_button = Button(window2, text='Clear', width=12, command=clear_text)
        clear_button.grid(row=0, column=1, pady=10, padx=10)

        close_button = Button(window2, text='Close', width=12, command=another_close)
        close_button.grid(row=0, column=2, pady=10, padx=10)

    elif button_id == EnumeForButton.second:
        ok_button = Button(window2, text='Edit', width=12, command=update_item)
        ok_button.grid(row=0, column=0, pady=10, padx=10)

        clear_button = Button(window2, text='Clear', width=12, command=clear_text)
        clear_button.grid(row=0, column=1, pady=10, padx=10)

        close_button = Button(window2, text='Close', width=12, command=another_close)
        close_button.grid(row=0, column=2, pady=10, padx=10)

        nameofcomponent_entry.delete(0, END)
        nameofcomponent_entry.insert(END, selected_item[1])
        typeofcomponent_entry.delete(0, END)
        typeofcomponent_entry.insert(END, selected_item[2])
        priceofcomponent_entry.delete(0, END)
        priceofcomponent_entry.insert(END, selected_item[3])

########################################################################################################################

def filter_gui():
    global window3
    global firstvariable
    global othervariable
    global ok_button

    # Vytvara okno a kontroluje ci nie je otvorene
    try:
        if window3.state() == 'normal':
            window3.focus()
    except:
        window3 = Toplevel()
        window3.title('Filter GUI')
        window3.geometry('400x200')

    # OptionMenu
    firstchoices = ['Name', 'Price']
    otherchoices = ['All', 'Graphic Card', 'Processor', 'Motherboard']

    firstvariable = StringVar(window3)
    firstvariable.set('Choose')

    othervariable = StringVar(window3)
    othervariable.set('Choose')

    # Pri preklikavani resp. pri vyberani z moznosti + volanie funkcie
    firstvariable.trace('w', choose)
    othervariable.trace('w', otherchoose)

    # Tlacidla
    firstchoose = OptionMenu(window3, firstvariable, *firstchoices)
    firstchoose.grid(row=0, column=0, pady=10, padx=10)

    anotherchoose = OptionMenu(window3, othervariable, *otherchoices)
    anotherchoose.grid(row=1, column=0, pady=10, padx=10)

    ok_button = Button(window3, text='OK', width=12, command=filter_items, state=DISABLED)
    ok_button.grid(row=2, column=0, pady=10, padx=10)

    cancel_button = Button(window3, text='Cancel', width=12, command=filter_close)
    cancel_button.grid(row=2, column=1, pady=10, padx=10)

########################################################################################################################

# Vytvara okno
window = Tk()

# ListBox
component_list = Listbox(window, height=12, width=50)
component_list.grid(row=1, column=0, columnspan=3, rowspan=6, pady=10, padx=10)

# Scroller
scrollbar = Scrollbar(window)
scrollbar.grid(row=1, column=3, pady=10)

# Nastavenie scrollovania pre listbox
component_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=component_list.yview)

# Bind Select
component_list.bind('<<ListboxSelect>>', select_item)

# Tlacidla
add_button = Button(window, text='Add', width=12, command=lambda: another_gui(EnumeForButton.first))
add_button.grid(row=0, column=0, pady=10, padx=10)

remove_button = Button(window, text='Remove', width=12, command=remove_item, state=DISABLED)
remove_button.grid(row=0, column=1, pady=10, padx=10)

edit_button = Button(window, text='Edit', width=12, command=lambda: another_gui(EnumeForButton.second), state=DISABLED)
edit_button.grid(row=0, column=2, pady=10, padx=10)

filter_button = Button(window, text='Filter', width=12, command=filter_gui)
filter_button.grid(row=0, column=3, pady=10, padx=10)

close_button = Button(window, text='Close', width=12, command=window_close)
close_button.grid(row=8, column=0, pady=10, padx=10)

# Nadpis a velkost okna
window.title('Component database')
window.geometry('480x340')

# Volanie funkcie whrenrun_list()
whenrun_list()

# Spusta program
window.mainloop()