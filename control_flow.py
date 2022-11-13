
name = "ahmed"
# print("Hello Ahmed" if name == "ahmed" else "Welcome new person")

# ==

# if name == "ahmed":
#     print("#" * 30)
#     print(" Hello Ahmed ".center(30, "#"))
#     print("#" * 30)
# else:
#     print("#" * 37)
#     print(" Welcome new person ".center(37, "#"))
#     print("#" * 37)

# first_list = ["pal", "eg", "leb", "sud", "ser", "jor"]
# second_list = ["ksa", "ema", "qat", "kew"]
# first_discount = 70
# second_discount = 40
#
# your_country = input("Enter your country: ")
#
# if your_country in first_list:
#     print(f"Your discount is : {first_discount}")
# elif your_country in second_list:
#     print(f"Your discount is : {second_discount}")
# else:
#     print("You have no discount")

################################################################################

admins = ["Ahmed", "Ali", "Yahya"]
name = input("Enter your name: ").strip().capitalize()

if name in admins:
    print(f"Hello {name}")
    answer = input("Are you want to delete or update you name, (y,n)? ")
    if answer == "y":
        option = input("You want delete or update the name? ")
        if option == "update":
            new_name = input("Enter new name pleas: ").strip().capitalize()
            admins[admins.index(name)] = new_name
            print("Your name is updated.")
            print(admins)
        elif option == "delete":
            admins.remove(name)
            print("Your name is deleted.")
            print(admins)
    else:
        print(f"enjoy mr.{name}")
else:
    print("Your not admin")
    answer = input("Are you want to add you to admins, (y,n)? ")
    if answer == "y":
        admins.append(name)
        print(admins)
    else:
        print("thank you")
