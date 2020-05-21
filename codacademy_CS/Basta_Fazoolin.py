from datetime import *


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (
            self.name
            + " menu available from "
            + self.start_time
            + " to "
            + self.end_time
        )

    def calculate_bill(self, purchased_items):
        total_bill = 0
        for item in purchased_items:
            total_bill += self.items[item]
        return total_bill


brunch = Menu(
    "Brunch",
    {
        "pancakes": 7.50,
        "waffles": 9.00,
        "burger": 11.00,
        "home fries": 4.50,
        "coffee": 1.50,
        "espresso": 3.00,
        "tea": 1.00,
        "mimosa": 10.50,
        "orange juice": 3.50,
    },
    "11 AM",
    "4 PM",
)

early_bird = Menu(
    "Early-bird",
    {
        "salumeria plate": 8.00,
        "salad and breadsticks (serves 2, no refills)": 14.00,
        "pizza with quattro formaggi": 9.00,
        "duck ragu": 17.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 1.50,
        "espresso": 3.00,
    },
    "3 PM",
    "6 PM",
)

dinner = Menu(
    "Dinner",
    {
        "crostini with eggplant caponata": 13.00,
        "ceaser salad": 16.00,
        "pizza with quattro formaggi": 11.00,
        "duck ragu": 19.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 2.00,
        "espresso": 3.00,
    },
    "5 PM",
    "11 PM",
)

kids = Menu(
    "Kids",
    {
        "chicken nuggets": 6.50,
        "fusilli with wild mushrooms": 12.00,
        "apple juice": 3.00,
    },
    "11 AM",
    "9 PM",
)

breakfast_order = ["pancakes", "home fries", "coffee"]
print(brunch.calculate_bill(breakfast_order))

e_b_order = ["salumeria plate", "mushroom ravioli (vegan)"]
print(early_bird.calculate_bill(e_b_order))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menu = []
        dttime = datetime.strptime(time, "%I %p")
        for menu in self.menus:
            if (dttime >= datetime.strptime(menu.start_time, "%I %p")) and (
                dttime <= datetime.strptime(menu.end_time, "%I %p")
            ):
                available_menu.append(menu)
        return available_menu


flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise(
    "12 East Mulberry Street", [brunch, early_bird, dinner, kids]
)

print(flagship_store.available_menus("5 PM"))
