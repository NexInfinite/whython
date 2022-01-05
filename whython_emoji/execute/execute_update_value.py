# *###################
# * IMPORTS
# *###################

from values.value_number import Number
from values.value_list import List
from values.value_string import String

from runtime_results import RTResult
from errors import RTError


# *###################
# * UPDATE VALUE
# *###################

def execute_update_value_func(self, exec_ctx):
    list_ = exec_ctx.symbol_table.get("list")
    index_ = exec_ctx.symbol_table.get("index")
    value_ = exec_ctx.symbol_table.get("new_value")

    if not isinstance(list_, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "First argument must be a list",
            exec_ctx
        ))

    if not isinstance(index_, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Second argument must be a number",
            exec_ctx
        ))

    if not isinstance(value_, Number) or isinstance(value_, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Third argument must be a number or a string",
            exec_ctx
        ))

    try:
        list_.elements[index_.value] = value_.value
    except:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Could not change value of index '{index_.value}' as it is not in range of list.",
            exec_ctx
        ))

    return RTResult().success(Number.ignore)