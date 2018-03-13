def is_vowel(char):
    return char.lower() in 'aeiouåäö'

def rovar_sprak(text):
    result = ""
    for char in text:
        if is_vowel(char) or not char.isalpha():
            result = result + char
        else:
            result = result + char + "o" + char.lower()
    return result


text = input("Vilken text vill du översätta till rövarspråket? ")

print(rovar_sprak(text))
