# Translation Dictionary
# Create a translation dictionary to convert English words to Spanish. Implement functions to add new translations, lookup translations, and remove translations.

translation = {
    # 'ingles':'espanol'
}

def add_new_translations(translations_english,translations_spanish):
    translation[translations_english] = translations_spanish

def lookup_translations(translations_en):
    if translations_en in translation:
        return translation[translations_en]

def remove_translations(translations_en):
    if translations_en in translation:
        del translation[translations_en]

add_new_translations("Hi","hola")
add_new_translations("one","1")
add_new_translations("two","2")
add_new_translations("how","como")

lookup = lookup_translations("Hi")
remove_translations("one")
print(translation)
print(lookup)