from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    __ORDER_MAKER = {
        "food": lambda t: t.order_food,
        "drinks": lambda t: t.order_drink,
    }

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
        self.products = {
            "food": self.food_menu,
            "drinks": self.drinks_menu
        }
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

    @staticmethod
    def _check_product_name_in_menu(name, menu, product_type):
        if name in [p.name for p in menu]:
            raise Exception(f"{product_type} {name} is already in the menu!")

    def _find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def _sort_ordered_products(self, table: Table, order_type: str, ordered_products: tuple) -> tuple:
        available_products, unavailable_products = [], []
        products = {pr.name: pr for pr in self.products[order_type]}
        for product_name in ordered_products:
            if product_name in products:
                product_obj = products[product_name]
                self.__ORDER_MAKER[order_type](table)(product_obj)
                available_products.append(repr(product_obj))
            else:
                unavailable_products.append(product_name)

        return available_products, unavailable_products

    def _get_table_order_report(self, table_number: int, order: str, ordered_products: tuple) -> str:
        table = self._find_table_by_number(table_number)
        if table is not None:
            available_products, unavailable_products = self._sort_ordered_products(table, order, ordered_products)
            info = [f"Table {table_number} ordered:"]
            info.extend(available_products)
            info.append(f"{self.name} does not have in the menu:")
            info.extend(unavailable_products)
            return '\n'.join(info)

        return f"Could not find table {table_number}"

    def add_food(self, food_type: str, name: str, price: float) -> str:
        self._check_product_name_in_menu(name, self.food_menu, food_type)
        if food_type in self.__FOOD_MAPPER:
            food = self.__FOOD_MAPPER[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str) -> str:
        self._check_product_name_in_menu(name, self.drinks_menu, drink_type)
        if drink_type in self.__DRINKS_MAPPER:
            drink = self.__DRINKS_MAPPER[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> str:
        if self._find_table_by_number(table_number) is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.__TABLES_MAPPER:
            table = self.__TABLES_MAPPER[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        for table in self.tables_repository:
            if not table.is_reserved and number_of_people <= table.capacity:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *ordered_food: tuple) -> str:
        return self._get_table_order_report(table_number, "food", ordered_food)

    def order_drink(self, table_number: int, *ordered_drinks: tuple) -> str:
        return self._get_table_order_report(table_number, "drinks", ordered_drinks)

    def leave_table(self, table_number: int) -> str:
        table = self._find_table_by_number(table_number)
        if table is not None:
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
