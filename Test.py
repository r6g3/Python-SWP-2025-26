def geheim(a, b, c = 42, **data):
    pass

def main():
    #geheim(1,2,c = 52,**{"name": "Joana"})
    #geheim(1,2,4)
    #geheim(a = 1,2,3) #Nach einem benannten Attribut kann kein unbenanntes Attribut kommen
    #geheim(2,3, a = 1) #ungülting weil a schon 2 ist (mehrere Werte für a)
    x = {1,3,3}
    
def geheim(a, b, /, *, c): # Davor kann alles positionsbezogen sein / ist eine Grenze, danach muss alles benannt sein.
        pass

def geheim2(a,b, *args, **kwargs):
        pass
#def geheim2(*(1,2)):
    #pass
#def geheim3(b=2, *(1,)):
    #pass
def geheim4(*args, **kwargs):
    pass



if __name__== "__main__":
    main()