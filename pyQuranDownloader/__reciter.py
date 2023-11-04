from typing import List, Type

def get_reciter(*,
        name: str = "",
        id: str = ""
    ) -> Type['Reciters._Any']:
    """
    Retrieves information about a reciter based on their name or ID.

    Args:
        name (str): The name of the reciter.
        or
        id (str): The unique identifier of the reciter.

    Returns:
        Type['Reciters._Any']: The reciter object.

    Raises:
        Exception: If neither 'name' nor 'id' is specified.
        Exception: If the specified reciter (by 'name' or 'id') is not found.

    Examples:
        >>> get_reciter(name='Saoud Al-Shuraim')
        <Reciters.SAOUD_AL_SHURAIM object at 0x...>

        >>> get_reciter(id='lhdan')
        <Reciters.MUHAMMAD_AL_LUHAIDAN object at 0x...>
    """
    if name == "" and id == "":
        raise Exception("pyQuranDownloader error: you must specify at least 1 arg, 'name': str or 'id': str")
    for reciter in Reciters.ALL:
        if reciter.ID.lower() == id.lower() or reciter.NAME.lower().replace(' ', '') == name.lower().replace(' ', ''):
            return reciter
    err = ""
    if name is None and id is not None:
        err += "id"
    elif id is None and name is not None:
        err += "name"
    else:
        err += "name or id"
    raise Exception(f"pyQuranDownloader error: reciter {err} not found ({id}).")

class Reciters:
    """
    Provides information about various Quran reciters.
    """

    class _Any:
        """
        Base class for reciters, containing common attributes.
        """
        ID: str = None
        NAME: str = None
        RIWAYAT: str = None
        BIOGRAPHY: str = None
        IMGLINK: str = None
        DOWNLOADSERVER: str = None

    class MAHER_AL_MUAIQLY(_Any):
        ID = "maher"
        NAME = "Maher Al Muaiqly"
        RIWAYAT = "Hafs (A'n 'Aasim)"
        BIOGRAPHY = "Né le 7 janvier 1969 à Médine il est un imam et prédicateur saoudien connu pour sa récitation du Coran."
        IMGLINK = "https://i.pinimg.com/564x/26/5d/3b/265d3b30f8d48c7acfc92d27d31c72ee.jpg"
        DOWNLOADSERVER = "server12"

    class SAOUD_AL_SHURAIM(_Any):
        ID = "shur"
        NAME = "Saoud Al-Shuraim"
        RIWAYAT = "Hafs (A'n 'Aasim)"
        BIOGRAPHY = "Né le 19 janvier 1964 à Riyad il est un célèbre imam et récitateur saoudien également imam de la grande mosquée de La Mecque"
        IMGLINK = "https://s-media-cache-ak0.pinimg.com/564x/41/75/00/4175004b89851b4d92d9ba543deba383.jpg"
        DOWNLOADSERVER = "server7"

    class YASSER_AL_DOSSARY(_Any):
        ID = "yasser"
        NAME = "Yasser Al-Dosari"
        RIWAYAT = "Hafs (A'n 'Aasim)"
        BIOGRAPHY = "Né en 1981 à Riyad il est un célèbre imam et récitateur saoudien reconnu pour sa psalmodie exceptionnelle du Coran."
        IMGLINK = "https://i.pinimg.com/564x/28/08/6e/28086e4bac69ea06098568974847d672.jpg"
        DOWNLOADSERVER = "server11"

    class MUHAMMAD_AL_LUHAIDAN(_Any):
        ID = "lhdan"
        NAME = "Muhammad Al-Luhaidan"
        RIWAYAT = "Hafs (A'n 'Aasim)"
        BIOGRAPHY = "Né en 1965 à Jeddah, il est un imam et récitateur saoudien reconnu pour sa récitation du Coran"
        IMGLINK = "https://i.pinimg.com/564x/a4/cd/74/a4cd749ed1726e63e8a62e279e5ea564.jpg"
        DOWNLOADSERVER = "server8"
    
    class ALI_JABER(_Any):
        ID = "a_jbr"
        NAME = "Ali Jaber"
        RIWAYAT = "Hafs (A'n 'Aasim)"
        BIOGRAPHY = "Né à Jeddah en Arabie Saoudite, il est un ancien imam à la grande mosquée de la Mecque"
        IMGLINK = "https://cdns-images.dzcdn.net/images/artist/b02b0e8820acd3940b727be95ca8ece9/500x500.jpg"
        DOWNLOADSERVER = "server11"

    class MISHARY_AL_AFASY(_Any):
        ID = "afs"
        NAME = "Mishary Al Afasy"
        RIWAYAT = "Hafs (A'n 'Aasim)"
        BIOGRAPHY = "Né le 5 septembre 1976 au Koweït il est récitateur et chanteur religieux renommé reconnu mondialement pour sa voix captivante."
        IMGLINK = "https://i.pinimg.com/564x/93/08/8b/93088be16e324b36b2d98a12748366a6.jpg"
        DOWNLOADSERVER = "server8"

    class NASSER_AL_QATAMI(_Any):
        ID = "qtm"
        NAME = "Nasser Al Qatami"
        RIWAYAT = "Hafs (A'n 'Aasim)"
        BIOGRAPHY = "Né le 18 janvier 1980 au Koweït est un célèbre récitateur du Coran. Sa voix exceptionnelle et sa précision dans la récitation en ont fait une référence mondiale."
        IMGLINK = "https://i.pinimg.com/564x/6f/2d/35/6f2d3586e913233f1f03ade207398949.jpg"
        DOWNLOADSERVER = "server6"
        
    ALL: List[Type['Reciters._Any']] = [MAHER_AL_MUAIQLY, SAOUD_AL_SHURAIM, YASSER_AL_DOSSARY, MUHAMMAD_AL_LUHAIDAN, ALI_JABER, MISHARY_AL_AFASY, NASSER_AL_QATAMI]
    
    ALL_HAFS_AN_HASHIM: List[Type['Reciters._Any']] = []
    for reciter in ALL:
        if reciter.RIWAYAT == "Hafs (A'n 'Aasim)":
            ALL_HAFS_AN_HASHIM.append(reciter)