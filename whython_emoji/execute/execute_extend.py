# *###################
# * IMPORTS
# *###################

from values.value_list import List
from values.value_number import Number
from runtime_results import RTResult

from errors import RTError

# *###################
# * EXTEND
# *###################

def execute_extend_func(self, exec_ctx):
    list_a = exec_ctx.symbol_table.get("list_a")
    list_b = exec_ctx.symbol_table.get("list_b")

    if not isinstance(list_a, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "First argument must be a list",
            exec_ctx
        ))

    if not isinstance(list_b, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Second argument must be a list",
            exec_ctx
        ))

    list_a.elements.extend(list_b.elements)
    return RTResult().success(Number.null)