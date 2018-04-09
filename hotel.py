import pytest

class Hotel:
  _guests = []

  def check_in(self, guest_name):
    self._guests.append(guest_name)

  def check_out(self, guest_name):
    self._guests.remove(guest_name)

  def guests(self):
    return self._guests

def test_check_in_a_guest():
  hotel = Hotel()
  hotel.check_in('Bob Barker')
  assert(('Bob Barker' in hotel.guests()) == True)

def test_check_out_a_guest():
  hotel = Hotel()
  hotel.check_in('Bob Dylan')
  hotel.check_out('Bob Dylan')
  assert(('Bob Dylan' in hotel.guests()) == False)
