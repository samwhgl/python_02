# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_errors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 15:27:14 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 10:32:43 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Check whether a plant is healthy based on water and sunlight levels.

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Water level (must be between 1 and 10).
        sunlight_hours (int): Sunlight exposure in hours (must be between 2 and 10).

    Returns:
        str: A message indicating the plant is healthy.

    Raises:
        ValueError: If any input value is out of the allowed range.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(
            f"Water level {water_level} is too low (minimum is 1)"
        )

    if water_level > 10:
        raise ValueError(
            f"Water level {water_level} is too high (maximum is 10)"
        )

    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (minimum is 2)"
        )

    if sunlight_hours > 10:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (maximum is 10)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    Run test cases for the plant health checker.
    """
    print("=== Garden Plant Health Checker ===")
    print("Testing good values...")

    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as error:
        print("Error:", error)

    print("Testing empty plant name...")
    try:
        check_plant_health("", 4, 5)
    except ValueError as error:
        print("Error:", error)

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 12, 5)
    except ValueError as error:
        print("Error:", error)

    print("Testing with bad sunlight hours...")
    try:
        check_plant_health("tomato", 3, 11)
    except ValueError as error:
        print("Error:", error)

    print("All error-raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()


