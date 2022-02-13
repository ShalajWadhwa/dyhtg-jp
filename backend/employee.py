import json
# from coords_api_func import get_coords

# func needs to be get_coords from coords_api_func
def user_Create(func, user_EmployeeNumber, firstname, lastname, email, phone_number, city, post_code, weather, news):
    user_NewUser = {user_EmployeeNumber:  {}}
    user_NewUser[user_EmployeeNumber]["first_name"] = firstname
    user_NewUser[user_EmployeeNumber]["last_name"] = lastname
    user_NewUser[user_EmployeeNumber]["email"] = email
    user_NewUser[user_EmployeeNumber]["phone_number"] = phone_number
    user_NewUser[user_EmployeeNumber]["city"] = city
    user_NewUser[user_EmployeeNumber]["post_code"] = post_code
    user_NewUser[user_EmployeeNumber]["weather"] = weather
    user_NewUser[user_EmployeeNumber]["news"] = news

    lat, long = func(post_code) # Location API

    user_NewUser[user_EmployeeNumber]["lat"] = lat
    user_NewUser[user_EmployeeNumber]["long"] = long

    with open('database/db.json', 'r+') as openfile:
        data = json.load(openfile)
        data.update(user_NewUser)
        openfile.seek(0)
        json.dump(data, openfile)


def user_Delete(employee_number):
    with open('database/db.json', 'r') as openfile:
        user_Library = json.load(openfile)
    del user_Library[str(employee_number)]
    with open('database/db.json', 'w') as openfile:
        user_Library = json.dump(user_Library, openfile)


# def user_Search(search_input):
#     with open('database/db.json', 'r') as openfile:
#         user_Library = json.load(openfile)

#     for employee in user_Library:
#         if search_input in user_Library[employee].values():
#             return {employee : user_Library[employee]}
#         else:
#             return "Employee Not Found"


# Filler
# import requests
# import time
# for emp in range(10):
#     response = requests.get("https://random-data-api.com/api/users/random_user").json()
#     user_Create(get_coords, user_EmployeeNumber=response["id"], firstname=response["first_name"], lastname=response["last_name"],
#                 email=response["email"], phone_number=response["phone_number"], city="Glasgow", post_code="G12 8QQ", weather=None, news=None)
#     time.sleep(0.5)

# print("DB Filled")