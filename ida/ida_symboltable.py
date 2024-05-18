import idc
import idautils
import idaapi

for line in open("symbols.txt",'r'):
    #print(int(line[:16], 16), line[33:47], line[48:].strip())
    idaapi.set_name(int(line[:16], 16), line[48:].strip(), idaapi.SN_FORCE)