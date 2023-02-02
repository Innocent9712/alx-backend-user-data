#!/usr/bin/env python3
"""5. Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> str:
    """a function called hash_password that takes a password
    string arguments and returns a salted, hashed password,
    which is a byte string"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())