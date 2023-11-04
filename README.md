# pyQuranDownloader

![GitHub](https://img.shields.io/badge/GitHub-RKDeveloppement-8A2BE2)
![Version](https://img.shields.io/badge/Version-1.0.1-8A2BE2)

pyQuranDownloader is a Python3 module for downloading and managing Quran recitations of multiple reciters from mp3quran.net

## Supported Reciters
pyQuranDownloader supports downloading from multiple reciters, including:

- Maher Al Muaiqly
- Saoud Al-Shuraim
- Yasser Al-Dosari
- Muhammad Al-Luhaidan
- Ali Jaber
- Mishary Al Afasy
- Nasser Al Qatami

## Installation

To use this module, you can install it via pip:

```bash
pip install pyQuranDownloader
```

## Usage

Here are some basic examples of how to use the module :

```py
import pyQuranDownloader

# Create an instance of the downloader by selecting all the reciters and start the download.
pyQuranDownloader.download(
    sheikhs=pyQuranDownloader.Reciters.ALL,
    directory="Quran",
    max_threads=5,
    inbackground=True
)
```

```py
import pyQuranDownloader

save_directory = "Quran"

# Download the recitations of the reciters you like the most
if not pyQuranDownloader.is_downloaded(
    sheikhs=[pyQuranDownloader.Reciters.MAHER_AL_MUAIQLY, pyQuranDownloader.Reciters.YASSER_AL_DOSSARY],
    directory=save_directory):

    pyQuranDownloader.download(
        sheikhs=[
            pyQuranDownloader.Reciters.MAHER_AL_MUAIQLY,
            pyQuranDownloader.Reciters.YASSER_AL_DOSSARY
            ],
        directory=save_directory,
        max_threads=5,
        inbackground=True
    )
```

```py
import pyQuranDownloader

reciter_name = "Maher Al Muaiqly"

# Retrieve the information based on the reciter's ID or full nam
reciter_data = pyQuranDownloader.get_reciter(name=reciter_name) # args: <name: str, id: str>
>>> reciter_data.ID
# maher
>>> reciter_data.RIWAYAT
# Hafs (A'n 'Aasim)
>>> reciter_data.IMGLINK
# https://i.pinimg.com/564x/26/5d/3b/265d3b30f8d48c7acfc92d27d31c72ee.jpg
# and other information: (ID, NAME, RIWAYAT, BIOGRAPHY, IMGLINK, DOWNLOADSERVER)
```

## Author
This module was created by [RKDeveloppement](https://github.com/RKDeveloppement/).