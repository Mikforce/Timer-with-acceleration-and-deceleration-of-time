import time
from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("300x250")

root.title("Time Counter")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root, width=3, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=180, y=20)


def sabmit():
        global btn
        try:
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        except:
            print("Please input the right value")
        while temp > -1:

            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp, 60)


            hours = 0
            if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
                hours, mins = divmod(mins, 60)

            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            root.update()

            k = time.sleep(1)

            if (temp == 0):
                messagebox.showinfo("Отсчет", "Время закончилось")

            temp -= 1




def action():

    time.sleep(3)



# button widget
btn = Button(root, text='Начать отсчет', bd='5',
             command=sabmit)
btn.place(x=50, y=120)

btn2 = Button(root, text='Замедлить', bd='5',
             command=action)
btn2.place(x=200, y=120)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
