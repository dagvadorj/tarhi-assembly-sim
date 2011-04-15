
# regsiters
# pc: program counter
# sp: stack pointer
# m: mule
# r0
# r1
# r3
# 

instructions = {
    "read": "00",
    "write": "01",
    # move direct data to register (m only)
    "import": "10"
    # "alu": "11"
    }
    
sizes = {
    "32": "000", # default
    "16h":  "001",
    "16l": "010",
    "8hh": "011",
    "8hl": "100",
    "8lh": "101",
    "8ll": "110",
    "m": "111" # memory
    }

def disassembly(inp):
    chunks = inp.split(" ")
    buf = ""
    if instructions.has_key(chunks[0]):
        buf += instructions[chunks[0]]
    else:
        buf += "11" 
    return buf
    
if __name__=="__main__":
    fa = open("a.asm", "r")
    fo = open("a.o", "w")
    lines = fa.readlines()
    for line in lines:
        fo.write(disassembly(line))
        fo.write(" ")
    fa.close()
    fo.close()
        
