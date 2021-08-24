class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(0, self.pages)]
        self.index = 0
        self.photo = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(int(photos_count / 4))

    def add_photo(self, label):
        if len(self.photos[-1]) == 4:
            return "No more free slots"
        if len(self.photos[self.index]) == 4:
            self.index += 1
            self.photo = 0
        self.photos[self.index].append(label)
        self.photo += 1
        return f"{label} photo added successfully on page {self.index + 1} slot {self.photo}"

    def display(self):
        result = ""
        for page in self.photos:
            result_photos = ["[]" for _ in page]
            result += "-----------\n"
            result += f"{' '.join(result_photos)}\n"
        result += "-----------"
        return result
