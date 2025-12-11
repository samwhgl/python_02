# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 16:08:04 by shaegels          #+#    #+#              #
#    Updated: 2025/12/10 14:52:28 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def check_temperature(temp_str: str) -> int | None:
    """
    Vérifie si une chaîne de caractères peut être convertie en température valide pour les plantes.

    La température doit être comprise entre 0°C et 40°C inclus.

    Args:
        temp_str (str): La température sous forme de chaîne de caractères.

    Returns:
        int | None: La température valide en entier si elle est correcte, sinon None.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None

    return temp


def test_temperature_input() -> None:
    """
    Teste plusieurs valeurs de température pour vérifier la fonction check_temperature.

    Affiche si chaque température est valide pour les plantes ou non.
    """
    print("=== Garden Temperature Checker ===")
    test_values = ["25", "abc", "100", "-50"]
    for value in test_values:
        result = check_temperature(value)
        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
