from .__reciter import Reciters

import os
from typing import List, Type
from time import sleep
from threading import Thread, active_count

from urllib3 import PoolManager

def is_downloaded(*,
        sheikhs: List[Type['Reciters._Any']] = Reciters.ALL,
        directory: str = 'Quran'
    ) -> bool:
    """
    Checks if audio files for the specified reciters are downloaded.

    Args:
        sheikhs (List[Type['Reciters._Any']], optional): The list of reciters to check.
            By default, all reciters are checked. Use `Reciters.ALL` for all reciters.
        directory (str, optional): The directory where the audio files are stored.
            By default, the directory is 'Quran'.

    Returns:
        bool: True if all files are downloaded, otherwise False.

    Raises:
        AssertionError: If the 'directory' parameter is not a string.
        AssertionError: If a specified reciter does not belong to the list of available reciters.

    Example:
        >>> is_downloaded(sheikhs=[Reciters.MISHARY_AL_AFASY, Reciters.MUHAMMAD_AL_LUHAIDAN], directory='AudioFiles')
        True
    """
    assert isinstance(directory, str), f"directory parameter must be str, not {type(directory)}"

    for sheikh in sheikhs:
        assert sheikh in Reciters.ALL, f"{sheikh} n'appartient pas à pyQuranDownloader.Reciters"
        for i in range(1, 115):
            if not os.path.isfile(f"{directory}/{sheikh.ID}/{i:03d}.mp3"):
                return False
    return True

def download(*,
        sheikhs: List[Type['Reciters._Any']] = Reciters.ALL,
        directory: str = 'Quran',
        max_threads: int = 10,
        inbackground: bool = False
    ):
    """
    Downloads audio files for the specified reciters.

    Args:
        sheikhs (List[Type['Reciters._Any']], optional): The list of reciters to download.
            By default, all reciters are downloaded. Use `Reciters.ALL` for all reciters.
        directory (str, optional): The directory where the audio files will be stored.
            By default, the directory is 'Quran'.
        max_threads (int, optional): The maximum number of threads for concurrent downloads.
            Default is 10.
        inbackground (bool, optional): If True, the download will run in the background as a separate thread.
            If False, the download will be synchronous and block the main thread until complete.
            Default is False.

    Raises:
        AssertionError: If any of the input parameters have incorrect types.

    Example:
        >>> download(sheikhs=[Reciters.MISHARY_AL_AFASY, Reciters.MUHAMMAD_AL_LUHAIDAN], directory='AudioFiles', max_threads=5, inbackground=True)
    """
    assert isinstance(directory, str), f"directory parameter must be str, not {type(directory)}"
    assert isinstance(max_threads, int), f"max_threads parameter must be int, not {type(max_threads)}"
    assert isinstance(inbackground, bool), f"inbackground parameter must be bool, not {type(inbackground)}"
    for sheikh in sheikhs:
        assert sheikh in Reciters.ALL, f"{sheikh} n'appartient pas à pyQuranDownloader.Reciters"
        if not os.path.isdir(f"{directory}/{sheikh.ID}"):
            os.makedirs(f"{directory}/{sheikh.ID}")
    if directory.endswith('/'):
        directory = directory[:-1]
    if directory.startswith('/'):
        directory = directory[1:]
    __downloadquran(sheikhs=sheikhs, path=directory, max_threads=max_threads, inbackground=inbackground)

def __downloadquran(sheikhs: List[Reciters._Any], path: str, max_threads: int, inbackground: bool):
    for sheikh in sheikhs:
        http = PoolManager()
        base_url = f"https://{sheikh.DOWNLOADSERVER}.mp3quran.net/{sheikh.ID}"
        for i in range(1, 115):
            url = f"{base_url}/{i:03d}.mp3"
            started = False
            while not started:
                if active_count() < max_threads:
                    Thread(target=__startdownload, args=(http, url, f"{path}/{sheikh.ID}/{url[-7:]}")).start()
                    started = True
                else:
                    sleep(0.5)
            if not inbackground:
                console_size = os.get_terminal_size()
                message = f"Downloading {sheikh.NAME} ({int((i*100)//114)}%)..."
                message += (' ' * (console_size.columns - len(message) - 1))
                if console_size.columns > len(message):
                    print(message, end="\r")
    if not inbackground:
        print()

def __startdownload(http: PoolManager, url: str, path: str):
    with open(file=path, mode="wb+") as saveQuran:
        response = http.urlopen('GET', url)
        saveQuran.write(response.data)