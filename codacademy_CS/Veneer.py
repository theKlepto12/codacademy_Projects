class Art:
    def __init__(self, artist, title, year, medium):
        self.artist = artist
        self.title = title
        self.year = year
        self.medium = medium

    def __repr__(self):
        return (
            self.artist
            + '. "'
            + self.title
            + '". '
            + str(self.year)
            + ", "
            + self.medium
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


girl_with_mandolin = Art(
    "Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas"
)

print(girl_with_mandolin)

veneer = Marketplace()
print(veneer.show_listings())
