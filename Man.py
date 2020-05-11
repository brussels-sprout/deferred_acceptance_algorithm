# deferred_acceptance_algorithm
# by brussels_sprout


class Man:
    collection = {}

    def __init__(self, name, preferences):
        self.name = name  # string
        self.preferences = preferences  # list of objects; smaller index means higher preference

        self.engaged_with = None  # woman object
        self.is_engaged = bool(self.engaged_with)

        self.update_collection(self)

    @classmethod
    def update_collection(cls, self):  # takes the class and the object; adds object to collection with its name as the key
        cls.collection.update({self.name: self})

    def be_proposed(self, woman):  # woman object man got proposed by
        if not self.is_engaged:
            self.engage(woman)
        elif self.preferences.index(woman) < self.preferences.index(self.engaged_with):
            self.reject(self.engaged_with)
            self.engage(woman)
        else:
            self.reject(woman)

    def reject(self, woman):  # woman object man rejected
        woman.be_rejected(self)

    def engage(self, woman):  # woman object man engaged (could be temporary or permanent engagement)
        self.engaged_with = woman
        woman.be_engaged(self)
