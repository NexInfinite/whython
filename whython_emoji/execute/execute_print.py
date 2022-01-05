# *###################
# * IMPORTS
# *###################

from values.value_number import Number

from runtime_results import RTResult

# *###################
# * PRINT
# *###################

def execute_print_func(self, exec_ctx):
    print(str(exec_ctx.symbol_table.get("value")))
    return RTResult().success(Number.ignore)