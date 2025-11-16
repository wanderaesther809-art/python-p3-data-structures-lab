spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods: list)->list:
    return [food["name"] for food in spicy_foods]

    pass

def get_spiciest_foods(spicy_foods: list )->list:
    return [food for food in spicy_foods if food["heat_level"]>5] 
    pass

def print_spicy_foods(spicy_foods: list )->None:
    for food in spicy_foods:
        name =food["name"]
        cuisine =food["cuisine"]
        heat =food["heat_level"]
        chillis = "🌶" * heat

        output =f"{name} ({cuisine}) | Heat Level: {chillis}"
        print(output)


    pass

def get_spicy_food_by_cuisine(spicy_foods : list, cuisine: str) -> dict:
    for food in spicy_foods:
        if food.get ("cuisine") == cuisine:

            return food
    return None

    pass

def print_spiciest_foods(spicy_foods:list) -> None:
    spiciest_list =get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_list)
   
    pass

def get_average_heat_level(spicy_foods:list) -> float:
    if not spicy_foods:
        return 0.0
    heat_levels =[food["heat_level"]for food in spicy_foods]
    total_heat = sum(heat_levels)
    return total_heat / len(spicy_foods)


    pass

def create_spicy_food(spicy_foods:list , spicy_food: dict) -> list:

    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
