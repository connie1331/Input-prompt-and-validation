"""
Author:           Khanh Vu
Lab:              Lab 1
Date:             04.17.2022
Description:      This module is a collection of individual functions to prompt user for inputs and to validate inputs
                  depending on input type (e.g. int, float, item from a menu)
Sources:          Lab 1 specifications
                  CIS 233Y Python II - Week 1 Lecture notes and videos
                  https://stackoverflow.com/questions/3886402/how-to-get-numbers-after-decimal-point
"""

# An input_int function that asks the user to type in a whole number


def input_int(prompt="Please enter a whole number: ", error_string="Invalid input. Enter a whole number only!",
              ge=None, gt=None, lt=None, le=None):
    # Change prompt text depending on the value of keyword arguments
    if ge is not None and gt is None and lt is None and le is None:
        prompt = f"Please enter a whole number that is greater than or equal to {ge}: "
    elif gt is not None and ge is None and lt is None and le is None:
        prompt = f"Please enter a whole number that is greater than {gt}: "
    elif lt is not None and ge is None and gt is None and le is None:
        prompt = f"Please enter a whole number that is less than {lt}: "
    elif le is not None and ge is None and gt is None and lt is None:
        prompt = f"Please enter a whole number that is less than or equal to {le}: "
    elif ge is not None and lt is not None and gt is None and le is None:
        prompt = f"Please enter a whole number that is (greater than or equal to) {gt} but less than {lt}: "
    elif ge is not None and le is not None and gt is None and lt is None:
        prompt = f"Please enter a whole number that is (greater than or equal to) {ge} " \
                 f"but (less than or equal to) {le}: "
    elif gt is not None and lt is not None and ge is None and le is None:
        prompt = f"Please enter a whole number that is (greater than) {gt} but (less than or equal to) {le}: "
    elif gt is not None and le is not None and ge is None and lt is None:
        prompt = f"Please enter a whole number that is (greater than) {gt} but (less than or equal to) {le}: "

    # Validate user input
    while True:
        try:
            whole_number = int(input(prompt))
            if gt is not None and whole_number <= gt:
                print ("Invalid input! Enter value that is greater than ", gt)
                continue
            elif ge is not None and whole_number < ge:
                print ("Invalid input! Enter value that is greater than or equal to ", ge)
                continue
            elif lt is not None and whole_number >= lt:
                print("Invalid input! Enter value that is less than ", lt)
                continue
            elif le is not None and whole_number > le:
                print("Invalid input! Enter value that is less than or equal ", le)
                continue
            else:
                return whole_number
        except ValueError:
            print(error_string)


# An input_float function that asks the user to type in a decimal number
def input_float(prompt="Please enter a decimal number: ", error_string="Invalid input. Enter a decimal number only!"):
    while True:
        try:
            input_number = float(input(prompt))
            int_number = int(input_number)    # Converting the input number to integer. If the user enters integer,
            # the difference between input number and the converted_to_int number will be zero.
            # Other wise, the input number is float unless users enter string
            dif = input_number - int_number
            if dif == 0:
                print(error_string)
                continue
            else:
                return input_number
        except ValueError:
            print("Invalid input. Try again!")


# An input_string function that asks the user to type in a piece of text
def input_string(prompt="Please enter a piece of text: ", error_string="Invalid input. "
                                                                       "Enter a non-numeric text string only!"):
    while True:
        try:
            string_input = input(prompt)
            string_input = float(string_input)      # If the input can be converted to a float, it's a number
            print(error_string)       # If the input can't be converted to a float, it is a string and
            continue                                 # the code will throw an valueError exception
        except ValueError:
            return string_input                      # ,so it should return the input value


# A y_or_n function that asks the user to answer a year or no question and returns True if they type yes(or some
# variant) and False if they type no (or some variant)
def y_or_n(prompt="Please enter \"y\" or \"n\": ", error_string="Invalid input. Enter \"y\" or \"n\" only!"):
    while True:
        response = input(prompt)
        if response.lower() != "y" and response.lower() != "n" \
                and response.lower() != "yes" and response.lower() != "no":
            print(error_string)
            continue
        else:
            if response.lower() != "y" or response.lower() != "yes":
                return True
            else:
                return False

# A select_item function that takes a list of choices, prompts the user to select a choice, and returns the choice that
# the user selected (e.g., the user should be able to select a type of food from a list of food)


def select_item(*item, prompt="Enter a number to select the item: ", error_string="Invalid input. Enter a number "
                                                                                  "from the menu to select an item!"):
    while True:
        count = 0
        print("Menu")
        try:
            for i in item:                                      # Print the menu
                count += 1
                print(count, ". ", i)

            number_selected = int(input(prompt))     # Prompt user to enter a number to select the item
            # print("Items selected: ", item[number_selected - 1])
            return item[number_selected - 1]
        except ValueError or IndexError:
            print(error_string)
            print()


# An interface called input_value that takes a type keyword argument, and executes one of the above functions depending
# on the type (type="int", type = "float", type = "string", type = "y_or_n" , type = "item_selected")
def input_value(type_selected, *args, **kwargs):
    if type_selected == "int":
        input_int(**kwargs)
    elif type_selected == "float":
        input_float()
    elif type_selected == "string":
        input_string()
    elif type_selected == "y_or_n":
        y_or_n()
    elif type_selected == "item_selected":
        select_item(*args)
    else:
        print("Unspecified input type. Integer input test is selected!")
        input_int(**kwargs)
"""
if __name__ == "__main__":
    input_value("int", gt=5, le=15)     # Integer input test
    #input_int()
    #input_value("float")                # Float input test
    #nput_float()
    #input_value("string")               # String input test
    #input_string(prompt="Enter a text:")
    #input_value("y_or_n")               # y or n input test
    #y_or_n()
    #input_value("item_selected", "Milk", "Coffee", "Cheese")         # Select an item test
    #select_item("Honey", "Bok choy", "Ramen", "Cassava root", "Flour", prompt="Choose an item: ")
    #input_value("asfdsd")               # Unspecified input type test
"""



