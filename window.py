from tkinter import*
import os

from generateur import*

class Window:

    password = Password(name='', number=0, maj=0, mini=0, special=0)

    ## DEBUG ##
    passwordName = 'n'
    number = 2
    maj = 2
    mini = 2
    special = 2
    ############

    def __init__(self, size, first, title) -> None:
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(str(size[0]) + "x" + str(size[1]))
        self.window.minsize(size[0], size[1])
        self.window.config(bg='#C0C0C0')
        self.window.iconbitmap('image/logo-cadena.ico')
        self.frame = Frame(self.window, bg='#C0C0C0')
        self.frame2 = Frame(self.window, bg='#C0C0C0',)

        menu = Menu(self.window)


        if first:
            menu.add_command(label=' -  Add', command= Window.LaunchAdd)
            menu.add_command(label=' -  Open Password List', command= Window.OpenTxt)

            ButtonGenerate = Button(self.frame, bg='#FFFFFF', fg='black', font=('Berlin Sans FB', 12), width=15, height=2, command= self.SetLabelPassword, text='Generate')
            ButtonGenerate.grid(column= 1, row=1)
            self.LabelPassword = Label(self.frame, bg='#FFFFFF', text=Window.password.password, width=15, height=5)
            self.LabelPassword.grid(column=2, row=1)

        else:
            global NameEntry
            global MailEntry
            global PasswordEntry

            NameEntry = Entry(self.frame2, width=40)
            NameEntry.grid(column=2,row=2)
            LabelName = Label(self.frame2, font=('Arial Black', 15), text='Name :', width=9, height=2, background='#C0C0C0', anchor=E)
            LabelName.grid(column=1, row=2)

            MailEntry = Entry(self.frame2, width=40)
            MailEntry.grid(column=2,row=3)
            LabelMail = Label(self.frame2, font=('Arial Black', 15), text='Mail / ID * :', width=9, height=2, background='#C0C0C0', anchor=E)
            LabelMail.grid(column=1, row=3)

            PasswordEntry = Entry(self.frame2, width=40)
            PasswordEntry.grid(column=2,row=4)
            LabelPassword = Label(self.frame2, font=('Arial Black', 15), text='Password :', width=9, height=2, background='#C0C0C0', anchor=E)
            LabelPassword.grid(column=1, row=4)

            
            ButtonValidate = Button(self.frame, bg='#FFFFFF', borderwidth=3, width=21, height=1, text=' >    ADD    <', font=('Arial Black', 18), command=Window.AddList)
            ButtonValidate.grid(column=1, row=1)

        self.frame.pack(expand=YES)
        self.frame2.pack(expand=YES)
        self.window.config(menu= menu)
        self.window.mainloop()

    ## ------------ ##

    def LaunchAdd():
        AddWindow = Window((400, 250), False, "  -  Add Password  -  ")
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
    AddList = staticmethod(AddList)


    def OpenTxt():
        os.system('start notepad Password List.txt')
    OpenTxt = staticmethod(OpenTxt)

    def GeneratePassword(cls):
        Window.password = Password(Window.passwordName, Window.number, Window.maj, Window.mini, Window.special)
    GeneratePassword = classmethod(GeneratePassword)

    def SetLabelPassword(self):
        Window.GeneratePassword()
        self.LabelPassword.config(text=Window.password.password)
