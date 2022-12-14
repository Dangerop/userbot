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
    STRING_SESSION = "1BVtsOGsBu37bJA2gr0q_U5RzC0VFJGhzNiAM98SGHbVrZEQt68Yw6r9zWRjP8DByYjnXbd97KjukwpwJluFaUBvCeQAIt0B0oAVMhLnfzdRnyg3altmfsaetwvt4WhUTo3DZ0RB8Z_byAjC_XW2f0v_ZFUpJEgtF036j6pTvkXO4VNXh5H0lKm3keqUW8ZFWPn6u2jlRV0o2uYmzKKe1BcD6qXItnsPigdkL-fstYXAwAGy-9Vg_lHdalV9S-F4K2gc8EcKIqtPYzH_-0eTiRKDDRgjy4VZvsdZlsgjXQoi3j_FjQpN-SgnHJMOp152LEPAfmsbeDva2N4yvK0vTr7DM_Gf4Jl4="
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
