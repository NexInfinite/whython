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

    "var": "var",       to        "var": "let",
will change
    var x = 10          to        let x = 10

You cannot change the value to be a value with spaces, for example

"let this be" will not work but "let_this_be" will work!
"""

KEYWORDS_DICT = {
    "var": "😀",
    "and": "👌",
    "or": "🤏",
    "elif": "😑",
    "else": "🤬",
    "if": "❓",
    "not": "❌",
    "do": "⏩",
    "for": "🔁",
    "to": "👉",
    "step": "🦶",
    "while": "🤨",
    "func": "🥶",
    "end": "💀",
    "return": "👹",
    "continue": "😈",
    "break": "😱"
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
# changing the below to
# global_symbol_table.set("nill", Number.null)
# will make `nill` work instead of `null` in command line
global_symbol_table.set("null", Number.null)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("pi", Number.pi)

# changing the below to
# global_symbol_table.set("shout", BuiltInFunction("print"))
# will make shout("value") work instead of print("value")
# If you want an example of what each of this functions do go to values/value_builtinfunc.py and find the correct function.
global_symbol_table.set("📣", BuiltInFunction("print"))
global_symbol_table.set("💬", BuiltInFunction("input"))
global_symbol_table.set("🤓", BuiltInFunction("input_int"))
global_symbol_table.set("🔄", BuiltInFunction("clear"))
global_symbol_table.set("🤡", BuiltInFunction("exit"))
global_symbol_table.set("📲", BuiltInFunction("update_value"))
global_symbol_table.set("🔢", BuiltInFunction("is_num"))
global_symbol_table.set("🔠", BuiltInFunction("is_str"))
global_symbol_table.set("🔣", BuiltInFunction("is_list"))
global_symbol_table.set("🚚", BuiltInFunction("is_func"))
global_symbol_table.set("🔚", BuiltInFunction("append"))
global_symbol_table.set("🔝", BuiltInFunction("pop"))
global_symbol_table.set("🔛", BuiltInFunction("extend"))
global_symbol_table.set("😳", BuiltInFunction("run"))
global_symbol_table.set("📏", BuiltInFunction("len"))
global_symbol_table.set("🤑", BuiltInFunction("randint"))
global_symbol_table.set("👄", BuiltInFunction("to_str"))
global_symbol_table.set("👅", BuiltInFunction("to_int"))
global_symbol_table.set("🧠", BuiltInFunction("pyeval"))

# *###################
# * GRAMMAR RULES
# * YOU CAN EDIT THIS!
# *###################

# With this True you will need "var".
# With it False you can either use "var" or not.
GRAMMAR_USE_IDENTIFIER_FOR_ASSIGNMENT = True
# More coming soon....