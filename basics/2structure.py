from sys import argv

arg0, arg1, arg2 = argv

print arg0, arg1, arg2

def print_arguments(*args):
    """Prints arguments"""
    for arg in args:
        print arg

print_arguments("dit","dat","enzo")
