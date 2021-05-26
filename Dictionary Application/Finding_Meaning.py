def meaning(word):
    from PyDictionary import PyDictionary
    c=PyDictionary().meaning(word)
    if len(word.split())>1:
        return 'Please Enter a Word'
    elif c==None:
        return 'Cannot Find The Meaning'
    else:
        try:
            return PyDictionary().meaning(word)['Noun'][0].title()
        except:
            try:
                return PyDictionary().meaning(word)['Adjective'][0].title()
            except:
                return 'Cannot Find The Meaning'