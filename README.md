Project Title :- Simple Python ATM Simulation Program.

Overview of the Project :- 
  A simple in-memory ATM (Automated Teller Machine) simulation is implemented by this Python program. Its main purpose is to illustrate basic programming ideas, such as function          calls, user authentication, and the use of global variables to manage application state 
  (credentials and account balances) in different modules.

FEATURES :- 
  1. In-Memory User Database : Stores all account data (username, password, and balance) in a central dictionary (username).
  2. Global State Tracking : Throughout the session, the user who is currently logged in and their float balance are tracked using global variables (u1 and balance).
  3. Security and Authentication : When you log in, the system changes your balance from text to a number so it can do math. After you make a transaction, it changes the balance             back to text before saving everything, so your info stays safe.
  4. Password Change : Allows the logged-in user to update their account password using change_password(), with the change immediately reflected in the central username                      dictionary.
  5. Transaction Capabilities : Various transactions like Cash deposite, cash withdrawl, balance inquiry, password change can be performed through a single menu.
  6. Immediate Persistence : It takes care that the updated balance after every succesful transaction is immediately saved back into the local database.
  7. Continous session loop : Once logged in the user can perform all operations as many times as he wants.

Technologies/tools used :-
  1. Data Structures : Different data structures are used in the program  like Dictionary to store and manage account credentials and        balances. Lists to hold the balance and          password for each user.
  2. Standard Input/Output : Standard tools like 'input()' is used here to read user data such as useernames, passowrods, menu choices, and transaction amounts. 'print()' is used            to display all output, including menu, prompts, success messages.
  3. Program structure and Control : The complete program application is modularized into dedicated functions, modules, loops, if-else statements, etc.
  4. Data Conversion Tools : Various tools are used where ever necessary to convert data into desired data type so that the code runs accurately without any errors.

Steps to install and Run the project :-
  1. Install Python : If you don't already have Python installed on your local system, or else you'll need to download and install the latest version.
  2. Save the Code : Copy the entire code and save it with a '.py' extension.
  3. Run the Program : You must run this program interactively from the command line, as it continuously asks for user input.

Instructions for testing :-
  There are no such specific instructions for using this program only be carefull while putting the inputs if by mistake you will put any wrong datatype input the program will stop
  and display a invalid datatype error.

Screenshots :-

<img width="1633" height="378" alt="Screenshot 2025-11-23 220959" src="https://github.com/user-attachments/assets/5b2d5da1-c1cf-4c82-af60-761121595a91" />

<img width="1644" height="254" alt="Screenshot 2025-11-23 221015" src="https://github.com/user-attachments/assets/599c39dc-555a-4c9f-9c38-3660f52b234b" />

<img width="1643" height="231" alt="Screenshot 2025-11-23 221035" src="https://github.com/user-attachments/assets/281eaff3-3c93-4725-8f13-2c0acf4efd74" />

<img width="1650" height="249" alt="Screenshot 2025-11-23 221058" src="https://github.com/user-attachments/assets/283bbafc-299d-4fcd-8253-c1b108e888db" />

<img width="1657" height="251" alt="Screenshot 2025-11-23 221117" src="https://github.com/user-attachments/assets/8dcebc5a-89d8-4f8c-8d2e-4cb887a50d56" />
