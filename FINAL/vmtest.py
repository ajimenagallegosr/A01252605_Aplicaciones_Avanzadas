from VirtualMachine import VirtualMachine
import json

with open("output.json", "r") as f:
    data = json.load(f)

quadruples = data["quadruples"]
constants = data["constants"]

vm = VirtualMachine(quadruples)

for addr, val in constants["int"].items():
    vm.globalMemory.set_value(addr=int(addr), value=val)

for addr, val in constants["float"].items():
    vm.globalMemory.set_value(addr=int(addr), value=val)

for addr, val in constants["string"].items():
    vm.globalMemory.set_value(addr=int(addr), value=val)

vm.run()
