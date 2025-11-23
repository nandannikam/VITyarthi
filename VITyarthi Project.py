username = {
    "dr_adarsh" : ["abc", 200000.0],
    "mr_rahul" : ["xyz", 100000.0],
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
                balance = (username[u1][1])
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
    
    try:
        t = int(input("Please Enter your choice : "))
    except ValueError:
        print("Invalid choice. Please enter a number from 1 to 5.")
        return True
         
    if (t == 1):
        withdrawl()
        return True
    elif (t == 2):
        deposite()
        return True
    elif (t == 3):
        check_balance()
        return True
    elif (t == 4):
        change_password()
        return True
    elif (t == 5):
        exit()
        return False
    else:
         print("Invalid choice. Please enter a number from 1 to 5.")
         return True

def withdrawl():
        global balance
        global u1
        try:
            amt1 = float(input("Enter the amount : "))
            if (0 < amt1 <= balance):
                balance -= amt1
                username[u1][1] = float(balance)
                print("Amount withdrawled succesfully.")
                print("Thanks for using ATM services.")
            else :
                print("Sorry! Insufficient Balance")
        
        except ValueError:
             print("Invalid input. Please enter a numerical amount.")

def deposite():
        global balance
        global u1
        try:
            amt2 = float(input("Enter the amount : "))
            if (0 < amt2):
                 balance += amt2
                 username[u1][1] = float(balance)
                 print("Amount Deposited succesfully.")
                 print("Thanks for using ATM services.")
            else:
                 print("Invalid amount. You must deposit a positive value.")
            
        except ValueError:
             print("Invalid input. Please enter a numerical amount.")

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
    while menu():
        pass