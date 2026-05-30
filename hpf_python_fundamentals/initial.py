# Var, Data Types, Operators, Conditionals, Loops, Functions


# Variables
name = 'Lewis'
age = 30
height = 5.9
is_student = True
HomeAddress = 'Python'
homeAddress = 60
home_address = 9.0
characteristics = ["tall", "dark", "handsome"]
address = ("Nairobi", "Kenya")
likes_dislikes = {
    "likes": ["python", "javascript", "java"],
    "dislikes": "None"
}

# print(name, type(name))
# print(age, type(age))
# print(height, type(height))
# print(is_student, type(is_student))
# print(HomeAddress, type(HomeAddress))
# print(homeAddress, type(homeAddress))
# print(home_address, type(home_address))
# print(characteristics, type(characteristics))
# print(address, type(address))
# print(likes_dislikes, type(likes_dislikes))


# Operators
# -, *, /, //, %, **

def calculate_discounted_price(actual_value, discount):
    """
        * = Multiplication (multiplies two numbers)
        / = Division (divides two numbers)
        // = Floor Division (returns integer part of quotient)
        % = Modulus (returns remainder of division)
        ** = Exponent (raises a number to a power)
    """

    #conditionals
    # ==, !=, >, <, >=, <=
    if discount <= 10:
        print("Discount is less than or equal to 10%")
    elif discount == 10:
        print("Discount is equal to 10%")
    else:
        print("Discount is greater than 10%")

    # loops

    while(discount >= 10):
        discounted_price = actual_value - (actual_value * discount // 100)
        print("Discounted price from function:", discounted_price)
        return discounted_price
        break

# getting user input
run = True

while(run):
    print("Welcome to the discount calculator")
    print("Please enter the following details or enter close to exit:")
    actual_value, discount = input("Enter the actual value and discount (e.g., 100 10): ").split()
    close = input("Enter close to exit: ")
    if close == "close":
        run = False
        break

    actual_value = int(actual_value)
    discount = int(discount)

    calculate_discounted_price(actual_value, discount)


# final_amount = calculate_discounted_price(actual_value, discount)
# print("Final amount:", final_amount)
# print("Discounted price:", calculate_discounted_price(actual_value, discount))



    # for i in range(1, 101):
    #     if i%3 == 0:
    #         print(i)

    # likes = likes_dislikes["likes"]
    # print(likes[0])

    # print("Keys and Values:")
    # for key, values in likes_dislikes.items():
    #     print(key, values)

    # print("Values only:")
    # for values in likes_dislikes.values():
    #     print(values)

    # print("Keys Only:")
    # for key in likes_dislikes.keys():
    #     print(key)

    # print("Access without using .items()")
    # for val in likes_dislikes:
    #     print(likes_dislikes[val])



