#!/usr/bin/env python3
import argparse

def caesarCipher(text: str,shift: int) -> str:
    lowerCaseMax = 122
    lowerCaseMin = 97
    uperCaseMax = 90
    uperCaseMin = 65
    shiftedText = "" 

    for symbol in text:
        if not symbol.isalpha():
            shiftedText += symbol
            continue

        value = ord(symbol)
        ordinalShift = value + shift

        if (value >= uperCaseMin and value <= uperCaseMax):
            if (ordinalShift < uperCaseMin):
                ordinalShift = uperCaseMax - (uperCaseMin - ordinalShift)
            elif (ordinalShift > uperCaseMax):
                ordinalShift = uperCaseMin + (ordinalShift - uperCaseMax) - 1
        elif (value >= lowerCaseMin and value <= lowerCaseMax):
            if (ordinalShift < lowerCaseMin):
                ordinalShift = lowerCaseMax - (lowerCaseMin - ordinalShift)
            elif (ordinalShift > lowerCaseMax):
                ordinalShift = lowerCaseMin + (ordinalShift - lowerCaseMax) - 1

        characterShift = chr(ordinalShift)
        shiftedText += characterShift
        continue


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
