from abc import ABC, abstractmethod


class CalcInterface(ABC):

    @classmethod
    @abstractmethod
    def exec_operation(cls, operand1: str, operand2: str, operation: enumerate) -> object:
        """
        Method to implement for operation.

        :param operand1:
            First operand of the operation
        :param operand2:
            Second operand of the operation
        :param operation:
            Operation to be performed
        :return:
            Result of the operation
        """
        pass
