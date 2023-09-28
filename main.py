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


# Define a global variable to track collision
collision = False
collision_ernesti = False
collision_kernesti = False
# Create locks for thread safety
ernesti_lock = threading.Lock()
kernesti_lock = threading.Lock()

monkey_ernesti_lock = threading.Lock()
monkey_kernesti_lock = threading.Lock()
def check_collision_ernesti():
    global collision_ernesti
    x0, y0, x1, y1 = canvas.coords(monkey_ernesti)  # Get the current position of the monkey_ernesti
    monkey_center_ernesti_x = (x0 + x1) / 2  # Calculate the horizontal center of the monkey_ernesti
    continent_x = canvas.winfo_width()  # Get the width of the canvas (should be the right edge)

    if monkey_center_ernesti_x >= continent_x and not collision_ernesti:
        collision_ernesti = True
        print("Collision with ernesti!")
        winsound.Beep(800, 900)

def check_collision_kernesti():
    global collision_kernesti
    x0, y0, x1, y1 = canvas.coords(monkey_kernesti)
    monkey_center_kernesti_x = (x0 + x1) / 2
    continent_x = canvas.winfo_width()

    if monkey_center_kernesti_x >= continent_x and not collision_kernesti:
        collision_kernesti = True
        print("Kernesti Collision!")
        winsound.Beep(940, 800)

# Create global variables to track the monkeys
monkey_ernesti = None
monkey_kernesti = None

# Create locks for thread safety
ernesti_lock = threading.Lock()
kernesti_lock = threading.Lock()



# Button to start monkeys

def start_monkeys_swimming():
    create_new_monkey_and_start_thread_ernesti()
    create_new_monkey_and_start_thread_kernesti()
def create_new_monkey_and_start_thread_kernesti():
    global monkey_kernesti
    with kernesti_lock:
        if monkey_kernesti is None:
            monkey_kernesti = canvas.create_oval(50, 550, 60, 560, fill="red")
            thread_kernesti = threading.Thread(target=move_monkey_kernesti)
            thread_kernesti.start()

def start_monkeys_swimming():
    create_new_monkey_and_start_thread_ernesti()
    create_new_monkey_and_start_thread_kernesti()
# Button to start monkeys swimming

def create_new_monkey_and_start_thread_ernesti():
    global monkey_ernesti
    with ernesti_lock:
        if monkey_ernesti is None:
            monkey_ernesti = canvas.create_oval(50, 450, 60, 460, fill="brown")

            thread_ernesti = threading.Thread(target=move_monkey_ernesti)
            thread_ernesti.start()

def create_new_monkey_and_start_thread_kernesti():
    global monkey_kernesti
    with kernesti_lock:
        if monkey_kernesti is None:
            monkey_kernesti = canvas.create_oval(50, 150, 60, 160, fill="red")
            thread_kernesti = threading.Thread(target=move_monkey_kernesti)
            thread_kernesti.start()

start_button = tk.Button(ikkuna, text="Start Swimming", command=start_monkeys_swimming)
start_button.pack()


def move_monkey_ernesti():
    global monkey_ernesti
    x1 = 50  # Initial x-coordinate
    x2 = 350  # Destination x-coordinate
    while x1 < x2:
        with monkey_ernesti_lock:
            if monkey_ernesti is None:
                break  # Exit the loop if monkey is removed
            canvas.move(monkey_ernesti, 5, 0)  # Move the monkey 5 pixels to the right
            winsound.Beep(440, 500)
            x1 += 5

        ikkuna.update()
        time.sleep(0.1)
    with monkey_ernesti_lock:
        if monkey_ernesti is not None:
            canvas.delete(monkey_ernesti)
            monkey_ernesti = None
            create_new_monkey_and_start_thread_ernesti()

def move_monkey_kernesti():
    global monkey_kernesti
    x1 = 50  # Initial x-coordinate
    x2 = 350  # Destination x-coordinate
    while x1 < x2:
        with monkey_kernesti_lock:
            if monkey_kernesti is None:
                break  # Exit the loop if monkey is removed
            canvas.move(monkey_kernesti, 5, 0)  # Move the monkey 5 pixels to the right
            x1 += 5
            winsound.Beep(100, 400)
        ikkuna.update()
        time.sleep(0.1)
    with monkey_kernesti_lock:
        if monkey_kernesti is not None:
            canvas.delete(monkey_kernesti)
            monkey_kernesti = None
            create_new_monkey_and_start_thread_kernesti()

ikkuna.mainloop()