from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = getenv("SESSION_NAME", "1BVtsOGQBu25trH7eapb3zob4yooFybImIZzty1MUsNibA1TaI8iMwwuif1icmoaKWLYAyIdvtAS-HKQJmiFP4am_fR-Jseh9fmkqyaZSTX0Ty8BQVDqcJDp98Ubxq6wkoGat1ZdhwYVBcwpEGS1CseKoIIMoOhcY2ufEaTw1fQQjk2AVQiU_w_4RTFe_326_Gr36xodg-tgv8dC6KfSMxhw7UISzuqIMbDWnYLKX6hjb7u6nN-cZmUr6S7WGRYBMcWQHm2Adkg3lCVHuXEv7LvU0AkWma5DRZsAoCj17B0yk-w4wMZyxE4JZ0SMrNWBBGe3Xm5-VxK9iNfRrCZl-sNaG-M27Zbo=")
BOT_TOKEN = getenv("BOT_TOKEN")

API_ID = int(getenv("2279350"))
API_HASH = getenv("aead80ba4d8b62830a90247b92821a41")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

SUDO_USERS = list(map(int, getenv("1312124716").split()))
