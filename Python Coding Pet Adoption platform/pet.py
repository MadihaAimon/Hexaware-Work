class Pet:
    def _init_(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def str(self):
        return f"{self.name} - Age: {self.age}, Breed: {self.breed}"

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, name):
        self.name = name
    @property
    def age(self):
        return self.age
    
    @age.setter
    def age(self, age):
        self.age = age
    @property
    def breed(self):
        return self.breed
    @breed.setter
    def breed(self, breed):
        self.breed = breed    
        
class Dog(Pet):
     def init(self, name, age, breed, dog_breed):
        super().init(name, age, breed)
        self.dog_breed = dog_breed

     def str(self):
        return f"{super().str()}, Dog Breed: {self.dog_breed}"

     @property
     def dog_breed(self):
        return self.dog_breed
     @dog_breed.setter
     def set_dog_breed(self, dog_breed):
        self.dog_breed = dog_breed

class Cat(Pet):
    def init(self, name, age, breed, cat_color):
        super().init(name, age, breed)
        self.cat_color = cat_color

    def str(self):
        return f"{super().str()}, Cat Color: {self.cat_color}"

    @property
    def cat_color(self):
        return self.cat_color
    @cat_color.setter
    def set_cat_color(self, cat_color):
        self.cat_color = cat_color    

class PetShelter:
    def init(self):
        self.available_pets = []

    def add_pet(self, pet):
        self.available_pets.append(pet)

    def remove_pet(self, pet):
        if pet in self.available_pets:
            self.available_pets.remove(pet)

    def list_available_pets(self):
        for pet in self.available_pets:
            print(pet)