# deferred_acceptance_algorithm
# by brussels_sprout

# elements.py contains the class definitions and related variables


class Element:
    collection = None  # ignore this, i mean it. :)

    def __init__(self, name):
        self.name = name  # string

        # list of objects; index 0 is the most preferable
        self.preferences = []

        self.engaged_with = None  # man/woman object

        self.update_collection(self)

    @property
    def is_engaged(self):
        return bool(self.engaged_with)  # bool(None) is False

    # adds object to collection with its name as the key
    @classmethod
    def update_collection(cls, self):
        cls.collection.update({self.name: self})


class Woman(Element):
    collection = {}  # {object.name: object, ...} (format)

    # preferences (not self.preferences) is a list of names (strings)
    # adds man objects to woman's preference list
    def set_preferences(self, preferences):
        # p is a name (string)
        for p in preferences:
            self.preferences.append(men[p])

    # man object that woman proposes to
    def propose(self, man):
        man.be_proposed(self)

    # man object who engaged the woman
    # (could be temporary or permanent engagement)
    def be_engaged(self, man):
        self.engaged_with = man

    # man object who rejected the woman
    def be_rejected(self, man):
        self.preferences.remove(man)

        self.engaged_with = None


class Man(Element):
    collection = {}  # {object.name: object, ...} (format)

    # preferences (not self.preferences) is a list of names (strings)
    # adds woman objects to man's preference list
    def set_preferences(self, preferences):
        for p in preferences:
            self.preferences.append(women[p])

    # woman object man got proposed by
    def be_proposed(self, woman):
        # if man not engaged then
        if not self.is_engaged:
            self.engage(woman)
        # if woman proposing is more preferable than engaged woman then
        elif self.preferences.index(woman) < \
                self.preferences.index(self.engaged_with):
            self.reject(self.engaged_with)
            self.engage(woman)
        else:
            self.reject(woman)

    # woman object man engaged
    # (could be temporary or permanent engagement)
    def engage(self, woman):
        self.engaged_with = woman

        woman.be_engaged(self)

    # woman object man rejected
    def reject(self, woman):
        woman.be_rejected(self)


women = Woman.collection
men = Man.collection
