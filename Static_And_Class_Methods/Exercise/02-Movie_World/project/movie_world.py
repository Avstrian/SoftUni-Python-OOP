from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        target_customer: Customer = ""
        target_dvd: DVD = ""
        for customer in self.customers:
            if customer.id == customer_id:
                target_customer = customer
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                target_dvd = dvd

        for dvd in target_customer.rented_dvds:
            if dvd.id == dvd_id and dvd.is_rented:
                return f"{target_customer.name} has already rented {dvd.name}"

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                if dvd.is_rented:
                    return "DVD is already rented"

        if target_customer.age < target_dvd.age_restriction:
            return f"{target_customer.name} should be at least {target_dvd.age_restriction} to rent this movie"

        target_customer.rented_dvds.append(target_dvd)
        target_dvd.is_rented = True
        return f"{target_customer.name} has successfully rented {target_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        target_customer: Customer = ""
        target_dvd: DVD = ""
        for customer in self.customers:
            if customer.id == customer_id:
                target_customer = customer
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                target_dvd = dvd

        if target_dvd in target_customer.rented_dvds:
            target_customer.rented_dvds.remove(target_dvd)
            target_dvd.is_rented = False
            return f"{target_customer.name} has successfully returned {target_dvd.name}"
        return f"{target_customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            if dvd == self.dvds[-1]:
                result += f"{dvd.__repr__()}"
            else:
                result += f"{dvd.__repr__()}\n"

        return result
