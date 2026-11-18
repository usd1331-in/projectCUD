#!/bin/bash
WORDLIST=/usr/share/wordlists/rockyou.txt

hashcat -m 0 -a 0 data/weak.hashes "$WORDLIST"
hashcat -m 0 data/weak.hashes "$WORDLIST" --show
