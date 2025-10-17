#!/usr/bin/env python3
import argparse

def caesarCipher(text: str,shift: int) -> str:
    shiftedText = "" 
    for letter in text:
        if not letter.isalpha():
            shiftedText += characterShift
            continue
        ordinalShift = ord(letter) + shift
        characterShift = chr(ordinalShift)
        shiftedText += characterShift

    return shiftedText

def main():
    parser = argparse.ArgumentParser(
        description="Ceasar cipher encryption/decryption")
    parser.add_argument(
        "input", help="string to be encrypted/decrypted, A-Z", type=str)
    parser.add_argument(
        "shift", help="integer, positive or negative", type=int)
    
    args = parser.parse_args()

    text = caesarCipher(args.input, args.shift)

    print(text)

if __name__ == "__main__":
    main()
