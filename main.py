#!/usr/bin/env python3
import argparse

def main():
    # Take user string and shift 
    parser = argparse.ArgumentParser(
        description="Ceasar cipher encryption/decryption")
    parser.add_argument(
        "input", help="string to be encrypted/decrypted, A-Z", type=str)
    parser.add_argument(
        "shift", help="integer, positive or negative", type=int)
    
    args = parser.parse_args()
    print(f"input: {args.input}")               
    print(f"shift: {args.shift}")               
    # Shift every letter in string 
    # Return string

if __name__ == "__main__":
    main()
