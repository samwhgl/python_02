# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 10:59:19 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 10:33:38 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    """
    Base exception class for garden-related errors.
    """


class PlantError(GardenError):
    """
    Raised when a plant-related error occurs.
    """


class WaterError(GardenError):
    """
    Raised when a water-related error occurs.
    """


class SunlightError(GardenError):
    """
    Raised when a sunlight-related error occurs.
    """


class GardenManager:
    """
    Manage plants, watering, and health checks in a garden.
    """

    def __init__(self):
        """
        Initialize the garden manager with an empty plant registry.
        """
        self.plants = {}

    def add_plant(self, name, water_level, sunlight_hours):
        """
        Add a new plant to the garden.

        Args:
            name (str): Name of the plant.
            water_level (int): Initial water level.
            sunlight_hours (int): Daily sunlight hours.

        Returns:
            str: Confirmation message.

        Raises:
            PlantError: If the plant name is invalid or already exists.
        """
        if not name:
            raise PlantError("Plant name cannot be empty")

        if name in self.plants:
            raise PlantError(f"Plant '{name}' already exists!")

        self.plants[name] = {
            "water": water_level,
            "sun": sunlight_hours,
        }

        return f"Added {name} successfully!"

    def water_plants(self):
        """
        Water all plants in the garden.

        Raises:
            WaterError: If there is not enough water.
        """
        print("Opening water system")

        try:
            for plant, data in self.plants.items():
                if data["water"] <= 0:
                    raise WaterError("Not enough water in the tank")
                print(f"Watering {plant} - success")
        except WaterError as error:
            print("Error watering plants:", error)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name):
        """
        Check the health status of a specific plant.

        Args:
            plant_name (str): Name of the plant to check.

        Returns:
            str: Health status message.

        Raises:
            PlantError: If the plant does not exist.
            WaterError: If the water level is too high.
            SunlightError: If the sunlight level is too high.
        """
        if plant_name not in self.plants:
            raise PlantError(f"Plant '{plant_name}' not found!")

        data = self.plants[plant_name]

        if data["water"] > 10:
            raise WaterError(
                f"Water level {data['water']} is too high (max 10)"
            )

        if data["sun"] > 12:
            raise SunlightError(
                f"Sunlight level {data['sun']} is too high (max 12)"
            )

        return (
            f"{plant_name}: healthy "
            f"(water: {data['water']}, sun: {data['sun']})"
        )


def run_tests():
    """
    Run demonstration tests for the garden management system.
    """
    manager = GardenManager()

    print("=== Garden Management System ===")
    print("Adding plants to the garden...")

    plants_to_add = [
        ("tomato", 5, 8),
        ("lettuce", 15, 6),
        ("", 4, 8),
    ]

    for name, water, sun in plants_to_add:
        try:
            message = manager.add_plant(name, water, sun)
            print(message)
        except GardenError as error:
            print("Error handling plant:", error)

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")
    for plant_name in manager.plants:
        try:
            result = manager.check_plant_health(plant_name)
            print(result)
        except GardenError as error:
            print(f"Error checking {plant_name}:", error)

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in the tank")
    except GardenError as error:
        print("Caught GardenError:", error)
    finally:
        print("System recovered and continuing...")

    print("Garden management system test completed")


if __name__ == "__main__":
    run_tests()
