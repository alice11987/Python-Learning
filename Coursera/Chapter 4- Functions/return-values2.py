#return value- The return statement ends the function execution and 'send back' the result of the function
def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    else :
        return 'Hello'

print greet('en'),'Glenn'
print greet('es'),'Sally'
print greet('fr'),'Michael'
