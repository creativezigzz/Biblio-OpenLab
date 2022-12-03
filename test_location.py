import pytest
from lib.location import Location, Section


def test_number_of_sections():
    path = ['./Locations/Section 1', '/.Locations/Section 2']
    loc = Location('L101')
    loc.add_sections()
    section_1 = Section(path[0])
    section_2 = Section(path[0])
    assert section_1 != section_2
    assert isinstance(loc.sections, list)
    assert isinstance(loc.sections[0], Section)
    