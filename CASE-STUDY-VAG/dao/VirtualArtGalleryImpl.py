'''from typing import List
from dao.IvirtualArtGallery import IvirtualArtGallery
from entity.artwork import Artwork
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from exception.UserNotFoundException import UserNotFoundException
from util.DBConnection import DBConnection
from tabulate import tabulate

class VirtualArtGalleryImpl(IvirtualArtGallery):
    def __init__(self):
        db_connection = DBConnection()  # Create an instance of DBConnection
        self.connection = db_connection.get_connection()  # Get DB connection

    def get_next_artworkID(self) -> int:
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT MAX(ArtworkID) FROM Artwork")
            max_id = cursor.fetchone()[0]
            return (max_id + 1) if max_id is not None else 1
        except Exception as e:
            print("Error in fetching next artwork ID:", e)
            return 1
        finally:
            cursor.close()

    def addArtwork(self, artwork: Artwork) -> bool:
        cursor = self.connection.cursor()
        try:
            query = """
                INSERT INTO Artwork (ArtworkID, Title, Description, CreationDate, Medium, ImageURL) 
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                self.get_next_artworkID(), 
                artwork.get_title(), 
                artwork.get_description(), 
                artwork.get_creationDate(), 
                artwork.get_medium(), 
                artwork.get_imageURL()
            ))
            self.connection.commit()
            print("------ Artwork added ------")
            return True
        except Exception as e:
            print("Error in adding artwork:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()
    
    def updateArtwork(self, artworkId: int, artwork: Artwork) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "UPDATE Artwork SET "
            params = []

            if artwork.get_title():
                query += "Title = ?, "
                params.append(artwork.get_title())
            if artwork.get_description():
                query += "Description = ?, "
                params.append(artwork.get_description())
            if artwork.get_creationDate():
                query += "CreationDate = ?, "
                params.append(artwork.get_creationDate())
            if artwork.get_medium():
                query += "Medium = ?, "
                params.append(artwork.get_medium())
            if artwork.get_imageURL():
                query += "ImageURL = ?, "
                params.append(artwork.get_imageURL())

            query = query.rstrip(", ")
            query += " WHERE ArtworkID = ?"
            params.append(artworkId)

            cursor.execute(query, tuple(params))
            self.connection.commit()
            print("------ Artwork updated ------")
            return True
        except Exception as e:
            print(f"Error in updating artwork: {e}")
            return False
        finally:
            cursor.close()

    def removeArtwork(self, artworkId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "SELECT COUNT(*) FROM Artwork WHERE ArtworkID = ?"
            cursor.execute(query, (artworkId,))
            count = cursor.fetchone()[0]
            if count == 0:
                raise ArtWorkNotFoundException(artworkId)

            cursor.execute("DELETE FROM Artwork WHERE ArtworkID = ?", (artworkId,))
            self.connection.commit()
            print("------ Artwork removed ------")
            return True
        except ArtWorkNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print("Error in removing artwork:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def getArtworkById(self, artworkId: int) -> Artwork:
        cursor = self.connection.cursor()
        try:
            query = "SELECT * FROM Artwork WHERE ArtworkID = ?"
            cursor.execute(query, (artworkId,))
            artwork = cursor.fetchone()
            if artwork is None:
                raise ArtWorkNotFoundException(artworkId)

            artwork_details = [
                ['ArtworkID', artwork[0]],
                ['Title', artwork[1]],
                ['Description', artwork[2]],
                ['CreationDate', artwork[3]],
                ['Medium', artwork[4]],
                ['ImageURL', artwork[5]]
            ]
            print(tabulate(artwork_details, tablefmt="grid"))
            return artwork
        except ArtWorkNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error in getting artwork details:", e)
        finally:
            cursor.close()

    def searchArtworks(self, search_object: str) -> List[Artwork]:
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT * FROM Artwork 
                WHERE Title LIKE ? OR Medium LIKE ? OR Description LIKE ?
            """
            cursor.execute(query, (f"%{search_object}%", f"%{search_object}%", f"%{search_object}%"))
            artwork_data = cursor.fetchall()
            artworks = [Artwork(*artwork) for artwork in artwork_data]

            if artworks:
                artwork_table = [[art.artworkId, art.title, art.description, art.creationDate, art.medium, art.imageURL] for art in artworks]
                print(tabulate(artwork_table, headers=["Artwork ID", "Title", "Description", "Creation Date", "Medium", "Image URL"], tablefmt="grid"))

            return artworks
        except Exception as e:
            print("Error in searching artworks:", e)
            return []
        finally:
            cursor.close()

    def addArtworkToFavorite(self, userId: int, artworkId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO User_Favorite_Artwork(UserID, ArtworkID) VALUES (?, ?)"
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            print("Added to favorites")
            return True
        except Exception as e:
            print("Error in adding to favorites:", e)
            return False
        finally:
            cursor.close()

    def removeArtworkFromFavorite(self, userId: int, artworkId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM User_Favorite_Artwork WHERE UserID = ? AND ArtworkID = ?"
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            print("Removed from favorites")
            return True
        except Exception as e:
            print("Error in removing from favorites:", e)
            return False
        finally:
            cursor.close()

    def getUserFavoriteArtworks(self, userId: int) -> List[Artwork]:
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT a.* 
                FROM Artwork a 
                JOIN User_Favorite_Artwork u 
                ON a.ArtworkID = u.ArtworkID 
                WHERE u.UserID = ?
            """
            cursor.execute(query, (userId,))
            artworks = cursor.fetchall()
            return [Artwork(*artwork) for artwork in artworks]
        except Exception as e:
            print("Error in fetching favorite artworks:", e)
            return []
        finally:
            cursor.close()
'''
from typing import List
from dao.IvirtualArtGallery import IvirtualArtGallery
from entity.artwork import Artwork
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from exception.UserNotFoundException import UserNotFoundException
from util.DBConnection import DBConnection
from tabulate import tabulate

