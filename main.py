#password manager in python
import getpass
password_storage = {}
#create variables and functions
def add_password(user_name, user_id,password):
  key = (user_name,user_id)
  password_storage[key] = password 
  print("The password has been done/added!")

def retrieve_password(user_name,user_id,password):
  key = (user_name,user_id)
  if key in password_storage:
    print("Able to retrieve password!")
  else:
    print("Unable to find password!")

def edit_password(user_name, user_id, new_password): 
  key = (user_name, user_id)
  if key in password_storage:
    password_storage[key] = new_password
    print("password has been updated!")
  else:
    print("Unable to find password to edit!")

def delete_password(user_name, user_id):
  key = (user_name, user_id)
  if key in password_storage:
    del password_storage[key]
    print("Deleted the password!")
  else:
    print("unable to find password to delete!")

def main():
  print("let's create a password manager in Python!")
  while True:
    print("1. Add Password", "\n2. Retrieve Password", "\n3. Edit Password", "\n4. Delete Password", "\n5. Exit")
    option = input("Select an option!")
    if option == "1":
      user_name = input("Please input the user name: ")
      user_id = input("Please input the user ID : ")
      password = getpass.getpass("Please input the password: ")
      add_password(user_name,user_id,password)
    elif option == "2":
      user_name = input("Please input the user name: ")
      user_id = input("Please  input the user ID: ")
      retrieve_password(user_name,user_id,password)
    elif option == "3":
      user_name = input("Please input the user name: ")
      user_id = input(" Please input/enter the user ID:  ")
      new_password = getpass.getpass("Please input the new password: ")
      edit_password(user_name,user_id,new_password)
    elif option == "4":
      user_name = input("Please input the user name: ")
      user_id = input("Please  input the user ID: ")
      delete_password(user_name,user_id )
    elif option == "5":
      print("Exit !")
      break
    else:
      print("Please try again entering valud options! ")

main()
