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
import user


@pytest.fixture
def mserv(request, user_url, auth):
    return user.user(user_url, auth)


@pytest.fixture
def auser(request):
    # Recorded 1956
    return ('e@example.com', 'first', 'last')


def test_simple_run(mserv, auser):
    trc, u_id = mserv.create(auser[0], auser[1], auser[2])
    assert trc == 200
    trc, email, fname, lname = mserv.read(u_id)
    assert (trc == 200 and email == auser[0] and fname == auser[1]
            and lname == auser[2])
    mserv.delete(u_id)
    # No status to check
