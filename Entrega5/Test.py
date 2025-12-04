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
int suma(a: float, y: int){
        var res : float;
        {
            res = a + y;
        }
    }; 
void resta(a: int, y: int){
        var res : int;
        {
            res = a - y;
            print(suma(1.1, 4));
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

programNuevo = '''
program patito;
var i, j, k : int;
    f : float;

void uno(a: int, b: int, j:int){
    {
        if ( a > 0){
            i = a + b * j + i;
        }
        else{
            print(a + b);
        };
    }
};

int dos(a: int, g: float){
    var i : int;
    {
        i = a;
        while(a > 0) do {
            a = a - k * j;
            uno(a*2, a + k);
            g = g * j - k;
        };
        return(i+k*j);
    }
};
main {
    i = 2;
    k = i + 1;
    f = 3.14;
    print(dos(i+k, f*3) + 3);
}
end
'''

program7 = """
program quadruplos;
var a, b, c : int;

main {
    a = 1;
    while (a < 5) do {
        a = a + 1;
        print("hola"); 
    };
}
end
"""

program8 = """
program quadruplos;
var a, b : int;
    c : float;
main {
    a = 2;
    b = 4;
    c = a * b; //8
    print(c);
    c = b / a; // 2
    print(c);
    c = a + b - 3; // 3
    print(c);
    print(5);

}
end
"""

programMaestra = '''
program flow;
var n: int; acc: int;
main {
    n = 3;
    acc = 0;
    while(n>=0)do {
        acc = acc + 1;
        print("iter ", acc, " n= ", n);
        n = n - 1;
    } ;
    if (acc>=3) {
        print("done ", acc, " iters");
    } else {
        print("never");
    } ;
    [
        n = 3;
        acc = 0;
        while (n>=0) do {
            acc = acc + 1;
            print("iter ", acc, " n= ", n);
            n = n - 1;
        } ;         
        if (acc>=3) {
            print("done ", acc, " iters");
        } else {
            print("never");
        } ;
    ]
} end
'''

if __name__ == "__main__":
    test_input(programNuevo)

    for func_name, info in semantic.func_dir.directory.items():
        print(f"\nVariables de función '{func_name}':")
        if info['vars'] is None:
            print(" (No hay VarTable — fue eliminada en el Paso 12)")
        else:
            for var, data in info['vars'].table.items():
                print(f"   {var} : {data['type']}, {data['address']}")
