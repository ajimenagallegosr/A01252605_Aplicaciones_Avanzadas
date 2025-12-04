import json
from VirtualMachine import VirtualMachine

with open("output.json", "r") as f:
    data = json.load(f)

quadruples = data["quadruples"]
constants = data["constants"]

vm = VirtualMachine(quadruples)

for addr, val in constants["int"].items():
    vm.global_add[int(addr)] = val

for addr, val in constants["float"].items():
    vm.global_add[int(addr)] = val

for addr, val in constants["string"].items():
    vm.global_add[int(addr)] = val

vm.run()
