import binascii
from Crypto.Cipher import PKCS1_OAEP
from fastapi import FastAPI
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from hashlib import sha512

# tested on http://127.0.0.1:8000/docs#/
# server run by command in terminal: uvicorn main:app --reload


def generate_api():
    """ create instance of API
    :return: API instance
    """
    app = FastAPI()
    return app


def generate_symetric_key():
    """ create symetric key
    :return: symetric key value
    """
    key = Fernet.generate_key()
    return key


def generate_fernet():
    """ create fernet based on symetric key
    :return: Fernet object
    """
    f = Fernet(key)
    return f


def generate_asymetric_keys():
    """ create public and private key values
    :return: public and private key made from key and exponential value
    """
    key_pair_generator = RSA.generate(bits=1024)
    public_key_generator = key_pair_generator.publickey()
    return key_pair_generator, public_key_generator


key_pair, public_key = generate_asymetric_keys()


def generate_signature():
    """ generating signature for intended message using hashing and asymetric keys
    :return: signed message
    """
    msg = b'A message for signing'
    hashing = int.from_bytes(sha512(msg).digest(), byteorder='big')
    signature = pow(hashing, key_pair.d, key_pair.n)
    return signature


def verify_signature():
    """ verify whether the message is signed
    :return: value later casted to boolean with info on message verification
    """
    signature = generate_signature()
    msg = b'A message for signing'  # if message is the same as in generate_signature() func, result = true
    hashing = int.from_bytes(sha512(msg).digest(), byteorder='big')
    hash_from_signature = pow(signature, key_pair.e, key_pair.n)
    return hashing == hash_from_signature


def encode_message():
    """ encode message
    :return: encoded message
    """
    mess = b"Message to encode"
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(mess)
    return encrypted


def decode_message():
    """ decode message
    :return: decoded message
    """
    encrypted = encode_message()
    decryptor = PKCS1_OAEP.new(key_pair)
    decrypted = decryptor.decrypt(encrypted)
    return decrypted


app = generate_api()
key = generate_symetric_key()
f = generate_fernet()

signature = generate_signature()
verification = verify_signature()
encrypted = encode_message()
decrypted = decode_message()


@app.get("/")
async def get_symetric_key():
    """ randomly generate symetric key, GET
    :return: key
    """
    return {"key": key}


@app.post("/")
async def post_symetric_key():
    """ randomly generate symetric key, POST
    :return: key
    """
    return {"key": key}


@app.post("/encoded_messages")
async def post_encoded_message(message):
    """ encode message, POST
    :param message: message to encode
    :return: encoded message
    """
    message_bytes = message.encode('utf-8')
    token = f.encrypt(message_bytes)
    return {"message": token}


@app.post("/decoded_messages")
async def post_decoded_message(message):
    """ decode message, POST
    :param message: message to decode
    :return: decoded message
    """
    message_bytes = message.encode('utf-8')
    token = f.decrypt(message_bytes)
    return {"message": token}


@app.get("/asymetric_key")
async def get_asymetric_key():
    """ generate private and public keys consisting of key and his exponential, GET
    :return: private and public key values as HEX values
    """
    return {"private_key":
                {"key": hex(key_pair.n), "exp": hex(key_pair.e)},
            "public_key":
                {"key": hex(key_pair.n), "exp": hex(key_pair.d)}}


@app.post("/posted_asymetric_key")
async def post_asymetric_key():
    """ generate private and public keys consisting of key and his exponential, POST
        :return: private and public key values as HEX values
        """
    return {"private_key":
                {"key": hex(key_pair.n), "exp": hex(key_pair.e)},
            "public_key":
                {"key": hex(key_pair.n), "exp": hex(key_pair.d)}}


@app.post("/signed")
async def post_sign():
    """ sign message, POST
    :return: signed message
    """
    return {"signed": hex(signature)}


@app.post("/verification")
async def post_verify():
    """ verify if message is signed, POST
    :return: boolean value whether the message is signed
    """
    return {"ver": bool(verification)}


@app.post("/encode_asymetric")
async def asymetric_encode():
    """ encode message using asymetric keys, POST
    :return: encoded message
    """
    return {"message": binascii.hexlify(encrypted)}


@app.post("/decode_asymetric")
async def asymetric_decode():
    """ decode message using asymetric keys, POST
    :return: decoded message
    """
    return {"message": decrypted}
