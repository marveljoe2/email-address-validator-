def email_val(address):
  val_at = address.find("@gmail")
  val_dot = address.find(".com")
  
  if (val_at == -1):
    print(f"\n{address} is invalid")
  elif (address.count("@") >= 2):
    print(f"\n{address} is invalid")
  elif (val_dot == -1):
    print(f"\n{address} is invalid")
  elif (address.count("gmail") >= 2):
    print(f"\n{address} is invalid")
  elif (address.count("com") >= 2):
    print(f"\n{address} is invalid")
  elif (address.count(".") >= 2):
    print(f"\n{address} is invalid")
  else:
    print(f"\n{address} is valid")

print("\nCheck if your email address is valid")

while True:
  menu = """
  1 - Check your email
  2 - exist program
  """
  
  print(menu)
  choice = input("> ")
  if choice == "1":
    email_address = input("Enter your email: ")
    email_val(email_address)
  elif choice == "2":
    print("\nExiting program")
    break 
  else:
    print("\nI don't understand yiur command")