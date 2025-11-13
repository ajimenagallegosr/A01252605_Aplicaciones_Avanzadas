#from parser5xd import parser
from Parser import parser
import Semantic as semantic

semantic.func_dir = semantic.FunctionDirectory()
semantic.current_function = None

"""codigo = 
program test;

var x, y: int;

void foo(z : int, b : float) {
    {
    print("hola");
    }
};

main {
}
end

"""
codigo = """
program test;
var a,b,c,d : int;
    f, e : float;

main
{
    f = a + 2 * 2.14 + (2 / 5 * 4);
    print(a, b, "hola");
    print(b < a - 4);

}
end
"""


print("Antes del parseo:", semantic.func_dir.directory)

parser.parse(codigo)

print("Después del parseo:", semantic.func_dir.directory)

for func_name, info in semantic.func_dir.directory.items():
    print(f"\nVariables de función '{func_name}':")
    if info['vars'] is None:
        print(" (No hay VarTable — fue eliminada en el Paso 12)")
    else:
        for var, data in info['vars'].table.items():
            print(f"   {var} : {data['type']}")


