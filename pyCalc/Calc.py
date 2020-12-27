from pyCalc.CalcInterface import CalcInterface
from pyCalc.Operation import Operation
from pyCalc.OperationFactory import OperationFactory


class Calc(CalcInterface):

    @classmethod
    def exec_operation(cls, operand1, operand2, operation: Operation) -> object:
        return OperationFactory.getInstance(operation).execute(operand1, operand2)
