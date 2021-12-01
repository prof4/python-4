def hello_world_printer(string, n):
    print(string *n)

string = input("wat is uw zin of woord: ") + "\n"
n = int(input("hoe vaak moet uw string worden geprint: "))
hello_world_printer(string, n)
