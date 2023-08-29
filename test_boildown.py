from boildown import projectRGB, bit
from operator import xor

class TestBit:
  def testOne(self):

    assert bit(0b0110, 0) == 0
    assert bit(0b0110, 1) == 1
    assert bit(0b0110, 2) == 1
    assert bit(0b0110, 3) == 0

  def test_two(self):

    assert bit(0b1110, 0) == 0
    assert bit(0b1110, 1) == 1
    assert bit(0b1110, 2) == 1
    assert bit(0b1110, 3) == 1


class TestBoilDown:

  def testWhite(self):

    input = (255,255,255)

    R2R1R0G1G0B2B1B0 = 0b11111111
    R5R4R3G4G3G2B4B3 = 0b11111111

    expected = xor(R2R1R0G1G0B2B1B0, R5R4R3G4G3G2B4B3)
    
    result = projectRGB(input)
    assert result == expected

  def testBlackAndWhite(self):

    input = (0b00001111, 0b00001111, 0b00001111)

    left = 0b11111111
    right = 0b00101101
    expected = xor(left, right)

    result = projectRGB(input)
    assert result == expected

