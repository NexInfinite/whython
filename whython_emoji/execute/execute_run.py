# *###################
# * IMPORTS
# *###################

from values.value_string import String
from values.value_number import Number
from runtime_results import RTResult

from errors import RTError

# *###################
# * RUN
# *###################

def execute_run_func(self, exec_ctx):
    from run import run
    fn = exec_ctx.symbol_table.get("filename")

    if not isinstance(fn, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Argument must be a string",
            exec_ctx
        ))

    fn = fn.value

    try:
        if not fn.endswith(".whython"):
            fn += ".whython"
        with open(fn, "r") as f:
            script = f.read()
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Failed to load script '{fn}'\n{e}",
            exec_ctx
        ))

    _, error = run(fn, script)
    if error:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Failed to load script '{fn}'\n{error.as_string()}",
            exec_ctx
        ))

    return RTResult().success(Number.ignore)