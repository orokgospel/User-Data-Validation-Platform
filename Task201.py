
import random


'''Using 'for' In other to accepting the data details of students not more than 2'''
data_details = []
for x in range(0,2):
    print("\nWELCOME TO HNG LOGIN FOR YOUR START-NG STUDENTS DETAILS")
    First_name=input("\nEnter your First Name:\n")
    Last_name=input("Enter your Last Name:\n")
    email =input("Enter your Email Address:\n")

    def randomString(length=9):
        """ Generate a random string of fixed length for user password"""
        your_letters = First_name[0:2] + Last_name[0:2]
        return ''.join(random.choice(your_letters) for i in range (length))
    password= randomString()
    print("Your password is:", password)
    Generated_password = input("Are you satisfied with the generated password for you? yes/no:\n")
    if  Generated_password =="yes":
        details=['First Name: '+First_name,
                 "Last Name: "+ Last_name,
                 "Email Address: "+email,
                 "Password: "+ password
                 ]
        data_details.append(details)
        print("Your HNG Details are:\n")
        for data in details:
            print(data)

    else:
        '''if the user is not satisfied with the generated password'''
        Choose_Password=input("Enter a password not less than 7 characters:\n")
        while len(Choose_Password)<7:
            Choose_Password=input("Error!!\ninput a new password equal to or greater than 7 in length:\n")
        else:
            details =['First Name: '+First_name,
                      "Last Name: "+ Last_name,
                      "Email Address: "+email,
                      "Password: "+ Choose_Password
                      ]
        data_details.append(details)
        for data in details:
            print(data)


def all_students_details():
    print("\nThe Current Students Details are:\n")
    for each_details in data_details:
        print(each_details)

all_students_details()
