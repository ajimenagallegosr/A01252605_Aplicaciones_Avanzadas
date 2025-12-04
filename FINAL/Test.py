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


fibonnaci_completo = """
program pruebas_recursion;
var n, i, fact_main, fact_it, fact_rec, f0, f1, temp, fib_main, fib_it_res, fib_rec_res: int;

int factIter(n: int){
    var i, acc: int;
    {
        acc = 1;
        i = 1;
        while (i < n + 1) do {
            acc = acc * i;
            i = i + 1;
        };
        return acc;
    }
};

int factRec(n: int){
    {
        if (n == 0){
            return 1;
        } else {
            return n * factRec(n - 1);
        };
    }
};

int fibIter(n: int){
    var a, b, k, t: int;
    {
        a = 0;
        b = 1;
        k = 0;
        while (k < n) do {
            t = a + b;
            a = b;
            b = t;
            k = k + 1;
        };
        return a;
    }
};

int fibRec(n: int){
    {
        if (n == 0){
            return 0;
        } else {
            if (n == 1){
                return 1;
            } else {
                return fibRec(n - 1) + fibRec(n - 2);
            };
        };
    }
};

main {

    n = 10;

    fact_main = 1;
    i = 1;
    while (i < n + 1) do {
        fact_main = fact_main * i;
        i = i + 1;
    };

    print("n factorial:", n);
    print("factorial en main:", fact_main);

    fact_it = factIter(n);
    print("factorial iterativo:", fact_it);

    fact_rec = factRec(n);
    print("factorial recursivo:", fact_rec);


    n = 10;

    f0 = 0;
    f1 = 1;
    i = 0;
    print("n fibonnaci:", n);
    while (i < n) do {
        temp = f0 + f1;
        f0 = f1;
        f1 = temp;
        i = i + 1;
    };

    fib_main = f0;
    print("fib en main:", fib_main);

    fib_it_res = fibIter(n);
    print("fib iterativo:", fib_it_res);

    fib_rec_res = fibRec(n);
    print("fib recursivo:", fib_rec_res);

} end
"""

iterativo = """
program iterativo;
var n, fact_it, fib_it_res: int;

int factIter(n: int){
    var i, acc: int;
    {
        acc = 1;
        i = 1;
        while (i < n + 1) do {
            acc = acc * i;
            i = i + 1;
        };
        return acc;
    }
};

int fibIter(n: int){
    var a, b, k, t: int;
    {
        a = 0;
        b = 1;
        k = 0;
        while (k < n) do {
            t = a + b;
            a = b;
            b = t;
            k = k + 1;
        };
        return a;
    }
};

main {

    n = 10;

    print("n:", n);

    fact_it = factIter(n);
    print("factorial iterativo:", fact_it);

    fib_it_res = fibIter(n);
    print("fib iterativo:", fib_it_res);

} end

"""

recursivo = """
program recursivo;
var n, fact_rec, fib_rec_res: int;

int factRec(n: int){
    {
        if (n == 0){
            return 1;
        } else {
            return n * factRec(n - 1);
        };
    }
};

int fibRec(n: int){
    {
        if (n == 0){
            return 0;
        } else {
            if (n == 1){
                return 1;
            } else {
                return fibRec(n - 1) + fibRec(n - 2);
            };
        };
    }
};

main {

    n = 10;

    print("n:", n);

    fact_rec = factRec(n);
    print("factorial recursivo:", fact_rec);
    fib_rec_res = fibRec(n);
    print("fib recursivo:", fib_rec_res);
} end
"""

factorial_main = '''
program main_version;
var n, i, fact_main, f0, f1, temp, fib_main: int;

main {

    n = 10;

    fact_main = 1;
    i = 1;
    while (i < n + 1) do {
        fact_main = fact_main * i;
        i = i + 1;
    };

    print("n factorial:", n);
    print("factorial en main:", fact_main);

    n = 10;

    f0 = 0;
    f1 = 1;
    i = 0;
    while (i < n) do {
        temp = f0 + f1;
        f0 = f1;
        f1 = temp;
        i = i + 1;
    };

    fib_main = f0;

    print("n fibonacci:", n);
    print("fib en main:", fib_main);

} end
'''

func_con_otra_func = '''
program test;
var i,j, x : int;

    int dos(a: int){
        var x : int;
        {
            x = a + 1;
            return x;
        }
    };

    void uno(a: int){
        var x : int;
        {
            x = a + 3;
            print(x);
        }
    };
main
{   
    i = 2;
    j = 5;

    while (i<j) do {
        uno(dos(1));
        i = i + 1;
        print(5 * (10/2));
    };
}
end
'''
if __name__ == "__main__":
    test_input(func_con_otra_func)

    for func_name, info in semantic.func_dir.directory.items():
        print(f"\nVariables de función '{func_name}':")
        if info['vars'] is None:
            print(" (No hay VarTable — fue eliminada en el Paso 12)")
        else:
            for var, data in info['vars'].table.items():
                print(f"   {var} : {data['type']}, {data['address']}")
"""
    fib_rec_res = fibRec(n);
    print("fib recursivo:", fib_rec_res);
"""