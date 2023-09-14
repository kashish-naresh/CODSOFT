# Importing tkinter for working with GUI
from tkinter import *

# Adding items function
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open('file.txt', 'a+') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')

#Deleting items function
def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open('file.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)

        tasks_list_file.close()


# Initializing GUI window
root = Tk()
root.title('To-Do List')
root.geometry('550x385')
root.resizable(0, 0)
root.config(bg="#262626")

# Heading Label
Label(root, text='To-Do List',fg='#d9d9d9', bg='#262626', font=("Broadway", 17), wraplength=300).place(
    x=220, y=7)

# Listbox with all the tasks + Scrollbar
tasks = Listbox(root, selectbackground='#00bfff',fg='#f2f2f2', bg='#595959', font=('Bahnschrift', 12), height=12, width=43)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=466, y=50, height=244)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=75, y=50)

# Adding items to Listbox
with open('file.txt', 'a+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

# Creating Entry to enter new item
new_item_entry = Entry(root, width=67)
new_item_entry.place(x=76, y=300)

# Creating Buttons
add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=165, y=330)

delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                 command=lambda: delete_item(tasks))
delete_btn.place(x=280, y=330)

# Finalizing window
root.update()
root.mainloop()
