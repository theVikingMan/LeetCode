from enum import Enum

class AccountStatus:
  available, reserved, checked_out = 1, 2, 3

class Book:
  def __init__(self, status=AccountStatus.available):
    self.status = status

b = Book()
print(b.status)