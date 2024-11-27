from abc import ABC, abstractmethod
from typing import List
from entity.artwork import Artwork

class IvirtualArtGallery(ABC):

    @abstractmethod
    def addArtwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def updateArtwork(self, artwork: Artwork, artworkId: int) -> bool:
        pass

    @abstractmethod
    def removeArtwork(self, artworkId: int) -> bool:
        pass

    @abstractmethod
    def getArtworkById(self, artworkId: int) -> Artwork:
        pass

    @abstractmethod
    def searchArtworks(self, search_object: str) -> List[Artwork]:
        pass

    @abstractmethod
    def addArtworkToFavorite(self, userId: int, artworkId: int) -> bool:
        pass

    @abstractmethod
    def removeArtworkFromFavorite(self, userId: int, artworkId: int) -> bool:
        pass

    @abstractmethod
    def getUserFavoriteArtworks(self, userId: int) -> List[Artwork]:
        pass
