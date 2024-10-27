class Lift:
    def __init__(self, start_floor, name):
        self.current_floor = start_floor
        self.commands = []
        self.moves = 0
        self.name = name

    def move_up(self, trg):
        while self.current_floor != trg:
            self.current_floor += 1
            self.commands.append(
                f"Проехать вверх на {self.current_floor} этаж")
            self.moves += 1
        self.open_doors()
        self.close_doors()

    def move_down(self, trg):
        while self.current_floor != trg:
            self.current_floor -= 1
            self.commands.append(f"Проехать вниз на {self.current_floor} этаж")
            self.moves += 1
        self.open_doors()
        self.close_doors()

    def open_doors(self):
        self.commands.append("Открыть двери")

    def close_doors(self):
        self.commands.append("Закрыть двери")


def generate_automat():
    automat = dict()
    for i in range(1, max_floor + 1):
        for j in range(1, max_floor + 1):
            key = (i, j)
            value = dict()
            for x in range(1, max_floor + 1):
                for y in range(1, max_floor + 1):
                    if abs(i - x) <= abs(j - x):
                        direction_1 = 1 if (i - x) < 0 else 0
                        direction_2 = 1 if (x - y) < 0 else 0
                        value[(x, y)] = {
                            'action_1': lift_1.move_up if direction_1
                            else lift_1.move_down,
                            'action_2': lift_1.move_up if direction_2
                            else lift_1.move_down,
                            'lift': lift_1
                        }
                    else:
                        direction_1 = 1 if (j - x) < 0 else 0
                        direction_2 = 1 if (x - y) < 0 else 0
                        value[(x, y)] = {
                            'action_1': lift_2.move_up if direction_1
                            else lift_2.move_down,
                            'action_2': lift_2.move_up if direction_2
                            else lift_2.move_down,
                            'lift': lift_2
                        }
            automat[key] = value
    return automat


max_floor = 20
lift_1, lift_2 = Lift(1, 'first'), Lift(1, 'second')
automat = generate_automat()

queue = [(1, 2), (1, 5), (4, 9), (10, 1)]


while queue:
    print()
    item = queue.pop(0)
    lift: Lift = automat[(lift_1.current_floor,
                          lift_2.current_floor)][item]['lift']
    print(f'Вызов с {item[0]} этажа до {item[1]}')
    print(f'Принял вызов лифт {lift.name} находящийся '
          f'на {lift.current_floor} этаже')
    action_1 = automat[(lift_1.current_floor,
                        lift_2.current_floor)][item]['action_1']
    action_2 = automat[(lift_1.current_floor,
                        lift_2.current_floor)][item]['action_2']
    action_1(item[0])
    action_2(item[1])

    for com in lift.commands:
        print(com)
    print(f'Лифт выполнил {lift.moves} движений')
    lift.moves = 0
    lift.commands = []
