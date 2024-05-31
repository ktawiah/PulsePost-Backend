from decouple import config

if config(option="DEVELOPMENT_MODE", cast=bool):
    from .local import Local
else:
    from .prod import Production
