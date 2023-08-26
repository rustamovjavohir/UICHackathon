class Web:
    class Client:
        """ SWAGGER TAGS FOR CLIENT WEB APP"""
        PREFIX = 'client'

        PAYMENT = f'{PREFIX}_payment'
        CARD = f'{PREFIX}_card'
        QR_SCAN = f'{PREFIX}_qr_scan'
        PROFILE = f'{PREFIX}_profile'
        REGISTRATION = f'{PREFIX}_registration'

    class User:
        """Swagger tags for staff web app"""
        PREFIX = 'user'
        AUTHORIZATION = f'{PREFIX}_authorization'

    class Pet:
        """Swagger tags for pets web app"""
        PREFIX = 'pet'
