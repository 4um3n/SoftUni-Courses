from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


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

    def __init__(self, name: str) -> None:
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

    def add_food(self, food_type: str, name: str, price: float) -> str:
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.__FOOD_MAPPER:
            food = self.__FOOD_MAPPER[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str) -> str:
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.__DRINKS_MAPPER:
            drink = self.__DRINKS_MAPPER[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> str:
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.__TABLES_MAPPER:
            table = self.__TABLES_MAPPER[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        for table in self.tables_repository:
            return table.reserve(number_of_people)

    def _check_order_of_available_table(self, table: Table, order: str, ordered_products: tuple) -> tuple:
        product_in_menu, product_not_in_menu = [], []
        products = self.food_menu if order == "food" else self.drinks_menu
        products_names_in_menu = {pr.name: pr for pr in products}

        for product_name in ordered_products:
            if product_name in products_names_in_menu:
                table.order_food(products_names_in_menu[product_name])
                product_in_menu.append(products_names_in_menu[product_name])
            else:
                product_not_in_menu.append(product_name)

        return product_in_menu, product_not_in_menu

    def _check_table_availability(self, table_number: int, order: str, ordered_products: tuple) -> str:
        for table in self.tables_repository:
            if table.table_number == table_number:
                products_in_menu, products_not_in_menu = self._check_order_of_available_table(
                    table, order, ordered_products)
                info = [f"Table {table_number} ordered:"]
                info.extend([repr(d) for d in products_in_menu])
                info.append(f"{self.name} does not have in the menu:")
                info.extend(products_not_in_menu)
                return '\n'.join(info)

        return f"Could not find table {table_number}"

    def order_food(self, table_number: int, *ordered_food: tuple) -> str:
        return self._check_table_availability(table_number, "food", ordered_food)

    def order_drink(self, table_number: int, *ordered_drinks: tuple) -> str:
        return self._check_table_availability(table_number, "drinks", ordered_drinks)

    def leave_table(self, table_number: int) -> str:
        for table in self.tables_repository:
            if table.table_number == table_number:
                table_bill = table.get_bill()
                self.total_income += table_bill
                table.clear()
                return f"Table: {table_number}\n" \
                       f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self) -> str:
        info = []
        for table in self.tables_repository:
            temp_info = table.free_table_info()
            if temp_info is not None:
                info.append(temp_info)

        return '\n'.join(info)

    def get_total_income(self) -> str:
        return f"Total income: {self.total_income:.2f}lv"
