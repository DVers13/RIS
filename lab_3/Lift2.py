from enum import Enum


class Direction(Enum):
    up = 'UP'
    down = 'DOWN'
    static = 'STATIC'


class DoubleLift:

    def __init__(self, current_positions: list[int] = [1, 1], max_home_floor: int = 2):
        self.current_positions = current_positions
        self.max_home_floor = max_home_floor
        self.direction = Direction.static
        self.generate_automat()

    def generate_automat(self):
        self.automat = {
            (i, j): {
                'active_lift': lambda x, pos: 0 if abs(x - pos[0]) <= abs(x - pos[1]) else 1,
                'direction': lambda x: Direction.up if (self.current_positions[self.active_lift] - x) < 0 else Direction.down,
                'action': lambda d, t: self.move_up(t) if d in [Direction.up, Direction.static] else self.move_down(t)            }
            for i in range(1, self.max_home_floor + 1)
            for j in range(1, self.max_home_floor + 1)
        }

    def run(self, origin, target):
        self.active_lift = self.automat[tuple(self.current_positions)]['active_lift'](origin, self.current_positions)

        print(f'Лифт {self.active_lift + 1} принял команду')

        direction_to_origin = self.automat[tuple(self.current_positions)]['direction'](origin)

        self.automat[tuple(self.current_positions)]['action'](direction_to_origin, origin)

        self.open_close(True)

        direction_to_target = self.automat[tuple(self.current_positions)]['direction'](target)

        self.automat[tuple(self.current_positions)]['action'](direction_to_target, target)

        self.open_close(False)
        print(f'Лифт {self.active_lift + 1} ожидает')
        print(self.current_positions)
        
    def move_up(self, trg):
        while self.current_positions[self.active_lift] != trg:
            self.current_positions[self.active_lift] += 1
            print(
                f'Лифт {self.active_lift + 1} поднялся на {self.current_positions[self.active_lift]} этаж')

    def move_down(self, trg):
        while self.current_positions[self.active_lift] != trg:
            self.current_positions[self.active_lift] -= 1
            print(
                f'Лифт {self.active_lift + 1} спустился на {self.current_positions[self.active_lift]} этаж')

    def open_close(self, enter):
        print(f'Лифт {self.active_lift + 1} открыл дверь')
        (print(f'Пассажиры вошли на этаже {self.current_positions[self.active_lift]}')
         if enter else
         print(f'Пассажиры вышли на этаже {self.current_positions[self.active_lift]}'))
        print(f'Лифт {self.active_lift + 1} закрыл дверь')
