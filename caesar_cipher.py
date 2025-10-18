#!/usr/bin/env python3
import argparse

def caesarCipher(text: str,shift: int) -> str:
    uperCaseMin = ord('a')
    uperCaseMax = ord('z')
    uperCaseRange = range(uperCaseMin, uperCaseMax + 1)
    lowerCaseMin = ord('A')
    lowerCaseMax = ord('Z')
    lowerCaseRange = range(lowerCaseMin, lowerCaseMax + 1)
    shiftedText = "" 

    for symbol in text:
        if not symbol.isalpha():
            shiftedText += symbol
            continue

        ordValue = ord(symbol)
        ordShift = ordValue + shift

        if ordValue in uperCaseRange:
            if (ordShift < uperCaseMin):
                ordShift = uperCaseMax - (uperCaseMin - ordShift) + 1
            elif (ordShift > uperCaseMax):
                ordShift = uperCaseMin + (ordShift - uperCaseMax) - 1

        if ordValue in lowerCaseRange:
            if (ordShift < lowerCaseMin):
                ordShift = lowerCaseMax - (lowerCaseMin - ordShift) + 1
            elif (ordShift > lowerCaseMax):
                ordShift = lowerCaseMin + (ordShift - lowerCaseMax) - 1

        characterShift = chr(ordShift)
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
