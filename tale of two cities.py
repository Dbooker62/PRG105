file_name = "tale_of_two_cities.txt"
word_counts = {}

with open(file_name, "r") as file:
    for line in file:

        words = line.strip().split()

        for word in words:

            word = word.lower()

            if word in word_counts:

                word_counts[word] += 1
            else:

                word_counts[word] = 1

    file.close()

unique_words = [word for word, count in word_counts.items() if count == 1]

print("Unique words:")
for word in unique_words:
    print(word)
