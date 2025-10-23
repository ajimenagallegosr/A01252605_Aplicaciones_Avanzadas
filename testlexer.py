from Avance1 import lexer

test_cases = [
    # 1. reservadas
    '''
    program miPrograma;
    var x, y, total : int;
    var nombre : float;
    main {
        print(total);
    }
    end
    ''',

    # 2. numeros y operaciones
    '''
    var a : int;
    var b : float;
    a = 10;
    b = 3.1416;
    a = a + 5 * ( 2 - 1 );
    b = b / 2.0;
    ''',

    # 3. condicionales
    '''
    if ( a > 5 ) {
        print("mayor que 5");
    }
    else {
        print("no mayor");
    }
    while (a != 0) do {
        a = a - 1;
    }
    ''',

    # 4. comentarios y strings
    '''
    // Este es un comentario
    print("Hola mundo"); // otro comentario
    print("123 + 456");
    ''',

    # 5. errores 
    '''
    var x : int;
    x = 20 @ 5;
    x = #;
    ''',

    # 6. mas identificadores
    '''
    var _x : int;
    var x2y3 : float;
    var x_y_z : int;
    program123 varif ifvar
    '''
]

for i, data in enumerate(test_cases, start=1):
    print(f"\n=== Test {i} ===")
    lexer.input(data)
    for tok in lexer:
        print(tok)
