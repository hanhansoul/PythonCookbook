# class Root:
#     def draw(self):
#         # the delegation chain stops here
#         assert not hasattr(super(), 'draw')
#
#
# class Shape(Root):
#     def __init__(self, shapename, **kwds):
#         self.shapename = shapename
#         super().__init__(**kwds)
#
#     def draw(self):
#         print('Drawing.  Setting shape to:', self.shapename)
#         super().draw()
#
#
# class ColoredShape(Shape):
#     def __init__(self, color, **kwds):
#         self.color = color
#         super().__init__(**kwds)
#
#     def draw(self):
#         print('Drawing.  Setting color to:', self.color)
#         super().draw()
#
#
# cs = ColoredShape(color='blue', shapename='square')
# cs.draw()


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    """
        Within each method, super() is used to call the previous implementation. The use of
    super(SubPerson, SubPerson).name.__set__(self, value) in the setter function is no mistake. To delegate to
    the previous implementation of the setter, control needs to pass through the __set__() method of the
    previously defined name property. However, the only way to get to this method is to access it as a class
    variable instead of an instance variable. This is what happens with the super(SubPerson, SubPerson) operation.
    """

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        # print(super())
        a1 = super(SubPerson, self)
        a2 = super(SubPerson, SubPerson)
        super(SubPerson, SubPerson).name.__set__(self, value)
        # super(SubPerson, self).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

    def super_test(self):
        print(super())
        print(super(SubPerson, self))
        print(super(SubPerson, SubPerson))


class SubPersonPart(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPersonPart, SubPersonPart).name.__set__(self, value)


s = SubPerson('GUI')
print(s.name)
s.name = 'LAR'
s.name = 42
