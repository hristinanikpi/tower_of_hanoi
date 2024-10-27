from src.backend import *
from tkinter import *
import time 

# Function that prints out the solution (lists all the moves) and the time taken to solve
def print_solution():
    
    # Clear previous solution from the listbox and the canvas before displaying the new solution
    myListBox.delete(0, END)
    myCanvas.delete("all") 
    timeLabel.config(text="")
    rodLabel.config(text="")

    # Read number of disks and check if it is valid 
    input_value = myText.get()
    if not input_value:
        myCanvas.delete("all")  # Clear previous drawings
        myListBox.delete(0, END)
        myListBox.insert(END, "Please enter a number grater than 2.")
        return

    try:
        # Convert the input value to intiger and check if it is less than 3
        n = int(input_value)
        if n < 3:
            myCanvas.delete("all")  # Clear previous drawings
            myListBox.delete(0, END)
            myListBox.insert(END, "Please enter a number greater than 2.")
            return
        
        # Draw the rods and the initial positions of the disks
        myCanvas.delete("all")  # Clear previous drawings
        rodLabel.config(text="A                  B                  C")
        for i in range(3):
            myCanvas.create_line(100 + i*100, 180, 100 + i*100, 50, width=6, fill="black")
        base_y = 180
        for i in range(n):
            width = 20 + (n - i - 1) * 20  # Start with the widest disk at the bottom
            top_y = base_y - (i + 1) * 20  # Place each disk higher than the previous one
            myCanvas.create_rectangle(100 - width // 2, top_y, 100 + width // 2, top_y + 20, fill="blue")

        myCanvas.update()  # Update the canvas immediately
        myCanvas.after(2000)  # Wait for a brief moment to show the current state

        # Record the start time
        start_time = time.time()

        # Get the list of moves from tower_of_hanoi_service
        moves = tower_of_hanoi_service(n)["moves"]
        
        # Display the solution by printing all moves into the list box
        myListBox.delete(0, END)
        for i, move in enumerate(moves):
            myListBox.insert(END, str(i + 1) + ". " + move)

        # Calculate elapsed time and print it out
        elapsed_time = time.time() - start_time 
        timeLabel.config(text=f"Time taken: {elapsed_time:.6f} seconds")

        myCanvas.delete("all")  # Clear previous drawings
        #rodLabel.config(text="A                  B                  C")
        for i in range(3):
            myCanvas.create_line(100 + i*100, 180, 100 + i*100, 50, width=6, fill="black")
        base_y = 180
        for i in range(n):
            width = 20 + (n - i - 1) * 20  # Start with the widest disk at the bottom
            top_y = base_y - (i + 1) * 20  # Place each disk higher than the previous one
            myCanvas.create_rectangle(300 - width // 2, top_y, 300 + width // 2, top_y + 20, fill="blue")


        myCanvas.update()  # Update the canvas immediately
        myCanvas.after(2000)  # Wait for a brief moment to show the current state

    # Handle invalid input (e.g., non-integer entries)
    except ValueError:
        myListBox.delete(0, END)
        myListBox.insert(END, "Please enter a valid number.")

# Function to redraw the disks based on their current positions
def draw_towers():
    # Clear previous drawings
    myCanvas.delete("all")  

    for i in range(1, 4):
        # Draw the rods
        myCanvas.create_line(100 + (i - 1) * 100, 180, 100 + (i - 1) * 100, 50, width=6, fill="black")

        # Draw disks starting from the bottom
        for rod_index in range(1, 4):  # 1 for A, 2 for B, 3 for C
            rod_key = chr(64 + rod_index)  # Converts 1->'A', 2->'B', 3->'C'
            for i, disk in enumerate(towers[rod_key]):
                width = 20 + (disk - 1) * 20  # Disk width based on its size
                top_y = 180 - (i + 1) * 20  # Position each disk above the previous one
                myCanvas.create_rectangle(100 + (rod_index - 1) * 100 - width // 2, top_y,
                                        100 + (rod_index - 1) * 100 + width // 2, top_y + 20, fill="blue")

# Function that prints out the solution (lists all the moves) and the time taken to solve
def animate_solution():
    # Clear previous solution from the listbox and the canvas before displaying the new solution
    myListBox.delete(0, END)
    myCanvas.delete("all") 
    timeLabel.config(text="")
    rodLabel.config(text="")
    
    input_value = myText.get()
    if not input_value:
        myListBox.delete(0, END)
        myListBox.insert(END, "Please enter a number of disks.")
        return

    try:
        n = int(input_value)
        if n < 1:
            myListBox.delete(0, END)
            myListBox.insert(END, "Please enter a number greater than 0.")
            return

        moves = tower_of_hanoi_service(n)["moves"]

        rodLabel.config(text="A                  B                  C")
        for i in range(3):
            myCanvas.create_line(100 + i*100, 180, 100 + i*100, 50, width=6, fill="black")

        base_y = 180
        for i in range(n):
            width = 20 + (n - i - 1) * 20  # Start with the widest disk at the bottom
            top_y = base_y - (i + 1) * 20  # Place each disk higher than the previous one
            myCanvas.create_rectangle(100 - width // 2, top_y, 100 + width // 2, top_y + 20, fill="blue")


        myCanvas.update()  # Update the canvas immediately
        myCanvas.after(3000)  # Wait for a brief moment to show the current state

        rodLabel.config(text="A                  B                  C")
        for i in range(3):
            myCanvas.create_line(100 + i*100, 180, 100 + i*100, 50, width=6, fill="black")
        base_y = 180
        for i in range(n):
            width = 20 + (n - i - 1) * 20  # Start with the widest disk at the bottom
            top_y = base_y - (i + 1) * 20  # Place each disk higher than the previous one
            myCanvas.create_rectangle(100 - width // 2, top_y, 100 + width // 2, top_y + 20, fill="blue")


         # Initialize the towers
        global towers
        disks = list(range(n))
        disks.reverse()
        towers = {"A": list(range(n, 0, -1)), "B": [], "C": []}  # rod 'A' has all disks, others are empty



        for i, move in enumerate(moves):
            from_rod_position = move.find("from")
            from_rod = move[from_rod_position+9:from_rod_position+10]
            to_rod_position = move.find("to")
            to_rod = move[to_rod_position+7:to_rod_position+8]
            myListBox.insert(END, str(i + 1) + ". " + move)
            
            # Perform the move
            disk = towers[from_rod].pop()  # Remove the top disk from the from_rod
            towers[to_rod].append(disk)     # Add the disk to the to_rod
            
            draw_towers()  # Redraw the rods after each move
            
            myCanvas.update()  # Update the canvas immediately
            myCanvas.after(1000)  # Wait for a brief moment to show the current state

    
    # Handle invalid input (e.g., non-integer entries)
    except ValueError:
        myListBox.delete(0, END)
        myListBox.insert(END, "Please enter a valid number.")



# Root window
root = Tk()
root.title("Tower of Hanoi Solver")
root.geometry('800x800')
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
myFrame.place(relx=0.5, rely=0.4, anchor=CENTER) 
myListBox = Listbox(myFrame, relief="flat", font=("Arial",12), fg="blue", width=40, height=13)
myListBox.pack(side="left")
myScrollBar = Scrollbar(myFrame,orient="vertical",command=myListBox.yview)
myScrollBar.pack(side ="right", fill = "y" )
myListBox.configure(yscrollcommand=myScrollBar.set)

# Canvas for visualizing towers and disks
myFrame2 = Frame(root)
myFrame2.place(relx=0.5, rely=0.72, anchor=CENTER)
myCanvas = Canvas(myFrame2, width=400, height=200, bg="white")
#myCanvas.pack(side="left", fill=BOTH, expand=True) 
scrollBarV = Scrollbar(myFrame2, orient="vertical",command=myCanvas.yview)
scrollBarV.pack(side ="right", fill = "y" )
scrollBarH = Scrollbar(myFrame2, orient="horizontal",command=myCanvas.xview)
scrollBarH.pack(side ="bottom", fill = "x" )
myCanvas.configure(xscrollcommand=scrollBarH.set, yscrollcommand=scrollBarV.set)
myCanvas.pack(side="left", fill=BOTH, expand=True) 

# Add a frame to the canvas to hold all elements
canvas_frame = Frame(myCanvas)
myCanvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Function to update the scroll region when new content is added
def update_scrollregion(event):
    myCanvas.configure(scrollregion=myCanvas.bbox("all"))

# Bind the update function to the canvas frame
canvas_frame.bind("<Configure>", update_scrollregion)

# Rod Label
rodLabel = Label(root, text="", fg="blue", font=("Arial",13))  
rodLabel.place(relx=0.5, rely=0.9, anchor=CENTER)
rodLabel.configure(background='white')

# Button Widget for providing solution to the puzzle 
myButton = Button(root, text = "Solve", font=("Arial",13), fg = "white", command=print_solution)
myButton.configure(background='blue')
myButton.place(relx=0.5, rely=0.17, anchor=CENTER)

# Time Label
timeLabel = Label(root, text="", fg="blue", font=("Arial",13))  
timeLabel.place(relx=0.5, rely=0.96, anchor=CENTER)
timeLabel.configure(background='white')

root.mainloop()

