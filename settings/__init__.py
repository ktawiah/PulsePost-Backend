from decouple import config

if config(option="DEVELOPMENT_MODE", cast=bool):
    from .local import Local  # noqa: F401
else:
    from .prod import Production  # noqa: F401
