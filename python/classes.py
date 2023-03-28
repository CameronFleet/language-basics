
class Dog:
    def __init__(self, breed: str, name: str, age: int) -> None:
        self.breed: str = breed
        self.name: str = name
        self._age: int = age

    def bark(self) -> None:
        print("WOOF!")

    def __str__(self) -> str:
        return f"Dog(breed={self.breed}, name={self.name}, age={self._age})"


if __name__ == '__main__':
    jax = Dog("Golden Retriever", "Jax", 9)
    print(jax)
    print(jax.breed)
    jax.bark()
