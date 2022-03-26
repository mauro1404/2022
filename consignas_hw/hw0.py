#################################################
# hw0.py
#
# Nombre: Mauro Rolon
# DNI:35136122
#################################################

#################################################
# Funciones que tenés que programar
#################################################

def hello_world():
# Modificar este código para que devuelva el string "Hello World!"
    
    return "Hello World!"

#################################################
# Funciones de Test (no modificar)
#################################################

def test_hello():
    print('Testeando testHelloWorld()... ', end='')
    assert hello_world() == "Hello World!"ghbg
    print('Pasó!')

#################################################
# main
#################################################

def main():
    test_hello()   

if __name__ == '__main__':
    main()
