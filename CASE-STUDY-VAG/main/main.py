'''from tabulate import tabulate
from exception.UserNotFoundException import UserNotFoundException
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.artwork import Artwork


class MainModule:
    def __init__(self):
        self.service = VirtualArtGalleryImpl()

    def menu(self):
        print("*" * 50)
        print("Welcome to Virtual Art Gallery")
        print("*" * 50)
        while True:
            menu = [
                ["1.", "Add artwork"],
                ["2.", "Update artwork"],
                ["3.", "Remove artwork"],
                ["4.", "Get Artwork By ID"],
                ["5.", "Search artworks"],
                ["6.", "Add Artwork To Favorite"],
                ["7.", "Remove Artwork From Favorite"],
                ["8", "Get User Favorite Artworks"],
                ["9", "Exit"]
            ]

            print(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))

            choice = input("Enter your choice: ")

            if choice == "1":
                artworkId = self.service.get_next_artworkID()
                title = input("Enter artwork title: ")
                description = input("Enter artwork description: ")
                creationDate = input("Enter artwork creation date: ")
                medium = input("Enter artwork medium: ")
                imageUrl = input("Enter artwork image url: ")
                if artworkId is None:
                    print("-------Artwork ID cannot be null------")
                else:
                    artwork = Artwork(
                        artworkId=artworkId,
                        title=title,
                        description=description,
                        creationDate=creationDate,
                        medium=medium,
                        imageURL=imageUrl
                    )
                    self.service.addArtwork(artwork)

            elif choice == "2":
                try:
                    artworkId = int(input("Enter Artwork ID to update: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Artwork WHERE ArtworkID=?"
                    cursor.execute(query, (artworkId,))
                    if cursor.fetchone() is None:
                        raise ArtWorkNotFoundException(artworkId)

                    newTitle = input("Enter new artwork title (leave blank to skip): ")
                    newDescription = input("Enter new artwork description (leave blank to skip): ")
                    newCreationDate = input("Enter new artwork creation date (leave blank to skip): ")
                    newMedium = input("Enter new artwork medium (leave blank to skip): ")
                    newImageUrl = input("Enter new artwork image URL (leave blank to skip): ")

                    artwork = Artwork(
                        artworkId=artworkId,
                        title=newTitle if newTitle else None,
                        description=newDescription if newDescription else None,
                        creationDate=newCreationDate if newCreationDate else None,
                        medium=newMedium if newMedium else None,
                        imageURL=newImageUrl if newImageUrl else None
                    )

                    # Corrected the order of arguments here
                    self.service.updateArtwork(artworkId, artwork)
                except ArtWorkNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("An unexpected error occurred:", e)

            elif choice == "3":
                try:
                    artworkId = int(input("Enter Artwork ID to remove: "))
                except Exception as e:
                    print("Invalid input for Artwork ID.", e)
                    continue
                self.service.removeArtwork(artworkId)

            elif choice == "4":
                try:
                    artworkId = int(input("Enter Artwork ID to get details: "))
                    self.service.getArtworkById(artworkId)
                except Exception as e:
                    print("Invalid input:", e)

            elif choice == "5":
                search_object = input("Enter Search Object: ")
                self.service.searchArtworks(search_object)

            elif choice == "6":
                try:
                    userID = int(input("Enter User ID: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Users WHERE UserID=?"
                    cursor.execute(query, (userID,))
                    if cursor.fetchone() is None:
                        raise UserNotFoundException(userID)
                    artworkId = int(input("Enter Artwork ID to add to favourites: "))
                    self.service.addArtworkToFavorite(userID, artworkId)
                except UserNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Invalid input:", e)

            elif choice == "7":
                try:
                    userID = int(input("Enter User ID: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Users WHERE UserID=?"
                    cursor.execute(query, (userID,))
                    if cursor.fetchone() is None:
                        raise UserNotFoundException(userID)

                    artworkId = int(input("Enter Artwork ID to remove favourites: "))
                    self.service.removeArtworkFromFavorite(userID, artworkId)
                except UserNotFoundException as ue:
                    print("Error:", ue)
                except Exception as e:
                    print('Invalid input:', e)

            elif choice == "8":
    try:
        userID = int(input("Enter User ID: "))
        favorite_artworks = self.service.getUserFavoriteArtworks(userID)  # Get the favorite artworks

        if favorite_artworks:
            artwork_table = [[art.artworkId, art.title, art.description, art.creationDate, art.medium, art.imageURL] for art in favorite_artworks]
            print(tabulate(artwork_table, headers=["Artwork ID", "Title", "Description", "Creation Date", "Medium", "Image URL"], tablefmt="grid"))
        else:
            print(f"No favorite artworks found for user with ID {userID}.")
    except Exception as e:
        print("Invalid input:", e)


    

            elif choice == "9":
                print("Thank you for using Virtual Art Gallery!")
                break
            else:
                print("Invalid Choice. Try again")


if __name__ == '__main__':
    MainModule().menu()
'''
import sys
import os

# Add the root directory of the project to sys.path
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(case study-vag),'C:\Users\mubee\Downloads\case study-vag\case study-vag\util\PropertyFile.txt')))

