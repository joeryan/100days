import pytest
from hotel import Hotel

def test_check_in_a_guest():
  hotel = Hotel()
  hotel.check_in('Bob Barker', 302)
  assert(('Bob Barker' in hotel.guests()) == True)

def test_does_not_accept_guest_in_occupied_room():
  hotel = Hotel()
  hotel.check_in('Bob Barker', 303)
  assert(hotel.check_in('Roy Orbison', 303) == False)

def test_accepts_guest_into_unoccupied_room():
  hotel = Hotel()
  hotel.check_in('Bob Barker', 303)
  assert(hotel.check_in('Roy Orbison', 305) == True)

def test_check_out_a_guest():
  hotel = Hotel()
  hotel.check_in('Bob Dylan', 306)
  hotel.check_out('Bob Dylan')
  assert(('Bob Dylan' in hotel.guests()) == False)

def test_check_out_a_guest_releases_room():
  hotel = Hotel()
  hotel.check_in('Jim Maui', 301)
  hotel.check_out('Jim Maui')

