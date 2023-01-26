from tkinter import*
import os

from generateur import*

class Window:

    password = Password(number=0, maj=0, mini=0, special=0)
    
    number = 2
    maj = 2
    mini = 3
    special = 1

    def __init__(self, size, first, title) -> None:
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(str(size[0]) + "x" + str(size[1]))
        self.window.minsize(size[0], size[1])
        self.window.config(bg='#C0C0C0')
        self.window.iconbitmap('image/logo-cadena.ico')
        self.frame = Frame(self.window, bg='#C0C0C0')
        self.frame2 = Frame(self.window, bg='#C0C0C0',)
        self.frame3 = Frame(self.window, bg='#C0C0C0',)

        menu = Menu(self.window)


        if first:
            menu.add_command(label=' -  Add', command= Window.LaunchAdd)
            menu.add_command(label=' -  Open Password List', command= Window.OpenTxt)

            ButtonGenerate = Button(self.frame, bg='#FFFFFF', font=('Arial Black', 23), width=10, height=1, command= self.SetLabelPassword, text='Generate')
            ButtonGenerate.grid(column= 1, row=1)

            self.LabelPassword = Label(self.frame2, bg='#FFFFFF',font=('Arial Black', 25), text=Window.password.password, width=15, height=1,  background='#C0C0C0')
            self.LabelPassword.grid(column=1, row=1)

            ## ----------------------------- ##

            ButtonEasy = Button(self.frame3, width=7, height=1, text='Easy', font=('Arial Black', 15), command=Window.DiffEasy)
            ButtonEasy.grid(column=1, row=1)
            ButtonMedium = Button(self.frame3, width=7, height=1, text='Medium', font=('Arial Black', 15), command=Window.DiffMedium)
            ButtonMedium.grid(column=3, row=1)
            ButtonHard = Button(self.frame3, width=7, height=1, text='Hard', font=('Arial Black', 15), command=Window.DiffHard)
            ButtonHard.grid(column=5, row=1)

            LabelPresent2 = Label(self.frame3, width=2, background='#C0C0C0')
            LabelPresent2.grid(column=2, row=1)
            LabelPresent3 = Label(self.frame3, width=2, background='#C0C0C0')
            LabelPresent3.grid(column=4, row=1)

        else:
            global NameEntry
            global MailEntry
            global PasswordEntry

            NameEntry = Entry(self.frame, width=40)
            NameEntry.grid(column=2,row=2)
            LabelName = Label(self.frame, font=('Arial Black', 15), text='Name :', width=9, height=1, background='#C0C0C0', anchor=E)
            LabelName.grid(column=1, row=2)

            MailEntry = Entry(self.frame, width=40)
            MailEntry.grid(column=2,row=3)
            LabelMail = Label(self.frame, font=('Arial Black', 15), text='Mail / ID * :', width=9, height=1, background='#C0C0C0', anchor=E)
            LabelMail.grid(column=1, row=3)

            PasswordEntry = Entry(self.frame, width=40)
            PasswordEntry.grid(column=2,row=4)
            LabelPassword = Label(self.frame, font=('Arial Black', 15), text='Password :', width=9, height=1, background='#C0C0C0', anchor=E)
            LabelPassword.grid(column=1, row=4)

            ButtonValidate = Button(self.frame2, bg='#FFFFFF', borderwidth=3, width=21, height=1, text=' >      ADD      <', font=('Arial Black', 18), command=Window.AddList)
            ButtonValidate.grid(column=1, row=2)

        self.frame.pack(expand=YES)
        self.frame2.pack(expand=YES)
        self.frame3.pack(expand=YES)
        self.window.config(menu= menu)
        self.window.mainloop()

    ## ------------ ##

    def LaunchAdd():
        AddWindow = Window((400, 200), False, "  -  Add Password  -  ")
    LaunchAdd = staticmethod(LaunchAdd)

    def AddTxt(name, mail, password):
        if name != '' and password != '':
            file = open('Password List.txt', 'a')
            file.write(f'{name} : \n')
            if mail != '':
                file.write(f'Email : {mail} \n')
            file.write(f'Password : {password} \n \n')
            file.close()
    AddTxt = staticmethod(AddTxt)

    def AddList():
        global NameEntry
        global MailEntry
        global PasswordEntry
        Window.AddTxt(name=NameEntry.get(), mail=MailEntry.get(), password=PasswordEntry.get())
        NameEntry.delete(0, END)
        MailEntry.delete(0, END)
        PasswordEntry.delete(0, END)
    AddList = staticmethod(AddList)


    def OpenTxt():
        os.system('start notepad Password List.txt')
    OpenTxt = staticmethod(OpenTxt)

    def GeneratePassword(cls):
        Window.password = Password(Window.number, Window.maj, Window.mini, Window.special)
    GeneratePassword = classmethod(GeneratePassword)

    def SetLabelPassword(self):
        Window.GeneratePassword()
        self.LabelPassword.config(text=Window.password.password, background='#A8A8A8')
        LabelPresentCopy = Label(self.frame2, width=1, background='#C0C0C0')
        LabelPresentCopy.grid(column=2, row=1)
        ButtonCopy = Button(self.frame2, width=4, height=1, text='Copy', font=('Arial Black', 8), command=self.ButtonCopy)
        ButtonCopy.grid(column=3, row=1)

    def DiffEasy(cls):
        Window.number = 2
        Window.maj = 2
        Window.mini= 3
        Window.special = 1
    DiffEasy = classmethod(DiffEasy)

    def DiffMedium(cls):
        Window.number = 3
        Window.maj = 3
        Window.mini= 4
        Window.special = 2
    DiffMedium = classmethod(DiffMedium)

    def DiffHard(cls):
        Window.number = 4
        Window.maj = 3
        Window.mini= 5
        Window.special = 2
    DiffHard = classmethod(DiffHard)

    def ButtonCopy(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(Window.password.password)