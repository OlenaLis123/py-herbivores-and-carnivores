class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return ("{Name:"
                + f" {self.name}, Health: {self.health}, Hidden: {self.hidden}"
                + "}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if (animal in Animal.alive
                and isinstance(animal, Herbivore)
                and not animal.hidden):
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
