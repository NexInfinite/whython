# *###################
# * IMPORTS
# *###################

from values.value_string import String
from values.value_number import Number
from runtime_results import RTResult
from errors import RTError


# *###################
# * TO INTEGER
# *###################

def execute_to_int_func(self, exec_ctx):
    value = exec_ctx.symbol_table.get("value")

    if not isinstance(value, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"The first argument must be a string.",
            exec_ctx
        ))

    return RTResult().success(Number(int(value.value)))