import calendar


class DVD:
    def __init__(self, name: str, self_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = self_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, self_id: int, name: str, date: str, age_restriction: int):
        _, month, year = date.split('.')
        year = int(year)
        month = calendar.month_name[int(month)]
        return cls(name, self_id, year, month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
