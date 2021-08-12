# *###################
# * IMPORTS
# *###################

from values.value_list import List
from values.value_number import Number
from runtime_results import RTResult

from errors import RTError

# *###################
# * APPEND
# *###################

def execute_append_func(self, exec_ctx):
    list_ = exec_ctx.symbol_table.get("list")
    value = exec_ctx.symbol_table.get("value")

    if not isinstance(list_, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "First argument must be a list",
            exec_ctx
        ))

    list_.elements.append(value)
    return RTResult().success(Number.null)