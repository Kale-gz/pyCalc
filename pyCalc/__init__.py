from pyCalc.Calc import *


def main() -> None:
    """
    Main function of the program
    """
    c = Calc()
    d = c.exec_operation(1, 2, Operation.ADD)
    print(d)


main()
