"""
    Use for readable console messages

example:
    printer.push_context('moving', 'warning')
    printer.log('move first file')
result:
    [moving] move first file
context (text in brackets) is yellow, other text white (classic)
"""


class Printer:
    def __init__(self):
        pass

    def push_context(self):
        pass

    def log(self):
        pass

    def error(self):
        pass

    def warning(self):
        pass
