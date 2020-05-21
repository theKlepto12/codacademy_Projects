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
            return listing


veneer = Marketplace()
# print(veneer.show_listings())


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = type(bool)

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            added_listing = Listing(artwork, price, self)
            veneer.add_listing(added_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)


edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art(
    "Picasso, Pablo",
    "Girl with a Mandolin (Fanny Tellier)",
    1910,
    "oil on canvas",
    edytta,
)

# print(girl_with_mandolin)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return self.art.title + " is selling for " + self.price


edytta.sell_artwork(girl_with_mandolin, "6M (USD)")
print(veneer.show_listings())

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)

print(veneer.show_listings())
