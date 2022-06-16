import run as whython
import os

def main():
    welcome()
    while True:
        try:
            text = input("ocr > ")
            if text.strip() == "": continue
            if text.strip() == "exit": print("Goodbye!"); return
            result, error = whython.run("<stdin>", text)

            if error: print(error.as_string())
            elif result:
                for element in result.elements:
                    try:
                        if element.value is not None:
                            print(element)
                    except AttributeError:
                        pass
        except KeyboardInterrupt:
            print("\nType 'Exit' to leave shell.")

def welcome():
    print("Welcome to whython v1.3")

    # Get info about saves
    editing_location = os.path.abspath("editable_/editable.py")
    print(f"Current save location for editing func/var names is: {editing_location}\n")

if __name__ == "__main__":
    main()
