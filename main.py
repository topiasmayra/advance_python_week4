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
stop_thread_kernesti = False
stop_thread_ernesti = False
collision_ernesti = False
collision_kernesti = False
# Create locks for thread safety
ernesti_sentence = []
kernesti_sentence = []
monkey_ernesti_lock = threading.Lock()
monkey_kernesti_lock = threading.Lock()
current_word_index_kernesti = 0
current_word_index_ernesti = 0
sentence_words = ["Ernesti", "ja", "Kernesti", "tässä", "terve!", "Olemme", "autiolla", "saarella,", "ja", "voisitteko", "tulla", "sieltä", "sivistyksestä", "joku", "hakemaan", "meidät", "pois!", "Kiitos!"]



# Create a lock
lock = threading.Lock()

def ernesti_select_word():
    global current_word_index_ernesti
    # Acquire the lock before modifying ernesti_sentence and current_word_index_ernesti
    with lock:
        if current_word_index_ernesti < len(sentence_words):
            word = sentence_words[current_word_index_ernesti]
            ernesti_sentence.append(word)
            current_word_index_ernesti += 1

def kernesti_select_word():
    global current_word_index_kernesti
    # Acquire the lock before modifying kernesti_sentence and current_word_index_kernesti
    with lock:
        if current_word_index_kernesti < len(sentence_words):
            word = sentence_words[current_word_index_kernesti]
            kernesti_sentence.append(word)
            current_word_index_kernesti += 1


# Function to check and display Kernesti's progress


def move_monkey_ernesti():
    global monkey_ernesti, stop_thread_ernesti
    x1 = 50  # Initial x-coordinate
    x2 = 350  # Destination x-coordinate
    while x1 < x2 and not stop_thread_ernesti:
        with monkey_ernesti_lock:
            if monkey_ernesti is None:
                break  # Exit the loop if monkey is removed
            canvas.move(monkey_ernesti, 5, 0)  # Move the monkey 5 pixels to the right
            x1 += 5
            winsound.Beep(100, 400)
            check_collision_ernesti()  # Check for collision after each movement
        ikkuna.update()
        time.sleep(0.1)
    with monkey_ernesti_lock:
        if monkey_ernesti is not None:
            canvas.delete(monkey_ernesti)
            monkey_ernesti = None
            stop_thread_ernesti = False  # Reset the flag
            create_new_monkey_and_start_thread_ernesti()

def check_collision_kernesti():
    global collision_kernesti, stop_thread_kernesti
    x0, y0, x1, y1 = canvas.coords(monkey_kernesti)
    monkey_center_kernesti_x = (x0 + x1) / 2
    continent_x = canvas.winfo_width()

    if monkey_center_kernesti_x >= continent_x and not collision_kernesti:
        collision_kernesti = True
        print("Kernesti Collision!")
        winsound.Beep(940, 800)
        kernesti_select_word()
        stop_thread_kernesti = True  # Stop the thread
def check_collision_ernesti():
    global collision_ernesti, stop_thread_ernesti
    x0, y0, x1, y1 = canvas.coords(monkey_ernesti)
    monkey_center_ernesti_x = (x0 + x1) / 2
    continent_x = canvas.winfo_width()

    if monkey_center_ernesti_x >= continent_x and not collision_ernesti:
        collision_ernesti = True
        print("Ernesti Collision!")
        winsound.Beep(500, 800)
        ernesti_select_word()
        stop_thread_ernesti = True  # Stop the thread
        collision_ernesti = False



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


def create_new_monkey_and_start_thread_ernesti():
    global monkey_ernesti
    with ernesti_lock:
        if monkey_ernesti is None:
            monkey_ernesti = canvas.create_oval(50, 450, 60, 460, fill="brown")
            collision_ernesti = False
            thread_ernesti = threading.Thread(target=move_monkey_ernesti)
            thread_ernesti.start()

def create_new_monkey_and_start_thread_kernesti():
    global monkey_kernesti
    global collision_kernesti
    with kernesti_lock:
        if monkey_kernesti is None:
            monkey_kernesti = canvas.create_oval(50, 150, 60, 160, fill="red")
            collision_kernesti = False
            thread_kernesti = threading.Thread(target=move_monkey_kernesti)
            thread_kernesti.start()

start_button = tk.Button(ikkuna, text="Start Swimming", command=start_monkeys_swimming)
start_button.pack()
def move_monkey_kernesti():
    global monkey_kernesti, stop_thread_kernesti
    x1 = 50  # Initial x-coordinate
    x2 = 350  # Destination x-coordinate
    while x1 < x2 and not stop_thread_kernesti:
        with monkey_kernesti_lock:
            if monkey_kernesti is None:
                break  # Exit the loop if monkey is removed
            canvas.move(monkey_kernesti, 5, 0)  # Move the monkey 5 pixels to the right
            x1 += 5
            winsound.Beep(500, 400)
            check_collision_kernesti()  # Check for collision after each movement
        ikkuna.update()
        time.sleep(0.1)
    with monkey_kernesti_lock:
        if monkey_kernesti is not None:
            canvas.delete(monkey_kernesti)
            monkey_kernesti = None
            stop_thread_kernesti = False  # Reset the flag
            create_new_monkey_and_start_thread_kernesti()


def check_kernesti_progress():
    global current_word_index_kernesti
    if current_word_index_kernesti < len(sentence_words):
        words_learned = current_word_index_kernesti
        total_words = len(sentence_words)
        print(f"Kernesti has learned {words_learned}/{total_words} words.")
        print(collision_kernesti)
        print("ernesti collision" + str(collision_ernesti))
        print("ernesti threath" + str(stop_thread_ernesti))




button_to_check= tk.Button(ikkuna, text="Check Progress", command=check_kernesti_progress)
button_to_check.pack()
ikkuna.mainloop()