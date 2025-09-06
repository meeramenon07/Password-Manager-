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
