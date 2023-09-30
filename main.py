import tkinter as tk
import winsound
from PIL import Image, ImageTk
import time
import threading
import random
import simpleaudio as sa
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
rescue= False
collision = False
stop_thread_kernesti = False
stop_thread_ernesti = False
collision_ernesti = False
collision_kernesti = False
points = False
stop_generating_monkeys = False
# Create locks for thread safety
ernesti_sentence = []
kernesti_sentence = []
monkey_ernesti_lock = threading.Lock()
monkey_kernesti_lock = threading.Lock()
current_word_index_kernesti = 0
current_word_index_ernesti = 0
# Add variables to keep track of monkeys
total_monkeys_sent_ernesti = 0
total_monkeys_sent_kernesti = 0
ernesti_monkeys_making_it = 0
kernesti_monkeys_making_it = 0
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
def check_collision_kernesti():
    global collision_kernesti
    if monkey_kernesti is not None:
        x0, y0, x1, y1 = canvas.coords(monkey_kernesti)
        monkey_center_kernesti_x = (x0 + x1) / 2
        continent_x = canvas.winfo_width()

        if monkey_center_kernesti_x >= continent_x and not collision_kernesti:
            collision_kernesti = True
            print("Kernesti Collision!")
            winsound.Beep(940, 800)
            kernesti_select_word()
            execute_function()

def check_collision_ernesti():
    global collision_ernesti
    if monkey_ernesti is not None:
        x0, y0, x1, y1 = canvas.coords(monkey_ernesti)
        monkey_center_ernesti_x = (x0 + x1) / 2
        continent_x = canvas.winfo_width()

        if monkey_center_ernesti_x >= continent_x and not collision_ernesti:
            collision_ernesti = True
            print("Ernesti Collision!")
            winsound.Beep(500, 800)
            ernesti_select_word()
            execute_function()

# Create global variables to track the monkeys
monkey_ernesti = None
monkey_kernesti = None

# Create locks for thread safety
ernesti_lock = threading.Lock()
kernesti_lock = threading.Lock()
# Define a flag to track if the function has been called
kernesti_rescued = False
ernesti_rescued = False
def rescve_kernesti():
    global kernesti_rescued
    
    # Check if the function has been called already
    if not kernesti_rescued:
        ship_kernesti = canvas.create_rectangle(200, 250, 240, 280, fill="green")
        x = 200  # Initial x-coordinate of the ship
        while x > 50:
            canvas.move(ship_kernesti, -10, 0)  # Move ship 10 pixels to the left (north)
            ikkuna.update()
            time.sleep(0.1)
            x -= 10

        # Delete the ship when it reaches the island
        canvas.delete(ship_kernesti)
        
        # Display the text
        canvas.create_text(400, 300, text="Kernesti on iloinen koska hän sai avun perille ensimmäisenä", fill="black", font=("Arial", 8))
        
        # Set the flag to True to indicate that the function has been called
        kernesti_rescued = True

        filename = 'kernesti.wav'
        wave_object = sa.WaveObject.from_wave_file(filename)
        play_object = wave_object.play()
        play_object.wait_done()
        i_suppose_i_have_earned_so_much_points(4)
        people_fed_per_monkey = 4
        monkeys_on_ernesti_end = current_word_index_kernesti / people_fed_per_monkey
        monkeys_on_kernesti_end = current_word_index_ernesti / people_fed_per_monkey
        result_label = tk.Label(ikkuna, text="")
        result_label.pack()
        if monkeys_on_ernesti_end > monkeys_on_kernesti_end:
            result_label.config(text="The 'ernesti' end of the continent has more people.")
        elif monkeys_on_kernesti_end > monkeys_on_ernesti_end:
            result_label.config(text="The 'kernesti' end of the continent has more people.")
        else:
            result_label.config(text="Both ends of the continent have an equal number of people.")
        i_suppose_i_have_earned_so_much_points(5)
    # Button to start monkeys






