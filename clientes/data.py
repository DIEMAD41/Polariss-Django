import random

clientes = [
    ('Juan Pérez', '555-1234', 'juanperez', 'password123', 25, 'Ciudad A'),
    ('María Rodríguez', '555-5678', 'mariarodriguez', 'securepass', 30, 'Ciudad B'),
    ('Carlos Gómez', '555-9876', 'carlosgomez', 'mypassword', 22, 'Ciudad C'),
    ('Ana Martínez', '555-4321', 'anamartinez', '12345678', 28, 'Ciudad A'),
    ('Pedro Sánchez', '555-8765', 'pedrosanchez', 'p@ssw0rd', 35, 'Ciudad B'),
    ('Luisa Herrera', '555-2345', 'luisaherrera', 'pass1234', 27, 'Ciudad C'),
    ('Javier López', '555-7654', 'javierlopez', 'securepass', 32, 'Ciudad A'),
    ('Sofía Torres', '555-5432', 'sofiatorres', 'password123', 29, 'Ciudad B'),
    ('Miguel Ramírez', '555-8765', 'miguelramirez', 'mypassword', 24, 'Ciudad C'),
    ('Carmen García', '555-2345', 'carmengarcia', '12345678', 31, 'Ciudad A'),
    ('Alejandro Ruiz', '555-6543', 'alejandroruiz', 'p@ssw0rd', 26, 'Ciudad B'),
    ('Laura Jiménez', '555-7890', 'laurajimenez', 'pass1234', 33, 'Ciudad C'),
    ('Daniel Castro', '555-0987', 'danielcastro', 'securepass', 28, 'Ciudad A'),
    ('Patricia Navarro', '555-5678', 'patricianavarro', 'password123', 29, 'Ciudad B'),
    ('Héctor Flores', '555-3456', 'hectorflores', 'mypassword', 30, 'Ciudad C'),
    ('Elena Silva', '555-8765', 'elenasilva', '12345678', 27, 'Ciudad A'),
    ('Roberto Vargas', '555-1234', 'robertovargas', 'p@ssw0rd', 31, 'Ciudad B'),
    ('Isabel Castro', '555-4567', 'isabelcastro', 'pass1234', 26, 'Ciudad C'),
    ('Francisco Méndez', '555-7890', 'francomendez', 'securepass', 29, 'Ciudad A'),
    ('Silvia Ríos', '555-2345', 'silviarios', 'password123', 34, 'Ciudad B'),
]


#Este fragmento de codigo es para llenar datos en la BD se pone en la primera linea de la clase ClienteListView
'''
   # Cargar los clientes
    print("Iniciar la carga de clientes")
    for cliente in mis_clientes:
        print("Grabando . . . ", cliente)
        Cliente.objects.create(
            nombrec=cliente[0],
            telefenoc=cliente[1],
            usuarioc=cliente[2],
            passwordc=cliente[3],
            edadc=cliente[4],
            localidad=cliente[5]
        )
'''