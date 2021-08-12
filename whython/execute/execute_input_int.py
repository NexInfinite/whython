# *###################
# * IMPORTS
# *###################

from values.value_number import Number
from values.value_string import String

from runtime_results import RTResult

# *###################
# * PRINT
# *###################

def execute_input_int_func(self, exec_ctx):
    prompt = exec_ctx.symbol_table.get("prompt=0")
    while True:
        if isinstance(prompt, String):
            text_input = input(prompt)
        else:
            text_input = input()
        try:
            text_int = int(text_input)
            break
        except ValueError:
            print(f"'{text_input}' is not an integer. Try again!")
    return RTResult().success(Number(text_int))