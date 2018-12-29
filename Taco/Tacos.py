import requests
import json
from flask import Flask, render_template, request
import random


app = Flask(__name__)
app.debug = True
myTacos = {}        # in-process dictionary storage to store the selected ingredients for each taco.
myTacoName ={}      # in-process dictionary storage to store the synthesized taco names based on ingredients.
tacoIndex = 0       # global count to keep track of index of tacos. Used as key for above 2 dictionarues. 

## Code to access REST endpoints and store the ingredients in JSON objects.
url = "https://tacos-ocecwkpxeq.now.sh/shells"
response = requests.get(url)
shellsOptions = json.loads(response.content)
url2 = "https://tacos-ocecwkpxeq.now.sh/mixins"
responseMixins = requests.get(url2)
mixinsOptions = json.loads(responseMixins.content)
url3 = "https://tacos-ocecwkpxeq.now.sh/baseLayers"
responseBase = requests.get(url3)
baseOptions = json.loads(responseBase.content)
url4 = "https://tacos-ocecwkpxeq.now.sh/seasonings"
responseSeasoning = requests.get(url4)
seasoningOptions = json.loads(responseSeasoning.content)
url5 = "https://tacos-ocecwkpxeq.now.sh/condiments"
responseCondiments = requests.get(url5)
condimentsOptions = json.loads(responseCondiments.content)

## Code to convert JSON data to dictionary database indexed starting from 0
ShellsData={}
for i in range(len(shellsOptions)):
    ShellsData[i] = shellsOptions[i]['name']
    
BaseData={}
for i in range(len(baseOptions)):
    BaseData[i] = baseOptions[i]['name']
    
condimentData={}
for i in range(len(condimentsOptions)):
    condimentData[i] = condimentsOptions[i]['name']

seasoningData={}
for i in range(len(seasoningOptions)):
    seasoningData[i] = seasoningOptions[i]['name']

mixinsData={}
for i in range(len(mixinsOptions)):
    mixinsData[i] = mixinsOptions[i]['name']
    
## Code to Name the tacos based on the condiments selected. This can be later connected to a database for lookup

condDict={}

condDict["Pickled Vegetables"] = "Pickled" 

condDict["Baja White Sauce"] = "White" 

condDict["Beet Salsa"] = "Beet" 

condDict["Chipotlé Sauce"] = "Chipotle" 

condDict["Guacamole"] = "Guac" 

condDict["Mango Avocado Salsa"] = "Mango" 

condDict["Phoning it in Pico de Gallo"] = "Pico" 

condDict["Pickled Red Onions"] = "Red Onions" 

condDict["Salsa Sauce"] = "Salsa" 

condDict["Simple Salsa Verde"] = "Verde" 

condDict["Roasted Tomatillo and Mushroom Sauce"] = "Mushroom" 

condDict["Black Olives"] = "Olives" 

condDict["Salsa de chile de árbol"] = "chile" 

condDict["Cashew Cheeze"] = "cashew" 

condDict["Guacamole (Simple)"] = "Guac" 

condDict["Sour Cream"] = "cream" 

condDict["Cranberry Salsa"] = "cranberry" 

condDict["Garlic Lime Sauce"] = "garlic" 

condDict["Mango Lime Salsa"] = "lime" 

condDict["Salsa de Aguacate"] = "aguacate" 

