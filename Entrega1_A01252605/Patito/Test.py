#from parser5xd import parser
from Parser import parser
import Semantic as semantic

semantic.func_dir = semantic.FunctionDirectory()
semantic.current_function = None

codigo3 = '''
program test;

var x, y: int;

void foo(z : int, b : float) {
    var res : float;
    {
    print("hola");
    res = z + b;
    }
};

main {
    print(x);
}
end
'''

codigo2 = '''
program test;
var a,b,c,d : int;
    f, e : float;

    void suma(a: float, y: int){
        var res : float;
        {
            res = 1;
            res = a + y;
        }
    }; 

    void resta(uno: int, dos: int){
        var res : int;
        {
            res = uno - dos;
        }
    }; 
main
{
    if(a < b){
        a = b;
        a = 2;
        while (a > b) do {
        print(c);
        };
        print("hola");
    } else {
        b = 1;
    };
    print(a);
    suma(a, b);
}
end
'''
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

codigo4 = '''
program test;
var a,b,c,d : int;

void suma(a: float, y: int){
        var res : float;
        {
            res = a + y;
        }
    }; 

void resta(a: float, y: int){
    var res : float;
    {
        res = a + y;
    }
}; 

main
{

}
end
'''

codigo5 = '''
program test;
var a,b,c,d : int;

main
{
    a = b + c;
}
end
'''

codeLoopIf = """
program prueba;
var a,b,c,d : int;
main {
    if(a+b>d){
        if(a<b){
            a = 0;
            b = b+d;
        }
        else{
            c = a+b;
        };
    }
    else{
        a = b+c;
    };
    d = b+a*c;
}
end
"""

code2222 = '''
program prueba;
var a,b,c : int;

void suma(a: float, y: int){
        var res : float;
        {
            res = a + y;
        }
    }; 
main {
    a = b + c;
    print(a);
}
end
'''


print("Antes del parseo:", semantic.func_dir.directory)

parser.parse(codigo2)

print("Después del parseo:", semantic.func_dir.directory)

for func_name, info in semantic.func_dir.directory.items():
    print(f"\nVariables de función '{func_name}':")
    if info['vars'] is None:
        print(" (No hay VarTable — fue eliminada en el Paso 12)")
    else:
        for var, data in info['vars'].table.items():
            print(f"   {var} : {data['type']}")


