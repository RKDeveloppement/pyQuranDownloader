import pyQuranDownloader

save_directory = "Quran"

# Download the recitations of the reciters you like the most.
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