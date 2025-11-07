semantic_cube = {
    '+': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float'
    },
    '-': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float'
    },
    '*': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float'
    },
    '/': {
        ('int', 'int'): 'float',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float'
    },
    '>': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'int',
        ('float', 'int'): 'int',
        ('float', 'float'): 'int'
    },
    '<': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'int',
        ('float', 'int'): 'int',
        ('float', 'float'): 'int'
    },
    '!=': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'int',
        ('float', 'int'): 'int',
        ('float', 'float'): 'int'
    },
    '==': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'int',
        ('float', 'int'): 'int',
        ('float', 'float'): 'int'
    },
    '=': {
        ('int', 'int'): 'int',
        ('float', 'float'): 'float',
        ('float', 'int'): 'float'
        # ('int','float') no permitido, error semántico
    }
}

class VarTable:
    def __init__(self):
        self.table = {}  # { id : {type} }

    def add(self, name, type):
        if name in self.table:
            raise Exception(f"ERROR: Variable '{name}' ya está declarada.")
        self.table[name] = { 'type': type }

    def get_type(self, name):
        if name not in self.table:
            raise Exception(f"ERROR: Variable '{name}' no declarada.")
        return self.table[name]['type']
    
class FunctionDirectory:
    def __init__(self):
        self.directory = {}  # { func_name : info }

    def add_function(self, name, type):
        if name in self.directory:
            raise Exception(f"ERROR: La función '{name}' ya está declarada.")
        self.directory[name] = {
            'type': type,
            'vars': VarTable()
        }

    def add_var(self, func_name, var_name, var_type):
        self.directory[func_name]['vars'].add(var_name, var_type)

    def get_var_type(self, func_name, var_name):
        return self.directory[func_name]['vars'].get_type(var_name)

func_dir = FunctionDirectory()
current_function = 'global'