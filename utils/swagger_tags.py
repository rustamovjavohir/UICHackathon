class Web:
    class Client:
        """ SWAGGER TAGS FOR CLIENT MOBILE APP """
        PREFIX = 'web_client'

        PAYMENT = f'{PREFIX}_payment'
        CARD = f'{PREFIX}_card'
        QR_SCAN = f'{PREFIX}_qr_scan'
        PROFILE = f'{PREFIX}_profile'
        REGISTRATION = f'{PREFIX}_registration'

    class User:
        """Swagger tags for staff mobile app"""
        PREFIX = 'web_user'
        AUTHORIZATION = f'{PREFIX}_authorization'
