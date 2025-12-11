# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 11:59:11 by shaegels          #+#    #+#              #
#    Updated: 2025/12/10 13:03:09 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operation():
    """
    Demonstrate how different built-in Python exceptions can be raised
    and caught using try/except blocks.
    """
    print("Testing ValueError...")
    try:
        num = int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing KeyError...")
    try:
        garden_dict = {"rose": 1, "sunflower": 2}
        value = garden_dict["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("Testing multiple errors together...")
    try:
        num = int("abc")
        result = 10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types():
    """
    Run all built-in error demonstrations.
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operation()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

