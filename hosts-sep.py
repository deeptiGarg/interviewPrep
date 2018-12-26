# sri.amazon.com
# sports.espn.com
# espn.com
# google.com
# abcd.org
# amazon.com
# www.amazon.com
# prime.sri.amazon.com


#[ "sri.amazon.com","sports.espn.com","espn.com","google.com","abcd.org", "amazon.com","www.amazon.com", "prime.sri.amazon.com"]

dictCount = {}
def splitWords():
    ltHosts = [ "sri.amazon.com","sports.espn.com","espn.com","google.com","abcd.org", "amazon.com","www.amazon.com", "prime.sri.amazon.com"]
    
    for host in ltHosts:
        #dictCount[host] = 1
        if(host.rfind('.')!=-1):
            if(host.rfind(".")==host.find(".")):     #only 1 . exists
                addToDict(host,host.rfind('.')+1,1)
            else:
                addToDict(host,host.find('.')+1,2)
    print(dictCount)

def addToDict(str,idx,c):
    if str in dictCount:
        dictCount[str] +=1
    else:
        dictCount[str] =1
    if(c==1):      #base case
        if str[idx:] in dictCount:
            dictCount[str[idx:]] += 1
        else:
            dictCount[str[idx:]] = 1
    else:
        host = str[idx:]
        if(host.rfind(".")==host.find(".")):
            addToDict(host,host.rfind('.')+1,1)
        else:
            addToDict(host,host.find('.')+1,2)

splitWords()