
class VirtualMachine:
    def __init__(self, quads):
        self.quads = quads
        self.program_counter = 0 # Count in what quad the virtual machine is going

        # Memory address
        self.global_add = {}
    
    def get_value(self, addr):
        if addr is None:
            return None

        if addr in self.global_add:
            return self.global_add.get(addr)
        else:
            raise Exception(f"Unknown address {addr}")
    
    def set_value(self, addr, value):
        self.global_add[addr] = value
    
    def run(self):
        while(self.program_counter < len(self.quads)):
            op = self.quads[self.program_counter][0]
            a1 = self.quads[self.program_counter][1]
            a2 = self.quads[self.program_counter][2]
            res = self.quads[self.program_counter][3]

            v1 = self.get_value(a1)
            v2 = self.get_value(a2)

            # assignation
            if(op == "="):
                value = self.get_value(a1)
                self.set_value(res, value)
            
            # arithmetic
            elif(op == "+"):
                self.set_value(res, v1+v2)
            
            elif(op == "-"):
                self.set_value(res, v1-v2)
            
            elif(op == "*"):
                self.set_value(res, v1*v2)
            
            elif(op == "/"):
                self.set_value(res, v1/v2)
            
            # comparison
            elif(op == ">"):
                self.set_value(res, v1 > v2)
            
            elif(op == "<"):
                self.set_value(res, v1 < v2)
            
            elif(op == "=="):
                self.set_value(res, v1 == v2)
            
            elif(op == "!="):
                self.set_value(res, v1 != v2)
            
            elif(op == "GOTO"):
                self.program_counter = res
                continue
            
            elif(op == "GOTOF"):
                if v1 == False:
                    self.program_counter = res
                    continue
            
            elif(op == "PRINT"):
                value = self.get_value(res)
                print(value)
            
            elif(op == "<="):
                self.set_value(res, v1 <= v2)
            
            elif(op == ">="):
                self.set_value(res, v1 >= v2)
            
            self.program_counter += 1