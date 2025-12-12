# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 10:59:19 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 11:45:43 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

class SunlightError(GardenError):
	pass

class GardenManager:
	def __init__(self):
		self.plants = {}

	def add_plant(self, name, water_level, sunlight_hours):
		if not name:
			raise PlantError("Plant name cannot be empty")
		if name in self.plants:
			raise PlantError(f"Plant '{name}' already exists! ")
		self.plants[name] = {
			"water": water_level,
			"sun": sunlight_hours
		}
		return f"Added {name} succesfully!"

	def water_plant(self):
		print("Opening water system")
		try:
			for plant, data in self.plants.items():
				if data["water"] <= 0:
					raise WaterError("Not enough water in the tank")
				print(f"Watering {plant} - success")
		except WaterError as e:
			print("Error watering plants", e)
		finally:
			print("Closing watering system (cleanup)")

	def check_plant_health(self, plant_name):
		if plant_name not in self.plants:
			raise PlantError(f"Plant '{plant_name}' not found!")
		data = self.plants[plant_name]
		if data['water'] > 10:
			raise WaterError(f"Water level {data['water']} is too high (max 10)")
		if data['sun'] > 12:
			raise SunlightError(f"Sunlight error {data['sun']} is too high (max 12)")
		return f"{plant_name}: healthy (water: {data['water']}, sun:{data['sun']})"

def run_tests():
	gm = GardenManager()
	print("=== Garden Management System ===")
	print("Adding plant to the garden...")
	plants_to_add = [
		("tomato", 5, 8),
		("lettuce", 15, 6),
		("", 4, 8)
	]
	for name, w, s in plants_to_add:
		try:
			message = gm.add_plant(name, w, s)
			print(message)
		except GardenError as e:
			print("Error handling plnat:", e)

	print("Watering plants...")
	gm.water_plant()

	print("Checking plant health...")
	for plants in gm.plants:
		try:
			result = gm.check_plant_health(plants)
			print (result)
		except GardenError as e:
			print(f"Error checking {plants}", e)

	print("Testing error recovery")
	try:
		raise GardenError("Not enough water in the tank")
	except GardenError as e:
		print("Caught GardenError:", e)
	finally:
		print("System recovered and continuing...")
	print("Garden management system test completed")

if __name__ == "__main__":
	run_tests()
