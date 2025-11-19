GlobalInt = {}       #1000 - 1099
GlobalFloat = {}     #2000 - 2099
LocalInt = {}        #3000 - 3099
LocalFloat = {}      #4000 - 4099
TempInt = {}         #5000 - 5099
TempFloat = {}       #6000 - 6099
TempBool = {}        #7000 - 7099
ConstantInt = {}     #8000 - 8099
ConstantFloat = {}   #9000 - 9099
ConstantString = {}  #10000 - 10099
QuadListMemory = []    # cuádruplos

counters = {
    "global_int": 1000,
    "global_float": 2000,
    "local_int": 3000,
    "local_float": 4000,
    "temp_int": 5000,
    "temp_float": 6000,
    "temp_bool": 7000,
    "const_int": 8000,
    "const_float": 9000,
    "const_string": 10000
}

MemoryTables = {
    "global_int": GlobalInt, #ya
    "global_float": GlobalFloat, #ya
    "local_int": LocalInt,
    "local_float": LocalFloat,
    "temp_int": TempInt,
    "temp_float": TempFloat,
    "temp_bool": TempBool,
    "const_int": ConstantInt,
    "const_float": ConstantFloat,
    "const_string": ConstantString
}

def allocate_global(var_type):
    if var_type == 'int':
        addr = counters['global_int']
        counters['global_int'] += 1
        return addr
    elif var_type == 'float':
        addr = counters['global_float']
        counters["global_float"] += 1
        return addr

def allocate_local(var_type):
    if var_type == 'int':
        addr = counters['local_int']
        counters['local_int'] += 1
        return addr
    elif var_type == 'float':
        addr = counters['local_float']
        counters["local_float"] += 1
        return addr

def allocate_temporal(var_type):
    if var_type == 'int':
        addr = counters['temp_int']
        counters['temp_int'] += 1
        return addr
    elif var_type == 'float':
        addr = counters['temp_float']
        counters["temp_float"] += 1
        return addr
    elif var_type == 'bool':
        addr = counters['temp_bool']
        counters["temp_bool"] += 1
        return addr

def allocate_cons(value):
    if isinstance(value, int):
        if value not in ConstantInt:
            addr = counters['const_int']
            counters['const_int'] += 1
            ConstantInt[value] = addr
        return ConstantInt[value]
    
    elif isinstance(value, float):
        if value not in ConstantFloat:
            addr = counters['const_float']
            counters['const_float'] += 1
            ConstantFloat[value] = addr
        return ConstantFloat[value]
    
    elif isinstance(value, str):
        if value not in ConstantString:
            addr = counters['const_string']
            counters['const_string'] += 1
            ConstantString[value] = addr
        return ConstantString[value]