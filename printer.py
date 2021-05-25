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
    _COLORS_TYPES = {
        "error": 31,
        "success": 32,
        "warning": 33,
        "info1": 34,
        "info2": 35,
        "info3": 36,
        "default": 0
    }

    def __init__(self, sign=''):
        self.context_info = []
        self.sign = sign  # sign between contexts and text

    def push_context(self, text, color_type):
        color_code = self.get_color_code(color_type)
        self.context_info.append('\033[' + color_code + 'm[' + text + ']\033[0m')

    def pop_context(self):
        try:
            self.context_info.pop()
        except IndexError:
            self.error("You try to remove non-existent context!")

    def log(self, text, color_type="default", with_context=True):
        if with_context:
            print("".join(self.context_info) + self.sign + self.resolve_text_color(text, color_type))
        else:
            print(self.resolve_text_color(text, color_type))

    def error(self, text):
        self.log(text, "error")

    def warning(self, text):
        self.log(text, "warning")

    def info1(self, text):
        self.log(text, "info1")

    def info2(self, text):
        self.log(text, "info2")

    def info3(self, text):
        self.log(text, "info3")

    def success(self, text):
        self.log(text, "success")

    def default(self, text):
        self.log(text, "default")

    def get_color_code(self, color_type):
        try:
            return str(self._COLORS_TYPES[color_type])
        except KeyError:
            self.log("Color type '" + color_type + "' doesn't exist!", "error", with_context=False)
            return ''

    def resolve_text_color(self, text, color_type):
        color_code = self.get_color_code(color_type)
        if color_code != '':
            return '\033[' + color_code + 'm' + text + '\033[0m'
        else:
            return ''
