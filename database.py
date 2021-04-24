# create record
# update record
# read record
# delete record
#CRUD

# find user 

import os
import validation

userDBPath = "data/user_record/"
AuthSessionPath = "data/auth_session/"


def create(userAccountNumber, firstName, lastName, email, pin):

    # create a file
    # name of the file would be accountNumber
    #.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then deleted created file

    userData = firstName + "," + lastName + "," + email + "," + pin + "," + str(0)

    if doesAccountNumberExist(userAccountNumber):

        return False

    if doesEmailExist(email):
        print("User already exists")
        return False

    completionState = False

    try:

        f = open(userDBPath + str(userAccountNumber) + ".txt", "x")

    except FileExistsError:

        doesFileContainData = read(userDBPath + str(userAccountNumber) + ".txt")
        if not doesFileContainData:
            delete(userAccountNumber)

    else:

        f.write(str(userData));
        completionState = True

    finally:

        f.close();
        return completionState

def createAuth(userAccountNumber, pin):

    # create a file
    # name of the file would be accountNumber
    #.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then deleted created file

    userData = AccountNumber + "," +  pin 

    if doesAccountNumberExist(userAccountNumber):

        return False

    if doesEmailExist(email):
        print("User already exists")
        return False

    completionState = False

    try:

        f = open(authenticatedUser + str(userAccountNumber) + ".txt", "x")

    except FileExistsError:

        doesFileContainData = read(authenticatedUser + str(userAccountNumber) + ".txt")
        if not doesFileContainData:
            delete(userAccountNumber)

    else:

        f.write(str(userData));
        completionState = True

    finally:

        f.close();
        return completionState


def read(userAccountNumber):

    # find user with account number
    # fetch content of the file
    isValidAccountNumber = validation.account_number_validation(userAccountNumber)

    try:

        if isValidAccountNumber:
            f = open(userDBPath + str(userAccountNumber) + ".txt", "r")
        else:
            f = open(userDBPath + userAccountNumber, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def update(userAccountNumber):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(userAccountNumber):

    # find user with account number
    # delete the user record (file)
    # return true

    isDeleteSuccesful = False

    if os.path.exists(AuthSessionPath + str(userAccountNumber) + ".txt"):

        try:

            os.remove(AuthSessionPath + str(userAccountNumber) + ".txt")
            isDeleteSuccesful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return isDeleteSuccesful


def doesEmailExist(email):

    allUsers = os.listdir(userDBPath)

    for user in allUsers:
        userList = str.split(read(user), ',')
        if email in userList:
            return True
    return False


def doesAccountNumberExist(accountNumber):

    allUsers = os.listdir(userDBPath)

    for user in allUsers:

        if user == str(accountNumber
    ) + ".txt":

            return True

    return False


def authenticatedUser(accountNumber, pin):

    if doesAccountNumberExist(accountNumber
):

        user = str.split(read(accountNumber
    ), ',')

        if pin == user[3]:
            return user

    return False

    #database = {
    #2193613008: ["VeNita", "LaNier", "vl@aol.com", 1234, 5000]
   # }

# create (2193613008, "VeNita", "LaNier", "vl@aol.com", "1234")
#delete(1834974986)