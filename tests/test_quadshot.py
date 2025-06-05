import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'QuadShot'))
import QuadShot
import ram


def test_twos_comp():
    assert QuadShot.twos_comp(0b11111111, 8) == -1
    assert QuadShot.twos_comp(0b00001111, 8) == 15


def test_sign_and_cmp():
    assert QuadShot.sign(-5) == -1
    assert QuadShot.sign(0) == 0
    assert QuadShot.sign(7) == 1
    assert QuadShot.cmp(5, 3) == 1
    assert QuadShot.cmp(3, 5) == -1
    assert QuadShot.cmp(4, 4) == 0


def test_ram_get_put():
    r = ram.RAM()
    r.put('010E', '12')
    assert r.get('010E') == '0012'


def test_swap():
    cpu = QuadShot.CPU()
    cpu.registers['0100'] = '12345678'
    cpu.swap(['0100'])
    assert cpu.registers['0100'] == '56781234'

def test_push_pop_private():
    cpu = QuadShot.CPU()
    cpu.push('private', 'ABCD')
    assert cpu.pop('private') == 'ABCD'

def test_fetch_decode():
    cpu = QuadShot.CPU()
    cpu.ram.put('0000', '00C0')
    cpu.ram.put('0001', '0001')
    func, args, forward, op = cpu.fetch('0000')
    assert func == cpu.jmp
    assert args == ['0001']
    assert forward == 1
    assert op == '00C0'

def test_cpu_run_simple():
    cpu = QuadShot.CPU()
    cpu.ram.put('0000', '00D0')
    cpu.ram.put('0001', '0001')
    cpu.ram.put('0002', '0001')
    cpu.ram.put('0003', '00A4')
    cpu.ram.put('0004', '0001')
    cpu.ram.put('0005', '0000')
    cpu.init = 0
    cpu.run()
    assert cpu.registers['0001'] == '0002'
