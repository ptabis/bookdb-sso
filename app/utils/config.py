from os import getenv


class config:
    dev = int(getenv("DEV") or 0)
    hosts_whitelist = tuple(getenv("HOSTS_WHITELIST", "").split(","))

    class datasources:
        class redis:
            host = getenv("REDIS_HOST") or "localhost"
            port = int(getenv("REDIS_PORT") or 6379)
