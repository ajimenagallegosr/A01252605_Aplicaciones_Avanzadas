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
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool'
    },
    '<': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool'
    },
    '!=': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool'
    },
    '==': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool'
    },
    '=': {
        ('int', 'int'): 'int',
        ('float', 'float'): 'float',
        ('float', 'int'): 'float',
        ('int', 'float') : 'error'
        # ('int','float') no permitido, error semántico
    }
}

class VarTable:
    def __init__(self, name):
        self.table = {} 
        self.name = name

    def add(self, var_name, var_type):
        if var_name in self.table:
            raise Exception(f"ERROR: Variable '{var_name}' it's already declared.")
        self.table[var_name] = { 'type': var_type }

    def get_type(self, var_name): # Search
        if var_name not in self.table:
            raise Exception(f"ERROR: Variable '{var_name}' it's not declared.")
        return self.table[var_name]['type']

class FunctionDirectory:
    def __init__(self):
        self.directory = {}  # { func_name : info }

    def add_function(self, name, type):
        if name in self.directory:
            raise Exception(f"ERROR: The function '{name}' it's already declared.")
        self.directory[name] = {
            'type': type,
            'vars': VarTable(name)
        }

    def add_var(self, func_name, var_name, var_type):
        self.directory[func_name]['vars'].add(var_name, var_type)


    def get_var_type(self, func_name, var_name):
        return self.directory[func_name]['vars'].get_type(var_name)

func_dir = FunctionDirectory()
current_function = 'global'
current_type = None
temp_ids = []

PilaO = []       # operandos, a, b, c, 1, 2
PilaT = []       # tipos, int, float, etc
PilaOper = []    # operadores, +, -, *, etc
QuadList = []    # cuádruplos
PilaGoTo = []
temp_counter = 0

def new_temp():
    global temp_counter
    name = f"t{temp_counter}"
    temp_counter += 1
    return name

def generate_quad(op, l, r, res):
    QuadList.append([op, l, r, res])
    print(f"Cuádruplo generado: {[op, l, r, res]}")

def print_quads():
    print("\nCUADRUPLOS FINALES")
    for i, q in enumerate(QuadList):
        print(f"{i}: {q}")