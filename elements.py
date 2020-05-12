# deferred_acceptance_algorithm
# by brussels_sprout


class Woman:
    collection = {}  # {object.name: object, ...} (format)

    def __init__(self, name):  # preferences (not self.preferences) is a list of names (strings)
        self.name = name  # string

        self.preferences = []  # list of objects; index 0 is the most preferable
        # self.set_preferences(preferences)

        self.engaged_with = None  # man object
        self.is_engaged = bool(self.engaged_with)  # bool(None) == False

        self.update_collection(self)

    def set_preferences(self, preferences):  # adds man objects to woman's preference list
        if men == {}:
            pass
        else:
            for p in preferences:  # p is a name (string)
                self.preferences.append(men[p])

    @classmethod
    def update_collection(cls, self):  # adds object to collection with its name as the key
        cls.collection.update({self.name: self})

    def propose(self, man):  # man object that woman proposes to
        man.be_proposed(self)

    def be_engaged(self, man):  # man object who engaged the woman (could be temporary or permanent engagement)
        self.engaged_with = man

    def be_rejected(self, man):  # man object who rejected the woman
        self.preferences.remove(man)


class Man:
    collection = {}  # {object.name: object, ...} (format)

    def __init__(self, name):  # preferences (not self.preferences) is a list of names (strings)
        self.name = name  # string

        self.preferences = []  # list of objects; index 0 is the most preferable
        # self.set_preferences(preferences)

        self.engaged_with = None  # woman object
        self.is_engaged = bool(self.engaged_with)  # bool(None) == False

        self.update_collection(self)

    def set_preferences(self, preferences):  # adds woman objects to man's preference list
        if women == {}:
            pass
        else:
            for p in preferences:
                self.preferences.append(women[p])

    @classmethod
    def update_collection(cls, self):  # adds object to collection with its name as the key
        cls.collection.update({self.name: self})

    def be_proposed(self, woman):  # woman object man got proposed by
        if not self.is_engaged:  # man not engaged
            self.engage(woman)
        # if woman proposing is more preferable than engaged woman then ...
        elif self.preferences.index(woman) < self.preferences.index(self.engaged_with):
            self.reject(self.engaged_with)
            self.engage(woman)
        else:
            self.reject(woman)

    def engage(self, woman):  # woman object man engaged (could be temporary or permanent engagement)
        self.engaged_with = woman
        woman.be_engaged(self)

    def reject(self, woman):  # woman object man rejected
        woman.be_rejected(self)


women = Woman.collection
men = Man.collection
