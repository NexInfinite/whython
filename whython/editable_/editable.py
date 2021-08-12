# *###################
# * IMPORTS
# *###################

from symbol_table import SymbolTable

from values.value_builtinfunc import BuiltInFunction
from values.value_number import Number

# *###################
# * KEYWORDS
# * YOU CAN EDIT THIS!
# *###################

"""
How to use:

Change the value in the dict (right hand side) to the new value you want it to be.
For example changing

    `"var": "var",`     to      `"var": "let",`
will change
    var x = 10          to      let x = 10

You cannot change the value to be a value with spaces, for example

"let this be" will not work but "let_this_be" will work!
"""

KEYWORDS_DICT = {
    "var": "let",
    "and": "and",
    "or": "or",
    "elif": "elif",
    "else": "else",
    "if": "if",
    "not": "not",
    "do": "do",
    "for": "for",
    "to": "to",
    "step": "step",
    "while": "while",
    "func": "func",
    "end": "end",
    "return": "return",
    "continue": "continue",
    "break": "break",
}

# *###################
# * SYMBOL TABLE
# * YOU CAN EDIT THIS!
# *###################

"""
How to use:

Change the value in the first argument of .set()
For example:
    global_symbol_table.set("null", Number.null)
    ->
    global_symbol_table.set("nill", Number.null)

    This will change the value `null` to `nill` in the command line.
"""

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("pi", Number.pi)

global_symbol_table.set("shout", BuiltInFunction.print)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("input_int", BuiltInFunction.input_int)
global_symbol_table.set("clear", BuiltInFunction.clear)
global_symbol_table.set("exit", BuiltInFunction.exit)
global_symbol_table.set("update_value", BuiltInFunction.update_value)
global_symbol_table.set("is_num", BuiltInFunction.is_num)
global_symbol_table.set("is_str", BuiltInFunction.is_str)
global_symbol_table.set("is_list", BuiltInFunction.is_list)
global_symbol_table.set("is_func", BuiltInFunction.is_func)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("run", BuiltInFunction.run)
global_symbol_table.set("len", BuiltInFunction.len)
global_symbol_table.set("randint", BuiltInFunction.randint)
