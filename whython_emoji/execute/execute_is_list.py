# *###################
# * IMPORTS
# *###################

from values.value_list import List
from values.value_number import Number
from runtime_results import RTResult


# *###################
# * IS LIST
# *###################

def execute_is_list_func(self, exec_ctx):
    is_list = isinstance(exec_ctx.symbol_table.get("value"), List)
    return RTResult().success(Number.true if is_list else Number.false)