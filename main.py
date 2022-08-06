def main():

    inp = input("What's your name: ")
    hello(inp)

    print(hello(inp))

def hello(to="world"):
    return f"Hello, {to}"


if __name__ =="__main__":

    main()