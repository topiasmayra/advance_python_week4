import tkinter as tk
import winsound
from PIL import Image, ImageTk
import time
import threading
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
monkey_ernesti = canvas.create_oval(50, 50, 60, 60, fill="brown",tags="ernesti_monkey")
monkey_kernesti = canvas.create_oval(50, 550, 60, 560, fill="red")

# Define a global variable to track collision
collision = False
collision_ernesti = False
collision_kernesti = False

def check_collision_ernesti():
    global collision_ernesti
    x0, y0, x1, y1 = canvas.coords(monkey_ernesti)  # Get the current position of the monkey_ernesti
    monkey_center_ernesti_x = (x0 + x1) / 2  # Calculate the horizontal center of the monkey_ernesti
    continent_x = canvas.winfo_width()  # Get the width of the canvas (should be the right edge)

    if monkey_center_ernesti_x >= continent_x and not collision_ernesti:
        collision_ernesti = True
        print("Collision with ernesti!")
        winsound.Beep(800, 900)

        # Delete the kernesti monkey object
        canvas.delete(monkey_ernesti)
def check_collision_kernesti():
    global collision_kernesti
    x0, y0, x1, y1 = canvas.coords(monkey_kernesti)
    monkey_center_kernesti_x = (x0 + x1) / 2
    continent_x = canvas.winfo_width()

    if monkey_center_kernesti_x >= continent_x and not collision_kernesti:
        collision_kernesti = True
        print("Kernesti Collision!")
        winsound.Beep(940, 800)

        # Delete the kernesti monkey object
        canvas.delete("kernesti_monkey")



# Define the function for moving ernesti monkey
def move_ernesti_monkey():
    global collision_ernesti
    x0, y0, x1, y1 = canvas.coords(monkey_ernesti)  # Get the current position of the monkey_ernesti
    y_center = (y0 + y1) / 2  # Calculate the vertical center of the monkey_ernesti
    island_top = 0  # Set the top of the island

    while not collision:
        for i in range(500):
            if y0 > 0:  # Check if the monkey_ernesti is still above the top of the canvas
                canvas.move(monkey_ernesti, 1, 0)  # Move right
                ikkuna.update()
                # short beep
                winsound.Beep(440, 500)
                time.sleep(0.05)
                check_collision_ernesti()  # Check for collision after each movement

# Define the function for moving kernesti monkey
def move_kernesti_monkey():
    global collision_kernesti
    x0, y0, x1, y1 = canvas.coords(monkey_kernesti)  # Get the current position of the monkey_kernesti
    y_center = (y0 + y1) / 2  # Calculate the vertical center of the monkey_kernesti
    island_top = 0  # Set the top of the island

    # while not collision:  # Commented out to remove collision detection
    for i in range(500):
        canvas.move(monkey_kernesti, 1, 0)  # Move right
        ikkuna.update()
        winsound.Beep(100, 400)
        time.sleep(0.05)
        check_collision_kernesti()

# Create threads for each monkey
thread_ernesti = threading.Thread(target=move_ernesti_monkey)
thread_kernesti = threading.Thread(target=move_kernesti_monkey)

# Start the threads
thread_ernesti.start()
thread_kernesti.start()
while True:
    if collision_ernesti and collision_kernesti:
        i_suppose_i_have_earned_so_much_points(1)
        break  # Exit the loop


# Continuously check for collisions until both monkeys have collided

ikkuna.mainloop()

