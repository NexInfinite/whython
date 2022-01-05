# *###################
# * IMPORTS
# *###################

from values.value_number import Number

from runtime_results import RTResult
from errors import RTError


# *###################
# * RANDINT
# *###################

def execute_randint_func(self, exec_ctx):
    import random
    from_ = exec_ctx.symbol_table.get("from")
    to_ = exec_ctx.symbol_table.get("to")

    if not isinstance(from_, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "First argument must be a number",
            exec_ctx
        ))

    if not isinstance(to_, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Second argument must be a number",
            exec_ctx
        ))

    try:
        random_num = random.randint(from_.value, to_.value)
        return RTResult().success(Number(random_num))
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Error generating number\n{e}",
            exec_ctx
        ))