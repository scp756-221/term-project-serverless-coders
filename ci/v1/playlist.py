"""
Python  API for the playlist service.
"""

# Standard library modules

# Installed packages
import requests


class playlist():
    """Python API for the playlist service.

    Handles the details of formatting HTTP requests and decoding
    the results.

    Parameters
    ----------
    url: string
        The URL for accessing the playlist service. Often
        'http://cmpt756s2:30001/'. Note the trailing slash.
    auth: string
        Authorization code to pass to the playlist service. For many
        implementations, the code is required but its content is
        ignored.
    """
    def __init__(self, url, auth):
        self._url = url
        self._auth = auth

    def create(self, name, songs):
        """Create an artist, song pair.

        Parameters
        ----------
        artist: string
            The artist performing song.
        song: string
            The name of the song.
        orig_artist: string or None
            The name of the original performer of this song.

        Returns
        -------
        (number, string)
            The number is the HTTP status code returned by playlist.
            The string is the UUID of this song in the playlist database.
        """
        payload = {'ListName': name,
                   'Songs': songs}
        r = requests.post(
            self._url,
            json=payload,
            headers={'Authorization': self._auth}
        )
        return r.status_code, r.json()['playlist_id']

    def read(self, p_id):
        """Read an artist, song pair.

        Parameters
        ----------
        m_id: string
            The UUID of this song in the playlist database.

        Returns
        -------
        status, artist, title, orig_artist

        status: number
            The HTTP status code returned by playlist.
        artist: If status is 200, the artist performing the song.
          If status is not 200, None.
        title: If status is 200, the title of the song.
          If status is not 200, None.
        orig_artist: If status is 200 and the song has an
          original artist field, the artist's name.
          If the status is not 200 or there is no original artist
          field, None.
        """
        r = requests.get(
            self._url + p_id,
            headers={'Authorization': self._auth}
            )
        if r.status_code != 200:
            return r.status_code, None, None, None

        item = r.json()['Items'][0]
        return r.status_code, item['ListName'], item['Songs']

    def delete(self, p_id):
        """Delete an artist, song pair.

        Parameters
        ----------
        m_id: string
            The UUID of this song in the playlist database.

        Returns
        -------
        Does not return anything. The playlist delete operation
        always returns 200, HTTP success.
        """
        requests.delete(
            self._url + p_id,
            headers={'Authorization': self._auth}
        )