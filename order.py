import uuid
from datetime import datetime
from counters import calculate_calories, calculate_price
from load_data import load_data

class Order:
    def __init__(self, items, date=None):
        self.order_id = str(uuid.uuid4().hex)[:6]
        self.order_accepted = False
        self.order_refused_reason = ""
        self.date = date if date else datetime.now()
        self.items = items

    @property
    def calories(self):
        total_calories = calculate_calories(self.items)
        if total_calories <= 2000:
            self.order_accepted = True
        else:
            self.order_refused_reason = "Your order exceeds the maximum amount of calories allowed"
        return total_calories

    @property
    def price(self):
        return calculate_price(self.items)

def display_menu(dishes, combinations):
    dish_names = ', '.join(dish['name'] for dish in dishes)
    combo_names = ', '.join(combo['name'] for combo in combinations)
    print(f"Find the menu below: {dish_names}, and {combo_names}.")

def get_user_orders():
    print("Please enter your orders: ")
    return input()

def order_func():
    all_dishes = load_data("data/meals.json")['meals']
    all_combinations = load_data("data/combos.json")['combos']

    display_menu(all_dishes, all_combinations)

    user_orders = get_user_orders()
    result = order_validator(user_orders)

    return result

def order_validator(order):
    items = [item.strip() for item in order.split(',')]
    dishes_data = load_data("data/meals.json")
    combos_data = load_data("data/combos.json")

    dish_names = {dish['name'] for dish in dishes_data['meals']}
    combo_names = {combo['name'] for combo in combos_data['combos']}

    invalid_items = [item for item in items if item not in dish_names and item not in combo_names]

    if invalid_items:
        return f"Invalid items: {', '.join(invalid_items)}."
    
    return items