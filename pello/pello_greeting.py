def greeting():
    try:
        from blessings import Terminal
        term = Terminal()
        print(term.green + term.bold + "Hello World!" + term.normal)
    except ImportError:
        print("Hello World!")
