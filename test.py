class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self. sound = sound

        def make_sound(self):
            return f"{self.name} the{self.species} says {self.sound}"
        #creating four animals objects
        dog = Animal(name="Puppy", species="Dog", sound="woof" )
        cat = Animal(name="Cherry", species="Cat", sound="Meow" )
        cow = Animal(name="Caro", species="Cow", sound="Moo" )
        lion = Animal(name="Simba", species="Lion", sound="Roar" )
        #Accessing the objects and their sounds
        print(dog.make_sound())
        print(cat.make_sound())
        print(cow.make_sound())
        print(lion.make_sound())