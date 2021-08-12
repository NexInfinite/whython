import run as whython
from values.value_number import Number

while True:
    text = input("whython > ")
    if text.strip() == "": continue
    result, error = whython.run("<stdin>", text)

    if error: print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            if not isinstance(result.elements[0], Number) and result.elements[0] is None:
                print(result.elements[0])
        else:
            print(repr(result))