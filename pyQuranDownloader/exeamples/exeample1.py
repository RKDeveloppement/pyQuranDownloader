import pyQuranDownloader

# Create an instance of the downloader by selecting all the reciters and start the download.
pyQuranDownloader.download(
    sheikhs=pyQuranDownloader.Reciters.ALL,
    directory="Quran",
    max_threads=5,
    inbackground=True
)