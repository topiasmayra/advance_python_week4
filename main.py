import tkinter as tk
import winsound
from PIL import Image, ImageTk
import time

ikkuna = tk.Tk()
ikkuna.title("Exercise 5")
ikkuna.geometry("700x700")

# Add a frame for buttons at the top
button_frame = tk.Frame(ikkuna)
button_frame.pack(side="top", fill="x")

point_button = []
for i in range(5):
    button_temp = tk.Button(button_frame, text="Points: " + str(i + 1), padx=40)
    button_temp.pack(side="left")
    point_button.append(button_temp)

# comment out this function
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    ikkuna.update()
    time.sleep(1)
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440 + i * 100, 500)
        ikkuna.update()


# Add two images to the window
island = Image.open("island.png")
continent = Image.open("manner.png")

# Resize the images to fit the window
island = island.resize((200, 600), Image.LANCZOS)
continent = continent.resize((200, 600), Image.LANCZOS)

# Convert the images to a Tkinter-compatible photo image
island_photo = ImageTk.PhotoImage(island)
continent_photo = ImageTk.PhotoImage(continent)

# Create labels with the images
island_label = tk.Label(ikkuna, image=island_photo)
island_label.pack(side="left")  # Place island image on the left

continent_label = tk.Label(ikkuna, image=continent_photo)
continent_label.pack(side="right")  # Place continent image on the left

# Create a canvas
canvas = tk.Canvas(ikkuna, width=900, height=600)
canvas.pack(side="top")

# Define function for drawing monkeys from Island to Continent
monkey = canvas.create_oval(50, 50, 60, 60, fill="brown")

# ...

# Define a global variable to track collision
collision = False


# Define the function for checking collision
def check_collision():
    global collision
    x0, y0, x1, y1 = canvas.coords(monkey)  # Get the current position of the monkey
    monkey_center_x = (x0 + x1) / 2  # Calculate the horizontal center of the monkey
    continent_x = canvas.winfo_width()  # Get the width of the canvas (should be the right edge)

    if monkey_center_x >= continent_x:
        collision = True
        print("Collision!")
        winsound.Beep(440, 500)
    


# Define the function for moving monkeys
def move_monkeys():
    global collision
    x0, y0, x1, y1 = canvas.coords(monkey_)  # Get the current position of the monkey
    y_center = (y0 + y1) / 2  # Calculate the vertical center of the monkey
    island_top = 0  # Set the top of the island

    while not collision:
        for i in range(500):
            if y0 > 0:  # Check if the monkey is still above the top of the canvas
                canvas.move(monkey, 1, 0)  # Move
                ikkuna.update()
                time.sleep(0.05)
                check_collision()  # Check for collision after each movement




move_monkeys()

ikkuna.mainloop()