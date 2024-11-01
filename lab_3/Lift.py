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

    def run(self, origin, target, direction):
        self.active_lift = None
        self.direction = direction
        if abs(self.current_positions[0] - origin) <= abs(self.current_positions[1] - origin):
            self.active_lift = 0
        else:
            self.active_lift = 1
        print(f'Лифт {self.active_lift + 1} принял команду')
        direction_to_origin = Direction.up if (
            self.current_positions[self.active_lift] - origin) < 0 else Direction.down
        if direction_to_origin in [Direction.up, Direction.static]:
            self.move_up(origin)
        else:
            self.move_down(origin)
        self.open_close(True)
        if self.direction in [Direction.up, Direction.static]:
            self.move_up(target)
        else:
            self.move_down(target)
        self.open_close(False)
        print(f'Лифт {self.active_lift + 1} ожидает')

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
