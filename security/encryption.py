from cryptography.fernet import Fernet
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Generate a random key for Fernet encryption
key = Fernet.generate_key()


def hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against its bcrypt hash.
    """
    return pwd_context.verify(plain_password, hashed_password)


def encrypt_data(data: str) -> bytes:
    
    fernet = Fernet(key)
    return fernet.encrypt(data.encode('utf-8'))


def decrypt_data(data: bytes) -> str:
   
    fernet = Fernet(key)
    return fernet.decrypt(data).decode('utf-8')
