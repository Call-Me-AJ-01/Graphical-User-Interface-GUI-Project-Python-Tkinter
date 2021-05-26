def trans(word,destination):
    from googletrans import Translator
    dic={"tamil":"ta","hindi":"hi","japanese":"ja","french":"fr","english":"en","telugu":"te"}
    translator = Translator()
    translation = translator.translate(word, dest=dic[destination.lower()])
    return translation.text