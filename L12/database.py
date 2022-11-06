import json

class Database:
    def __init__(self, collection):  # collection : movies, books, games
        self.collection = collection
        self.collection_list = ["movies", "books", "games"]
        self.data = self.open_file()


    def open_file(self):
        for i in self.collection_list:
            if i == self.collection:
                with open(f"databases/{i}.json", 'r+') as f:
                    data = json.load(f)
        return data

    def update_existing_to_file(self, data, title):
        for i in self.collection_list:
            if i == self.collection:
                if list(data.keys())[0] in self.data:
                    self.data.update(data)
                if list(data.keys())[0] not in self.data:
                    self.data.update(data)
                    del self.data[title]


    def delete_from_file(self, to_delete):
        for i in self.collection_list:
            if i == self.collection:
                if to_delete in self.data:
                    del self.data[to_delete]


    def add_new(self, data):
        for i in self.collection_list:
            if i == self.collection:
                if list(data.keys())[0] not in self.data:
                    self.data.update(data)


    def write_to_file(self):
        for i in self.collection_list:
            if i == self.collection:
                with open(f"databases/{i}.json", 'w') as f:
                    json.dump(self.data, f)

    def search(self, key):
        for k in self.data:
            if k.lower() == key.lower():
                return self.data[k]


    # testing
    def show(self):
        return self.data


# # # testing
# update = {'Movie2': {'producer': 'Peter', 'description': 'This is a m testing it ', 'genre': '', 'year': '1200', 'picture': 'path to image'}}
# # add = {'Movie8': {'producer': 'Hello', 'description': 'This is a movie', 'genre': 'smt', 'year': '1200', 'picture': 'path to image'}}
# load_db = Database("movies")
# load_db.update_existing_to_file(update)
# # load_db.add_new(add)
# # # load_db.delete_from_file("Movie8")
# load_db.write_to_file()
# for i in load_db.show().items():
#     print(i)
# # print(load_db.search("Movie2"))
