from googletrans import Translator, constants

translator = Translator()
print(translator.translate(input("Enter the text to translate :"), dest='ml').text)


# how are you? welcome to python turorial