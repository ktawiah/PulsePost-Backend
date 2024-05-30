from split_settings.tools import include, optional
from decouple import config

include("base.py")

if config(option="DEVELOPMENT_MODE", cast=bool):
    include("local.py")
else:
    include("prod.py")
