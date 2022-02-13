import json
from geopy.geocoders import Nominatim
from coords_api_func import get_coords

# with open('../database/db.json', 'r+') as openfile:

#     json_object = json.load(openfile)

# user_Library = json_object

# totalEmployees = 50
# def user_GenerateEmployeeNumber():
    
#     global totalEmployees
#     totalEmployees += 1
#     temp_user_EmployeeNumber = 0000 + totalEmployees

#     return temp_user_EmployeeNumber

def user_Create(user_EmployeeNumber, firstname, lastname, email, phone_number, city, post_code, weather, news, service):
#   user_EmployeeNumber = user_GenerateEmployeeNumber()
    user_NewUser = { user_EmployeeNumber :  {} }
    user_NewUser[user_EmployeeNumber]["first_name"] = firstname
    user_NewUser[user_EmployeeNumber]["last_name"] = lastname
    user_NewUser[user_EmployeeNumber]["email"] = email
    user_NewUser[user_EmployeeNumber]["phone_number"] = phone_number
    user_NewUser[user_EmployeeNumber]["city"] = city
    user_NewUser[user_EmployeeNumber]["post_code"] = post_code
    user_NewUser[user_EmployeeNumber]["weather"] = weather
    user_NewUser[user_EmployeeNumber]["news"] = news
    user_NewUser[user_EmployeeNumber]["service"] = service

    #location API
    lat, long = get_coords(post_code)

    user_NewUser[user_EmployeeNumber]["lat"] = lat
    user_NewUser[user_EmployeeNumber]["long"] = long

    with open('database/db.json', 'r+') as openfile:
        data = json.load(openfile)
        data.update(user_NewUser)
        openfile.seek(0)
        json.dump(data, openfile)

#####

def user_Delete(employee_number):
    with open('database/db.json', 'r') as openfile:
        user_Library = json.load(openfile)

    if employee_number in user_Library.keys():
        del user_Library[employee_number]
        with open('database/db.json', 'w') as openfile:
            user_Library = json.dump(user_Library, openfile)
        return "Employee Removed"
    else:
        return "Employee Not Found"


# def user_Information(input_UserLibrary):
#     for key, value in input_UserLibrary.items():
#         print(key, end=": ")
#         if type(value) is str or float:
#             print(value, end=" ")
#         if type(value) == None:
#             pass
#         else:
#             value


def user_Search(search_input):
    with open('database/db.json', 'r') as openfile:
        user_Library = json.load(openfile)
    try:
        for temp_UserNumber in user_Library:
            if search_input in user_Library[temp_UserNumber].values():
                # print( temp_UserNumber, end = " ")
                # print( user_Information(user_Library[temp_UserNumber]))

                return temp_UserNumber, user_Library[temp_UserNumber]
    except:
            print("Error with Search")


######



# user_Search( user_Library, "Hessel" )

################################## Data Fill - Shalaj
# emp_number = 0
# for emp_number in range(20):
#     user_Create(emp_number+1, "a", "b", "c@mail.com", "1111111111", "Glasgow", "G12 8QQ", None, None, None)
##################################

# print(user_Delete("101"))

# weather api function (loop)
# for all employees get weather api using employees lon/lat

#################################################################print(user_Search( user_Library, "Daniel")) # Uncomment


# user_Delete( user_Library, "firstname" )
# print(user_Library)

####adding long/lat to all###
# with open(r'C:\Users\hello\Desktop\JPM HackAThon - 22\db.json', 'r+') as openfile:
#     data = json.load(openfile)
#     for i in data:
#         key = data[i]

#         lat, long = get_coords(key)

#         data[i]["lat"] = lat
#         data[i]["long"] = long

#         data.update()
#         openfile.seek(0)
#         json.dump(data, openfile)