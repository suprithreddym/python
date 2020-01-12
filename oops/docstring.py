class Song:
    """Class to represent a song

    Attributes:
        title:
        album:
        duration:
        """
    def __init__(self,title,album,duration=0):
        """song init method"""
        self.title = title
        self.album=album
        self.duration=duration


help(Song.__init__)
print('=' * 50)
print(Song.__doc__)
print('=' * 50)
print(Song.__init__.__doc__)
