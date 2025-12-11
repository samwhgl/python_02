# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_errors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 15:27:14 by shaegels          #+#    #+#              #
#    Updated: 2025/12/10 16:20:08 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PlantError(Exception):
	pass

class WaterError(PlantError):
	pass

class SunlightError(PlantError):
	pass


def check_plant_health(plant_name, water_level, sunlight_hours):
