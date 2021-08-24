from project.animal import Animal
from project.cheetah import Cheetah
from project.caretaker import Caretaker
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            animal_type = type(animal)
            self.__budget -= price
            return f'{animal.name} the {animal_type.__name__} added to the zoo'
        elif self.__budget - price < 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            worker_type = type(worker)
            return f"{worker.name} the {worker_type.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        budget_needed = 0
        for worker in self.workers:
            budget_needed += worker.salary

        if budget_needed > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= budget_needed
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_for_tending = 0
        for animal in self.animals:
            money_for_tending += animal.money_for_care

        if money_for_tending > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= money_for_tending
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        status = ""
        status += f"You have {len(self.animals)} animals\n"
        lion_data = []
        cheetah_data = []
        tiger_data = []
        lions = 0
        cheetahs = 0
        tigers = 0

        for animal in self.animals:
            if type(animal) == Lion:
                lions += 1
                lion_data.append(repr(animal))
            elif type(animal) == Cheetah:
                cheetahs += 1
                cheetah_data.append(repr(animal))
            elif type(animal) == Tiger:
                tigers += 1
                tiger_data.append(repr(animal))

        status += f"----- {lions} Lions:\n"
        status += '\n'.join(lion_data) + "\n"
        status += f"----- {tigers} Tigers:\n"
        status += '\n'.join(tiger_data) + "\n"
        status += f"----- {cheetahs} Cheetahs:\n"
        status += '\n'.join(cheetah_data)
        return status

    def workers_status(self):
        status = ""
        status += f"You have {len(self.workers)} workers\n"
        keeper_data = []
        caretaker_data = []
        vet_data = []
        keepers = 0
        caretakers = 0
        vets = 0

        for worker in self.workers:
            if type(worker) == Keeper:
                keepers += 1
                keeper_data.append(repr(worker))
            elif type(worker) == Caretaker:
                caretakers += 1
                caretaker_data.append(repr(worker))
            elif type(worker) == Vet:
                vets += 1
                vet_data.append(repr(worker))

        status += f"----- {keepers} Keepers:\n"
        status += '\n'.join(keeper_data) + "\n"
        status += f"----- {caretakers} Caretakers:\n"
        status += '\n'.join(caretaker_data) + "\n"
        status += f"----- {vets} Vets:\n"
        status += '\n'.join(vet_data)
        return status
