# *###################
# * IMPORTS
# *###################

import os

from values.value_number import Number
from runtime_results import RTResult

# *###################
# * PRINT
# *###################

def execute_clear_func(self, exec_ctx):
    os.system("cls" if os.name == "nt" else "clear")
    return RTResult().success(Number.null)