import sys
import traceback


def raise_exception_without_try_block():
    print("Before exception")
    raise Exception("does this stop execution?")
    # it does stop execution, the process closes
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_tb) 
    print("After exception")

def raise_exception_with_try_block():
    try:
        raise Exception("raised exception in try block")
    except Exception as err:
        print("Exception caught")
        # sys.exc_info is only available inside the except block
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(exc_type, exc_value, exc_tb)

if __name__ == "__main__":
    raise_exception_with_try_block()
