"""
Author:           Khanh Vu
Lab:              Lab 1 (Revised)
Date:             04.19.2022
Description:      This module is a collection of individual functions to prompt user for inputs and to validate inputs
                  depending on input type (e.g. int, float, item from a menu)
Sources:          Lab 1 specifications
                  CIS 233Y Python II - Week 1 Lecture notes and videos
                  https://stackoverflow.com/questions/3886402/how-to-get-numbers-after-decimal-point
                  Week 3 Lecture
"""


# A num_in_range_validation function that returns True if the number is in a specifies range.
# Otherwise, it returns false
def num_in_range_validation(ge, gt, lt, le, num):
    if gt is not None and num <= gt:
        return False
    elif ge is not None and num < ge:
        return False
    elif lt is not None and num >= lt:
        return False
    elif le is not None and num > le:
        return False
    else:
        return True


# An input_num function that prompts the user for either any number or a whole number only
def input_num(prompt="Please enter a number: ",
              error_string="Invalid input. Enter a number only!",
              ge=None, gt=None, lt=None, le=None
              , num_conversion=float):
    # Prompt user for input
    while True:
        try:
            num_input = num_conversion(input(prompt))
            # Call num_in_range_input() to prompt user to input a number falling in a specified range
            if num_in_range_validation(ge, gt, lt, le, num_input):
                return num_input
            else:
                print(error_string)
                print()
                continue
        except ValueError:
            print(error_string)
            print()


# An input_int function that prompts user for a whole number
def input_int(prompt="Please enter a whole number:"
              , error_string="Invalid input. Enter a whole number only!"
              , ge=None, gt=None, lt=None, le=None):
    int_input = input_num(prompt=prompt, error_string=error_string, ge=ge, gt=gt, lt=lt, le=le, num_conversion=int)
    return int_input


# An input_float function that prompts user for a decimal number
def input_float(prompt="Please enter a number: "
                , error_string="Invalid input. Enter a number only!"
                , ge=None, gt=None, lt=None, le=None):
    float_input = input_num(prompt=prompt, error_string=error_string, ge=ge, gt=gt, lt=lt, le=le, num_conversion=float)
    return float_input


# An input_string function that asks the user to type in a piece of text
def input_string(prompt="Please enter a piece of text: "
                 , error_string="Invalid input. Input cannot be empty!"
                 , valid=lambda val: val != ""):
    while True:
        string_input = input(prompt)
        if valid(string_input):
            return string_input
        else:
            print(error_string)
            print()
            continue


# A descriptive_prompt function that suggests string what they should enter
def add_descriptive_prompt(suggested_input_list):
    # A prompt text that is more descriptive
    descriptive_prompt = "Please select one the following items only: "
    descriptive_prompt += suggested_input_list[0]  # Modify prompt text if a list of items is provided
    for i in range(len(suggested_input_list) - 1):
        descriptive_prompt += ", " + suggested_input_list[i + 1]
    return descriptive_prompt


# A y_or_n function that asks the user to answer a year or no question and returns True if they type yes(or some
# variant) and False if they type no (or some variant)
def y_or_n(prompt="Please enter \"y\" or \"n\": ", error_string="Invalid input!"):
    y_n_dict = {"y": True
                , "yes": True
                , "true": True
                , "n": False
                , "no": False
                , "false": False}

    while True:
        response = input(prompt)
        if response.lower() in tuple(y_n_dict.keys()):
            return y_n_dict[response.lower()]
        else:
            print(error_string)
            print(add_descriptive_prompt(tuple(y_n_dict.keys())))
            print()


# A select_item function that takes a list of choices, prompts the user to select a choice, and returns the choice that
# the user selected (e.g., the user should be able to select a type of food from a list of food)
def select_item(prompt=None
                , error_string="Invalid input."
                , items=("Α", "α", "Β", "β", "Γ", "γ", "Δ", "δ", "Ε", "ε"
            , "Ζ", "ζ", "Η", "η", "Θ", "θ", "Ι", "ι", "Κ", "κ", "Λ", "λ", "Μ", "μ", "Ν", "ν", "Ξ", "ξ", "Ο", "ο", "Π"
            , "π", "Ρ", "ρ", "Σ", "ς", "Τ", "τ", "Υ", "υ", "Φ", "φ", "Χ", "χ", "Ψ", "ψ", "Ω", "ω"), maps=None):

    # Modify the item dictionary
    mod_maps = {}
    if maps is not None:
        for key in maps.keys():
            mod_maps[str(key).lower()] = maps[key]
    else:
        for item in items:
            mod_maps[str(item).lower()] = item

    if prompt is None:
        prompt = add_descriptive_prompt(tuple(mod_maps.keys())) + "\nEnter a value: "

    # Prompt user for input and validate it
    while True:
        user_input = input(prompt)
        if user_input.lower() in mod_maps.keys():
            return mod_maps[user_input.lower()]
        else:
            print(error_string)
            print(add_descriptive_prompt(tuple(mod_maps.keys())))
            print()


# An interface called input_value that takes a type keyword argument, and executes one of the above functions depending
# on the type (type="int", type = "float", type = "string", type = "y_or_n" , type = "item_selected")
def input_value(type_selected, **kwargs):
    if type_selected == "int":
        return input_int(**kwargs)
    elif type_selected == "float":
        return input_float(**kwargs)
    elif type_selected == "string":
        return input_string(**kwargs)
    elif type_selected == "y_or_n":
        return y_or_n(**kwargs)
    elif type_selected == "item":
        return select_item(**kwargs)
    else:
        print("Unspecified input type. Integer input test is selected!")
        return input_int(**kwargs)

