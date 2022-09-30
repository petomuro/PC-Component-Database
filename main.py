from tkinter import END, StringVar, OptionMenu, Label, Entry, Toplevel, Button, DISABLED, Tk, Listbox, Scrollbar, \
    messagebox

from ComponentAPI import ComponentAPI


def when_run_list():
    component_list.delete(0, END)

    for row in component_api.fetch_all():
        component_list.insert(END, row)


def asc():
    component_list.delete(0, END)

    for row in component_api.order_by_name_asc():
        component_list.insert(END, row)


def desc():
    component_list.delete(0, END)

    for row in component_api.order_by_name_desc():
        component_list.insert(END, row)


def lowest():
    component_list.delete(0, END)

    for row in component_api.order_by_lowest_price():
        component_list.insert(END, row)


def highest():
    component_list.delete(0, END)

    for row in component_api.order_by_highest_price():
        component_list.insert(END, row)


def graphic():
    component_list.delete(0, END)

    for row in component_api.fetch_all_graphic_cards():
        component_list.insert(END, row)


def processor():
    component_list.delete(0, END)

    for row in component_api.fetch_all_processors():
        component_list.insert(END, row)


def motherboard():
    component_list.delete(0, END)

    for row in component_api.fetch_all_motherboards():
        component_list.insert(END, row)


def add_item():
    if name_of_component_text.get() == '' or type_of_component_text.get() == '' or price_of_component_text.get() == '':
        messagebox.showerror('Required fields', 'Fill all fields')

        return

    component_api.insert(name_of_component_text.get(), type_of_component_text.get(), price_of_component_text.get())

    component_list.delete(0, END)
    component_list.insert(END,
                          (name_of_component_text.get(), type_of_component_text.get(), price_of_component_text.get()))

    clear_text()
    when_run_list()
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
    component_api.remove(selected_item[0])

    when_run_list()


def update_item():
    component_api.update(selected_item[0], name_of_component_text.get(), type_of_component_text.get(),
                         price_of_component_text.get())

    when_run_list()
    window2.destroy()


def clear_text():
    name_of_component_entry.delete(0, END)
    type_of_component_entry.delete(0, END)
    price_of_component_entry.delete(0, END)


########################################################################################################################

def choose(*args):
    global second_choose
    global third_choose
    global variable

    second_choices = ['A - Z', 'Z - A']
    third_choices = ['Lowest', 'Highest']

    variable = StringVar(window3)
    variable.set('Choose')

    if first_variable.get() == 'Name':
        second_choose = OptionMenu(window3, variable, *second_choices)
        second_choose.grid(row=0, column=1, pady=10, padx=10)

        ok_button['state'] = 'disabled'

        other_variable.set('Choose')
        variable.trace('w', choose2)

        try:
            third_choose.destroy()
        except:
            pass

    elif first_variable.get() == 'Price':
        third_choose = OptionMenu(window3, variable, *third_choices)
        third_choose.grid(row=0, column=1, pady=10, padx=10)

        ok_button['state'] = 'disabled'

        other_variable.set('Choose')
        variable.trace('w', choose2)

        try:
            second_choose.destroy()
        except:
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


def other_choose(*args):
    if other_variable.get() == 'All':
        first_variable.set('Choose')

        ok_button['state'] = 'active'

        try:
            second_choose.destroy()
            third_choose.destroy()
        except:
            pass

    elif other_variable.get() == 'Graphic card':
        first_variable.set('Choose')

        ok_button['state'] = 'active'

        try:
            second_choose.destroy()
            third_choose.destroy()
        except:
            pass

    elif other_variable.get() == 'Processor':
        first_variable.set('Choose')

        ok_button['state'] = 'active'

        try:
            second_choose.destroy()
            third_choose.destroy()
        except:
            pass

    elif other_variable.get() == 'Motherboard':
        first_variable.set('Choose')
        ok_button['state'] = 'active'

        try:
            second_choose.destroy()
            third_choose.destroy()
        except:
            pass


