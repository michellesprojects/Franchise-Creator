import datetime

class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __rep__(self):
    return f'{self.name} menu available from {self.start_time} to {self.end_time}'

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total+= self.items[item]
    return total

class Franchise:

  def __init__(self,address, menus):
    self.address = address
    self.menus = menus

  def __rep__(self):
    return f'Franchise is located on {self.address}'

  def available_menus(self,time):
    menus = ""
    for menu in self.menus:
      if(menu.start_time <= time and menu.end_time >= time):
        menus += menu.name +", "
    
    return "Available menus: "+menus[:-2]

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#TESTING

brunch_food = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

dinner_food = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

arepas_food = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

kids_food = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
brunch_menu = Menu("brunch", brunch_food, datetime.time(11), datetime.time(16))

dinner_menu = Menu("dinner", brunch_food, datetime.time(16), datetime.time(22))

kids_menu = Menu("kids", kids_food,datetime.time(11), datetime.time(22))

arepas_menu = Menu("Arepas", arepas_food, datetime.time(10), datetime.time(20))

flagship = Franchise("1232 West End Road", [brunch_menu, dinner_menu, kids_menu])

new_store = Franchise("12 East Mulberry Street",[brunch_menu, dinner_menu, kids_menu])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

print(new_store.available_menus(datetime.time(12)))

basta = Business("Basta Basta", [flagship, new_store])

arepa = Business("Take a' Arepa", [arepas_place])

