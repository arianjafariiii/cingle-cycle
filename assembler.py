def instructureToBin(asm):
    ins = list(asm.split())
    opCode, rd, rs, rt, imm, addr = "", "", "", "", "", ""
 
    match ins[0]:
        case "and":
            (opCode), (rd, rs, rt) = bin(7), (map(bin, (map(int, ins[1:]))))
        case "nor":
            (opCode), (rd, rs, rt) = bin(2), (map(bin, (map(int, ins[1:]))))
        case "slt":
            (opCode), (rd, rs, rt) = bin(5), (map(bin, (map(int, ins[1:]))))  
        case "mul":
            (opCode), (rd, rs, rt) = bin(15), (map(bin, (map(int, ins[1:]))))      
        
        case "andi":
            (opCode), (rt, rs, imm) = bin(4), (map(bin, (map(int, ins[1:]))))
        case "sll":
            (opCode), (rt, rs, imm) = bin(12), (map(bin, (map(int, ins[1:]))))
        case "slti":
            (opCode), (rt, rs, imm) = bin(8), (map(bin, (map(int, ins[1:]))))

        case "jal":
            (opCode),(addr) = bin(11), bin(int(ins[1]))    
        

    return (opCode, rs, rt, rd, imm, addr)
   
def standardizeBin(opCode, rs, rt, rd, imm, addr):
    return opCode[2:].zfill(4), rs[2:].zfill(4), rt[2:].zfill(4), rd[2:].zfill(4), imm[2:].zfill(4), addr[2:].zfill(12)

def decode(ins):
    if '\n' in ins:
        ins = ins[:-1]
        
    opCode, rs, rt, rd, imm, addr = standardizeBin(*instructureToBin(ins))
    
    if opCode[2:4] == "00":
        return f"{opCode}{rs}{rt}{imm}"
    elif opCode == "1011":
        return f"{opCode}{addr}"
    else:
       return f"{opCode}{rs}{rt}{rd}"
    
def decodeInstructions(path):
    fRead = open(path, "r")
    
    fWrite = open("respond.txt", "w")
    for line in fRead:
        fWrite.write(decode(line) + "\n")        
        

decodeInstructions("test.txt")