class Art:
    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.year = year
        self.medium = medium
        self.owner = owner

    def __repr__(self):
        return (
            self.artist
            + '. "'
            + self.title
            + '". '
            + str(self.year)
            + ", "
            + self.medium
            + ". "
            + self.owner.name
            + ", "
            + self.owner.location
            + "."
        )


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        for listing in self.listings:
            self.listings.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


veneer = Marketplace()
print(veneer.show_listings())


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = type(bool)


edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art(
    "Picasso, Pablo",
    "Girl with a Mandolin (Fanny Tellier)",
    1910,
    "oil on canvas",
    edytta,
)

print(girl_with_mandolin)
