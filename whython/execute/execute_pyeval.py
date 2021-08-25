# *###################
# * IMPORTS
# *###################

from values.value_string import String
from runtime_results import RTResult
from errors import RTError


# *###################
# * PYTHON EVAL
# *###################

def execute_pyeval_func(self, exec_ctx):
    code = exec_ctx.symbol_table.get("code")
    try:
        # code = compile(code.value, "script", "exec")
        try:
            response = eval(code.value)
        except:
            response = exec(code.value)
        return RTResult().success(String(response))
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"The code could not be evaluated. \n\n{e}",
            exec_ctx
        ))
