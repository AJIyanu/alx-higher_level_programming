#!/usr/bin/python3

from base import Base as Base

b1 = Base()
print(type(b1))

class bbb(Base):
    pass

b2 = bbb()

print(type(b2))
