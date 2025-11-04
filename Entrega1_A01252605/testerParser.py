# Ana Jimena Gallegos Rongel
# A01252605 test cases
from ParserPatito2 import parser

codigo = '''
    program ejemplo;
    var x : int;
    main {
        if (x < 10) {
            print("entra");
        };
    }
    end
    '''

tests = [
    # Programa
    ("1. Programa mínimo",
    '''
    program test;
    main {
    }
    end
    '''),

    # Variables
    ("2. Declaración simple de variables",
    '''
    program var_simples;
    var x : int;
    main {
    }
    end
    '''),

    ("3. Declaración múltiple de variables",
    '''
    program var_multiples;
    var x, y, z : float;
    main {
    }
    end
    '''),

    # Statements
    ("4. Assign con número",
    '''
    program ejemplo;
    var x : int;
    main {
        x = 5;
    }
    end
    '''),

    ("5. Assign con expresión",
    '''
    program ejemplo;
    var x, y : int;
    main {
        x = 5 + 3 * 2;
        y = 2 + x;
    }
    end
    '''),

    ("6. Condition simple",
    '''
    program ejemplo;
    var x : int;
    main {
        if (x < 10) {
            print("entra");
        };
    }
    end
    '''),

    ("7. Condition con else",
    '''
    program ejemplo;
    var x : int;
    main {
        if (x > 5) {
            print("mayor");
        } else {
            print("menor");
        };
    }
    end
    '''),

    ("8. Cycle - While",
    '''
    program ejemplo;
    var x : int;
    main {
        x = 1;
        while (x < 5) do {
            x = x + 1;
            print("loop");
        };
    }
    end
    '''),

    ("9. FCall",
    '''
    program ejemplo;
    main {
        func_x();
    }
    end
    '''),

    ("10. Print con string y expresión",
    '''
    program ejemplo;
    var x : int;
    main {
        print("hola");
        print(x);
        print("suma", 3 + 5);
    }
    end
    '''),

    # Funciones
    ("11. Función sin parámetros tipo void",
    '''
    program ejemplo;
    void saluda() {
        var x : int;
        {
            print("Hola");
        }
    };
    main {
        saluda();
    }
    end
    '''),

    ("12. Función con parámetros tipo void",
    '''
    program ejemplo;
    void suma(a : int, b : float) {
        {
            print("Funcion con params");
        }
    };
    main {
        suma(5, 2.3);
    }
    end
    '''),

    ("13. Función con tipo de retorno int",
    '''
    program ejemplo;
    int cuadrado(a : int) {
        {
            print("Calculando cuadrado");
        }
    };
    main {
        cuadrado(4);
    }
    end
    '''),

    ("14. Función con tipo de retorno float",
    '''
    program ejemplo;
    float area(r : float) {
        {
            print("Calculando área");
        }
    };
    main {
        area(3.5);
    }
    end
    '''),

    # Corchetes - estatutos anidados
    ("15. Estatuto dentro de corchetes simple",
    '''
    program ejemplo;
    main {
        [ print("Hola dentro de corchetes"); ]
    }
    end
    '''),

    ("16. Estatutos múltiples dentro de corchetes",
    '''
    program ejemplo;
    var x : int;
    main {
        [
            x = 10;
            print("x vale", x);
            [ print("anidado"); ]
        ]
    }
    end
    '''),

    ("17. Combinación de corchetes y ciclo",
    '''
    program ejemplo;
    var x : int;
    main {
        x = 0;
        while (x < 3) do {
            print("loop interno", x);
            x = x + 1;
        };
    }
    end
    '''),

    ("18. Llamada a función dentro de corchetes",
    '''
    program ejemplo;
    void saludo() {
        {
            print("Hola!");
        }
    };
    main {
        [ saludo(); ]
    }
    end
    '''),

    # Casos de error
    ("19. Error, falta de punto y coma",
    '''
    program ejemplo
    main {
    }
    end
    '''),

    ("20. Error, declaración inválida",
    '''
    program ejemplo;
    var x int;
    main {
    }
    end
    '''),

    ("21. Error, asignación inválida",
    '''
    program ejemplo;
    var x : int;
    main {
        x = ;
    }
    end
    '''),
]


for i, (nombre, codigo) in enumerate(tests, 1):
    print("\n" + "="*50)
    print(f" Test {i}: {nombre}")
    print("="*50)
    parser.parse(codigo)

#parser.parse(codigo)