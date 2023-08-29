from boildown import projectRGB, bit, arrayProjection
from operator import xor
import numpy as np

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

class TestArrayProjection:

  def testOne(self):

    left = 0b11111111
    right = 0b00101101
    expected1 = xor(left, right)

    R2R1R0G1G0B2B1B0 = 0b11111111
    R5R4R3G4G3G2B4B3 = 0b11111111
    expected2 = xor(R2R1R0G1G0B2B1B0, R5R4R3G4G3G2B4B3)

    ar = np.array(
      [
        [
          [0b00001111, 0b00001111, 0b00001111],
          [0b11111111, 0b11111111, 0b11111111],
          [0b00001111, 0b00001111, 0b00001111]
        ],
        [
          [0b00001111, 0b00001111, 0b00001111],
          [0b00001111, 0b00001111, 0b00001111],
          [0b00001111, 0b00001111, 0b00001111]
        ]
      ]
    )

    result = np.apply_along_axis(projectRGB, 2, ar)

    assert result.shape == (2,3)
    assert result[0,0] == expected1
    assert result[0,1] == expected2


