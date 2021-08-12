# *###################
# * IMPORTS
# *###################

from values.value_basefunction import BaseFunction

from execute.execute_randint import execute_randint_func
from execute.execute_print import execute_print_func
from execute.execute_input import execute_input_func
from execute.execute_input_int import execute_input_int_func
from execute.execute_clear import execute_clear_func
from execute.execute_exit import execute_exit_func
from execute.execute_update_value import execute_update_value_func
from execute.execute_is_num import execute_is_num_func
from execute.execute_is_str import execute_is_str_func
from execute.execute_is_list import execute_is_list_func
from execute.execute_is_func import execute_is_func_func
from execute.execute_append import execute_append_func
from execute.execute_pop import execute_pop_func
from execute.execute_extend import execute_extend_func
from execute.execute_len import execute_len_func
from execute.execute_run import execute_run_func

from runtime_results import RTResult

# *###################
# * BUILTIN FUNCTION
# *###################

class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)

    def execute(self, args):
        res = RTResult()
        exec_ctx = self.generate_new_context()

        method_name = f"execute_{self.name}"
        method = getattr(self, method_name, self.no_visit_method)

        res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
        if res.should_return(): return res

        return_value = res.register(method(exec_ctx))
        if res.should_return(): return res
        return res.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f"No execute_{self.name} method defined!")

    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<built-in function {self.name}>"

    # *###################

    def execute_print(self, exec_ctx):
        """
        Print a value on the screen
        Example:
            print("Hello, world!")
        :arg value: value to be printed
        :return: exec_ctx
        """
        return execute_print_func(self, exec_ctx)
    execute_print.arg_names = ["value"]

    def execute_input(self, exec_ctx):
        """
        Get input of user
        Example:
            var name = input("What is your name? ")
        :arg prompt: prompt for input (optional)
        :return: the value of the input
        """
        return execute_input_func(self, exec_ctx)
    execute_input.arg_names = ["prompt=0"]

    def execute_input_int(self, exec_ctx):
        """
        Get int version of input from user, input must be an int
        Example:
            var number = input_int("Pick a number: ")
        :arg prompt: prompt for input (optional)
        :return: the value of the input
        """
        return execute_input_int_func(self, exec_ctx)
    execute_input_int.arg_names = ["prompt=0"]

    def execute_clear(self, exec_ctx):
        """
        Clear the screen, this will only work in a terminal. If you are
        using pycharm it will not clear the screen.
        Example:
            clear()
        """
        return execute_clear_func(self, exec_ctx)
    execute_clear.arg_names = []

    def execute_exit(self, exec_ctx):
        """
        Exit out of the terminal. You can use ctrl + c or this command.
        Example:
            exit()
        """
        return execute_exit_func(self, exec_ctx)
    execute_exit.arg_names = []

    def execute_update_value(self, exec_ctx):
        """
        Change the value of a list at a position
        Example:
            var list = [1, 2, 3]
            change_value(list, 1, 4)
            print(list) -> [1, 4, 3]
        :arg list: The list you want to change
        :arg index: The index of the value you want to change
        :arg new_value: The value you want to change the element to
        """
        return execute_update_value_func(self, exec_ctx)
    execute_update_value.arg_names = ["list", "index", "new_value"]

    def execute_is_num(self, exec_ctx):
        """
        Takes in value and checks if it is a number
        Example:
            var number = 12
            print(is_num(number)) -> 1
        :arg value:
        :return: 1 (true) or 0 (false)
        """
        return execute_is_num_func(self, exec_ctx)
    execute_is_num.arg_names = ["value"]

    def execute_is_str(self, exec_ctx):
        """
        Takes in value and checks if it is a string
        Example:
            var string = "hello!"
            print(is_str(string)) -> 1
        :arg value:
        :return: 1 (true) or 0 (false)
        """
        return execute_is_str_func(self, exec_ctx)
    execute_is_str.arg_names = ["value"]

    def execute_is_list(self, exec_ctx):
        """
        Takes in value and checks if it is a list
        Example:
            var list = [1, 2, 3]
            print(is_list(list)) -> 1
        :arg value:
        :return: 1 (true) or 0 (false)
        """
        return execute_is_list_func(self, exec_ctx)
    execute_is_list.arg_names = ["value"]

    def execute_is_func(self, exec_ctx):
        """
        Takes in value and checks if it is a function
        Example:
            var function = func hello() -> print("hello")
            print(is_func(function)) -> 1
        :arg value:
        :return: 1 (true) or 0 (false)
        """
        return execute_is_func_func(self, exec_ctx)
    execute_is_func.arg_names = ["value"]

    def execute_append(self, exec_ctx):
        """
        Takes in list and value, appends the value to
        the end of the list if the list is a valid List.
        Example:
            var list = [1, 2, 3]
            append(list, 4)
            print(list) -> 1, 2, 3, 4
        :arg list: The list you want to append the value to.
        :arg value: The value you are appending to the end of the list.
        """
        return execute_append_func(self, exec_ctx)
    execute_append.arg_names = ["list", "value"]

    def execute_pop(self, exec_ctx):
        """
        Removes and returns the value in the index given.
        Example:
            var list = [1, 2, 3]
            var popped = pop(list, 1)
            print(popped) -> 2
            print(list) -> 1, 3
        :arg list: The list you want to pop the value from
        :arg index: The position of the value you want to pop
        :return: The number popped
        """
        return execute_pop_func(self, exec_ctx)
    execute_pop.arg_names = ["list", "index"]

    def execute_extend(self, exec_ctx):
        """
        Add 2 lists together
        Example:
            var list_a = [1, 2, 3]
            var list_b = [4, 5, 6]
            extend(list_a, list_b)
            print(list_a) -> 1, 2, 3, 4, 5, 6
            print(list_b) -> 4, 5, 6
        :arg list_a: The list you want to be extended
        :arg list_b: The list you want to add onto list_a
        """
        return execute_extend_func(self, exec_ctx)
    execute_extend.arg_names = ["list_a", "list_b"]

    def execute_len(self, exec_ctx):
        """
        Get the length of a list of a string.
        Example 1:
            var list = [1, 2, 3]
            print(len(list)) -> 3

        Example 2:
            var string = "hello"
            print(len(string)) -> 5
        :param item: The item you want to get the length of
        :return: The length of the item.
        """
        return execute_len_func(self, exec_ctx)
    execute_len.arg_names = ["item"]

    def execute_run(self, exec_ctx):
        """
        Run an external script. The script must end
        in ".whython" but you dont need to add it
        to the run command. The position is relative to
        where the file "run" is located.
        Example 1:
            # Using the file hello_world.whython in examples
            run("examples/hello_world.whython")
            -> Hello, World!
        Example 2:
            # Using the file guesser.whython in examples
            run("examples/guesser") # Notice how you don't need .whython
            -> Hello, World!
        :arg filename: The filename if the file you want to run
        :return: The output from running that file.
        """
        return execute_run_func(self, exec_ctx)
    execute_run.arg_names = ["filename"]

    def execute_randint(self, exec_ctx):
        """
        Get a random number from the range given using
        pythons random function.
        Example:
            var random_number = randint(0, 10)
            print(random_number) -> 5
        :arg from: The lowest number possible
        :arg to: The highest number possible
        :return: The number chosen in the range
        """
        return execute_randint_func(self, exec_ctx)
    execute_randint.arg_names = ["from", "to"]

BuiltInFunction.print           = BuiltInFunction("print")
BuiltInFunction.print_ret       = BuiltInFunction("print_ret")
BuiltInFunction.input           = BuiltInFunction("input")
BuiltInFunction.input_int       = BuiltInFunction("input_int")
BuiltInFunction.clear           = BuiltInFunction("clear")
BuiltInFunction.exit            = BuiltInFunction("exit")
BuiltInFunction.update_value    = BuiltInFunction("update_value")
BuiltInFunction.is_num          = BuiltInFunction("is_num")
BuiltInFunction.is_str          = BuiltInFunction("is_str")
BuiltInFunction.is_list         = BuiltInFunction("is_list")
BuiltInFunction.is_func         = BuiltInFunction("is_func")
BuiltInFunction.append          = BuiltInFunction("append")
BuiltInFunction.pop             = BuiltInFunction("pop")
BuiltInFunction.extend          = BuiltInFunction("extend")
BuiltInFunction.run             = BuiltInFunction("run")
BuiltInFunction.len             = BuiltInFunction("len")
BuiltInFunction.randint         = BuiltInFunction("randint")