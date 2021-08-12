# *###################
# * IMPORTS
# *###################

from values.value_values import Value
from values.value_number import Number

from errors import RTError

# *###################
# * STRING
# *###################

class List(Value):
    """
    List class
    Examples:
        --------------------------
        Using "+" will append to the list

        var list = [1, 2, 3]
        list + 4 -> [1, 2, 3, 4]
        --------------------------
        Using "-" will pop from the list at index

        var list = [1, 2, 3]
        var popped = list - 1 -> [1, 3]
        popped: 2
        --------------------------
        Using "*" will extend 2 lists

        var list_a = [1, 2, 3]
        var list_b = [4, 5, 6]

        list_a*list_b -> [1, 2, 3, 4, 5, 6]
        list_a -> [1, 2, 3, 4, 5, 6]
        --------------------------
        Using "/" will get the item at that index

        var list = [1, 2, 3]
        list/1 -> 2
    """
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def added_to(self, other):
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def multiplied_by(self, other):
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, Value.illegal_operation(self, other)

    def subtracted_by(self, other):
        if isinstance(other, Number):
            new_list = self.copy()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Element at this index could not be removed from list because index is out of bounds',
                    self.context
                )
        else:
            return None, Value.illegal_operation(self, other)

    def divided_by(self, other):
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Element at this index could not be retrieved from list because index is out of bounds',
                    self.context
                )
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        copy = List(self.elements)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __str__(self):
        return f"{', '.join([str(x) for x in self.elements])}"

    def __repr__(self):
        return f"[{', '.join([str(x) for x in self.elements])}]"