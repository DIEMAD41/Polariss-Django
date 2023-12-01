import random

proveedores = [
    ('Juan Pérez', '555-1234', 'juanperez@gmail.com', 'Volaris'),
    ('María Rodríguez', '555-5678', 'mariarodriguez@gmail.com', 'Volaris'),
    ('Carlos Gómez', '555-9876', 'carlosgomez@gmail.com', 'Volaris'),
    ('Ana Martínez', '555-4321', 'anamartinez@gmail.com', 'Volaris'),
    ('Pedro Sánchez', '555-8765', 'pedrosanchez@gmail.com', 'Volaris'),
    ('Luisa Herrera', '555-2345', 'luisaherrera@gmail.com', 'Volaris'),
    ('Javier López', '555-7654', 'javierlopez@gmail.com', 'Volaris'),
    ('Sofía Torres', '555-5432', 'sofiatorres@gmail.com', 'Volaris'),
    ('Miguel Ramírez', '555-8765', 'miguelramirez@gmail.com', 'Volaris'),
    ('Carmen García', '555-2345', 'carmengarcia@gmail.com', 'Volaris'),
    ('Alejandro Ruiz', '555-6543', 'alejandroruiz@gmail.com', 'Volaris'),
    ('Laura Jiménez', '555-7890', 'laurajimenez@gmail.com', 'Volaris'),
    ('Daniel Castro', '555-0987', 'danielcastro@gmail.com', 'Volaris'),
    ('Patricia Navarro', '555-5678', 'patricianavarro@gmail.com', 'Volaris'),
    ('Héctor Flores', '555-3456', 'hectorflores@gmail.com', 'Volaris'),
    ('Elena Silva', '555-8765', 'elenasilva@gmail.com', 'Volaris'),
    ('Roberto Vargas', '555-1234', 'robertovargas@gmail.com', 'Volaris'),
    ('Isabel Castro', '555-4567', 'isabelcastro@gmail.com', 'Volaris'),
    ('Francisco Méndez', '555-7890', 'francomendez@gmail.com', 'Volaris'),
    ('Silvia Ríos', '555-2345', 'silviarios@gmail.com', 'Volaris'),
]


#Este fragmento de codigo es para llenar datos en la BD se pone en la primera linea de la clase ClienteListView
'''
       # Cargar los proveedores
        print("Iniciar la carga de proveedores")
        for proveedor in mis_proveedores:
            print("Grabando . . . ", proveedor)
            Proveedor.objects.create(
                nombreprov=proveedor[0],
                telefenoprov=proveedor[1],
                correoprov=proveedor[2],
                nombreop=proveedor[3],
            )
    '''