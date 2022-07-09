def umesh():
    try:
        print("Hello")
        print(10)
    except ZeroDivisionError:
        print("ZeroDivisionError")
        return 10
    finally:
        print("This code will run")
    return 5
print(umesh())