def filter_items():
    # The decision is made on the basis of the chosen option
    if variable.get() == 'A - Z':
        asc()

    elif variable.get() == 'Z - A':
        desc()

    elif variable.get() == 'Lowest':
        lowest()

    elif variable.get() == 'Highest':
        highest()

    elif other_variable.get() == 'All':
        when_run_list()

    elif other_variable.get() == 'Graphic card':
        graphic()

    elif other_variable.get() == 'Processor':
        processor()

    elif other_variable.get() == 'Motherboard':
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
    global name_of_component_text
    global name_of_component_label
    global name_of_component_entry
    global type_of_component_text
    global type_of_component_label
    global type_of_component_entry
    global price_of_component_text
    global price_of_component_label
    global price_of_component_entry

    # Creates window and checks if is not open
    try:
        if window2.state() == 'normal':
            window2.focus()
    except:
        window2 = Toplevel()

        if button_id == 'Add':
            window2.title('Add component')
        else:
            window2.title('Edit component')

        # window2.geometry('400x200')

    # Component name
    name_of_component_text = StringVar()

    name_of_component_label = Label(window2, text='Component name', font=('bold', 10))
    name_of_component_label.grid(row=1, column=0, pady=10, padx=10)

    name_of_component_entry = Entry(window2, textvariable=name_of_component_text)
    name_of_component_entry.grid(row=1, column=1)

    # Component type
    type_of_component_text = StringVar()

    type_of_component_label = Label(window2, text='Component type', font=('bold', 10))
    type_of_component_label.grid(row=2, column=0, pady=10, padx=10)

    type_of_component_entry = Entry(window2, textvariable=type_of_component_text)
    type_of_component_entry.grid(row=2, column=1)

    # Component price
    price_of_component_text = StringVar()

    price_of_component_label = Label(window2, text='Component price', font=('bold', 10))
    price_of_component_label.grid(row=3, column=0, pady=10, padx=10)

    price_of_component_entry = Entry(window2, textvariable=price_of_component_text)
    price_of_component_entry.grid(row=3, column=1)

    # Buttons
    if button_id == 'Add':
        ok_button = Button(window2, text='OK', width=12, command=add_item)
        ok_button.grid(row=0, column=0, pady=10, padx=10)

        clear_button = Button(window2, text='Clear', width=12, command=clear_text)
        clear_button.grid(row=0, column=1, pady=10, padx=10)

        close_button = Button(window2, text='Close', width=12, command=another_close)
        close_button.grid(row=0, column=2, pady=10, padx=10)
    elif button_id == 'Edit':
        ok_button = Button(window2, text='Edit', width=12, command=update_item)
        ok_button.grid(row=0, column=0, pady=10, padx=10)

        clear_button = Button(window2, text='Clear', width=12, command=clear_text)
        clear_button.grid(row=0, column=1, pady=10, padx=10)

        close_button = Button(window2, text='Close', width=12, command=another_close)
        close_button.grid(row=0, column=2, pady=10, padx=10)

        name_of_component_entry.delete(0, END)
        name_of_component_entry.insert(END, selected_item[1])

        type_of_component_entry.delete(0, END)
        type_of_component_entry.insert(END, selected_item[2])

        price_of_component_entry.delete(0, END)
        price_of_component_entry.insert(END, selected_item[3])


########################################################################################################################

def filter_gui():
    global window3
    global first_variable
    global other_variable
    global ok_button

    # Creates window and checks if is not open
    try:
        if window3.state() == 'normal':
            window3.focus()
    except:
        window3 = Toplevel()
        window3.title('Filter components')
        # window3.geometry('400x200')

    # Option menu
    first_choices = ['Name', 'Price']
    other_choices = ['All', 'Graphic card', 'Processor', 'Motherboard']

    first_variable = StringVar(window3)
    first_variable.set('Choose')

    other_variable = StringVar(window3)
    other_variable.set('Choose')

    # When clicking or selecting from options + function call
    first_variable.trace('w', choose)
    other_variable.trace('w', other_choose)

    # Buttons
    first_choose = OptionMenu(window3, first_variable, *first_choices)
    first_choose.grid(row=0, column=0, pady=10, padx=10)

    another_choose = OptionMenu(window3, other_variable, *other_choices)
    another_choose.grid(row=1, column=0, pady=10, padx=10)

    ok_button = Button(window3, text='OK', width=12, command=filter_items, state=DISABLED)
    ok_button.grid(row=2, column=0, pady=10, padx=10)

    cancel_button = Button(window3, text='Cancel', width=12, command=filter_close)
    cancel_button.grid(row=2, column=1, pady=10, padx=10)


########################################################################################################################

if __name__ == '__main__':
    component_api = ComponentAPI()

    # Create windows
    window = Tk()

    # Title and window size
    window.title('Components')
    # window.geometry('800x600')

    # Listbox
    component_list = Listbox(window, height=12, width=50)
    component_list.grid(row=1, column=0, columnspan=3, rowspan=6, pady=10, padx=10)

    # Scrollbar
    scrollbar = Scrollbar(window)
    scrollbar.grid(row=1, column=3, pady=10)

    # Set scrollbar for Listbox
    component_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=component_list.yview)

    # Bind Select
    component_list.bind('<<ListboxSelect>>', select_item)

    # Buttons
    add_button = Button(window, text='Add', width=12, command=lambda: another_gui('Add'))
    add_button.grid(row=0, column=0, pady=10, padx=10)

    remove_button = Button(window, text='Remove', width=12, command=remove_item, state=DISABLED)
    remove_button.grid(row=0, column=1, pady=10, padx=10)

    edit_button = Button(window, text='Edit', width=12, command=lambda: another_gui('Edit'),
                         state=DISABLED)
    edit_button.grid(row=0, column=2, pady=10, padx=10)

    filter_button = Button(window, text='Filter', width=12, command=filter_gui)
    filter_button.grid(row=0, column=3, pady=10, padx=10)

    close_button = Button(window, text='Close', width=12, command=window_close)
    close_button.grid(row=8, column=0, pady=10, padx=10)

    when_run_list()

    # Run program
    window.mainloop()