def rescve_ernesti():
    global ernesti_rescued
    print("rescue ernesti")
    if not ernesti_rescued:
        ship_ernesti = canvas.create_rectangle(200, 550, 240, 580, fill="blue")
        x = 200  # Initial x-coordinate of the ship
        while x > 50:
            canvas.move(ship_ernesti, -10, 0)  # Move ship 10 pixels to the left (west)
            ikkuna.update()
            time.sleep(0.1)
            x -= 10

        # Delete the ship when it reaches the island
        canvas.delete(ship_ernesti)
        canvas.create_text(400, 500, text="Ernesti on iloinen koska hän sai avun perille ensimmäisenä", fill="black", font=("Arial", 8))
        ernesti_rescued = True

        filename = 'ernesti.wav'
        wave_object = sa.WaveObject.from_wave_file(filename)
        play_object = wave_object.play()
        play_object.wait_done()
        i_suppose_i_have_earned_so_much_points(4)
        people_fed_per_monkey = 4
        monkeys_on_ernesti_end = current_word_index_kernesti / people_fed_per_monkey
        monkeys_on_kernesti_end = current_word_index_ernesti / people_fed_per_monkey
        result_label = tk.Label(ikkuna, text="")
        result_label.pack()
        if monkeys_on_ernesti_end > monkeys_on_kernesti_end:
            result_label.config(text="The 'ernesti' end of the continent has more people.")
        elif monkeys_on_kernesti_end > monkeys_on_ernesti_end:
            result_label.config(text="The 'kernesti' end of the continent has more people.")
        else:
            result_label.config(text="Both ends of the continent have an equal number of people.")
        i_suppose_i_have_earned_so_much_points(5)

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
        if monkey_ernesti is None and not rescue:
            monkey_ernesti = canvas.create_oval(50, 450, 60, 460, fill="brown")
            collision_ernesti = False
            thread_ernesti = threading.Thread(target=move_monkey_ernesti)
            thread_ernesti.start()

def create_new_monkey_and_start_thread_kernesti():
    global monkey_kernesti
    global collision_kernesti
    with kernesti_lock:
        if monkey_kernesti is None and not rescue:
            monkey_kernesti = canvas.create_oval(50, 150, 60, 160, fill="red")
            collision_kernesti = False
            thread_kernesti = threading.Thread(target=move_monkey_kernesti)
            thread_kernesti.start()

start_button = tk.Button(ikkuna, text="Start Swimming", command=start_monkeys_swimming)
start_button.pack()
def start_monkeys_swimming():
    global stop_generating_monkeys
    stop_generating_monkeys = False  # Reset the flag
    
    # Start generating monkeys until the condition is met or the flag is set
    while not stop_generating_monkeys:
        create_new_monkey_and_start_thread_ernesti()
        create_new_monkey_and_start_thread_kernesti()
        
        # Sleep for a while before creating the next pair of monkeys
        time.sleep(1)  # Adjust the delay as needed



def move_monkey_ernesti():
    global monkey_ernesti, stop_thread_ernesti, stop_generating_monkeys, rescue, stop_thread_kernesti
    x1 = 50  # Initial x-coordinate
    x2 = 350  # Destination x-coordinate
    while x1 < x2 and not stop_thread_ernesti and not stop_generating_monkeys:
        with monkey_ernesti_lock:
            if monkey_ernesti is None:
                break  # Exit the loop if monkey is removed

            probability_of_being_eaten = 0.05
            if random.random() < probability_of_being_eaten:
                print("ernesti eaten")
                winsound.Beep(450, 400)
                canvas.delete(monkey_ernesti)
                monkey_ernesti = None
                stop_thread_ernesti = True
                create_new_monkey_and_start_thread_ernesti()
                return  # Terminate the thread when the monkey is eaten

            else:
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
    if current_word_index_ernesti >= 10 and not rescue:
        rescue = True
        stop_thread_ernesti = True
        stop_thread_kernesti = True
        stop_generating_monkeys = True
        rescve_ernesti()  # This should be rescue_ernesti() instead



