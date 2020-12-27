from pyCalc.Operation import Operation
from pyCalc.Multiplication import Multiplication
from pyCalc.Division import Division
from pyCalc.Subtraction import Subtraction
from pyCalc.Addition import Addition


class OperationFactory:

    @staticmethod
    def getInstance(operation: Operation) -> object:
        if Operation.ADD == operation:
            return Addition
        if Operation.DIV == operation:
            return Division
        if Operation.MUL == operation:
            return Multiplication
        if Operation.SUB == operation:
            return Subtraction