from exception.UserNotFoundException import UserNotFoundException

from tabulate import tabulate
from exception.UserNotFoundException import UserNotFoundException
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.artwork import Artwork


class MainModule:
    def __init__(self):
        self.service = VirtualArtGalleryImpl()

    def menu(self):
        print("*" * 50)
        print("Welcome to Virtual Art Gallery")
        print("*" * 50)
        while True:
            menu = [
                ["1.", "Add artwork"],
                ["2.", "Update artwork"],
                ["3.", "Remove artwork"],
                ["4.", "Get Artwork By ID"],
                ["5.", "Search artworks"],
                ["6.", "Add Artwork To Favorite"],
                ["7.", "Remove Artwork From Favorite"],
                ["8", "Get User Favorite Artworks"],
                ["9", "Exit"]
            ]

            print(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))

            choice = input("Enter your choice: ")

            if choice == "1":
                artworkId = self.service.get_next_artworkID()
                title = input("Enter artwork title: ")
                description = input("Enter artwork description: ")
                creationDate = input("Enter artwork creation date: ")
                medium = input("Enter artwork medium: ")
                imageUrl = input("Enter artwork image url: ")
                if artworkId is None:
                    print("-------Artwork ID cannot be null------")
                else:
                    artwork = Artwork(
                        artworkId=artworkId,
                        title=title,
                        description=description,
                        creationDate=creationDate,
                        medium=medium,
                        imageURL=imageUrl
                    )
                    self.service.addArtwork(artwork)

            elif choice == "2":
                try:
                    artworkId = int(input("Enter Artwork ID to update: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Artwork WHERE ArtworkID=?"
                    cursor.execute(query, (artworkId,))
                    if cursor.fetchone() is None:
                        raise ArtWorkNotFoundException(artworkId)

                    newTitle = input("Enter new artwork title (leave blank to skip): ")
                    newDescription = input("Enter new artwork description (leave blank to skip): ")
                    newCreationDate = input("Enter new artwork creation date (leave blank to skip): ")
                    newMedium = input("Enter new artwork medium (leave blank to skip): ")
                    newImageUrl = input("Enter new artwork image URL (leave blank to skip): ")

                    artwork = Artwork(
                        artworkId=artworkId,
                        title=newTitle if newTitle else None,
                        description=newDescription if newDescription else None,
                        creationDate=newCreationDate if newCreationDate else None,
                        medium=newMedium if newMedium else None,
                        imageURL=newImageUrl if newImageUrl else None
                    )

                    # Corrected the order of arguments here
                    self.service.updateArtwork(artworkId, artwork)
                except ArtWorkNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("An unexpected error occurred:", e)

            elif choice == "3":
                try:
                    artworkId = int(input("Enter Artwork ID to remove: "))
                except Exception as e:
                    print("Invalid input for Artwork ID.", e)
                    continue
                self.service.removeArtwork(artworkId)

            elif choice == "4":
                try:
                    artworkId = int(input("Enter Artwork ID to get details: "))
                    self.service.getArtworkById(artworkId)
                except Exception as e:
                    print("Invalid input:", e)

            elif choice == "5":
                search_object = input("Enter Search Object: ")
                self.service.searchArtworks(search_object)

            elif choice == "6":
                try:
                    userID = int(input("Enter User ID: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Users WHERE UserID=?"
                    cursor.execute(query, (userID,))
                    if cursor.fetchone() is None:
                        raise UserNotFoundException(userID)
                    artworkId = int(input("Enter Artwork ID to add to favourites: "))
                    self.service.addArtworkToFavorite(userID, artworkId)
                except UserNotFoundException as e:
                    print("Error:", e)
                except Exception as e:
                    print("Invalid input:", e)

            elif choice == "7":
                try:
                    userID = int(input("Enter User ID: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Users WHERE UserID=?"
                    cursor.execute(query, (userID,))
                    if cursor.fetchone() is None:
                        raise UserNotFoundException(userID)

                    artworkId = int(input("Enter Artwork ID to remove favourites: "))
                    self.service.removeArtworkFromFavorite(userID, artworkId)
                except UserNotFoundException as ue:
                    print("Error:", ue)
                except Exception as e:
                    print('Invalid input:', e)

            elif choice == "8":
                try:
                    userID = int(input("Enter User ID: "))
                    favorite_artworks = self.service.getUserFavoriteArtworks(userID)  # Get the favorite artworks

                    if favorite_artworks:
                        artwork_table = [[art.artworkId, art.title, art.description, art.creationDate, art.medium, art.imageURL] for art in favorite_artworks]
                        print(tabulate(artwork_table, headers=["Artwork ID", "Title", "Description", "Creation Date", "Medium", "Image URL"], tablefmt="grid"))
                    else:
                        print(f"No favorite artworks found for user with ID {userID}.")
                except Exception as e:
                    print("Invalid input:", e)

            elif choice == "9":
                print("Thank you for using Virtual Art Gallery!")
                break
            else:
                print("Invalid Choice. Try again")


if __name__ == '__main__':
    MainModule().menu()
