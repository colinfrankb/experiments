import sys
import traceback

def custom_excepthook(exc_type, exc_value, exc_traceback):
    print("Custom exception hook called:")
    print("Type:", exc_type)
    print("Value:", exc_value)
    print("Traceback:")
    traceback.print_tb(exc_traceback)

sys.excepthook = custom_excepthook

print("Before exception")

raise Exception("does this stop execution?")

print("After exception")
