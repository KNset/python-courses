# dynamic variable 

login_username = "john"
login_password = "secret123"

username = input("Enter username : ")
password = input("Enter password : ")

if (username == login_username and password == login_password):
    print("Login successful")
else:
    print("username or password invalid .Login failed")