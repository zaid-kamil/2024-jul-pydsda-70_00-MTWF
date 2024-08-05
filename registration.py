print("Registration Application")
username = input('enter your username =>')
email = input('enter your email =>')
password = input('enter your password =>')
cpassword = input('confirm your password =>')

if username and email and password and cpassword:
    if username.isalnum():
        if '@' in email and email.endswith('.com'):
            if password == cpassword:
                if len(password) >= 8:
                    print("Registration Complete")
                    print("🎉🎉🎉🎉")
                else:
                    print("Password too small")
            else:
                print('Password does not match')
        else:
            print('Invalid Email')
    else:
        print('Invalid Username')
else:
    print('All fields are required')