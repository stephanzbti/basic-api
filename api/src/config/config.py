import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
HOST_BINDING = os.getenv("HOST_BINDING", "127.0.0.1")
HOST_PORT = os.getenv("HOST_PORT", "8080")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
