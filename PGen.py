from tkinter import *
from random import *
root = Tk()



digits = '0123456789'
lowercase_engletters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_engletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_rusletters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
uppercase_rusletters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
punctuation = '!#$%&*+-=?@^_'

TextR = 'Вас приветсвует программа по созданию паролей созданный DanOK17 \nYou are welcomed by the password creation program created by DanOK17\n\nНапишите "ru" если хотите продолжить на русском \nWrite "en" if you want to continue in English\n'
txt = StringVar()
txt2 = ''
pwd_length = 0
password = ''
chars = ''
language = ''
way = ''



def chk1():
    global chars, digits
    chars += digits
    print(chars)

def chk3():
    global chars, lowercase_engletters
    chars += lowercase_engletters
    print(chars)

def chk2():
    global chars, uppercase_engletters
    chars += uppercase_engletters
    print(chars)

def chk5():
    global chars, lowercase_rusletters
    chars += lowercase_rusletters
    print(chars)

def chk4():
    global chars, uppercase_rusletters
    chars += uppercase_rusletters

def chk6():
    global chars, punctuation
    chars += punctuation
    print(chars)

def further():
    global pwd_length, password, TextR, chars
    btn_d.pack_forget()
    chk1.pack_forget()
    chk2.pack_forget()
    chk3.pack_forget()
    chk4.pack_forget()
    chk5.pack_forget()
    chk6.pack_forget()
    for i in range(pwd_length):
        password += choice(chars)
    TextR = ''
    if language == 'ru':
        TextR=(password, '\n\n Хотите сохранить пароль?\n\n Если "Да", то заранее запишите полный путь к файлу, куда хотите записать пароль, в окно ввода')
        ch_da.pack(fill=BOTH, padx=10)
        ch_net.pack(fill=BOTH, padx=10)
    elif language == 'en':
        TextR = (password, '\n\n Do you want to save your password? \n\n If "Yes", then write down in advance the full path to the file where you want to write the password in the input window.')
        ch_da.pack(fill=BOTH, padx=10)
        ch_net.pack(fill=BOTH, padx=10)
    title.config(text=TextR)



def entry():
    global txt, txt2, TextR, pwd_length,language
    txt2 = str(txt.get())
    if txt2 == 'ru':
        language = 'ru'
        TextR ='Введите длинну пароля'
        title.config(text=TextR)
        ent.delete("0", END)
    elif txt2 == 'en':
        language = 'en'
        TextR = 'Enter password length'
        title.config(text=TextR)
        ent.delete("0", END)
    elif txt2 != 'ru' and txt2 != 'en':
        pwd_length = int(txt.get())
        print(pwd_length)
        ent.delete("0", END)
        if language == 'ru':
            TextR = 'Подумайте перед тем как ставить галочку. Если вы ее нажмете, но можете передумать, программа может работать некорректно!'
            title.config(text=TextR)
            if pwd_length is None:
                pass
            elif pwd_length is not None:
                chk1.config(text='Включить цифры?')
                chk2.config(text='Включить английские буквы верхнего регистра?')
                chk3.config(text='Включить английские буквы нижнего регистра?')
                chk4.config(text='Включить русские буквы верхнего регистра?')
                chk5.config(text='Включить русские буквы нижнего регистра?')
                chk6.config(text='Включить символы? "!#$%&*+-=?@^_"?')
                chk1.pack(fill=BOTH, padx=10)
                chk2.pack(fill=BOTH, padx=10)
                chk3.pack(fill=BOTH, padx=10)
                chk4.pack(fill=BOTH, padx=10)
                chk5.pack(fill=BOTH, padx=10)
                chk6.pack(fill=BOTH, padx=10)
                btn_d.pack(fill=BOTH, pady=2, padx=2)
        elif language == 'en':
            TextR = 'Think before you check the box. If you press it, but you can change your mind, the program may not work correctly!'
            title.config(text=TextR)
            if pwd_length is None:
                pass
            elif pwd_length is not None:
                chk1.pack(fill=BOTH, padx=10)
                chk2.pack(fill=BOTH, padx=10)
                chk3.pack(fill=BOTH, padx=10)
                chk4.pack(fill=BOTH, padx=10)
                chk5.pack(fill=BOTH, padx=10)
                chk6.pack(fill=BOTH, padx=10)
                btn_d.pack(fill=BOTH, pady=2, padx=2)
        btn_ent.destroy()

def da():
    global way
    way = str(txt.get())
    with open(way, "w") as f:
        f.write(password)
    TextR = 'Пароль сохранен!\n\nThe password is saved!'
    title.config(text=TextR)
    ch_da.pack_forget
    ch_net.pack_forget

def net():
    root.destroy()



root['bg'] = '#fafafa'
root.title('PGen')
root.wm_attributes('-alpha', 0.9)
root.geometry('1200x1000')

frametxt = Frame(root, bg='grey')
frametxt.place(relheight=0.6, relwidth=1)

frame_btn = Frame(root, bg='grey', bd=5)
frame_btn.place(relheight=0.4, relwidth=1, rely=0.60)


title = Label(frametxt, text=TextR, bg='white', font=40)
title.pack(fill=BOTH, expand=True, side=TOP)
ent = Entry(frame_btn, bg='white', font=100, bd=2, textvariable=txt)
ent.pack(fill=BOTH, pady=2)
btn_ent = Button(frame_btn, text='Ввести\n\nEnter', font=100, bd=2, command=lambda: entry())
btn_ent.pack(fill=BOTH, pady=2, padx=2)
btn_d = Button(frame_btn, text='Далее\n\nFurther', font=100, bd=2, command=further)
btn_d.pack_forget()
chv_da = IntVar()
chv_da.set(0)
ch_da = Checkbutton(frame_btn, text='Да', variable=chv_da, onvalue=1, offvalue=0, command=da, font=100)
ch_da.pack_forget()
chv_net = IntVar()
chv_net.set(0)
ch_net = Checkbutton(frame_btn, text='Нет', variable=chv_net, onvalue=1, offvalue=0, command=net, font=100)
ch_net.pack_forget()
c1v=IntVar()
c1v.set(0)
chk1 = Checkbutton(frame_btn, text='Include numbers', variable=c1v, onvalue=1, offvalue=0, command=chk1, font=100)
chk1.pack_forget()
c2v=IntVar()
c2v.set(0)
chk2 = Checkbutton(frame_btn, text='Include uppercase english letters?', variable=c2v, onvalue=1, offvalue=0, command=chk2, font=100)
chk2.pack_forget()
c3v=IntVar()
c3v.set(0)
chk3 = Checkbutton(frame_btn, text='Include lowercase english letters?', variable=c3v, onvalue=1, offvalue=0, command=chk3, font=100)
chk3.pack_forget()
c4v=IntVar()
c4v.set(0)
chk4 = Checkbutton(frame_btn, text='Include uppercase russian letters?', variable=c4v, onvalue=1, offvalue=0, command=chk4, font=100)
chk4.pack_forget()
c5v=IntVar()
c5v.set(0)
chk5 = Checkbutton(frame_btn, text='Include lowercase russian letters?', variable=c5v, onvalue=1, offvalue=0, command=chk5, font=100)
chk5.pack_forget()
c6v=IntVar()
c6v.set(0)
chk6 = Checkbutton(frame_btn, text='Include symbols? "!#$%&*+-=?@^_"?', variable=c6v, onvalue=1, offvalue=0, command=chk6, font=100)
chk6.pack_forget()



root.mainloop()