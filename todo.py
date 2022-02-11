from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Rewarding Habits")
root.iconbitmap("c:/gui/codemy.ico")
root.geometry("500x500")

# Define Font
my_font = Font(
    family="Futura",
    size=30,
    weight="bold")

# Create Frame
my_frame = Frame(root) # Put frame to anticipate for scrollbars
my_frame.pack(pady=10)

# Create listbox - every line on the list is one item
my_list = Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
)

my_list.pack(side=LEFT, fill=BOTH)

# Create List
todos = ["Do dishes", "Work out", "Buy groceries", "Stretch", "Be your best YOU"]

# Add list to listbox
for todo in todos:
    my_list.insert(END, todo)

# Create srcollbar
my_scrollbar = Scrollbar(my_frame, bg="#000000")
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# BUTTON FUNCTIONALITY
def delete_item():
    my_list.delete(ANCHOR) # ANCHOR targets whatever is highlighted

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    # Cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    # Get rid of selection bar
    my_list.selection_clear(0, END)

def uncross_item():
        # Cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    # Get rid of selection bar
    my_list.selection_clear(0, END)

def delete_crossed():
    idx = 0 # Start with first list item
    while idx < my_list.size(): # loop through available list items
        if my_list.itemcget(idx, "fg") == "#dedede":
            my_list.delete(my_list.index(idx))  

        idx += 1


# Add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete Completed Tasks", command=delete_crossed)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)


root.mainloop()