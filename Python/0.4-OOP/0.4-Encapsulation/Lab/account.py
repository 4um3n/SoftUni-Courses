class Account:
    def __init__(self, usr_id, balance, pin):
        self.__id = usr_id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return f"Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return f"Pin changed"
        return f"Wrong pin"
