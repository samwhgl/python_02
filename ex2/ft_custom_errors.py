# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 16:27:16 by shaegels          #+#    #+#              #
#    Updated: 2025/12/10 11:54:03 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related issues."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related issues."""
    pass


def test_plant_error():
    """
    Demonstrate raising and catching a PlantError.
    """
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error():
    """
    Demonstrate raising and catching a WaterError.
    """
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_garden_error():
    """
    Demonstrate that catching GardenError catches PlantError and WaterError.
    """
    print("Testing catching all garden errors...")

    functions = [
        lambda: raise_(PlantError("The tomato plant is wilting!")),
        lambda: raise_(WaterError("Not enough water in the tank!")),
    ]

    for function in functions:
        try:
            function()
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def raise_(err):
    """
    Helper function to raise an exception inside a lambda.
    """
    raise err


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    test_water_error()
    test_garden_error()
    print("All custom error types work correctly!")
