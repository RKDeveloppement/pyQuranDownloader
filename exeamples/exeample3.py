import pyQuranDownloader

reciter_name = "Maher Al Muaiqly"

# Retrieve the information based on the reciter's ID or full name.
reciter_data = pyQuranDownloader.get_reciter(name=reciter_name) # args: <name: str, id: str>
reciter_data.ID
# > maher
reciter_data.RIWAYAT
# > Hafs (A'n 'Aasim)
reciter_data.IMGLINK
# > https://i.pinimg.com/564x/26/5d/3b/265d3b30f8d48c7acfc92d27d31c72ee.jpg

# and other information: ID, NAME, RIWAYAT, BIOGRAPHY, IMG, DOWNLOADSERVER