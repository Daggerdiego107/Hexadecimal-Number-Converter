def dec_to_hex(dec):
    hex = []
    while dec > 0:
        residue = dec % 16

        if residue < 10:
            hex.append(str(residue))
        else:
            hex.append(chr(ord("A") + residue - 10))
        
        dec = dec // 16
    hex.reverse()
    return ''.join(hex)

dec = int(input("Type in a decimal number: "))
hex = dec_to_hex(dec)
print(f"The decimal number {dec} converted to hexadecimal is: 0x{hex}")