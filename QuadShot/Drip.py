import os

import ram
import Grind


jumps = {'JMP': '00C0',
         'JZ': '00C1',
         'JNZ': '00C2',
         'JS': '00C3',
         'JNS': '00C4',
         'JO': '00C5',
         'JNO': '00C6'}
table = {
    'arithmetic': {
        'ADD': ['00A0', '00B0'],
        'SUB': ['00A1', '00B1'],
        'MUL': ['00A2', '00B2'],
        'DIV': ['00A3', '00B3'],
        'MOD': ['00A6', '00B6'],
        'XOR': ['00A7', '00B7']},
    'INC':        '00A4',
    'DEC':        '00A5',
    'jumps':      jumps,
    'MOV':        ['00D0', '00D1', '00D2', '00D3', '00D4'],
    'CMP':        ['00DC', '00DA', '00DB', '00DD'],
    'PUSH':       '00E0',
    'POP':        '00E1',
    'PUSHG':      '00EA',
    'POPG':       '00EB',
    'OUT':        ['00F0', '00F1', '00F2'],
    'IN':         ['00FF', '00FE', '00FD'],
    'CALL':       '0A00',
    'RET':        '0B00',
    'SWP':        '0C00'
}


registers = {'AH': '0010',
             'AL': '0001',
             'AX': '0100',
             'BH': '0020',
             'BL': '0002',
             'BX': '0200',
             'CH': '0030',
             'CL': '0003',
             'CX': '0300',
             'DH': '0040',
             'DL': '0004',
             'DX': '0400',
             'ABX': '1000',
             'BCX': '2000',
             'CDX': '3000',
             'DAX': '4000'
             }

data_table = {
    'global': 0,
    'private': 1
}

d = []


def data(line):
    t, var = line.split('>')
    var, d = var.split('=')
    if t == 'literal':
        d = [d]
    elif t == 'list':
        d = list(d[1:-1].split(','))
    elif t == 'string':
        d = [tohex(ord(v)) for v in d[1:-1]] + ['000A']
    return var, d


def tokenize(lines):
    mode = 0
    for line in lines:
        op, args = None, None
        line = line.strip('\n')

        if '.data_' in line:
            mode = 1
            continue
        if '.exec_' in line:
            mode = 2
            continue
        if '%' in line:
            continue

        match mode:
            case 1:
                d.append(data(line.strip('\t').strip(' ')))
                continue
            case 2:
                if line.strip('\t').strip(' ')[0] == ';':
                    continue
                token = line.split(';')[0].strip('\t').split('|')[0]
                match token:
                    case t if ':' in t and t != '.':
                        yield t.strip('\t').strip(' '), []
                        continue
                    case t if 'END' in t:
                        yield 'END', []
                        continue
                    case t if t.startswith('.'):
                        yield t.strip('\t').strip(' '), []
                        continue
                    case _:
                        op, args = token.split()[0], token.split()[1].split(',')
            case _:
                pass

        yield op, args


def parse(lines):
    is_mem = lambda arg: arg[0] == '[' and arg[-1] == ']'
    for line in lines:
        op, args = line

        if args:
            match op:
                case 'DB':
                    if len(args[0]) == 4:
                        op, args = args, []
                    else:
                        args = [tohex(ord(n)) for n in args[0][1:-1]]
                        op, args = args[0], args[1:]

                case 'CMP':
                    if is_mem(args[1]):
                        op = table[op][0]
                        args[0] = registers[args[0]]
                        args[1] = args[1][1:-1]
                    elif args[1] in registers:
                        op = table[op][1]
                        args = [registers[a] for a in args]
                    elif is_mem(args[0]):
                        op = table[op][3]
                        args[0] = registers[args[0][1:-1]]
                    else:
                        op = table[op][2]
                        args[0] = registers[args[0]]

                case cmd if cmd in table['arithmetic']:
                    if args[1] in registers:
                        op = table['arithmetic'][op][0]
                        args = [registers[a] for a in args]
                    else:
                        op = table['arithmetic'][op][1]
                        args[0] = registers[args[0]]

                case cmd if cmd in table['jumps']:
                    op = table['jumps'][op]

                case 'MOV':
                    op, args = mov(args)

                case _ if len(args) == 1 and op in table:
                    match op:
                        case 'OUT':
                            if is_mem(args[0]):
                                op = table[op][2]
                                args[0] = registers[args[0][1:-1]]
                            elif args[0] in registers:
                                op = table[op][1]
                                args[0] = registers[args[0]]
                            else:
                                op = table[op][0]
                        case 'IN':
                            if args[0] in registers:
                                op = table[op][0]
                                args[0] = registers[args[0]]
                            elif is_mem(args[0]):
                                if args[0][1:-1] in registers:
                                    op = table[op][1]
                                    args[0] = registers[args[0][1:-1]]
                                else:
                                    op = table[op][2]
                                    args[0] = args[0][1:-1]
                        case 'CALL' | 'RET':
                            op, args = table[op], args
                        case _:
                            if args[0] in registers:
                                op = table[op]
                                args = [registers[args[0]]]
                            else:
                                op = table[op]

                case _:
                    pass

        else:
            match op:
                case 'OUT':
                    if args[0][0] == '[' and args[0][-1] == ']':
                        op = table[op][2]
                        args[0] = args[0][1:-1]
                    elif args[0] in registers:
                        op = table[op][1]
                        args[0] = registers[args[0]]
                    else:
                        op = table[op][0]
                case 'END':
                    op, args = '0000', []
                case _:
                    pass

        yield op, args


