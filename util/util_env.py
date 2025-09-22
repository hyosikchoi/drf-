import os
from pathlib import Path

from dotenv import load_dotenv

class EnvironmentManager:
    def __init__(self):
        load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
        self._environment_variables = {}
        self._set_os_env()
        self.postgres = None

    def _set_os_env(self):
        self._environment_variables.update(os.environ)

    def get(self, key: str, default=None) -> str:
        return self._environment_variables.get(key, default)

env_manager = EnvironmentManager()