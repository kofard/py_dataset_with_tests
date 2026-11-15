"""
| Wikipedia: https://en.wikipedia.org/wiki/Enigma_machine
| Video explanation: https://youtu.be/QwQVMqfoB2E
| Also check out Numberphile's and Computerphile's videos on this topic

This module contains function ``enigma`` which emulates
the famous Enigma machine from WWII.

Module includes:

- ``enigma`` function
- showcase of function usage
- ``9`` randomly generated rotors
- reflector (aka static rotor)
- original alphabet

Created by TrapinchO
"""
from __future__ import annotations
RotorPositionT = tuple[int, int, int]
RotorSelectionT = tuple[str, str, str]
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rotor1 = 'EGZWVONAHDCLFQMSIPJBYUKXTR'
rotor2 = 'FOBHMDKEXQNRAULPGSJVTYICZW'
rotor3 = 'ZJXESIUQLHAVRMDOYGTNFWPBKC'
reflector = {'A': 'N', 'N': 'A', 'B': 'O', 'O': 'B', 'C': 'P', 'P': 'C', 'D': 'Q', 'Q': 'D', 'E': 'R', 'R': 'E', 'F': 'S', 'S': 'F', 'G': 'T', 'T': 'G', 'H': 'U', 'U': 'H', 'I': 'V', 'V': 'I', 'J': 'W', 'W': 'J', 'K': 'X', 'X': 'K', 'L': 'Y', 'Y': 'L', 'M': 'Z', 'Z': 'M'}
rotor4 = 'RMDJXFUWGISLHVTCQNKYPBEZOA'
rotor5 = 'SGLCPQWZHKXAREONTFBVIYJUDM'
rotor6 = 'HVSICLTYKQUBXDWAJZOMFGPREN'
rotor7 = 'RZWQHFMVDBKICJLNTUXAGYPSOE'
rotor8 = 'LFKIJODBEGAMQPXVUHYSTCZRWN'
rotor9 = 'KOAEGVDHXPQZMLFTYWJNBRCIUS'

def _validator(rotpos: RotorPositionT, rotsel: RotorSelectionT, pb: str) -> tuple[RotorPositionT, RotorSelectionT, dict[str, str]]:
    """Checks if the values can be used for the ``enigma`` function"""
    if (unique_rotsel := len(set(rotsel))) < 3:
        msg = f'Please use 3 unique rotors (not {unique_rotsel})'
        raise Exception(msg)
    rotorpos1, rotorpos2, rotorpos3 = rotpos
    if not 0 < rotorpos1 <= len(abc):
        msg = f'First rotor position is not within range of 1..26 ({rotorpos1}'
        raise ValueError(msg)
    if not 0 < rotorpos2 <= len(abc):
        msg = f'Second rotor position is not within range of 1..26 ({rotorpos2})'
        raise ValueError(msg)
    if not 0 < rotorpos3 <= len(abc):
        msg = f'Third rotor position is not within range of 1..26 ({rotorpos3})'
        raise ValueError(msg)
    pbdict = _plugboard(pb)
    return (rotpos, rotsel, pbdict)

def _plugboard(pbstring: str) -> dict[str, str]:
    """https://en.wikipedia.org/wiki/Enigma_machine#Plugboard"""
    if not isinstance(pbstring, str):
        msg = f"Plugboard setting isn't type string ({type(pbstring)})"
        raise TypeError(msg)
    if len(pbstring) % 2 != 0:
        msg = f'Odd number of symbols ({len(pbstring)})'
        raise Exception(msg)
    if pbstring == '':
        return {}
    pbstring.replace(' ', '')
    tmppbl = set()
    for i in pbstring:
        if i not in abc:
            msg = f"'{i}' not in list of symbols"
            raise Exception(msg)
        if i in tmppbl:
            msg = f'Duplicate symbol ({i})'
            raise Exception(msg)
        tmppbl.add(i)
    del tmppbl
    pb = {}
    for j in range(0, len(pbstring) - 1, 2):
        pb[pbstring[j]] = pbstring[j + 1]
        pb[pbstring[j + 1]] = pbstring[j]
    return pb

def enigma(text: str, rotor_position: RotorPositionT, rotor_selection: RotorSelectionT=(rotor1, rotor2, rotor3), plugb: str='') -> str:
    """The only difference with real-world enigma is that ``I`` allowed string input.
    All characters are converted to uppercase. (non-letter symbol are ignored)

    | How it works:
    | (for every letter in the message)

    - Input letter goes into the plugboard.
      If it is connected to another one, switch it.

    - Letter goes through ``3`` rotors.
      Each rotor can be represented as ``2`` sets of symbol, where one is shuffled.
      Each symbol from the first set has corresponding symbol in
      the second set and vice versa.

      example::

      | ABCDEFGHIJKLMNOPQRSTUVWXYZ | e.g. F=D and D=F
      | VKLEPDBGRNWTFCJOHQAMUZYIXS |

    - Symbol then goes through reflector (static rotor).
      There it is switched with paired symbol.
      The reflector can be represented as ``2`` sets, each with half of the alphanet.
      There are usually ``10`` pairs of letters.

      Example::

      | ABCDEFGHIJKLM | e.g. E is paired to X
      | ZYXWVUTSRQPON | so when E goes in X goes out and vice versa

    - Letter then goes through the rotors again

    - If the letter is connected to plugboard, it is switched.

    - Return the letter"""
    text = text.upper()
    rotor_position, rotor_selection, plugboard = _validator(rotor_position, rotor_selection, plugb.upper())
    rotorpos1, rotorpos2, rotorpos3 = rotor_position
    rotor1, rotor2, rotor3 = rotor_selection
    rotorpos1 -= 1
    rotorpos2 -= 1
    rotorpos3 -= 1
    result = []
    for symbol in text:
        if symbol in abc:
            if symbol in plugboard:
                symbol = plugboard[symbol]
            index = abc.index(symbol) + rotorpos1
            symbol = rotor1[index % len(abc)]
            index = abc.index(symbol) + rotorpos2
            symbol = rotor2[index % len(abc)]
            index = abc.index(symbol) + rotorpos3
            symbol = rotor3[index % len(abc)]
            symbol = reflector[symbol]
            symbol = abc[rotor3.index(symbol) - rotorpos3]
            symbol = abc[rotor2.index(symbol) - rotorpos2]
            symbol = abc[rotor1.index(symbol) - rotorpos1]
            if symbol in plugboard:
                symbol = plugboard[symbol]
            rotorpos1 += 1
            if rotorpos1 >= len(abc):
                rotorpos1 = 0
                rotorpos2 += 1
            if rotorpos2 >= len(abc):
                rotorpos2 = 0
                rotorpos3 += 1
            if rotorpos3 >= len(abc):
                rotorpos3 = 0
        result.append(symbol)
    return ''.join(result)