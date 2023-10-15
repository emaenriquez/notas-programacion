# Phone Book
# Create a phone book dictionary that maps names to phone numbers. Implement functions to add a new contact, update an existing contact, delete a contact, and lookup a contact by name.

phone_book = {}

def add_new_contact(name,phone_number):
    phone_book[name] = phone_number

def update_existing_contact(name,phone_number):
    phone_book[name] = phone_number

def delete_conctact(name):
    del phone_book[name]

def lookup_contact_by_name(name):
    if name in phone_book:
        valor_encontrado = phone_book.get(name)
        return valor_encontrado
    
add_new_contact("emanuel",45321221)
add_new_contact("rodrigo",32321212)
add_new_contact("matias",31313131)

update_existing_contact("matias",213131212)
delete_conctact("rodrigo")

lookup_contact = lookup_contact_by_name("emanuel")
print(lookup_contact)
print(phone_book)


# Word Frequency
# Write a function that takes a sentence as input and returns a dictionary with each word as the key and its frequency as the value. Ignore punctuation and consider words in a case-insensitive manner.

# Student Grades
# Create a dictionary that maps student names to a list of their grades. Implement functions to add a new student with their grades, remove a student, calculate the average grade for a given student, and determine the highest and lowest grade for each student.

# Letter Count in a String
# Write a function that takes a string as input and returns a dictionary with each letter as the key and its count as the value. Ignore spaces and consider letters in a case-insensitive manner.

# Dictionary Inversion
# Write a function that takes a dictionary as input and returns a new dictionary where keys and values are inverted. If multiple keys have the same value, the new dictionary should have a list of keys for that value.

# Scrabble Score Calculator
# Create a function that calculates the scrabble score for a given word. Each letter has a score, and you can use a dictionary to map letters to their respective scores.

# Population Data
# Create a dictionary that maps country names to their population. Implement functions to find the country with the largest population, the country with the smallest population, and the average population of all countries.
