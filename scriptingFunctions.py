class funcs:
    
    #Checks if account details entered by user at sign-up match the parameters (username has 6 or more characters, passwords are between 8 and 15 characters and match)
    def checkSignUpParameters(username, password, passwordConfirm):
        if len(username) >= 6:
            if len(password) >= 8 and len(password) <= 15:
                if password == passwordConfirm:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def fornewPush():
        return 1



