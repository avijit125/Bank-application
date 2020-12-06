from tkinter import*
from atmdbhelper import atmdb
from tkinter import messagebox
from PIL import Image,ImageTk

class Atm:

    def __init__(self):
        self.db=atmdb()

        # load gui

        self.load_login_window()

    def load_login_window(self):
        self._root = Tk()

        self._root.title("ATM Login")
        self._root.minsize(400, 600)
        self._root.maxsize(400, 600)
        self._root.config(background="#F60A40")

        self._label1 = Label(self._root, text="ATM", fg="#fff", bg="#F60A40")
        self._label1.config(font=("Arial", 30))
        self._label1.pack(pady=(30, 30))

        self._accountID = Label(self._root, text="accountID", fg="#fff", bg="#F60A40")
        self._accountID.config(font=("Times", 16))
        self._accountID.pack(pady=(10, 10))

        self._accountIDInput = Entry(self._root)
        self._accountIDInput.pack(pady=(5, 25), ipady=10, ipadx=30)

        self._pincode = Label(self._root, text="pincode", fg="#fff", bg="#F60A40")
        self._pincode.config(font=("Times", 16))
        self._pincode.pack(pady=(10, 10))

        self._pincodeInput = Entry(self._root)
        self._pincodeInput.pack(pady=(5, 25), ipady=10, ipadx=30)

        self._login = Button(self._root, text="Login", bg="#fff", width=25, height=2,
                             command=lambda: self.check_login())
        self._login.pack()

        self._reg1 = Label(self._root, text="dont worry just register", fg="#fff", bg="#F60A40")
        self._reg1.config(font=("Times", 16))
        self._reg1.pack(pady=(25, 24))

        self._reg = Button(self._root, text="REGISTRATION", bg="#fff", width=25, height=2,command=lambda:self.regwindow())
        self._reg.pack()




        self._root.mainloop()



    def check_login(self):

        accountID = self._accountIDInput.get()
        pincode=self._pincodeInput.get()

        data = self.db.check_login(accountID,pincode)

        if len(data)==0:
            messagebox.showerror('error','invalid')
        else:
            self.user_id=data[0][0]
            self.is_logged_in=1
            self.login_handler()

    def login_handler(self):
        #to load
        self.clear()
        data=self.db.fetch_userdata(self.user_id)
        #display

        name = 'HI  ' + str(data[0][2])

        name_label=Label(self._root,text=name, fg="#fff", bg="#F60A40")
        name_label.config(font=("Times", 16))
        name_label.pack()

        self.goto_profil()



    def regwindow(self):
        self.clear()
        self._root.title("ATM Registration")
        self._root.minsize(400, 600)
        self._root.maxsize(400, 600)
        self._root.config(background="#F60A40")

        self._label2 = Label(self._root, text="ATM", fg="#fff", bg="#F60A40")
        self._label2.config(font=("Arial", 30))
        self._label2.pack(pady=(30, 30))

        self._accountID1 = Label(self._root, text=" create your accountID", fg="#fff", bg="#F60A40")
        self._accountID1.config(font=("Times", 16))
        self._accountID1.pack(pady=(10, 10))

        self._accountIDInput1 = Entry(self._root)
        self._accountIDInput1.pack(pady=(5, 25), ipady=10, ipadx=30)

        self._name = Label(self._root, text=" give your name", fg="#fff", bg="#F60A40")
        self._name.config(font=("Times", 16))
        self._name.pack(pady=(10, 10))

        self._nameID = Entry(self._root)
        self._nameID.pack(pady=(5, 25), ipady=10, ipadx=30)

        self._pincode1 = Label(self._root, text="set your pincode", fg="#fff", bg="#F60A40")
        self._pincode1.config(font=("Times", 16))
        self._pincode1.pack(pady=(10, 10))

        self._pincodeInput1 = Entry(self._root)
        self._pincodeInput1.pack(pady=(5, 25), ipady=10, ipadx=30)

        self._login1 = Button(self._root, text="done", bg="#fff", width=25, height=2,
                             command=lambda: self.reg_handeler())
        self._login1.pack()






    def reg_handeler(self):

        flag=self.db.register(self._accountIDInput1.get(), self._nameID.get(), self._pincodeInput1.get())

        if flag==1:
            messagebox.showinfo('success',"register successfully",)
            self._root.destroy()
            self.load_login_window()


        else:

            messagebox.showerror('Error',"try again")





    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()



    def logout(self):
        self.is_logged_in=0
        self._root.destroy()
        self.load_login_window()


    def check_your_balance(self):
        self.clear()
        data = self.db.fetch_userdata(self.user_id)
        balance = data[0][4]

        self._label3 = Label(self._root, text="YOUR CURRENT BALANCE", fg="#fff", bg="#F60A40")
        self._label3.config(font=("Arial", 10))
        self._label3.pack(pady=(10, 10))

        balance_label = Label(self._root, text=balance, fg="#fff", bg="#F60A40")
        balance_label.config(font=("Times", 16))
        balance_label.pack(pady=(40,35))

        self._goback = Button(self._root, text="back", bg="#fff", width=25, height=2, command=lambda: self.back())
        self._goback.pack()


    def back(self):
        self.login_handler()



    def dodeposit(self):
        self.clear()
        self._dodeposit = Label(self._root, text="enter your amount for deposit", fg="#fff", bg="#F60A40")
        self._dodeposit.config(font=("Times", 16))
        self._dodeposit.pack(pady=(10, 10))

        self._dodepositInput = Entry(self._root)
        self._dodepositInput.pack(pady=(5, 20), ipady=10, ipadx=30)

        self._login = Button(self._root, text="submit", bg="#fff", width=25, height=2,
                             command=lambda: self.check_deposit())
        self._login.pack()



    def check_deposit(self):

        data = self.db.fetch_userdata(self.user_id)
        self.ok = int(data[0][4]) + int(self._dodepositInput.get())

        flag = self.db.update(self.ok,self.user_id)

        if flag == 1:
            messagebox.showinfo('success', "Deposit successfully", )
            self.clear()
            self.login_handler()


        else:

            messagebox.showerror('Error', "try again")


    def dowithdraw(self):
        self.clear()
        self._dowithdraw = Label(self._root, text="enter your amount for withdraw", fg="#fff", bg="#F60A40")
        self._dowithdraw.config(font=("Times", 16))
        self._dowithdraw.pack(pady=(10, 10))

        self._dowithdrawInput = Entry(self._root)
        self._dowithdrawInput.pack(pady=(5, 20), ipady=10, ipadx=30)

        self._login = Button(self._root, text="submit", bg="#fff", width=25, height=2,
                             command=lambda: self.check_withdraw())
        self._login.pack()


    def check_withdraw(self):
        data = self.db.fetch_userdata(self.user_id)
        if (int(self._dowithdrawInput.get()) <= 2500):
            data = self.db.fetch_userdata(self.user_id)
            self.ok = int(data[0][4]) - int(self._dowithdrawInput.get())

            flag = self.db.update(self.ok, self.user_id)

            if flag == 1:
                messagebox.showinfo('success', "withdraw successfully", )
                self.clear()
                self.login_handler()


            else:

                messagebox.showerror('Error', "try again")

        else:
            messagebox.showerror("error","aktu lojja kor")







    def goto_profil(self):

        self._label2 = Label(self._root, text="welcome to Atm", fg="#fff", bg="#F60A40")
        self._label2.config(font=("Arial", 30))
        self._label2.pack(pady=(30, 30))

        imageurl="image/abc.png"

        load= Image.open(imageurl)
        load= load.resize((100,100),Image.ANTIALIAS)
        rander = ImageTk.PhotoImage(load)

        img = Label(image=rander)
        img.image = rander
        img.pack()

        self._label1 = Label(self._root, text="click an option below", fg="#fff", bg="#F60A40")
        self._label1.config(font=("Arial", 30))
        self._label1.pack(pady=(30, 30))

        self._cheack_balance = Button(self._root, text="cheack balance", bg="#fff", width=25, height=2, command=lambda: self.check_your_balance())
        self._cheack_balance.pack()

        self._deposit = Button(self._root, text="deposit", bg="#fff", width=25, height=2, command=lambda: self.dodeposit())
        self._deposit.pack()

        self._withdraw = Button(self._root, text="withdraw", bg="#fff", width=25, height=2, command=lambda:self.dowithdraw())
        self._withdraw.pack()

        self._logout2 = Button(self._root, text="Logout", bg="#fff", width=25, height=2,
                             command=lambda: self.logout())
        self._logout2.pack()











obj=Atm()