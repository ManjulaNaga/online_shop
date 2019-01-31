import traceback


def function1():
    function2()


def function2():
    function3()


def function3():
    try:
        raise Exception("An exception has occurred")
    except Exception:
        print("caught exception in function3..Reraising.....\n")
    raise  # reraises most recent exception


try:
    function1()

except Exception:
    print("Exception caught in main program")
    print("Traceback")
    traceback.print_exc()
