from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 5389893
    API_HASH = "6cd070b7f1aa49b521d641fc65017113"
    # the name to display in your alive message
    ALIVE_NAME = "B4BY_opBolte"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:lundxd@localhost:5432/catuserbot"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "BQAzAzO5wd3Ie0gkztx9_6RAhQEbLQHW9U0RpRuiM99kXmq2pwLVHkUC88EdqMA-nEHW-EVJDjdSEyjmGV-bkkjKMUQQyiL0JBHxNygCuKgYsTqeLWErM9u-NplxmrkyU5fFewaRHZ1sZnrgJYZ3tRayQNCKALyGwqRWNLG4r4X9uuerBfDWSmaW_UbryAbD7tSWSKIk3LbEU-kTOxcaqELlNt0zdm9I1H4ZfiPmubT_U1jd8iFzhMWdC2D4qjMBWD7O3_4qt7yaLeJvDuMCdW0NHbh8g6MjXfzhIlR7z-TJ76U4Quh7QeCQWK8v7OmezHnoWQTqUeeLXFt_khF8grRbAAAAAVdHOjgA"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5946619925:AAGYQQIdweo7CSohudEk17W9hMKcMFqwQWc"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001862193348
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
