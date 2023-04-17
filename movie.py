import csv


class Movie:
    def __init__(self, title, release_year, story_year):
        self.title = title
        self.release_year = release_year
        self.story_year = story_year

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_release_year(self):
        return self.release_year

    def set_release_year(self, release_year):
        self.release_year = release_year

    def get_story_year(self):
        return self.story_year

    def set_story_year(self, story_year):
        self.story_year = story_year


movies_list = []

try:
    with open('MarvelMovies.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            title = row[0]
            release_year = int(row[1])
            story_year = int(row[2])
            movie = Movie(title, release_year, story_year)

            movies_list.append(movie)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)


def sort_by_title(movie):
    return movie.get_title()


movies_list.sort(key=sort_by_title)

print("Title\t\tRelease Year\tStory Year")
print("---------------------------------------------")
for movie in movies_list:
    print(f"{movie.get_title()}\t{movie.get_release_year()}\t\t{movie.get_story_year()}")
