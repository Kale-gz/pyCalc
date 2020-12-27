from enum import Enum


class Operation(Enum):
    ADD = "+"
    SUB = "-"
    DIV = "/"
    MUL = "*"

    def __str__(self):
        return f"Operation {self.name} = {self.value}"

    @staticmethod
    def convert(value: str):
        for x in Operation:
            print(x)
            if value == x.value:
                print("Found!")
                return x
        return None
