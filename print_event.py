import random
import string

class Parent(object):
    def __init__(self):
        pass

    def __repr__(self):
        Thingsuperclass = str(self.__class__.__bases__[0].__name__)
        Thingclass = str(self.__class__.__name__)
        Thingattrs = str(self.__dict__)
        return '<'+Thingsuperclass+'('+Thingclass+' '+Thingattrs+')>'

class Letter(Parent):
    def __init__(self):
        self.letter = random.choice(string.lowercase)
        print "Created object with letter", self.letter


class Number(Parent):
    def __init__(self):
        self.num = random.randint(0,100)
        print "Created simple object with number", self.num


if __name__ == '__main__':
    num = Number()
    let = Letter()
    p = Parent()

    print num
    print let
    print p

# <Event(4-MouseMotion {'buttons': (0, 0, 0), 'pos': (15, 0), 'rel': (-304, -239)})>