import sys, os
from itertools import product

def menu():
    print(f'''    
.------------------------------------------------------------------------------.

██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗              
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝              
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║                 
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║                 
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║                 
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝                 
                                                                             
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                             
 By Kookie
'------------------------------------------------------------------------------'

Output file: {path}
Character set: {charset}
Minimum characters: {min}
Maximum characters: {max}
Size: {os.path.getsize(path)} bytes
Lines: {lines}                                                                 
    ''')
    
def generate(min, max, charset, path):
    n = 0
    while True:
        try:
            file = open(path, 'x')
            break
        except:
            n += 1
            path += f'({str(n)})'

    for i in range(max-min+1):
        for z in product(list(charset), repeat = min):
            file.write(''.join(z) + '\n')
        min += 1
    file.close
    with open(path, 'r') as file:
        for count, line in enumerate(file):
            pass
    return (count + 1)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 5:
            raise Exception
        min = int(sys.argv[1])
        max = int(sys.argv[2])
        charset = sys.argv[3]
        path = sys.argv[4]
    except:
        exit('\n[+] FORMAT: python3 <minimum-characters> <maximum-characters> <charset> <output-file>\n')
    lines = generate(min, max, charset, path)
    menu()
