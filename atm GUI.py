import tkinter
from tkinter import *
from tkinter import messagebox as mbox  

pinCode = ["1234", "1999", "2424", "1985", "5555", "1225"] 
accountHoldersName = ["harry den", "david beckingham", "tom reidy", "emma reidy", "kate reidy", "khalid alenizy"]
accountNumber = ['135323', '199281', "182838", "185597", "667432", "783453"]
balance = [567000, 21873, 2341871, 275638, 91820, 500240]


def main():
    window = tkinter.Tk()
    window.geometry("400x400")
    window.title("Login")
    Label(window, text="Hello and Welcome to KA Bank").pack()
    Label(window, text="Enter Your Full Name").pack()
    entry1 = Entry(window)
    entry1.pack()
    Label(window, text="Enter Your Pin").pack()
    entry2 = Entry(window)
    entry2.pack()
    def getPin():
        inputPin = entry2.get()
        inputName = entry1.get().lower()
        index = accountHoldersName.index(inputName)
        if inputName in accountHoldersName:
            if inputPin == pinCode[index]:
                mbox.showinfo(title="Successful", message="Login Successful, Welcome "+inputName)
                def main():
                    newWindow = Toplevel()
                    newWindow.geometry("400x400")
                    def withdraw():
                        newWindow.destroy()
                        newWindow2 = Toplevel()
                        newWindow2.geometry("400x400")
                        Label(newWindow2, text="Enter the amount to withdraw").pack()
                        amount = Entry(newWindow2)
                        amount.pack()
                        def withdrawAmount():
                            amount2 = amount.get()
                            amount2 = int(amount2)
                            if amount2 <= balance[index]:
                                balance[index] -= amount2
                                mbox.showinfo(title="Successful", message=f"Successfully Withdrawed {amount2} From Your Account\nYour balance is now {balance[index]}")
                                main()
                            else:
                                mbox.showerror(title="Error", message="Insufficient Balance")
                                newWindow2.destroy()
                                withdraw()
                        Button(newWindow2, text="Enter", command=withdrawAmount).pack()
                    def deposit():
                        newWindow3 = Toplevel()
                        newWindow3.geometry("400x400")
                        Label(newWindow3, text="Enter The Amount to Deposit").pack()
                        entryDeposit = Entry(newWindow3)
                        entryDeposit.pack()
                        def depositAmount():
                            depositInt = entryDeposit.get()
                            depositInt = int(depositInt)
                            balance[index] += depositInt
                            mbox.showinfo(title="Successful", message=f"Successfully Deposited {depositInt} From Your Account\nYour balance is now {balance[index]}")

                        depositButton = Entry(newWindow3, text="Enter", command=depositAmount).pack()

                    Label(newWindow, text="Do you want to withdraw, deposit or exit?").pack()
                    Label(newWindow, text=f"Name: {accountHoldersName[index].upper()} Account Number: {accountNumber[index]}").pack()
                    Label(newWindow, text=f"Your bank balance is £{balance[index]}").pack()
                    button1 = Button(newWindow, text="Withdraw", command=withdraw).pack()
                    button2 = Button(newWindow, text="Deposit", command=deposit).pack()
                    button3 = Button(newWindow, text="Exit", command=window.destroy).pack()
                main()
            else:
                mbox.showerror(title="Error", message="The Pin Is Invalid")
        else:
            mbox.showerror(title="Error", message="Account Does Not Exist")
    Button(window, command=getPin, text="Submit").pack()
    


    window.mainloop()
main()