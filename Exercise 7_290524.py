class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("The numerator and denominator must be integers.")
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1
            a = abs(numerator)
            b = abs(denominator)
            while b != 0:
                a, b = b, a % b
            self._numerator = abs(numerator) // a * sign
            self._denominator = abs(denominator) // a

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self + Fraction(other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator - self._denominator * other._numerator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self - Fraction(other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._numerator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self * Fraction(other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other._numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            new_numerator = self._numerator * other._denominator
            new_denominator = self._denominator * other._numerator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self / Fraction(other)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self._numerator * other._denominator == self._denominator * other._numerator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self._numerator * other._denominator < self._denominator * other._numerator
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self._numerator * other._denominator <= self._denominator * other._numerator
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self._numerator * other._denominator > self._denominator * other._numerator
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self._numerator * other._denominator >= self._denominator * other._numerator
        return NotImplemented

    def __float__(self):
        return self._numerator / self._denominator

    def __int__(self):
        return self._numerator // self._denominator

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"


class BankAccount:
    account_counter = 0

    def __init__(self, balance=0):
        self.balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1

    def get_account_number(self):
        return self.account_number


class Family:
    def __init__(self, father, mother, *children):
        self.father = father
        self.mother = mother
        self.children = list(children)

    def __iter__(self):
        return iter(self.children)

    def add_child(self, child):
        self.children.append(child)

#Fraction
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2) 
print(f1 - f2)
print(f1 * f2)  
print(f1 / f2)  
print(float(f1))  
print(int(f1)) 
print(f1 == Fraction(2, 4)) 
print(f1 < f2) 
print(f1 <= f2)  
print(f1 > f2) 
print(f1 >= f2) 

#BankAccount
accounts = [BankAccount() for _ in range(5)]
for account in accounts:
    print(f"Account Number: {account.get_account_number()}")

#Family
family = Family("Father", "Mother", "Child1", "Child2")
for child in family:
    print(child)

#Adding another child
family.add_child("Child3")
for child in family:
    print(child)