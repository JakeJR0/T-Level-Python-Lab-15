import pandas as pd
import regx
from datetime import datetime as time
try:
  data_frame = pd.Dataframe({
    "first_name": [],
    "last_name": [],
    "email_address": [],
    "address_1": [],
    "address_2": [],
    "city": [],
    "postcode": [],
    "birth": [],
    "age": []
  })
except:
  pass

def valid_postcode(post_code=""):
  post_code = re.findall(r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}', s)
  if post_code:
    return True
  else:
    return False


def enter_data():
  while True:
    try:
      while True:
        try:
          first_name = input("First Name: ")
          if len(first_name) <= 10:
            break
        except:
          pass
        
      while True:
        last_name = input("Last Name: ")
        if len(last_name) <= 20:
          break

      while True:
        try:
          email = input("Email: ")
          found = False
          for char in email:
            if char == "@":
              found = True
          if found:
            break
        except:
          pass

      while True:
        address_1 = input("Street: ")
        if len(address_1) <= 20:
          break
      while True:
        address_2 = input("District: ")
        if len(address_2) <= 20:
          break
        
      while True:
        city = input("City: ")
        if city <= 20:
          break
      while True:
        postcode = input("Postcode: ")
        if valid_postcode(postcode):
          break
      while True:
        try:
          birth = input("Date of birth: DD/MM/YY")
          birth = time.strptime(birth, "%d/%m/%Y")
          if birth:
            break
        except:
          pass

      while True:
        try:
          age = int(input("Age: "))
          if age >= 18 and age <= 75:
            break
        except:
          pass

      entry = [first_name, last_name, email, address_1, address_2, city, postcode, birth, age]
      data_frame.loc[len(data_frame.index)] = entry

    except:
      pass

enter_data()