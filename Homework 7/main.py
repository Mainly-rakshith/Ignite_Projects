# Name: Rakshith Jayakarthikeyan
# Assignment: PROG1003 - HW7 - Spelling

import string

def load_words(filename):
    word_list = set()
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                word_list.add(word)
    return word_list


def clean_token(token):
    # remove punctuation only from the start and end
    return token.strip(string.punctuation)


def check_spelling(text_file, dict_file):
    dictionary = load_words(dict_file)
    misspelled = []
    correct_counts = {}

    with open(text_file, "r", encoding="utf-8") as f:
        for line in f:
            for raw_word in line.split():
                word = clean_token(raw_word)
                if word == "":
                    continue
                key = word.lower()
                if key in dictionary:
                    correct_counts[key] = correct_counts.get(key, 0) + 1
                else:
                    misspelled.append(word)

    # Write misspelled words
    with open("misspelled_words.txt", "w", encoding="utf-8") as miss:
        for word in misspelled:
            miss.write(word + "\n")

    # Write correct words with counts (alphabetically)
    with open("correct_words.txt", "w", encoding="utf-8") as correct:
        for word in sorted(correct_counts.keys()):
            correct.write(word + " " + str(correct_counts[word]) + "\n")

    print("The following words are not spelled correctly:")
    for word in misspelled:
        print(word)


def main():
    filename = input("Enter file name: ").strip()
    check_spelling(filename, "words.txt")


if __name__ == "__main__":
    main()