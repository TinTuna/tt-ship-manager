class Mod:
    def __init__(self, name, author, files_touched):
        self.name = name
        self.author = author
        self.files_touched = files_touched
    def __getattr__(self, item):
        return super().__getattribute__(item)
    def __setattr__(self, att_name, value):
        super().__setattr__(att_name, value)