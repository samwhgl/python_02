# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_errors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 15:27:14 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 10:58:09 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def check_plant_health(plant_name, water_level, sunlight_hours):
	if not plant_name:
		raise ValueError("Plant name cannot be empty!")
	if water_level < 1:
		raise ValueError(f"Water level {water_level} is too low (min 1)")
	if water_level > 10:
		raise ValueError(f"Water level {water_level} is too high (max 10)")
	if sunlight_hours < 2:
		raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
	if sunlight_hours > 10:
		raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 10)")
	return f"Plant '{plant_name}' is healthy!"

def test_plant_checks():
	print("=== Garden Plant Health Checker ===")
	print("Testing good values...")
	try:
		result = check_plant_health("tomato", 5, 8)
		print(result)
	except ValueError as e:
		print(f"Error:", e)
	print("Testing empty plant name...")
	try:
		check_plant_health("", 4, 5)
	except ValueError as e:
		print("Error:", e)
	print("Testing bad water level...")
	try:
		check_plant_health("tomato", 12, 5)
	except ValueError as e:
		print("Error:", e)
	print("Testing with bad sunlight hours...")
	try:
		check_plant_health("tomato", 3, 11)
	except ValueError as e:
		print("Error", e)
	print("All errors raising test completed!")

if __name__ == "__main__":
	test_plant_checks()

