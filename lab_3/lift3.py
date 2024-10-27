class Lift:
    def __init__(self, start_floor, name):
        self.current_floor = start_floor
        self.commands = []
        self.moves = 0
        self.name = name

    def move_up(self):
        if self.current_floor < max_floor:
            self.current_floor += 1
            self.commands.append(
                f"Проехать вверх на {self.current_floor} этаж")
            self.moves += 1
        else:
            raise Exception("Ошибка: На взлет!")

    def move_down(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            self.commands.append(f"Проехать вниз на {self.current_floor} этаж")
            self.moves += 1
        else:
            raise Exception("Ошибка: Под землю собрались?")

    def open_doors(self):
        self.commands.append("Открыть двери")

    def close_doors(self):
        self.commands.append("Закрыть двери")

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.move_up()
            else:
                self.move_down()
        self.open_doors()
        self.close_doors()


class DoubleLift:
    def __init__(self, num_floors, elevator1_start, elevator2_start):
        self.num_floors = num_floors
        self.elevator1 = Lift(elevator1_start, name='1_Lift')
        self.elevator2 = Lift(elevator2_start, name='2_Lift')

    def find_elevator(self, origin):
        return min([self.elevator1, self.elevator2],
                   key=lambda elevator: abs(elevator.current_floor - origin))

    def call(self, origin, target):
        elevator = self.find_elevator(origin)
        elevator.go_to_floor(origin)
        elevator.go_to_floor(target)
        moves, commands, name = (elevator.moves, elevator.commands,
                                 elevator.name)
        elevator.moves, elevator.commands = 0, []
        return moves, commands, name


max_floor = 12
elevator_system = DoubleLift(
    num_floors=max_floor, elevator1_start=4, elevator2_start=10)

calls = [(3, 7), (9, 1), (4, 5)]

for origin, target in calls:
    moves, commands, name = elevator_system.call(origin, target)
    print(f"Вызов с {origin} этажа на {target} этаж принял {name}")
    print(f"Лифт совершил {moves} перемещений:")
    for command in commands:
        print(command)
    print("----------------------------")
