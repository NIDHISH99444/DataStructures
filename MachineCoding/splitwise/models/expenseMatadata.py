class ExpenseMetadata:
    def __init__(self, name, img_url, notes):
        self.name = name
        self.img_url = img_url
        self.notes = notes

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_img_url(self):
        return self.img_url

    def set_img_url(self, img_url):
        self.img_url = img_url

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes
