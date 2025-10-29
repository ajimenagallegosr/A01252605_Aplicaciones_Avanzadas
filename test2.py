# Ana Jimena Gallegos Rongel
# A01252605 test cases
from ParserPatito3 import parser

tests = [
    # Programa
    (" 1. Programa mínimo",
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

    ("Declaración múltiple de variables",
    '''
    program var_multiples;
    var x, y, z : float;
    main {
    }
    end
    '''),

    # Statements
    ("Assign con numero",
    '''
    program ejemplo;
    var x : int;
    main {
        x = 5;
    }
    end
    '''),

    ("Assign con expresión",
    '''
    program ejemplo;
    var x, y : int;
    main {
        x = 5 + 3 * 2;
        y = 2 + x;
    }
    end
    '''),

    ("Condition simple",
    '''
    program ejemplo;
    var x : int;
    main {
        if (x < 10) {
            print("entra");
        }
    }
    end
    '''),

    ("Condition con else",
    '''
    program ejemplo;
    var x : int;
    main {
        if (x > 5) {
            print("mayor");
        } else {
            print("menor");
        }
    }
    end
    '''),

    ("Cycle - While",
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

    ("FCall",
    '''
    program ejemplo;
    main {
        func_x(x);
    }
    end
    '''),

    ("Print con string y expresión",
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
    ("Función sin parametros",
    '''
    program ejemplo;
    void saluda() [
        var x : int;
        {
            print("Hola");
        }
    ];
    main {
        saluda();
    }
    end
    '''),

    ("Función con parametros",
    '''
    program ejemplo;
    void suma(a : int, b : float) [
        {
            print("Funcion con params");
        }
    ];
    main {
        suma(5, 2.3);
    }
    end
    '''),

    # Casos de error
    ("Error, falta de punto y coma",
    '''
    program ejemplo
    main {
    }
    end
    '''),

    ("Error, declaración inválida",
    '''
    program ejemplo;
    var x int;
    main {
    }
    end
    '''),

    ("Error, asignacion inválida",
    '''
    program ejemplo;
    var x : int;
    x = 5;
    main {
    }
    end
    '''),
]


for i, (nombre, codigo) in enumerate(tests, 1):
    print("\n" + "="*50)
    print(f" Test {i}: {nombre}")
    print("="*50)
    parser.parse(codigo)
