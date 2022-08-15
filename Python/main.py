from car import Car
from account import Account

if __name__ == '__main__':
    car1 = Car('AMS245',Account('Andres Herrera','AND8976'))
    print(vars(car1))