

class Target:
    # старый класс нашего проекта, который возвращает строку

    def get(self) -> str:
        return "123"


class NewClass:
    # новый класс, который будет возвращать int
    # наш проект не может работать с int, только со string

    def another_get(self) -> int:
        return 456


class Adapter(Target, NewClass):
    # делаем класс adapter, в котором прописываем как надо изменить NewClass,
    # для того чтобы он работал в проекте

    def get(self) -> str:
        return str(self.another_get())


def main(target):
    # Здесь у нашего target должна быть функция get(),
    # а также она должна возвращать строку

    print("Answer is: " + target.get())


if __name__ == '__main__':
    main(Target())      # все ок, ведь класс работает со str
    main(NewClass())    # ошибка, ведь класс работает с int
    main(Adapter())     # все ок, ведь класс работает со str

