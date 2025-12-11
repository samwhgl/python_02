# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 14:53:31 by shaegels          #+#    #+#              #
#    Updated: 2025/12/10 15:25:41 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def water_plants(plant_list):
	print("Opening watering system")
	try:
		for plant in plant_list:
			if plant is None:
				raise ValueError("invalid plant!")
			print(f"Watering {plant}")
	except ValueError as e:
		print(f"Error, Cannot water {plant} - {e}")
	finally:
		print("Closing watering ststem (cleanup)")

def test_watering_system():
	print("=== Garden Watering System")
	print("Testing normal watering...")
	list1 = ["tomto", "lettuce", "carrots"]
	list2 = ["tomato", None]
	water_plants(list1)
	print("Watering completed successfully!")
	water_plants(list2)
	print("Cleanup always happens, even with errors")

if __name__ == "__main__":
	test_watering_system()
