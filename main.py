def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  word_count = get_word_count(book_text)
  letter_count = get_letter_count(book_text)
  letter_count_lst = convert_dict_to_lst(letter_count)
  
  print("--- Begin report of book/frankenstein.txt ---")
  # print(book_text)
  print(f"There are {word_count} words in the book\n")
  # print(letter_count)
  print_letter_count_lst(letter_count_lst)
  print("--- End report ---\n")


def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_word_count(text):
  words = text.split()
  return len(words)

def get_letter_count(text):
  count = {}

  for letter in text:
    lowerd_letter = letter.lower()
    if lowerd_letter in count:
      count[lowerd_letter] += 1
    else:
      count[lowerd_letter] = 1
  
  return count

def convert_dict_to_lst(count):
  count_lst = []
  for item in count:
    count_lst.append({"letter":item, "count":count[item]})
  count_lst.sort(reverse=True, key=sort_on)
  return count_lst

def sort_on(dict):
  return dict["count"]

def print_letter_count_lst(lst):
  for item in lst:
    if(item["letter"].isalpha()):
      print(f"the '{item["letter"]}' character was found {item["count"]} times")



main()