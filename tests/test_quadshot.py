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
