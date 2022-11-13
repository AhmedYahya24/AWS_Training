batDetails = {
    "name": "ahmed",
    "tall": "180",
    "gender": "male",
}
# print(batDetails["name"], batDetails["tall"])

################################################

# def getTall(name):
#     if name == "batman":
#         print(batDetails["tall"])


# getTall("batman")

# name = input("UR name?\n")
# print(name)

################################################

# weight = input("UR weight?\n")
# boundWeight = int(weight) / 0.45
# print("boundWeight:", boundWeight)

################################################

# firstName = "ahmed"
# lastName = "yahya"
# userName = f"hello :) {firstName} goodbye {lastName} :("
# print(userName)

################################################

# price = 1000000
# isBadCredit = False
# if isBadCredit or False:
#     print(price - (price * 0.1))
#     print("~ is working")
# else:
#     print(price - (price * 0.2))
#     print("~ not working")

################################################

# temp = int(input("enter temperature value..\n"))
# if temp > 30:
#     print("it’s a hot day")
# elif temp < 10:
#     print("it’s a cold day")
# else:
#     print("it’s neither hot nor cold day")

################################################

# user_name = input("enter username..\n")
# if len(user_name) < 3:
#     print("must be mor than 3 character")
# elif len(user_name) > 50:
#     print("too long")
# else:
#     print("good name")

# x = "ahmed"
# match x:
#     case"ahmed":
#         print("hello ahmed")
#     case"sari":
#         print("hello sari")

################################################

# weight = float(input("enter ur weight:\n"))
# unit = input("enter unit of weight in k or b:")
#
# if unit == "k":
#     print(weight / 0.45)
# elif unit == "b":
#     print(weight * 0.45)

################################################

# secret_number = 26
# answer = 0
# init = 1
# while init <= 3:
#     answer = int(input("enter UR expecting:\n"))
#     if answer == secret_number:
#         print("you win")
#         break
#     elif init == 3:
#         print("failed")
#     init += 1

# for item in ["AWS", "EC2", "S3", "GSG"]:
#     print(item)
#
# print("###################### using range")
#
# # for ip in range(0, 10, 3):
# #     print(ip)
#
# total_count = 0
# for item in [10, 20, 30]:
#     total_count += item
# print(total_count)

################################################

# let user enter text and if that text include a word in our dictionary replace it with the emojy
# emojis = {
#     "happy": ":)",
#     "sad": ":(",
# }
# output = ""
# text = input("enter ur own text:\n")
# words = text.split(" ")
# print(words)
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
#
# # another practice
# user_number = input("enter ur number:\n")
# numbers = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
# }
# output = ""
# for ch in user_number:
#     output += numbers.get(ch, "") + " "
# print(output)

################################################

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# process = input("enter process you want apply:")

# def calc_numbers(num1, num2, process):
#     output = 0
#     if process == "+":
#         output = num1 + num2
#     elif process == "-":
#         output = num1 - num2
#     elif process == "*":
#         output = num1 * num2
#     elif process == "/":
#         output = num1 / num2
#     else:
#         print("something went wrong")
#     return output

# print(f"result = {calc_numbers(num1, num2, process)}")

################################################
# try:
#     age = input("UR age: ")
#     birth_year = 2022 - age
#     print(birth_year)
# except ValueError:
#     print("invalid age")
# except ZeroDivisionError:
#     print("UR age should be greater than 0")

# emojis = {
#     "happy": ":)",
#     "sad": ":(",
# }
# text = input("enter ur own text:\n")
#
#
# def refactor_string(text):
#     words = text.split(" ")
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# result = refactor_string(text)
# print(result)

################################################

# class User:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#     def greet_user(self):
#         print(f'hello {self.first_name} :)')
#
#
# user1 = User('ahmed')
# user1.greet_user()
#
# user2 = User("tamer")
# user2.greet_user()

################################################

# JSON => Javascript Object Notation
# import json
#
# data = {
#     "name": "ahmed",
#     "age": 24,
#     "gender": "male"
# }
# dumps_data = json.dumps(data)
# print("before dumps", type(dumps_data))
# loads_data = json.loads(dumps_data)
# print("before loads", type(loads_data))

################################################
# practical practices
# full name

first_name = input('What\'s your first name?\n')
mid_name = input('What\'s your mid name?\n')
last_name = input('What\'s your last name?\n')

first_name = first_name.strip().capitalize()
mid_name = mid_name.strip().capitalize()
last_name = last_name.strip().capitalize()

print(f'Hello {first_name} {mid_name:.1s}.{last_name}')

# 1- Email slicing
email = input('What\'s your email?\n').strip()
email_mark_index = email.index("@")
user_name = email[:email_mark_index]
website_domain = email[email_mark_index + 1:]
print(f"your username is: {user_name}\nyour website domain is: {website_domain}")
