from load_data import load_data

all_dishes = load_data("data/meals.json")['meals']
all_combinations = load_data("data/combos.json")['combos']

def calculate_calories(orders):
    total_calories = 0

    for order in orders:
        if 'combo' in order:
            total_calories += calculate_combo_calories(order)
        else:
            for dish in all_dishes:
                if order == dish['name'] or order == dish['id']:
                    total_calories += dish['calories']
    return total_calories

def calculate_combo_calories(orders):
    combo_meal_dict = {combo['name']: combo['meals'] for combo in all_combinations}
    total = calculate_calories(combo_meal_dict[orders]) if orders in combo_meal_dict else 0
    return total

def calculate_price(orders):
    total = 0

    for order in orders:
        if 'combo' in order:
            for combo in all_combinations:
                if order == combo['name']:
                    total += combo['price']
        else:
            for dish in all_dishes:
                if order == dish['name']:
                    total += dish['price']
    return total