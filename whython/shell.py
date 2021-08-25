import run as whython

def main():
    while True:
        text = input("whython > ")
        if text.strip() == "": continue
        result, error = whython.run("<stdin>", text)

        if error: print(error.as_string())
        elif result:
            for element in result.elements:
                try:
                    if element.value is not None:
                        print(element)
                except AttributeError:
                    pass

if __name__ == "__main__":
    main()