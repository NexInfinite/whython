# *###################
# * IMPORTS
# *###################

from values.value_list import List
from values.value_string import String
from values.value_number import Number
from runtime_results import RTResult

from errors import RTError

# *###################
# * LENGTH
# *###################

def execute_len_func(self, exec_ctx):
    item_ = exec_ctx.symbol_table.get("item")

    if isinstance(item_, List):
        return RTResult().success(Number(len(item_.elements)))
    elif isinstance(item_, String):
        return RTResult().success(Number(len(str(item_.value))))
    else:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Them item was not a list of a string",
            exec_ctx
        ))
