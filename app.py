import tkinter
window = tkinter.Tk()

window.title("Hello!")
canvas = tkinter.Canvas(window, width=750, height=500, bg='black')
canvas.pack()
canvas.create_text(370, 25, text="CapybaraClicker", fill="white", font='Arial 25 bold')
canvas.create_text(370, 55, text="крутой кликер", fill="white", font='Arial 15 bold')
canvas.create_oval(300, 300, 150, 150, fill="green")
button = tkinter.Button(window, text="click", width=40)
button.pack(pady=20)
button.place(x=220, y=400)

clickCount = 0

def click(event):
    global clickCount
    clickCount += 1
    if clickCount == 1:
        button.configure(text="Let`s Go!")
        print(f"{clickCount}")
    elif clickCount == 2:
        button.configure(text='Go!')
        print(f"{clickCount}")
    else:
        button.configure(text=f'У вас {clickCount} коинов')
        print(f"{clickCount}")

button.bind("<ButtonRelease-1>", click)
print("Go!")


window.mainloop()