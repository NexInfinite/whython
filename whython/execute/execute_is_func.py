# *###################
# * IMPORTS
# *###################

from values.value_function import Function
from values.value_number import Number
from runtime_results import RTResult


# *###################
# * IS FUNCTION
# *###################

def execute_is_func_func(self, exec_ctx):
    is_function = isinstance(exec_ctx.symbol_table.get("value"), Function)
    return RTResult().success(Number.true if is_function else Number.false)