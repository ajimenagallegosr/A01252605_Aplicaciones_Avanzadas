import Memory as memory

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
        ('int', 'float'): 'error'  # ('int','float') no permitido, error semántico
    },
    '>=': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool'
    },
    '<=': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool'
    },
}

class VarTable:
    def __init__(self, name):
        self.table = {}
        self.name = name

    def add(self, var_name, var_type, address):
        if var_name in self.table:
            raise Exception(f"ERROR: Variable '{var_name}' it's already declared.")
        self.table[var_name] = {
            'type': var_type,
            'address': address
        }

    def get_type(self, var_name):
        # Search
        if var_name not in self.table:
            raise Exception(f"ERROR: Variable '{var_name}' it's not declared.")
        return self.table[var_name]['type']


class FunctionDirectory:
    def __init__(self):
        self.directory = {}  # { func_name : info }

    def add_function(self, name, type, startLine, params):
        self.directory[name] = {
            'type': type,
            'vars': VarTable(name),
            'startLine': startLine,
            'params': params, #int, float, 
        }

    def add_var(self, func_name, var_name, var_type):
        prog_name = list(self.directory.keys())[0]

        if func_name == prog_name and var_type == 'int':  # Global int
            addr = memory.allocate("GlobalInt", var_name)
        elif func_name == prog_name and var_type == 'float':  # Global float
            addr = memory.allocate("GlobalFloat", var_name)
        elif var_type == 'int':  # Local int
            addr = memory.allocate("LocalInt", var_name)
        else:
            addr = memory.allocate("LocalFloat", var_name)

        self.directory[func_name]['vars'].add(var_name, var_type, addr)

    def get_var_type(self, func_name, var_name):
        try:
            return self.directory[func_name]['vars'].get_type(var_name)
        except:
            pass

        # global vars
        global_vars_scope = list(self.directory.keys())[0]
        return self.directory[global_vars_scope]['vars'].get_type(var_name)

    def get_address(self, func_name, var_name):
        # 1. search locally
        try:
            return self.directory[func_name]['vars'].table[var_name]['address']
        except KeyError:
            pass

        # 2. search globally
        global_scope = list(self.directory.keys())[0]
        try:
            return self.directory[global_scope]['vars'].table[var_name]['address']
        except KeyError:
            pass

        # 3. try temps
        if get_key(var_name, memory.TempInt) != None:
            return get_key(var_name, memory.TempInt)
        if get_key(var_name, memory.TempFloat) != None:
            return get_key(var_name, memory.TempFloat)
        if get_key(var_name, memory.TempBool) != None:
            return get_key(var_name, memory.TempBool)

        # 4. try constants
        if isinstance(var_name, int):
            if get_key(var_name, memory.ConstantInt) != None:
                return get_key(var_name, memory.ConstantInt)
            else:
                return memory.allocate('ConstantInt', var_name)

        if isinstance(var_name, float):
            if get_key(var_name, memory.ConstantFloat) != None:
                return get_key(var_name, memory.ConstantFloat)
            else:
                return memory.allocate('ConstantFloat', var_name)

        if isinstance(var_name, str):
            if get_key(var_name, memory.ConstantString) != None:
                return get_key(var_name, memory.ConstantString)
            else:
                return memory.allocate('ConstantString', var_name)


func_dir = FunctionDirectory()
current_function = 'global'
current_type = None

temp_ids = [] # variables locales
parameter_check = 0
call_function = None
call_stack = []

PilaO = []  # operandos, a, b, c, 1, 2
PilaT = []  # tipos, int, float, etc
PilaOper = []  # operadores, +, -, *, etc

QuadList = [["GOTO", None, None, None]]  # cuádruplos
QuadListMemory = [["GOTO", None, None, None]]  # quads memory

PilaGoTo = []

temp_counter = 0

def new_temp():
    global temp_counter
    name = f"t{temp_counter}"
    temp_counter += 1
    return name

def generate_quad(op, l, r, res):
    addr_l = func_dir.get_address(current_function, l)
    addr_r = func_dir.get_address(current_function, r)
    addr_res = func_dir.get_address(current_function, res)

    QuadList.append([op, l, r, res])
    QuadListMemory.append([op, addr_l, addr_r, addr_res])

    print(f"Cuádruplo generado: {[op, l, r, res]}")

def print_quads():
    print("\nCUADRUPLOS FINALES")
    for i, q in enumerate(QuadList):
        print(f"{i}: {q}")

    print("\nCUADRUPLOS FINALES memorias")
    for i, q in enumerate(QuadListMemory):
        print(f"{i}: {q}")

def get_key(value, dic):
    for k, v in dic.items():
        if v == value:
            return k
    return None
