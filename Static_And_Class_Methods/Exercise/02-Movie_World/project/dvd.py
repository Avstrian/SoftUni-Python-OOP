class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date: str, age_restriction):
        numbers_to_dates = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6:"June",
                            7: "July", 8: "August", 9: "September", 10: "October", 11: "November",
                            12: "December"}
        dates_list = date.split(".")
        target_month = ""
        for month in numbers_to_dates.keys():
            if month == int(dates_list[1]):
                target_month = numbers_to_dates[month]

        return cls(name, id, int(dates_list[-1]), target_month, age_restriction)

    def __repr__(self):
        status = ""
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"

