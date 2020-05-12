# deferred_acceptance_algorithm
# by brussels_sprout


class Woman:
    collection = {}  # {name: object, ...} (format)

    def __init__(self, name, preferences):
        self.name = name  # string

        self.preferences = []
        self.set_preferences(preferences)

        self.engaged_with = None
        self.is_engaged = bool(self.engaged_with)

        self.update_collection(self)

    def set_preferences(self, preferences):  # parameter is list of strings
        if men == {}:
            pass
        else:
            for p in preferences:
                self.preferences.append(men[p])

    @classmethod
    def update_collection(cls, self):  # takes the class and the object; adds object to collection with its name as the key
        cls.collection.update({self.name: self})

    def propose(self, man):  # man object that woman proposes to
        man.be_proposed(self)

    def be_rejected(self, man):  # man object who rejected the woman object
        self.preferences.remove(man)

    def be_engaged(self, man):  # man object who engaged the woman (could be temporary or permanent engagement)
        self.engaged_with = man


class Man:
    collection = {}  # {name: object, ...} (format)

    def __init__(self, name, preferences):
        self.name = name  # string

        self.preferences = []
        self.set_preferences(preferences)

        self.engaged_with = None  # woman object
        self.is_engaged = bool(self.engaged_with)

        self.update_collection(self)

    def set_preferences(self, preferences):  # parameter is list of strings
        if women == {}:
            pass
        else:
            for p in preferences:
                self.preferences.append(women[p])

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


women = Woman.collection
men = Man.collection
