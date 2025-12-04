class Addresses:
    def __init__(self):
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


class VirtualMachine:
    def __init__(self, quads):
        self.quads = quads
        self.program_counter = 0  # Count in what quad the virtual machine is going
        self.return_value = None  # Memory address
        self.globalMemory = Addresses() #1000 - 2099 + 8000 - 10099
        self.localMemory = Addresses()  #3000 - 7099
        # For funcs
        self.frame_stack = []  # para recursion
        self.pending_frames = []  # frame actual?

    def get_value(self, addr):
        if addr is None:
            return None
        if 1000 <= addr <= 2099 or 8000 <= addr <= 10099:
            try:
                return self.globalMemory.get_value(addr=addr)
            except:
                raise Exception(f"Unknown address {addr}")
        else:
            try:
                return self.localMemory.get_value(addr=addr)
            except:
                raise Exception(f"Unknown address {addr}")

    def set_value(self, addr, value):
        if 1000 <= addr <= 2099 or 8000 <= addr <= 10099:
            self.globalMemory.set_value(addr=addr, value=value)
        else:
            self.localMemory.set_value(addr=addr, value=value)

    def run(self):
        while(self.program_counter < len(self.quads)):
            op = self.quads[self.program_counter][0]
            a1 = self.quads[self.program_counter][1]
            a2 = self.quads[self.program_counter][2]
            res = self.quads[self.program_counter][3]

            if op in ["+", "-", "*", "/", "<", ">", "==", "!=", "GOTOF"]:
                v1 = self.get_value(a1)
                v2 = self.get_value(a2)
            elif op == "PARAMETER":
                v1 = self.get_value(a1)
                v2 = None
            else:
                v1 = a1
                v2 = a2

            # assignation
            if op == "=":
                if isinstance(a1, str):
                    self.set_value(res, self.return_value)
                    self.return_value = None
                else:
                    value = self.get_value(a1)
                    self.set_value(res, value)
                    #print(res, "=", value)

            # arithmetic
            elif(op == "+"):
                self.set_value(res, v1 + v2)
            elif(op == "-"):
                self.set_value(res, v1 - v2)
            elif(op == "*"):
                self.set_value(res, v1 * v2)
            elif(op == "/"):
                self.set_value(res, v1 / v2)

            # comparison
            elif(op == ">"):
                self.set_value(res, v1 > v2)
            elif(op == "<"):
                self.set_value(res, v1 < v2)
            elif(op == "=="):
                self.set_value(res, v1 == v2)
            elif(op == "!="):
                self.set_value(res, v1 != v2)

            # Flows
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

            # Functions
            elif(op == "ERA"):
                # Crear un nuevo frame pendiente para esta llamada
                self.pending_frames.append(Addresses())

            elif(op == "PARAMETER"):
                # Usar SIEMPRE el último ERA (la función más interna)
                self.pending_frames[-1].set_value(res, v1)


            elif(op == "GOSUB"):
                # Guardar el frame actual y el siguiente quad de retorno
                self.frame_stack.append((self.localMemory, self.program_counter + 1))

                # Cambiar al frame pendiente de la función que se está llamando
                self.localMemory = self.pending_frames.pop()

                self.program_counter = res
                continue


            elif(op == "RETURN"):
                self.return_value = self.get_value(a1)
                self.program_counter += 1
                continue

            elif(op == "ENDFUNC"):
                if self.frame_stack:
                    self.localMemory, ret_addr = self.frame_stack.pop()
                    self.program_counter = ret_addr
                    continue
                else:
                    self.localMemory = Addresses()
                    self.program_counter += 1
                    continue
            elif(op == "ENDPROGRAM"):
                break

            self.program_counter += 1
