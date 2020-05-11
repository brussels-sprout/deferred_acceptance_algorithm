# deferred_acceptance_algorithm
# by brussels_sprout


class Woman:
    collection = {}

    def __init__(self, name, preferences):
        self.name = name  # string
        self.preferences = preferences  # list

        self.engaged_with = None
        self.is_engaged = bool(self.engaged_with)

        self.update_collection(self)

    @classmethod
    def update_collection(cls, self):  # takes the class and the object; adds object to collection with its name as the key
        cls.collection.update({self.name: self})

    def propose(self):
        pass

    def be_rejected(self, man):  # man object who rejected the woman object
        self.preferences.remove(man)

    def be_engaged(self, man):  # man object who engaged the woman (could be temporary or permanent engagement)
        self.engaged_with = man
