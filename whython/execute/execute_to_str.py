# *###################
# * IMPORTS
# *###################

from values.value_string import String
from runtime_results import RTResult


# *###################
# * TO STRING
# *###################

def execute_to_str_func(self, exec_ctx):
    value = exec_ctx.symbol_table.get("value")
    return RTResult().success(String(str(value)))