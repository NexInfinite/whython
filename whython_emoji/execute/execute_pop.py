# *###################
# * IMPORTS
# *###################

from values.value_list import List
from values.value_number import Number
from runtime_results import RTResult

from errors import RTError

# *###################
# * POP
# *###################

def execute_pop_func(self, exec_ctx):
    list_ = exec_ctx.symbol_table.get("list")
    index = exec_ctx.symbol_table.get("index")

    if not isinstance(list_, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "First argument must be a list",
            exec_ctx
        ))

    if not isinstance(index, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Second argument must be an integer",
            exec_ctx
        ))

    try:
        element = list_.elements.pop(index.value)
    except IndexError:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Element at index '{index.value}' could not be removed as it is out of range of the list.",
            exec_ctx
        ))
    return RTResult().success(element)