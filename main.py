def main():
    # Open the file and read its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # Split the contents into words and count them
    words = file_contents.split()
    word_count = len(words)

    # Initialize a dictionary to count occurrences of each letter
    letter_count = {}
    for letter in file_contents.lower():  # Convert to lowercase to count letters uniformly
        if letter.isalpha():  # Check if the character is a letter
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    # Convert the dictionary to a list of dictionaries for sorting
    letter_count_list = [{"letter": letter, "count": count} for letter, count in letter_count.items()]
    # Sort the list by the number of occurrences in descending order
    letter_count_list.sort(key=lambda x: x["count"], reverse=True)

    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Loop through the sorted list and print each letter's count
    for item in letter_count_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")

    print("--- End report ---")


main()
