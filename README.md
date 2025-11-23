Project Title :- Simple Python ATM Simulation Program.

Overview of the Project :- 
  A simple in-memory ATM (Automated Teller Machine) simulation is implemented by this Python program. Its main purpose is to illustrate   basic programming ideas, such as function calls, user authentication, and the use of global variables to manage application state 
  (credentials and account balances) in different modules.

FEATURES :- 
  1. In-Memory User Database : Stores all account data (username, password, and balance) in a central dictionary (username).
  2. Global State Tracking : Throughout the session, the user who is currently logged in and their float balance are tracked using           global variables (u1 and balance).
  3. Security and Authentication : When you log in, the system changes your balance from text to a number so it can do math. After you       make a transaction, it changes the balance back to text before saving everything, so your info stays safe.
  4. Password Change : Allows the logged-in user to update their account password using change_password(), with the change immediately       reflected in the central username dictionary.
  5. Transaction Capabilities : Various transactions like Cash deposite, cash withdrawl, balance inquiry, password change can be             performed through a single menu.
  6. Immediate Persistence : It takes care that the updated balance after every succesful transaction is immediately saved back into         the local database.
  7. Continous session loop : Once logged in the user can perform all operations as many times as he wants.

Technologies/tools used :-
  1. Data Structures : Different data structures are used in the program  like Dictionary to store and manage account credentials and        balances. Lists to hold the balance and password for each user.
  2. Standard Input/Output : Standard tools like 'input()' is used here to read user data such as useernames, passowrods, menu choices,      and transaction amounts. 'print()' is used to display all output, including menu, prompts, success messages.
  3. Program structure and Control : The complete program application is modularized into dedicated functions, modules, loops, if-else       statements, etc.
  4. Data Conversion Tools : Various tools are used where ever necessary to convert data into desired data type so that the code runs        accurately without any errors.

Steps to install and Run the project :-
  1. Install Python : If you don't already have Python installed on your local system, or else you'll need to download and install the       latest version.
  2. Save the Code : Copy the entire code and save it with a '.py' extension.
  3. Run the Program : You must run this program interactively from the command line, as it continuously asks for user input.

Instructions for testing :-
  There are no such specific instructions for using this program only be carefull while putting the inputs if by mistake you will put     any wrong datatype input the program will sto and display a datatype error.

Screenshots :-

