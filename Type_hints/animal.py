class Animal:
    def __init__(self, name:str ) -> None:
        self.name: str = name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
    
    def make_sound(self) -> None:
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self) -> None:
        print('auau')

class Cat(Animal):
    def make_sound(self) -> None:
        print('miau')

if __name__ == '__main__':
    dog = Dog('Dog')
    cat = Cat('Cat')

    print(dog)
    print(dog.make_sound)
    print(cat)
    print(cat.make_sound)