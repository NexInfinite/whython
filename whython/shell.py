import run as whython

while True:
    text = input("whython > ")
    if text.strip() == "": continue
    result, error = whython.run("<stdin>", text)

    if error: print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            for element in result.elements:
                try:
                    if element.value is not None:
                        print(element)
                except AttributeError:
                    pass
        else:
            print(repr(result))