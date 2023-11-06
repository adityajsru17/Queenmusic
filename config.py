import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝗤𝗨𝗘𝗘𝗡")

OWNER_ID = list(map(int, getenv("OWNER_ID", " 6681615908").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheQueenBot/Queenmusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/jee_study_room")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/offtopic_community")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "100"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", "BQDB_5Dn1Mkrnlj3grICbQkM41jPFMT5ZMSb9vLw-5WXcEJ5wiB8akTpbyWD0jE2jdcrLy2Cdv8w7Uv_hLU5-s_yqkgflCtfr0B_HdeZ46lm-Z1vJ4EtVuq9Rudt8hZGVYm77lyW8P4965nIWDq8sFtYzymSNThKaU0dlP7TIBS-amgPbfIsQutljZNxZQwEqdUpR6vS0Mn5wliWLOKizPuzw5SWI_R_bVfycxNpEKQgYi8YQOPocHr2eUCpEKlE0PKB9CTu2pj2AHM2S_SYV5N5vv9QaxrNoSa0dghrIppxWzLOa-7cseEgBzrm3N_nSe3sARdnSoc2B0DM7s2cFFEhAAAAAY5J4AkA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/bae8ca4a24a6902df2e0c.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/1740a2b00e6d7d1037d3f.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/2472f903b18bd80f6512b.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/dab7d4437596b29320ef7.jpg"

STATS_IMG_URL = "https://telegra.ph/file/b0faef02869900e86c166.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/f6ca98e4844c60a0e0c4a.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/a0ec6ad68388cf2eb2a58.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/eb70060cd6b3453cc5809.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/429faeef353a9cfec60f1.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/af2c6868ee40d5a53c0eb.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/b61305e47d1ad1f2d72d9.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = ""

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/bae8ca4a24a6902df2e0c.jpg"
