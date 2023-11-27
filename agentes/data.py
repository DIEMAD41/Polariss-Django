import random



agentes = [
    (1, 'John Doe', '5551234567', 'john_doe', 'pass123', 1000, 28, 'City A'),
    (2, 'Jane Smith', '5559876543', 'jane_smith', 'pass456', 1200, 32, 'City B'),
    (3, 'Robert Johnson', '5552345678', 'robert_johnson', 'pass789', 800, 25, 'City C'),
    (4, 'Emily Davis', '5558765432', 'emily_davis', 'passabc', 1500, 30, 'City D'),
    (5, 'Michael Wilson', '5553456789', 'michael_wilson', 'passdef', 1100, 35, 'City E'),
    # Agrega más tuplas según sea necesario
    (6, 'Sophia Brown', '5557654321', 'sophia_brown', 'passefg', 900, 29, 'City F'),
    (7, 'Christopher Miller', '5558765432', 'christopher_miller', 'passhij', 1300, 27, 'City G'),
    (8, 'Ava Davis', '5559876543', 'ava_davis', 'passklm', 1000, 31, 'City H'),
    (9, 'Matthew Johnson', '5552345678', 'matthew_johnson', 'passnop', 1200, 26, 'City I'),
    (10, 'Olivia Smith', '5555678901', 'olivia_smith', 'passqrs', 1100, 34, 'City J'),
    (11, 'William Davis', '5557654321', 'william_davis', 'passtuv', 1400, 33, 'City K'),
    (12, 'Emma Wilson', '5551234567', 'emma_wilson', 'passwxy', 800, 28, 'City L'),
    (13, 'Liam Brown', '5558765432', 'liam_brown', 'passzab', 900, 32, 'City M'),
    (14, 'Isabella Miller', '5559876543', 'isabella_miller', 'pass123', 1000, 30, 'City N'),
    (15, 'Mia Johnson', '5552345678', 'mia_johnson', 'pass456', 1300, 29, 'City O'),
    (16, 'James Davis', '5555678901', 'james_davis', 'pass789', 1400, 31, 'City P'),
    (17, 'Sophia Wilson', '5551234567', 'sophia_wilson', 'passabc', 1200, 27, 'City Q'),
    (18, 'Benjamin Smith', '5558765432', 'benjamin_smith', 'passdef', 1500, 30, 'City R'),
    (19, 'Amelia Johnson', '5559876543', 'amelia_johnson', 'passhij', 1000, 29, 'City S'),
    (20, 'Logan Davis', '5552345678', 'logan_davis', 'passklm', 1100, 32, 'City T'),
    (21, 'Olivia Brown', '5555678901', 'olivia_brown', 'passnop', 1200, 31, 'City U'),
    (22, 'Lucas Wilson', '5557654321', 'lucas_wilson', 'passqrs', 900, 28, 'City V'),
    (23, 'Ava Smith', '5558765432', 'ava_smith', 'passuvw', 1000, 33, 'City W'),
    (24, 'Jackson Johnson', '5559876543', 'jackson_johnson', 'passxyz', 1100, 26, 'City X'),
    (25, 'Sophie Davis', '5552345678', 'sophie_davis', 'pass123', 1400, 35, 'City Y'),
    (26, 'Aiden Wilson', '5555678901', 'aiden_wilson', 'pass456', 800, 30, 'City Z'),
    (27, 'Charlotte Brown', '5558765432', 'charlotte_brown', 'pass789', 1200, 29, 'City AA'),
    (28, 'Mason Smith', '5559876543', 'mason_smith', 'passabc', 1500, 28, 'City BB'),
    (29, 'Amelia Davis', '5552345678', 'amelia_davis', 'passdef', 1000, 32, 'City CC'),
    (30, 'Ethan Wilson', '5555678901', 'ethan_wilson', 'passefg', 1100, 31, 'City DD'),
     ]


#Este fragmento de codigo es para llenar datos en la BD se pone en la primera linea de la clase ClienteListView
'''
   # Cargar los agentes
    print("Iniciar la carga de agentes")
    for agente in mis_agentes:
        print("Grabando . . . ", agente)
        Cliente.objects.create(
            nombreg=agente[1],
            telefenog=agente[2],
            usuariog=agente[3],
            passwordg=agente[4],
            saldo=agente[5],
            edadg=agente[6]
            localidadg=agente[7]
        )
'''