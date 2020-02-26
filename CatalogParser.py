import struct

def parse(fileInPath, fileOutPath):  
    structFmt = "=f 2d 2h 2f"
    structLen = struct.calcsize(structFmt)

    results = []
    with open(fileInPath, "rb") as fileIn:
        fileIn.seek(28)
        while True:
            data = fileIn.read(structLen)
            if not data: 
                break
            s = struct.unpack(structFmt, data)
            results.append(s)
    
    with open(fileOutPath, "wb") as fileOut:
        for s in results:
            data = struct.pack('=2d h', s[1], s[2], s[4])
            fileOut.write(data)

if __name__ == '__main__':
    parse('d:/catalogParsed/BSC5', 'd:/catalogParsed/BSC5_py.bin')



