# template
import tkinter as tk
import winsound
from PIL import Image
import time
ikkuna=tk.Tk()
ikkuna.title("Exercise 5")
ikkuna.geometry("700x700")
# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)
point_button=[]
for i in range(5):
    button_temp=tk.Button(ikkuna,text="Points: "+str(i+1),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100,500)


island=Image.open()




i_suppose_i_have_earned_so_much_points(3)
ikkuna.mainloop()

