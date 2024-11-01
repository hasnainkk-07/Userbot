# Required imports for the app class
from pyrogram import Client
from config import (
    API_ID,
    API_HASH,
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10
)

WORKERS = 8
NO_LOAD = []

class bot1(Client):
    """Starts the Pyrogram Client on the Bot Token when we do 'python3 -m X'"""

    def __init__(self):
        super().__init__(
            "bot1",
            session_string=STRING_SESSION1,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot2(Client):
    def __init__(self):
        super().__init__(
            "bot2",
            session_string=STRING_SESSION2,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot3(Client):
    def __init__(self):
        super().__init__(
            "bot3",
            session_string=STRING_SESSION3,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot4(Client):
    def __init__(self):
        super().__init__(
            "bot4",
            session_string=STRING_SESSION4,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot5(Client):
    def __init__(self):
        super().__init__(
            "bot5",
            session_string=STRING_SESSION5,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot6(Client):
    def __init__(self):
        super().__init__(
            "bot6",
            session_string=STRING_SESSION6,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot7(Client):
    def __init__(self):
        super().__init__(
            "bot7",
            session_string=STRING_SESSION7,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot8(Client):
    def __init__(self):
        super().__init__(
            "bot8",
            session_string=STRING_SESSION8,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot9(Client):
    def __init__(self):
        super().__init__(
            "bot9",
            session_string=STRING_SESSION9,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )

class bot10(Client):
    def __init__(self):
        super().__init__(
            "bot10",
            session_string=STRING_SESSION10,
            plugins=dict(root="X.modules.user", exclude=NO_LOAD),
            api_id=API_ID,
            api_hash=API_HASH,
            workers=WORKERS,
        )
