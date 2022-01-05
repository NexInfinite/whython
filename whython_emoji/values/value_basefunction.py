# *###################
# * IMPORTS
# *###################

from values.value_values import Value
from values.value_number import Number

from context import Context
from symbol_table import SymbolTable
from runtime_results import RTResult
from errors import RTError

# *###################
# * BASE FUNCTION
# *###################

class BaseFunction(Value):
    def __init__(self, name):
        super().__init__()
        self.name = name or "<anonymous>"
        self.args = []
        self.arg_names = []

    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self):
        res = RTResult()

        for i in range(len(self.arg_names)):
            arg = self.arg_names[i]
            if "=" in arg:
                try:
                    _ = self.args[i]
                except:
                    try:
                        self.args.append(Number(int(arg.split("=")[-1])))
                    except:
                        self.args.append(arg.split("=")[-1])

        if len(self.args) > len(self.arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(self.args) - len(self.arg_names)} too many args passed into {self}",
                self.context
            ))

        if len(self.args) < len(self.arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(self.arg_names) - len(self.args)} too few args passed into {self}",
                self.context
            ))

        return res.success(None)

    def populate_args(self, exec_ctx):
        for i in range(len(self.args)):
            arg_name = self.arg_names[i]
            arg_value = self.args[i]
            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_name, arg_value)

    def check_and_populate_args(self, arg_names, args, exec_ctx):
        res = RTResult()
        self.arg_names = arg_names
        self.args = args
        res.register(self.check_args())
        if res.should_return(): return res
        self.populate_args(exec_ctx)
        return res.success(None)