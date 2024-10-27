from Lift2 import DoubleLift

def main():
    d_lift = DoubleLift(current_positions=[1, 2], max_home_floor=4)
    d_lift.run(2, 4)
    d_lift.run(1, 2)
    # d_lift.run(1, 3)


if __name__ == '__main__':
    main()
