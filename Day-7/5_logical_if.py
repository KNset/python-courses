a = 600
b = 33
c = 500
print("Both conditions are True") if (a > b and c > a) else print("condition false")
print("Both conditions are True") if (a > b or c > a) else print("condition false")



username = "Tobias"
password = "secret123"
is_verified = False

if username  and password and is_verified:
  print("Login successful")
else:
  print("Login failed")