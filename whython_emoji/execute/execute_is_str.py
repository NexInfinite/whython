# *###################
# * IMPORTS
# *###################

from values.value_string import String
from values.value_number import Number
from runtime_results import RTResult


# *###################
# * IS STRING
# *###################

def execute_is_str_func(self, exec_ctx):
    is_str = isinstance(exec_ctx.symbol_table.get("value"), String)
    return RTResult().success(Number.true if is_str else Number.false)