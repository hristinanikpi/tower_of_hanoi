from backend import *
from tkinter import *
from tkinter import ttk
import time 

# Function that prints out the solution (lists all the moves) and the time taken to solve
def print_solution():
    input_value = myText.get()
    if not input_value:
        myListBox.delete(0, END)
        myListBox.insert(END, "Please enter a number of disks.")
        return

    try:
        # Convert the input to an integer
        n = int(input_value)

        # Check if n is less than 1
        if n < 1:
            myListBox.delete(0, END)
            myListBox.insert(END, "Please enter a number greater than 0.")
            return

        # Record the start time
        start_time = time.time()

        # Get the list of moves from tower_of_hanoi_service
        moves = tower_of_hanoi_service(n)["moves"]
        
        # Clear previous solution from the listbox before displaying the new solution
        myListBox.delete(0, END)
        
        # Print each move into the listbox
        for i, move in enumerate(moves):
            myListBox.insert(END, str(i + 1) + ". " + move)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time 
        timeLabel.config(text=f"Time taken: {elapsed_time:.6f} seconds")

    # Handle invalid input (e.g., non-integer entries)
    except ValueError:
        myListBox.delete(0, END)
        myListBox.insert(END, "Please enter a valid number.")

# Root window
root = Tk()
root.title("Tower of Hanoi Solver")
root.geometry('500x600')
root.configure(background='white')

# Label for entering the number of disks
myLabel = Label(root, text = "Enter the number of disks: ", fg="blue", font=("Arial",13))
myLabel.grid()
myLabel.place(relx=0.5, rely=0.05,anchor=CENTER)
myLabel.configure(background='white')

# Entry Field for entering the number of disks
myText = Entry(root, fg="blue", width=10)
myText.place(relx=0.5, rely=0.1,anchor=CENTER)

# List Box with a Scroll Bar to print out the solution 
myFrame = Frame (root)
myFrame.place(relx=0.5, rely=0.52, anchor=CENTER) 
myListBox = Listbox(myFrame,relief="flat", font=("Arial",12), fg="blue", width=40, height=16)
myListBox.pack(side="left")
myScrollBar = Scrollbar(myFrame,orient="vertical",command=myListBox.yview)
myScrollBar.pack(side ="right", fill = "y" )
myListBox.configure(yscrollcommand=myScrollBar.set)

# Button Widget for providing solution to the puzzle 
myButton = Button(root, text = "Solve", font=("Arial",13), fg = "white", command=print_solution)
myButton.configure(background='blue')
myButton.place(relx=0.5, rely=0.17, anchor=CENTER)

# Time Label
timeLabel = Label(root, text="", fg="blue", font=("Arial",13))  
timeLabel.place(relx=0.5, rely=0.87, anchor=CENTER)
timeLabel.configure(background='white')

root.mainloop()

