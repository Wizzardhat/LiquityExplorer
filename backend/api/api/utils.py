from dotenv import load_dotenv
import os

def load_env():
    # Load environment variables from .env file
    load_dotenv()
    return os.environ.get('MAINNET_RPC_URL')