class VirtualArtGalleryImpl(IvirtualArtGallery):
    def __init__(self):
        db_connection = DBConnection()  # Create an instance of DBConnection
        self.connection = db_connection.get_connection()  # Get DB connection

    def get_next_artworkID(self) -> int:
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT MAX(ArtworkID) FROM Artwork")
            max_id = cursor.fetchone()[0]
            return (max_id + 1) if max_id is not None else 1
        except Exception as e:
            print("Error in fetching next artwork ID:", e)
            return 1
        finally:
            cursor.close()

    def addArtwork(self, artwork: Artwork) -> bool:
        cursor = self.connection.cursor()
        try:
            query = """
                INSERT INTO Artwork (ArtworkID, Title, Description, CreationDate, Medium, ImageURL) 
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                self.get_next_artworkID(), 
                artwork.get_title(), 
                artwork.get_description(), 
                artwork.get_creationDate(), 
                artwork.get_medium(), 
                artwork.get_imageURL()
            ))
            self.connection.commit()
            print("------ Artwork added ------")
            return True
        except Exception as e:
            print("Error in adding artwork:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def updateArtwork(self, artworkId: int, artwork: Artwork) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "UPDATE Artwork SET "
            params = []

            if artwork.get_title():
                query += "Title = ?, "
                params.append(artwork.get_title())
            if artwork.get_description():
                query += "Description = ?, "
                params.append(artwork.get_description())
            if artwork.get_creationDate():
                query += "CreationDate = ?, "
                params.append(artwork.get_creationDate())
            if artwork.get_medium():
                query += "Medium = ?, "
                params.append(artwork.get_medium())
            if artwork.get_imageURL():
                query += "ImageURL = ?, "
                params.append(artwork.get_imageURL())

            query = query.rstrip(", ")
            query += " WHERE ArtworkID = ?"
            params.append(artworkId)

            cursor.execute(query, tuple(params))
            self.connection.commit()
            print("------ Artwork updated ------")
            return True
        except Exception as e:
            print(f"Error in updating artwork: {e}")
            return False
        finally:
            cursor.close()

    def removeArtwork(self, artworkId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "SELECT COUNT(*) FROM Artwork WHERE ArtworkID = ?"
            cursor.execute(query, (artworkId,))
            count = cursor.fetchone()[0]
            if count == 0:
                raise ArtWorkNotFoundException(artworkId)

            cursor.execute("DELETE FROM Artwork WHERE ArtworkID = ?", (artworkId,))
            self.connection.commit()
            print("------ Artwork removed ------")
            return True
        except ArtWorkNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print("Error in removing artwork:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def getArtworkById(self, artworkId: int) -> Artwork:
        cursor = self.connection.cursor()
        try:
            query = "SELECT * FROM Artwork WHERE ArtworkID = ?"
            cursor.execute(query, (artworkId,))
            artwork = cursor.fetchone()
            if artwork is None:
                raise ArtWorkNotFoundException(artworkId)

            artwork_details = [
                ['ArtworkID', artwork[0]],
                ['Title', artwork[1]],
                ['Description', artwork[2]],
                ['CreationDate', artwork[3]],
                ['Medium', artwork[4]],
                ['ImageURL', artwork[5]]
            ]
            print(tabulate(artwork_details, tablefmt="grid"))
            return artwork
        except ArtWorkNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error in getting artwork details:", e)
        finally:
            cursor.close()

    def searchArtworks(self, search_object: str) -> List[Artwork]:
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT * FROM Artwork 
                WHERE Title LIKE ? OR Medium LIKE ? OR Description LIKE ?
            """
            cursor.execute(query, (f"%{search_object}%", f"%{search_object}%", f"%{search_object}%"))
            artwork_data = cursor.fetchall()
            artworks = [Artwork(*artwork) for artwork in artwork_data]

            if artworks:
                artwork_table = [[art.artworkId, art.title, art.description, art.creationDate, art.medium, art.imageURL] for art in artworks]
                print(tabulate(artwork_table, headers=["Artwork ID", "Title", "Description", "Creation Date", "Medium", "Image URL"], tablefmt="grid"))

            return artworks
        except Exception as e:
            print("Error in searching artworks:", e)
            return []
        finally:
            cursor.close()

    def addArtworkToFavorite(self, userId: int, artworkId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO User_Favorite_Artwork(UserID, ArtworkID) VALUES (?, ?)"
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            print("Added to favorites")
            return True
        except Exception as e:
            print("Error in adding to favorites:", e)
            return False
        finally:
            cursor.close()

    def removeArtworkFromFavorite(self, userId: int, artworkId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM User_Favorite_Artwork WHERE UserID = ? AND ArtworkID = ?"
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            print("Removed from favorites")
            return True
        except Exception as e:
            print("Error in removing from favorites:", e)
            return False
        finally:
            cursor.close()

    def getUserFavoriteArtworks(self, userId: int) -> List[Artwork]:
        cursor = self.connection.cursor()
        try:
            query = """
                SELECT a.* 
                FROM Artwork a 
                JOIN User_Favorite_Artwork u 
                ON a.ArtworkID = u.ArtworkID 
                WHERE u.UserID = ?
            """
            cursor.execute(query, (userId,))
            artworks = cursor.fetchall()

            # Debugging: print out the fetched data
            print(f"Artworks fetched for user {userId}: {artworks}")

            if not artworks:
                print(f"No favorite artworks found for user {userId}")
                return []

            return [Artwork(*artwork) for artwork in artworks]
        except Exception as e:
            print("Error in fetching favorite artworks:", e)
            return []
        finally:
            cursor.close()
