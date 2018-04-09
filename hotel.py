import pytest

class Hotel:
  _guests = {}

  def check_in(self, guest_name, room_number):
    result = False
    if(room_number not in self._guests.values()):
      self._guests[guest_name] = room_number
      result = True
    return result

  def check_out(self, guest_name):
    del self._guests[guest_name]

  def guests(self):
    return self._guests.keys()

  
