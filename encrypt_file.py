#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import struct
import hashlib
import pyaes

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """Encrypts a file using AES (CBC mode) with the given key.
    
        key:
            The encryption key - a string that must be either 16,
            24, or 32 bytes long. Longer keys are more secure.
            
        in_filename:
            Name of the input file.
        
        out_filename:
            If None, '<in_filename>.enc' will be used.
            
        chunksize:
            Sets the size of the chunk which the function uses to
            read and encrypt the file. Larger chunk sizes can be
            faster for some files and machines. `chunksize` must
            be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    # iv = ''.join('aqzwsxedcrvnfjgu')

    # A 256 bit (32 byte) key
    key = "This_key_for_demo_purposes_only!"

    # For some modes of operation we need a random initialization vector
    # of 16 bytes
    iv = "InitializationVe"
    
    # aes = pyaes.AESModeOfOperationCBC(key, iv=iv)
    encryptor = pyaes.AESModeOfOperationCBC(key, iv=iv)
    filesize = os.path.getsize(in_filename)
    print('Filesize: {0}'.format(filesize))

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def main():
    encrypt_file('1234567812345678', '/home/jolvera/Python/backuppy/file.txt')

if __name__ == '__main__':
    main()
