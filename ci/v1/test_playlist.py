"""
Test the *_original_artist routines.

These tests are invoked by running `pytest` with the
appropriate options and environment variables, as
defined in `conftest.py`.
"""

# Standard libraries

# Installed packages
import pytest

# Local modules
import playlist


@pytest.fixture
def mserv(request, playlist_url, auth):
    return playlist.playlist(playlist_url, auth)


@pytest.fixture
def aplaylist(request):
    # Recorded 1956
    return ('list1', ['song1', 'song2'])


def test_simple_run(mserv, aplaylist):
    trc, p_id = mserv.create(aplaylist[0], aplaylist[1])
    assert trc == 200
    trc, listname, songs = mserv.read(p_id)
    assert (trc == 200 and listname == aplaylist[0] and songs == aplaylist[1])
    mserv.delete(p_id)
    # No status to check
