# *###################
# * IMPORTS
# *###################

from values.value_string import String

from runtime_results import RTResult

# *###################
# * PRINT
# *###################

def execute_input_func(self, exec_ctx):
    prompt = exec_ctx.symbol_table.get("prompt=0")
    if isinstance(prompt, String):
        text_input = input(prompt)
    else:
        text_input = input()
    return RTResult().success(String(text_input))