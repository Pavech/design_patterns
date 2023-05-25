class IProduct:
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print('Выпущен легковой автомобиль')


class Truck(IProduct):
    def release(self):
        print('Выпущен грузовой автомобиль')


class IWorkShop:
    def create(self) -> IProduct:
        pass


class CarWorkShop(IWorkShop):
    def create(self):
        return Car()


class TruckWorkShop(IWorkShop):
    def create(self):
        return Truck()


if __name__ == "__main__":
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()
