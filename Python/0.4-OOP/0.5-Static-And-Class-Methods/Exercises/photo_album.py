from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [list() for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_count = ceil(photos_count / 4)
        return cls(pages_count)

    def add_photo(self, label: str):
        for r in range(len(self.photos)):
            if len(self.photos[r]) < PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page {r + 1} slot {len(self.photos[r])}"

        return f"No more free slots"

    def display(self):
        separation_line = '-' * 11
        res = []
        for page in self.photos:
            page = ['[]' for _ in range(len(page))]
            res.append(separation_line)
            res.append(' '.join(page))

        res.append(separation_line)
        return '\n'.join(res)
