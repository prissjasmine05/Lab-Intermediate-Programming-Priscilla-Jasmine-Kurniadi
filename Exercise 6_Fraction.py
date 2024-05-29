class Fraction:
  def __init__(self, numerator, denominator):

    if denominator == 0:
      raise ZeroDivisionError("Denominator cannot be zero")
    self.numerator = numerator
    self.denominator = denominator

  def __str__(self):
    return f"{self.numerator}/{self.denominator}"

  def to_float(self):
    return self.numerator / self.denominator

fraction = Fraction(1, 3)

print("Fraction :", fraction)  
print("Fraction as float:", fraction.to_float())

############################################### punya sofi ##############

from fractions import Fraction as PyFraction

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        # Simplify the fraction using the fractions module
        fraction = PyFraction(self.numerator, self.denominator)
        self.numerator = fraction.numerator
        self.denominator = fraction.denominator

    def to_rational(self):
        return f"{self.numerator}/{self.denominator}"

    def to_float(self):
        return self.numerator / self.denominator

# Example usage
fraction = Fraction(2, 6)
print(fraction.to_rational())  # Output: 1/3
print(fraction.to_float())     # Output: 0.3333333333333333