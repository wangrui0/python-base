class Dog(object):
    __instane = None

    def __new__(cls, *args, **kwargs):
        if cls.__instane == None:
            cls.__instane = object.__new__(cls)
            return cls.__instane
        else:
            return cls.__instane


dog1 = Dog()
print(id(dog1))
dog2 = Dog()
print(id(dog2))
dog3 = Dog()
print(id(dog3))
"""
1340074620520
1340074620520
1340074620520
"""
