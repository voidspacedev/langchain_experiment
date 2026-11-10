from dotenv import load_dotenv
import os

load_dotenv()


def get_env_var(var_name: str) -> str:
    env_var = os.getenv(var_name)

    if not env_var:
        raise ValueError(f"No variable with name {var_name} found!")

    return env_var