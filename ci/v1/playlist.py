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
        """Create a playlist.

        Parameters
        ----------
        name: string
            The name of the playlist.
        songs: list of string
            Songs in the playlist.

        Returns
        -------
        (number, string)
            The number is the HTTP status code returned by playlist.
            The string is the UUID of this playlist in the playlist database.
        """
        payload = {'ListName': name,
                   'Songs': songs}
        r = requests.post(
            self._url,
            json=payload,
            headers={'Authorization': self._auth}
        )
        return r.status_code, r.json()['playlist_id']

    def add_song(self, p_id, song):
        payload = {'music_id': song}
        r = requests.put(
            self._url + 'add_song_to_list/' + p_id,
            json=payload,
            headers={'Authorization': self._auth}
            )
        return r.status_code

    def delete_song(self, p_id, song):
        payload = {'music_id': song}
        r = requests.put(
            self._url + 'delete_song_from_list/' + p_id,
            json=payload,
            headers={'Authorization': self._auth}
            )
        return r.status_code

    def read(self, p_id):
        """Read a playlist.

        Parameters
        ----------
        m_id: string
            The UUID of this playlist in the playlist database.

        Returns
        -------
        status, name, songs

        status: number
            The HTTP status code returned by playlist.
        name: If status is 200, the name of the playlist.
          If status is not 200, None.
        songs: If status is 200, the songs in the playlist.
          If status is not 200, None.
        """
        r = requests.get(
            self._url + p_id,
            headers={'Authorization': self._auth}
            )
        if r.status_code != 200:
            return r.status_code, None, None

        item = r.json()['Items'][0]
        return r.status_code, item['ListName'], item['Songs']

    def delete(self, p_id):
        """Delete a playlist.

        Parameters
        ----------
        m_id: string
            The UUID of this playlist in the playlist database.

        Returns
        -------
        Does not return anything. The playlist delete operation
        always returns 200, HTTP success.
        """
        requests.delete(
            self._url + p_id,
            headers={'Authorization': self._auth}
        )
