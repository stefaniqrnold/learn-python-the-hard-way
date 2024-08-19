from MyStuff import MyStuff

# dict style
MyStuff['apples']

# module style
MyStuff.apples()
print(MyStuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)