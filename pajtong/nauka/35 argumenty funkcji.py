def funkcja(arg1, arg2 = "World", *args, **kwargs):
    print(arg1, arg2, args, len(args), kwargs)
    for x in args:
        print(x)
    for x in kwargs.values():
        print(x)

funkcja("Hello")
funkcja("No", "siema")
funkcja("No", "siema", "!", ":-)", autor = "douen", rok = 2023)
