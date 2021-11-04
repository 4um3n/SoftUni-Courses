from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    __FOOD_MAPPER = {
        "Cake": Cake,
        "Bread": Bread,
    }
    __DRINKS_MAPPER = {
        "Tea": Tea,
        "Water": Water,
    }
    __TABLES_MAPPER = {
        "OutsideTable": OutsideTable,
        "InsideTable": InsideTable,
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value == ' ':
            raise ValueError(f"Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in Bakery.__FOOD_MAPPER:
            food = Bakery.__FOOD_MAPPER[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in Bakery.__DRINKS_MAPPER:
            drink = Bakery.__DRINKS_MAPPER[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in Bakery.__TABLES_MAPPER:
            table = Bakery.__TABLES_MAPPER[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.reserve(number_of_people):
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        for table in self.tables_repository:
            if table.table_number == table_number:
                food_in_menu, food_not_in_menu = [], []
                food_names_in_menu = {f.name: f for f in self.food_menu}
                for food_name in args:
                    if food_name in food_names_in_menu:
                        table.order_food(food_names_in_menu[food_name])
                        food_in_menu.append(food_names_in_menu[food_name])
                        continue

                    food_not_in_menu.append(food_name)

                info = [f"Table {table_number} ordered:"]
                [info.append(repr(f)) for f in food_in_menu]
                info.append(f"{self.name} does not have in the menu:")
                [info.append(f) for f in food_not_in_menu]
                return '\n'.join(info)

        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *args):
        for table in self.tables_repository:
            if table.table_number == table_number:
                drinks_in_menu, drinks_not_in_menu = [], []
                drinks_names_in_menu = {d.name: d for d in self.drinks_menu}
                for drink_name in args:
                    if drink_name in drinks_names_in_menu:
                        table.order_drink(drinks_names_in_menu[drink_name])
                        drinks_in_menu.append(drinks_names_in_menu[drink_name])
                        continue

                    drinks_not_in_menu.append(drink_name)

                info = [f"Table {table_number} ordered:"]
                [info.append(repr(d)) for d in drinks_in_menu]
                info.append(f"{self.name} does not have in the menu:")
                [info.append(d) for d in drinks_not_in_menu]
                return '\n'.join(info)

        return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                table_bill = table.get_bill()
                self.total_income += table_bill
                table.clear()
                return f"Table: {table_number}\n" \
                       f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self):
        info = []
        for table in self.tables_repository:
            temp_info = table.free_table_info()
            if temp_info is not None:
                info.append(temp_info)

        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
