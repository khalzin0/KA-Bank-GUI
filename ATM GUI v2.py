from customtkinter import *
from tkinter import messagebox as mbox

pinCode = ["1234", "1999", "2424", "1985", "5555", "1225"] 
accountHoldersName = ["harry den", "david beckingham", "tom reidy", "emma reidy", "kate reidy", "khalid alenizy"]
accountNumber = ['135323', '199281', "182838", "185597", "667432", "783453"]
balance = [567000, 21873, 2341871, 275638, 91820, 500240]

app = CTk()
app.geometry("400x800")
app.title("Log In")
set_appearance_mode("dark")

def entry():
    frame = CTkFrame(
        master=app, 
        border_width=2, 
        border_color="#00a2ff", 
        fg_color="#0f7fbf"
        )
    frame.pack(expand=True, padx=30, pady=10)

    CTkLabel(
        frame,
        text="Welcome to KA Bank v2.0",
        font=("Helvetica", 20)
        ).pack(anchor="s", padx=30, pady=10)
    
    CTkLabel(
        frame,
        text="Enter Your Full Name:",
        ).pack(anchor="s", padx=4, pady=5)
    
    name = CTkEntry(
        frame,
        placeholder_text="Enter Name"
        )
    name.pack()

    CTkLabel(
        frame,
        text="Enter Your Pin:",
        ).pack(anchor="s", padx=4, pady=5)
    
    pin = CTkEntry(
        frame,
        placeholder_text="Enter Pin",
        show="*",   # Hiding the pin with *
        width=70
        )
    pin.pack()

    def validation():
        inputPin = pin.get()
        inputName = name.get().lower()
        if inputName in accountHoldersName:
            index = accountHoldersName.index(inputName)
            if inputPin == pinCode[index]:
                mbox.showinfo(title="Successful", message="Login Successful, Welcome "+inputName)
                app.destroy()

                def main(): 
                    #  Main Menu
                    newWindow = CTk() 
                    newWindow.title("Main Menu")
                    newWindow.geometry("400x800")
                    
                    frame1 = CTkFrame(
                        master=newWindow, 
                        border_width=2, 
                        border_color="#00a2ff", 
                        fg_color="#0f7fbf",
                        )
                    frame1.pack(expand=True, padx=30, pady=10)

                    #  Withdraw Page
                    def withdraw():
                        newWindow.withdraw()
                        newWindow2 = CTkToplevel()
                        newWindow2.title("Withdraw")
                        newWindow2.geometry("400x800")

                        frame2 = CTkFrame(
                            master=newWindow2, 
                            border_width=2, 
                            border_color="#00a2ff", 
                            fg_color="#0f7fbf",
                            )
                        frame2.pack(expand=True, padx=30, pady=10)

                        CTkLabel(
                            frame2,
                            text="Enter Amount To Withdraw:",
                            font=("Helvetica", 16)
                            ).pack(anchor="s", padx=30, pady=10)
                        
                        amount = CTkEntry(
                            frame2,
                            placeholder_text="Enter Here",
                        )
                        amount.pack(padx=30, pady=10)

                        def withdrawAmount():
                            try:
                                amount2 = int(amount.get())  # Ensure valid integer input
                                if amount2 <= balance[index]:
                                    balance[index] -= amount2
                                    mbox.showinfo(title="Successful", message=f"Successfully Withdrawn £{amount2}\nYour new balance is £{balance[index]}")
                                    newWindow2.destroy()
                                    main()
                                else:
                                    mbox.showerror(title="Error", message="Insufficient Balance")
                                    newWindow2.destroy()
                                    withdraw()
                            except ValueError:
                                mbox.showerror(title="Error", message="Invalid input. Please enter a valid number.")

                        CTkButton(
                            frame2,
                            text="Enter",
                            command=withdrawAmount,
                        ).pack(expand=True, padx=30, pady=10)

                    #  Deposit Page
                    def deposit():
                        newWindow.destroy()
                        newWindow3 = CTkToplevel()
                        newWindow3.title("Deposit")
                        newWindow3.geometry("400x800")

                        frame3 = CTkFrame(
                            master=newWindow3, 
                            border_width=2, 
                            border_color="#00a2ff", 
                            fg_color="#0f7fbf",
                            )
                        frame3.pack(expand=True, padx=30, pady=10)
                        
                        CTkLabel(
                            frame3,
                            text="Enter Amount To Deposit:",
                            font=("Helvetica", 16)
                            ).pack(anchor="s", padx=30, pady=10)
                        
                        entryDeposit = CTkEntry(
                            frame3,
                            placeholder_text="Enter Here",
                        )
                        entryDeposit.pack()

                        def depositAmount():
                            try:
                                depositInt = int(entryDeposit.get())  # Ensure valid integer input
                                balance[index] += depositInt
                                mbox.showinfo(title="Successful", message=f"Successfully Deposited £{depositInt}\nYour new balance is £{balance[index]}")
                                newWindow3.destroy()
                                main()
                            except ValueError:
                                mbox.showerror(title="Error", message="Invalid input. Please enter a valid number.")

                        CTkButton(
                            frame3,
                            text="Enter",
                            command=depositAmount,
                        ).pack(expand=True, padx=30, pady=10)

                    CTkLabel(
                        frame1,
                        text="Do you want to withdraw, deposit or exit?",
                        font=("Helvetica", 16)
                        ).pack(anchor="s", padx=30, pady=10)
                    CTkLabel(
                        frame1,
                        text=f"Name: {accountHoldersName[index].upper()} \nAccount Number: {accountNumber[index]}",
                        ).pack(anchor="s")
                    CTkLabel(
                        frame1,
                        text=f"Your bank balance is £{balance[index]}",
                        ).pack(anchor="s")
                    CTkButton(
                            frame1,
                            text="Withdraw",
                            command=withdraw,
                        ).pack(expand=True, padx=30, pady=10)
                    CTkButton(
                            frame1,
                            text="Deposit",
                            command=deposit,
                        ).pack(expand=True, padx=30, pady=10)
                    CTkButton(
                            frame1,
                            text="Exit",
                            command=newWindow.destroy,
                        ).pack(expand=True, padx=30, pady=10)
                    newWindow.mainloop()
                main()
            else:
                mbox.showerror(title="Error", message="The Pin Is Invalid")
        else:
            mbox.showerror(title="Error", message="Account Does Not Exist")

    CTkButton(
        frame,
        text="Enter",
        command=validation
        ).pack(anchor="n", padx=30, pady=20)
    
    app.mainloop()

entry()