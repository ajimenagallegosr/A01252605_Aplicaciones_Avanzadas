GlobalInt = {}        #1000 - 1099
GlobalFloat = {}      #2000 - 2099

LocalInt = {}         #3000 - 3099
LocalFloat = {}       #4000 - 4099

TempInt = {}          #5000 - 5099
TempFloat = {}        #6000 - 6099
TempBool = {}         #7000 - 7099

ConstantInt = {}      #8000 - 8099
ConstantFloat = {}    #9000 - 9099
ConstantString = {}   #10000 - 10099

QuadListMemory = []   # cuádruplos


segments = {
    "GlobalInt": GlobalInt,        
    "GlobalFloat": GlobalFloat,    
    "LocalInt": LocalInt,
    "LocalFloat": LocalFloat,
    "TempInt": TempInt,
    "TempFloat": TempFloat,
    "TempBool": TempBool,
    "ConstantInt": ConstantInt,
    "ConstantFloat": ConstantFloat,
    "ConstantString": ConstantString
}

counters = {
    "GlobalInt": 1000,
    "GlobalFloat": 2000,
    "LocalInt": 3000,
    "LocalFloat": 4000,
    "TempInt": 5000,
    "TempFloat": 6000,
    "TempBool": 7000,
    "ConstantInt": 8000,
    "ConstantFloat": 9000,
    "ConstantString": 10000
}

limits = {
    "GlobalInt": 1999,
    "GlobalFloat": 2999,
    "LocalInt": 3999,
    "LocalFloat": 4999,
    "TempInt": 5999,
    "TempFloat": 6999,
    "TempBool": 7999,
    "ConstantInt": 8999,
    "ConstantFloat": 9999,
    "ConstantString": 10999
}

def allocate(segment_name, key):
    # Get correct dict
    segment_dict = segments[segment_name]

    # Create address
    addr = counters[segment_name]

    # Verify memory
    if addr > limits[segment_name]:
        raise Exception(f"Error: memory full in {segment_name}")

    # Save in dict
    segment_dict[addr] = key  # save like this because you can have multiple ids

    # Move counter
    counters[segment_name] += 1

    return addr
