operadoras = [
    ("Travel Adventures", "info@traveladventures.com"),
    ("Explore Destinations", "contact@exploredestinations.net"),
    ("Global Tours", "info@globaltours.org"),
    ("Wanderlust Expeditions", "support@wanderlustexpeditions.biz"),
    ("Discover Travel Co.", "info@discovertravelco.com"),
    ("Journey Jamboree", "info@journeyjamboree.net"),
    ("Destination Dreams", "support@destinationdreams.io"),
    ("Voyage Ventures", "info@voyageventures.com"),
    ("Tour Treasures", "contact@tourtreasures.biz"),
    ("Adventure Seekers", "info@adventureseekers.net"),
    ("Cityscape Tours", "support@cityscapetours.org"),
    ("WebTravel Specialists", "info@webtravelspecialists.com"),
    ("Swift Escapes", "contact@swiftescapes.net"),
    ("Global Wanderlust", "info@globalwanderlust.io"),
    ("NextGen Explorers", "support@nextgenexplorers.com"),
    ("EcoTravel Expeditions", "info@ecotravelexpeditions.net"),
    ("Skyline Tours", "contact@skylinetours.biz"),
    ("Metro Explorations", "info@metroexplorations.org"),
    ("Innovative Travel Co.", "support@innovativetravelco.com"),
    ("Pulse Adventures", "info@pulseadventures.net"),
    ("Elite Journeys", "contact@elitejourneys.biz"),
    ("ConnectGlobal Travels", "info@connectglobaltravels.io"),
    ("Express Travel Services", "support@expresstravelservices.com"),
    ("Compass Tours", "info@compasstours.net"),
    ("LinkWave Travels", "contact@linkwavetravels.org"),
    ("SwiftNet Adventures", "info@swiftnetadventures.com"),
    ("CityExpress Expeditions", "support@cityexpressexpeditions.io"),
    ("TechTravel Networks", "info@techtravelnetworks.net"),
    ("Wanderer's Edge", "contact@wanderersedge.biz"),
    ("NexLink Tours", "info@nexlinktours.com"),
]

'''
   # Cargar las operadora
    print("Iniciar la carga de operadoras")
    for operadora in mis_operadoras:
        print("Grabando . . . ", operadora)
        Operadora.objects.create(
            nombrec=cliente[0],
            email=cliente[1],
        )
'''