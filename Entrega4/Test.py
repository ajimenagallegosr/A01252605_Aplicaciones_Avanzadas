# test_parser.py
from Lexer import lexer
from Parser import parser
import Semantic as semantic

def test_input(source):
    print("\n--- Testing input ---")
    print(source)
    print("----------------------")
    
    lexer.input(source)
    result = parser.parse(source, lexer=lexer)
    print("")

# ------------------------------
# TEST CASES
# ------------------------------

# 1. Minimal valid program
program1 = """
program myProgram;
var 
    a, b, c : int;
main {
    print(1);
}
end
"""

# 2. Variable declarations + assignment
program2 = """
program test;
var a, b, c : int;
    x, y : float;
main {
    x = 10;
    y = x + 2 * 3;
    print(x, y);
}
end
"""

# 3. Function with parameters and return
program3 = """
program funcTest;
var a : int;

void foo(x:int, y:float) {
    var z : int;
    {
        print(x);
    }
};

main {
    foo(3, 2.5);
}
end
"""

# 4. If / Else and While
program4 = """
program condLoop;
main {
    if (3 < 5) {
        print(10);
    } else {
        print(20);
    };

    while (1 < 10) do {
        print(99);
    };
}
end
"""

program5 = '''
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

# 5. Program with errors (should trigger your p_error)
program_error = """
program badProg
var a int
main {
    print(;
}
end
"""

# ------------------------------
# RUN TESTS
# ------------------------------

program6 = """
program quadruplos;
var a, b, c : int;
void suma(a: float, y: int){
        var res : float;
        {
            res = a + y;
        }
    }; 
void resta(a: int, y: int){
        var res : int;
        {
            res = a - y;
        }
    }; 
main {
    a = 2 + c * 3;
    b = (5 + 4) * 3;
    print(b + 2, a);
    print("a");
    if ( a != b){
        print(a);
        while( a < 2 * 3) do {
            b = a * ( 2 + c);
            print("hola"); 
        };
    } else {
        print(b);
    };
    print("hola");
}
end
"""

program7 = """
program quadruplos;
var a, b, c : int;
main {
    while( a < != 2 * 3) do {
            b = a * ( 2 + c);
            print("hola"); 
        };
}
end
"""
if __name__ == "__main__":
    test_input(program6)

    for func_name, info in semantic.func_dir.directory.items():
        print(f"\nVariables de función '{func_name}':")
        if info['vars'] is None:
            print(" (No hay VarTable — fue eliminada en el Paso 12)")
        else:
            for var, data in info['vars'].table.items():
                print(f"   {var} : {data['type']}, {data['address']}")
