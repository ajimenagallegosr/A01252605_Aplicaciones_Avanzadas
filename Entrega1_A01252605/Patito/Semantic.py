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
        ('int', 'float') : 'error'
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

        prog_name = list(self.directory.keys())[0]

        if func_name == prog_name:
            #GLOBAL
            addr = memory.allocate_global(var_type)
            if var_type == 'int':
                memory.GlobalInt[var_name] = addr
            else:
                memory.GlobalFloat[var_name] = addr
        else:
            addr = memory.allocate_local(var_type)
            if var_type == "int":
                memory.LocalInt[var_name] = addr
            else:
                memory.LocalFloat[var_name] = addr


    def get_var_type(self, func_name, var_name):
        try:
            return self.directory[func_name]['vars'].get_type(var_name)
        except:
            pass

        program_scope = list(self.directory.keys())[0]  # usualmente el nombre del programa
        return self.directory[program_scope]['vars'].get_type(var_name)


func_dir = FunctionDirectory()
current_function = 'global'
current_type = None

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

    l_addr = get_address(l, current_function) if l is not None else None
    r_addr = get_address(r, current_function) if r is not None else None
    res_addr = get_address(res, current_function) if res is not None else None

    memory.QuadListMemory.append([op, l_addr, r_addr, res_addr])
    print(f"[MEMORY QUAD] {memory.QuadListMemory[-1]}")


def print_quads():
    print("\nCUADRUPLOS FINALES")
    for i, q in enumerate(QuadList):
        print(f"{i}: {q}")

    print("\nCUADRUPLOS FINALES DOS")
    for i, q in enumerate(memory.QuadListMemory):
        print(f"{i}: {q}")

def generate_quad_memory(op, l, r, res):
    memory.QuadListMemory.append([op, l, r, res])
    print(f"[MEMORY QUAD] {memory.QuadListMemory[-1]}")

def get_address(operand, func_name):
    #if isinstance(operand, int) or isinstance(operand, float):
     #   return operand
    
    if isinstance(operand, int) or isinstance(operand, float):
        return memory.allocate_cons(operand)
    
    elif isinstance(operand, str):
        print("AQUIIIII", operand)

    prog_name = list(func_dir.directory.keys())[0]

    if func_name != prog_name and func_name is not None:
        #Local
        if operand in memory.LocalInt:
            return memory.LocalInt[operand]
        if operand in memory.LocalFloat:
            return memory.LocalFloat[operand]
    #Global
    if operand in memory.GlobalInt:
        return memory.GlobalInt[operand]
    if operand in memory.GlobalFloat:
        return memory.GlobalFloat[operand]
    
    # Temporales
    if operand in memory.TempInt:
        return memory.TempInt[operand]
    if operand in memory.TempFloat:
        return memory.TempFloat[operand]
    if operand in memory.TempBool:
        return memory.TempBool[operand]
    
    elif isinstance(operand, str):
        return memory.allocate_cons(operand)

    
    return operand
