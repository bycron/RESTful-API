from os import path, environ
from dotenv import load_dotenv

load_dotenv(path.join(path.abspath(path.dirname(__file__)), '.env'))

main_user = environ.get("ADMIN_USER")
main_pass = environ.get("ADMIN_PASS")
guest_pass = environ.get("GUEST_PASS")
app_key = environ.get("APP_KEY")
