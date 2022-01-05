# *###################
# * IMPORTS
# *###################

from values.value_number import Number
from runtime_results import RTResult


# *###################
# * IS NUMBER
# *###################

def execute_is_num_func(self, exec_ctx):
    is_num = isinstance(exec_ctx.symbol_table.get("value"), Number)
    return RTResult().success(Number.true if is_num else Number.false)