## All POST requests go to this function
@app.route('/', methods=['POST'])
def createTaco():
    ## This is called if btnList is pressed
    if "btnList" in request.form:
        ## Load the myList.html template to show all the tacos created.
        return render_template('myList.html', myTacos=myTacos, myTacoName =myTacoName)
    
    ## This is called if btnHome is pressed
    if "btnHome" in request.form:
        ## Load the home.html template to create new tacos.
        return render_template('home.html',shellsOptions=ShellsData, mixinsOptions = mixinsData, baseOptions=BaseData, seasoningOptions=seasoningData, condimentsOptions = condimentData)
    
    ## This is called if btnRemove is pressed to remove selected tacos from the list
    if "btnRemove" in request.form:
        
        # Get all the selected tacos based on checkbox values
        delTacos = request.form.getlist('toDelete')
        if delTacos!=None:
            # For each checkbox which is selected, delete entry of the taco from both the tacoName and taco ingredients(myTaco) dictionaries
            for key in delTacos:
                myTacos.pop(int(key))
                myTacoName.pop(int(key))
        ## Load the myList.html template to show the remaining tacos in the list.
        return render_template('myList.html', myTacos=myTacos,myTacoName =myTacoName)
    
    # To increment the tacoIndex
    global tacoIndex
    
    ## This is called if createTaco button is pressed to add the taco to the backend dictionaries
    if "createTaco" in request.form:
        ##code to access the values selected
        shell= ShellsData[int(request.form['shellsOptions'])]
        baseLayer=BaseData[int(request.form['baseOptions'])]
        mixin=mixinsData[int(request.form['mixinsOptions'])]
        condiments=request.form['condimentsOptions']
        
        # Handle multi-select
        condiment = ""
        if(len(condiments)>1):            
            for i in range(len(condiments)-1):
                condiment = condiment + ", " + condimentData[int(i)]
            condiment = condiment + " and " + condimentData[int(len(condiments)-1)]
        else:
            condiment = condimentData[0]
        #seasoning=request.form['seasoningOptions']
        
        seasonings=request.form['seasoningOptions']
        seasoning = ""
        # Handle multi-select
        if(len(seasonings)>1):
            for i in range(len(seasonings)-1):
                seasoning = seasoning + ", " + seasoningData[int(i)]
            seasoning = seasoning + " and " + seasoningData[int(len(seasonings)-1)]
        else:
            seasoning =seasoningData[0]
        
        # Creating a custom taco name. Currently using only a lookup-dictionary for condiment.
        tacoName = condDict[condimentData[0]]+ " "+baseLayer+ " Taco" 
        
        # Add the new taco to the tacoName dictionary
        myTacoName[tacoIndex] = tacoName
        # Add the new taco's ingredients string to the myTacos dictionary
        myTacos[tacoIndex]=baseLayer+"; "+shell+"; "+mixin+"; "+condiment+"; and "+seasoning
        # Increment index for next taco
        tacoIndex = tacoIndex +1
        # Render the myList.html view template and pass the taco ingredents and taco name as parameters
        return render_template('myList.html', myTacos=myTacos, myTacoName =myTacoName )
        
    ##This is called if randomTaco button is pressed to build a random taco and add it to the backend dictionaries
    elif "randomTaco" in request.form:
        
        ## Code to select random values from each ingredients
        shell = shellsOptions[random.randint(0,len(shellsOptions)-1)]['name']
        baseLayer = baseOptions[random.randint(0,len(baseOptions)-1)]['name']
        mixin = mixinsOptions[random.randint(0,len(mixinsOptions)-1)]['name']
        seasoning = seasoningOptions[random.randint(0,len(seasoningOptions)-1)]['name']
        condiment = condimentsOptions[random.randint(0,len(condimentsOptions)-1)]['name']
        
        # Creating a custom taco name. Currently using only a lookup-dictionary for condiment.
        tacoName = condDict[condiment]+ " "+" House Surprise Taco"
        
        # Add the new taco to the tacoName dictionary
        myTacoName[tacoIndex] = tacoName
        # Add the new taco's ingredients string to the myTacos dictionary
        myTacos[tacoIndex]=baseLayer+"; "+shell+"; "+mixin+"; "+condiment+"; and "+seasoning
        # Increment index for next taco
        tacoIndex = tacoIndex +1
        # Render the myList.html view template and pass the taco ingredents and taco name as parameters
        return render_template('myList.html', myTacos=myTacos, myTacoName =myTacoName )

## All GET requests are handled by this function
@app.route('/', methods=['GET'])

## Function to load the dropdowns on the home page with ingredients.
def dropdownFill():
    ## home.html is the UI view which is being used
    return render_template('home.html', shellsOptions=ShellsData, mixinsOptions = mixinsData, baseOptions=BaseData, seasoningOptions=seasoningData, condimentsOptions = condimentData)

## Main Function to run the Flask app
if __name__ == "__main__":
    app.run()
	
