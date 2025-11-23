username = {
    "dr_adarsh" : ["abc", "200000"],
    "mr_rahul" : ["xyz", "100000"],
}

def login():
    while True:
        print("----- Welcome to ATM Machine Menu -----")
        print("Please enter your login credentials to use ATM Services")
        global u1
        global balance
        u1 = input("Please Enter the username : ")
        if (u1 in username):
            p1 = input("Enter the password : ")
            if (p1 == username[u1][0]):
                print("You've Logged in Succcesfully ! ")
                balance = float(username[u1][1])
                return True
            else:
                print("Sorry..Please enter correct password")
        else:
            print("Sorry..Enter correct username")



def menu():
    print("ATM Service Menu")
    print("1. Withdrawl Cash")
    print("2. Deposite Cash")
    print("3. Check Balance")
    print("4. Change Password")
    print("5. Exit")

    t = int(input("Please Enter your choice : "))

    if (t == 1):
        withdrawl()
    elif (t == 2):
        deposite()
    elif (t == 3):
        check_balance()
    elif (t == 4):
        change_password()
    elif (t == 5):
        exit()
        login()


def withdrawl():
        amt1 = int(input("Enter the amount : "))
        global balance
        global u1
        if (amt1 <= balance):
            balance -= amt1
            username[u1][1] = str(balance)
            print("Amount withdrawled succesfully.")
            print("Thanks for using ATM services.")


def deposite():
        amt2 = float(input("Enter the amount : "))
        global balance
        global u1
        balance += amt2
        username[u1][1] = str(balance)
        print("Amount Deposited succesfully.")
        print("Thanks for using ATM services.")

def check_balance():
        global balance
        print(f"The remaining balance in the account is {balance}")
        print("Thanks for using ATM services.")

def change_password():
        newpass = input("Enter the new Password : ")
        username[u1][0] = newpass
        print("Password has been succesfully changed.")
        print("Thanks for using ATM services.")
        print("Please visit again !")


def exit():
        print("Thanks for using ATM services.")
        print("Please visit again !")
        print("You've been succesfully logged out.")

if login():
    while True:
        menu()