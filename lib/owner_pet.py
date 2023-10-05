class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        #self.validate_pet_type = pet_type
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("Invalid pet type")
        
    
    

class Owner:
    def __init__(self, name):
        self.name = name

    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets
    
    
         
        
    