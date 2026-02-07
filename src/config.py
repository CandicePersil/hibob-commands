import dotenv
import os

dotenv.load_dotenv(dotenv_path="data/.env")


class BaseConfig:

    _service_id: str = os.getenv("SERVICE_ID")
    _service_password: str = os.getenv("SERVICE_PASSWORD")

    _configuration: dict[str, str] = {
        "id": _service_id,
        "pwd": _service_password,
    }

    @classmethod
    def get_config(cls, key: str) -> str | None:
        return cls._configuration.get(key)
