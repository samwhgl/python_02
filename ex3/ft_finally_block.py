# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 14:53:31 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 10:31:30 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def water_plants(plant_list):
    """
    Simulate a watering system for a list of plants.

    Args:
        plant_list (list): A list of plant names to water.

    Raises:
        ValueError: If a plant in the list is None.
    """
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: Cannot water plant - {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the watering system with valid and invalid plant lists.
    """
    print("=== Garden Watering System ===")
    print("Testing normal watering...")

    valid_plants = ["tomato", "lettuce", "carrots"]
    invalid_plants = ["tomato", None]

    water_plants(valid_plants)
    print("Watering completed successfully!")

    water_plants(invalid_plants)
    print("Cleanup always happens, even with errors")


if __name__ == "__main__":
    test_watering_system()
