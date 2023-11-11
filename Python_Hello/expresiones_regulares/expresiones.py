
#  son secuencias de caracteres que conforman un patrón de búsqueda. En Python, se pueden utilizar para realizar operaciones de búsqueda y sustitución en cadenas de texto.
import re

# Compilamos la expresión regular
patron = re.compile('ab+c')
patron = re.compile('a.b*')

# Probamos la expresión regular con una cadena de texto
texto = 'abc'

res = re.search('ab',texto)
res = re.findall('ab',texto)

print(res)

# Realizamos la búsqueda
coincidencia = patron.match(texto)

# Comprobamos si hubo una coincidencia
if coincidencia:
    print('Se encontró una coincidencia')
else:
    print('No se encontró ninguna coincidencia')


# \d -- busca digitos de 0 - 9

texto_num = """hola comoe stas ff 1 9 3 2 tdo
bien y vos"""

busca_gititos_num = re.findall(r"\d",texto_num)

# print(busca_gititos_num)

# \D -- busca todos menos los digitos numericos

busca_todo_digito = re.findall(r"\D",texto_num)

# print(busca_todo_digito)

# \W -- busca todos menos los caracteres alfanumericos

busca_todo_caracter = re.findall(r"\W",texto_num)

print(busca_todo_caracter)

# \s -- busca espacios en blanco (tab, espacio, nueva linea)

texto_esp = """
    hola
como estas
ff

todas estas letras son espacios en blanco

bien y vos
"""

busca_espacios = re.findall(r"\s",texto_esp)

print(busca_espacios)

# \S -- busca todos menos los espacios en blanco

busca_todo_espacio = re.findall(r"\S",texto_esp)

print(busca_todo_espacio)

# . -- busca cualquier caracter (excepto nueva linea)

texto_dot = "abcdefg\n"

busca_cualquier_caracter = re.findall(r".",texto_dot)

print(busca_cualquier_caracter)

# [] -- busca cualquier caracter que se encuentre dentro de los corchetes

texto_brackets = "abcdefg\n"

busca_cualquier_caracter_brackets = re.findall(r"[abc]",texto_brackets)

print(busca_cualquier_caracter_brackets)

# ^ -- busca al inicio de la cadena

texto_start = "abcdefg\n"

busca_al_inicio = re.findall(r"^abc",texto_start)

print(busca_al_inicio)

# $ -- busca al final de la cadena

texto_end = "abcdefg\n"

busca_al_final = re.findall(r"fg$",texto_end)

print(busca_al_final)

# * -- busca cero o más repeticiones del caracter o grupo de caracteres precedente

texto_star = "abcdefg\n"

busca_repeticiones = re.findall(r"ab*c",texto_star)

print(busca_repeticiones)

# + -- busca una o más repeticiones del caracter o grupo de caracteres precedente

texto_plus = "abcdefg\n"

busca_una_mas_repeticiones = re.findall(r"ab+c",texto_plus)

print(busca_una_mas_repeticiones)

# ? -- busca cero o una repeticiones del caracter o grupo de caracteres precedente

texto_question = "abcdefg\n"

busca_cero_una_repeticiones = re.findall(r"ab?c",texto_question)

print(busca_cero_una_repeticiones)

# {m} -- busca exactamente m repeticiones del caracter o grupo de caracteres precedente

texto_exact_repetitions = "abcdefg\n"

busca_exact_m_repeticiones = re.findall(r"ab{2}c",texto_exact_repetitions)

print(busca_exact_m_repeticiones)

# {m,n} -- busca entre m y n repeticiones del caracter o grupo de caracteres precedente

texto_between_repetitions = "abcdefg\n"

busca_m_n_repeticiones = re.findall(r"ab{1,3}c",texto_between_repetitions)

print(busca_m_n_repeticiones)

# (...) -- agrupa los elementos que coinciden con el contenido de los paréntesis

texto_parentheses = "abcdefg\n"

busca_agrupado = re.findall(r"(ab)*c",texto_parentheses)

print(busca_agrupado)


