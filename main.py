#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Ceasar cipher encryption/decryption")
    parser.add_argument(
        "input", help="string to be encrypted/decrypted, A-Z", type=str)
    parser.add_argument(
        "shift", help="integer, positive or negative", type=int)
    
    args = parser.parse_args()
    print(f"input: {args.input}")               

    caesarCipher = "" 
    for letter in args.input:
        if not letter.isalpha():
            caesarCipher += characterShift
            continue
        ordinalShift = ord(letter) + args.shift
        characterShift = chr(ordinalShift)
        caesarCipher += characterShift

    print(caesarCipher)

if __name__ == "__main__":
    main()
