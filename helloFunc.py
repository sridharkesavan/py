"""
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
"""


def hello(to="World"):
    print("hello,", to)


def main():
    hello()
    name = input("What's your name? ")
    hello(name)


main()
