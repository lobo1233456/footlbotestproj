from testbase.loader import TestLoader

loader = TestLoader()
for it in loader.load("footlbotest"):
    print(it)