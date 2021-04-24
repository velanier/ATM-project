import datetime as dt
import random
import validation
import database
from getpass import getpass
today =dt.datetime.now()
dt_string = today.strftime("%m/%d/%Y %H:%M:%S")

#database = {
    #2193613008: ["VeNita", "LaNier", "vl@aol.com", 1234, 5000]
   # }

def init():
     print ('Welcome to Python Phederal Credit Union')

     haveAccount = int(input("Do you have account with us: 1 (Yes) 2 (No) \n"))
    
     if(haveAccount == 1):
    
         login()

     elif(haveAccount == 2):

        register()

     else:
        print("You've selected an invalid option")
        init()

def login():

    print("********* Login to your account ***********")


    accountNumberFromUser = input("Enter your account number \n")
    
    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)

    if isValidAccountNumber:

        pin = getpass("Enter your PIN \n") 

        user = database.authenticatedUser(accountNumberFromUser,pin);
       
        if user:
            bankOperations(user)

        # for accountNumber,user in database.items():
        #     if accountNumber == int(accountNumberFromUser):
        #         if(user[3] == pin):
        #             bankOperations(user)

        print('Invalid Account Number or PIN')
        login()
    else: 

        print("Account Number must be 10 digits")
        init()

def register():
    print('****** Register for a new account ******')
    email = input("Enter your email address \n")
    firstName = input("Enter your first name \n")
    lastName = input("Enter your last name \n")
    pin = getpass("Create a PIN for yourself \n")

    accountNumber = generateAcctNumber()

    # database[accountNumber]= [firstName, lastName, email, pin, 5000 ]

    isUserCreated = database.create(accountNumber, firstName, lastName, email, pin)
   
    if isUserCreated:

        #using database module 
        print('Your account has been created')
        print('-----------------------------')
        print('Your account number is: %d' %accountNumber)
        print('-----------------------------')
        
        #return database
        
        login()

def bankOperations(user):
    print('Welcome %s %s' %( user[0], user[1] ) )
    print ('Today is:', dt_string)

    selectedOption = int(input('These are the available options: (1) Cash Deposit (2) Withdrawal (3) Complaint (4) Logout (5) Exit'))
   
    if (selectedOption == 1):
        print('You selected %s' %selectedOption)
        depositOperation()

    elif(selectedOption == 2):
        print('You selected %s' %selectedOption)   
        withdrawalOperation()

    elif (selectedOption == 3):
        print('You selected %s' %selectedOption) 
        complaintOperation()

    elif (selectedOption == 4):
        print('You selected %s, Goodbye' %selectedOption)
        login()
    elif (selectedOption == 5):
        print('You selected %s, Goodbye' %selectedOption)
        exit()

    else: 
        bankOperations(user)
        print('Invalid option selected')


def withdrawalOperation(): 
    withdrawalAmount= int(input('How much would you like to withdraw?'))
    if (withdrawalAmount > 1):
        print ('Take your cash')
        # get current balance
        # get amount to withdraw
        # check if current balance is > withdraw balance
        # deduct withdrawn amount from current balance
        # display current balance
        # bankOperations(user)

def depositOperation(): 
    depositAmount= int(input('How much would you like to deposit?'))
    balance = 5000 + depositAmount
    print ('Your balance is %s' %balance)
    # get current balance
    # get amount to deposit
    # add deposited amount from current balance
    #bankOperations(user)

def complaintOperation(): 
    print('Complaints')
    complaint=input('What would you like to report?')
    print('Thank you for contacting us')
    #bankOperations(user)

def generateAcctNumber():
    #print('Generating accont number')
    return random.randrange(1111111111,9999999999)

def getCurrentBalance(userDetails):
    return userDetails[4]


#### ACTUAL BANKING SYSTEM ####
#print(generateAcctNumber())
init()


       
              
