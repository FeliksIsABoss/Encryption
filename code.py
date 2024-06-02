import random
import tkinter
import tkinter as tk




f = open(my_file.txt, mode=wt)
encoding_scheme = {
    'a''gS23KbKvj2',
    'b''0cdfajuxEe',
    'c''s4N2oX451S',
    'd''5b8LEw63R9',
    'e''v0DCJboQbW',
    'f''0rAYLR7uUn',
    'g''t1ovsiatZY',
    'h''uPRsuHoH1c',
    'i''MESMavqnz0',
    'j''dDB7X5BuFN',
    'k''eLcaAbcqDk',
    'l''yIj61LpaMV',
    'm''V0VVYKXbOM',
    'n''H9cOTOEe6o',
    'o''pTDG5ZmRKx',
    'p''o5LKetcEJq',
    'q''9Ym6auhDiW',
    'r''HyXJOm8buo',
    's''XrGVPI7lc2',
    't''h3yIaGyV3a',
    'u''AEoDKIV0Wz',
    'v''T31nWASlr1',
    'w''wZEact7BYr',
    'x''5Z9TU0nCNZ',
    'y''1MKGcUa8bQ',
    'z''yWTBDqyhpl',
    'A''YJLGkYcKlE',
    'B''xKcJ7jNpe6',
    'C''RKhAyLL9pw',
    'D''gVmxRXjxB7',
    'E''f5gaRLk7rn',
    'F''qPZkffalBL',
    'G''HwkbAl29sU',
    'H''F90wLtYaHn',
    'I''gicnk5UbNP',
    'J''uMnHPl5SVU',
    'K''Jcqd5C04Ty',
    'L''HkbW9RsPc5',
    'M''DxgslaOAjG',
    'N''XjdMdGcQ7H',
    'O''tssZ6zkfl5',
    'P''2Fv6plkhMA',
    'Q''l16orAxYFQ',
    'R''iTSpTuG6Pb',
    'S''uxSsF88pFS',
    'T''iOIDzRe9mE',
    'U''nl4DCJ6ZGH',
    'V''fhvT2Tb524',
    'W''jTGIdP4MAu',
    'X''RArBHmMz1Q',
    'Y''H4knzStwfF',
    'Z''iT9HUzAKdA',
    ' ''D4aAn3kAK0',
    '!''fL1nuVe6r4',
    '.''BKhWh0bnQK',
    ',''Iv4qxCkNIC',
    '''W06zGjazqN'

}
def make_interval(string, interval)
    return ' '.join(string[ii+interval] for i in range(0, len(string), interval))
def encrypt(ENstring)
    encrypted_string = []
    stringlist = [ENstring]
    for i in stringlist
        encrypted_string.append(encoding_scheme[i])
    encrypted_string.reverse()
    encrypted_string = .join(encrypted_string)
    f.write(encrypted_string)
    return encrypted_string
def switch(case)
    if case == 1
        print(encryption code)
        string1 = input(Type in the string that you would like to encrypt )
        print(encrypt(string1))
    elif case == 2
        print(Decryption code)
        string2 = input(Type in the string that you would like to decrypt )
        print(decrypt(string2))
    else
        print(You did not enter a valid number!)
def decrypt(encryptstring)
    key_list = list(encoding_scheme.keys())
    val_list = list(encoding_scheme.values())
    decryptedstring = []
    encryptstring = make_interval(encryptstring,10)
    encryptstring = encryptstring.split()
    for i in encryptstring
        position = val_list.index(i)
        decryptedstring.append(key_list[position])
    decryptedstring.reverse()
    decryptedstring = ''.join(decryptedstring)
    return decryptedstring
    pass
while True
    nonencrypted = input(Type 1 to encrypt a string, and type 2 to input a string to decrypt )
    switch(nonencrypted)