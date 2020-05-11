# deferred_acceptance_algorithm
# by brussels_sprout


class Man:
    collection = {}

    def __init__(self, name, preferences):
        self.name = name  # string
        self.preferences = preferences  # list

        self.engaged_with = None

        self.update_collection(self)

    @classmethod
    def update_collection(cls, self):  # takes the class and the object; adds object to collection with its name as the key
        cls.collection.update({self.name: self})

    def be_proposed(self, woman):  # woman object man got proposed by
        pass

    def reject(self, woman):  # woman object man rejected
        woman.be_rejected(self)

    def engage(self, woman):  # woman object man engaged (could be temporary or permanent engagement)
        self.engaged_with = woman
