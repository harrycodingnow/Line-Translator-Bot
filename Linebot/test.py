from googletrans import Translator
translator = Translator()
input = "Hello Taiwan"
detection = translator.detect(input)

if detection.lang =='en':
    translation_text = translator.translate(input, dest='zh-tw')
else: 
    translation_text = translator.translate(input, dest='en')

print(translation_text.text)