def mov(args):
    match args[0] in registers:
        case True:
            match len(args[1]):
                case 4 if args[1][1:-1] in registers:
                    return '00D3', [registers[args[0]], registers[args[1][1:-1]]]
                case 6:
                    return '00D1', [registers[args[0]], args[1][1:-1]]
                case _:
                    return '00D0', [registers[args[0]], args[1]]
        case False:
            match args[0][1:-1] in registers:
                case True:
                    return '00D4', [registers[args[0][1:-1]], registers[args[1]]]
                case False:
                    return '00D2', [args[0][1:-1], registers[args[1]]]


def flatten(foo):
    for x in foo:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in flatten(x):
                yield y
        else:
            yield x


def tohex(val):
    return hex(val & 0xFFFF)[2:].zfill(4).upper()


def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if val & (1 << (bits - 1)) != 0:
        val -= (1 << bits)
    return val


def find_subs(program: list):
    sub_found = False
    subs = {}
    sub = []
    main = []
    name = ''
    for lineno in range(len(program)):
        if '.sub(' in program[lineno][0]:
            name = program[lineno][0][5:-2]
            sub = []
            sub_found = True
            sub.append((program[lineno][0][5:-2] + ':', []))
        elif sub_found and program[lineno][0] != '.endsub:':
            sub.append(program[lineno])
        elif program[lineno][0] == '.endsub:':
            subs[name] = sub
            sub_found = False
        else:
            main.append(program[lineno])
    return main, subs


def find_jumps(program):
    matches = {}
    l = program[:]
    for item in l:
        if item.endswith(':'):
            matches[item[:-1]] = l.index(item)
            l.remove(item)
    for i in range(len(l)):
        if l[i] in jumps.values():
            if l[i + 1] in matches.keys():
                print('Jump to', l[i + 1], end='')
                l[i + 1] = tohex(matches[l[i + 1]] - i)
                print(' =', twos_comp(int(l[i + 1], 16), 16))
    return l


def make_callable(program, calls):
    call = False
    out = []
    count = 0
    for i in range(len(program)):
        if program[i] == '0A00':
            call = True
            continue
        elif call:
            out.append(calls[program[i]])
            program[i] = out[-1]
            count += 1
            call = False
    return program, out


def load(program, fname):
    memory = ram.RAM()
    settings = None
    if fname + '.dripc' in os.listdir('.'):
        grind = Grind.Grind(file=fname + '.drip', config=fname + '.dripc')
        print(grind.subs, grind.switches)
        grind.sub()
        program = grind.out()
        if grind.switches:
            settings = grind.switches
    program = list(tokenize(program))
    var_table = {}
    for var in d:
        name, val = var
        var_table[name] = val
    program, subs = find_subs(program)
    subs2 = []
    sub_locs = {}
    sub_loc = 0
    for sub in subs:
        subs2.append(find_jumps(list(flatten(parse(subs[sub])))))
        sub_locs[sub] = tohex(sub_loc)
        sub_loc += len(subs2[-1])
    subs = subs2
    del subs2
    program, call_table, = make_callable(find_jumps(list(flatten(parse(program)))), sub_locs)
    sub_list = list(flatten(subs))
    program = sub_list + program
    base = int('FF00', 16)
    var_table_ref = {}
    address = int('FE00', 16)
    for varname in var_table:
        save = address
        var_table_ref[varname] = address
        print(varname, '-->', var_table[varname])
        for item in var_table[varname]:
            memory.put(tohex(address), item)
            address += 1
        address = save - 256
    final = program[:]
    for i in range(len(final)):
        if final[i][0] == '[':
            final[i] = final[i][1:-1]
        if final[i] in var_table_ref:
            final[i] = tohex(var_table_ref[final[i]])
    for i in range(len(final)):
        memory.put(tohex(i), final[i])
    for address, call in enumerate(call_table):
        memory.put(tohex(base + address), call)
    memory.show()
    return memory, len(list(flatten(subs)))
