def count_letter_a(s):
    count = s.lower().count('a')
    return count

# Exemplo de uso:
string = input("Informe uma string para verificar a ocorrência da letra 'a': ")
count = count_letter_a(string)
print(f"A letra 'a' aparece {count} vezes na string.")
