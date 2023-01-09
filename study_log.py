class StudyLog:
    print_string = ''
    tab = False
    point = 0

    def given (self, obj: object):
        self.print_string += "\n\x1b[33m---Дано---\x1b[0m"
        for string in obj.keys():
            self.print_string += f'\n\x1b[32m {string}=\x1b[0m {obj[string]}'
        
    def answer (self, obj: object):
        self.print_string += "\n\x1b[35m---Відповідь---\x1b[0m"
        for string in obj.keys():
            self.print_string += f'\n\x1b[32m {string} =\x1b[0m {obj[string]}'
    
    def task (self, name: str or int):
        self.print_string += f"\n\x1b[33m---Завдання \x1b[36m'{name}'\x1b[0m"
        self.point = 1
        self.tab = True

    def end_task (self):
        self.point = 0
        self.tab = False

    def header (self, header: str or int):
        self.print_string += f"\n\x1b[33m---{header}---\x1b[0m"
        self.point = 0
        self.tab = False

    def add_point (self, *strings: list[str]):
        tab = self.tab and "    " or ''
        point = self.point > 0 and f'{self.point}.' or ''
        log_string = f'\n{tab}{point}'
        for string in strings:
            log_string += f' {string}'
        if(self.point > 0):
            self.point += 1
        self.print_string += log_string
    
    def print(self):
        print(self.print_string)

    def green(self, string: str):
        return f'\x1b[32m{string}\x1b[0m'

    def red(self, string: str):
        return f'\x1b[31m{string}\x1b[0m'

    def yellow(self, string: str):
        return f'\x1b[33m{string}\x1b[0m'
    
    def blue(self, string: str):
        return f'\x1b[34m{string}\x1b[0m'