def move_monkey_kernesti():
    global monkey_kernesti, stop_thread_kernesti, stop_generating_monkeys,rescue, stop_thread_ernesti , collision_kernesti, stop_thread_kernesti
    x1 = 50  # Initial x-coordinate
    x2 = 350  # Destination x-coordinate
    while x1 < x2 and not stop_thread_kernesti and not stop_thread_ernesti and not stop_generating_monkeys:
        with monkey_kernesti_lock:
            if monkey_kernesti is None:
                break  # Exit the loop if monkey is removed

            probability_of_being_eaten = 0.05
            if random.random() < probability_of_being_eaten:
                print("kernesti eaten")
                winsound.Beep(1000, 400)
                canvas.delete(monkey_kernesti)
                monkey_kernesti = None
                stop_thread_kernesti = True
                create_new_monkey_and_start_thread_kernesti()
                return  # Terminate the thread when the monkey is eaten

            else:
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
    if current_word_index_kernesti >= 10 and not rescue:
        rescue = True
        stop_thread_ernesti = True
        stop_thread_kernesti = True
        stop_generating_monkeys = True
        rescve_kernesti()
def execute_function():
    global points
    if current_word_index_ernesti == 1 and current_word_index_ernesti == 1:
        if not points:
            i_suppose_i_have_earned_so_much_points(1)
            i_suppose_i_have_earned_so_much_points(2)
            print("Function executed for both ernesti and kernesti.")
            points= True
# Create a list to store monkey objects
monkeys = []

class Monkey:
    def __init__(self, canvas, x, y, color, probability_of_being_eaten):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.probability_of_being_eaten = probability_of_being_eaten
        self.dot = canvas.create_oval(x, y, x + 10, y + 10, fill=color)
        self.thread = threading.Thread(target=self.move)
        self.thread.start()
        self.stop_thread_flag = False  # Flag to indicate whether to stop the thread

    def move(self):
        while self.x < 800:
            dx = random.randint(1, 5)
            dy = random.randint(-2, 2)
            self.canvas.move(self.dot, dx, dy)
            self.x += dx
            self.y += dy
            winsound.Beep(6969, 10)
            time.sleep(0.1)
            if not self.stop_thread_flag:
                self.check_collision()  # Check for collision after each movement

        self.canvas.delete(self.dot)

    def check_collision(self):
        x0, y0, x1, y1 = self.canvas.coords(self.dot)
        monkey_center_x = (x0 + x1) / 2
        continent_x = self.canvas.winfo_width()

        if monkey_center_x >= continent_x and random.random() < self.probability_of_being_eaten:
            print(f"{self.color} monkey eaten")
            winsound.Beep(1000, 400)
            self.stop_thread()
        

    def stop_thread(self):
        self.stop_thread_flag = True  # Set the flag to stop the thread

   
# Create a list to store monkey objects
monkeys = []

# Function to start the monkey animation
def start_animation():
    global monkeys

    # Clear any existing monkeys
        monkey.stop_thread()
    monkeys = []

    # Create 10 Kernesti monkeys starting from the north
    for _ in range(10):
        x = random.randint(10, 790)
        y = random.randint(10, 290)
        kernesti = Monkey(canvas, x, y, "red", 0.05)
        monkeys.append(kernesti)

    # Create 10 Ernesti monkeys starting from the south
    for _ in range(10):
        x = random.randint(10, 790)
        y = random.randint(310, 590)
        ernesti = Monkey(canvas, x, y, "brown", 0.05)
        monkeys.append(ernesti)

# Create a button to start the animation
start_button = tk.Button(ikkuna, text="Start Animation", command=start_animation)
start_button.pack()


ikkuna.mainloop()