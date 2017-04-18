from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.
URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/games')
def games():
	return render_template('games.html')

@app.route('/developers')
def developers():
	return render_template('developers.html')

@app.route('/platforms')
def platforms():
	return render_template('platforms.html')

@app.route('/borderlands2')
def borderlands2():
	return render_template('borderlands2.html')

@app.route('/childoflight')
def childoflight():
	return render_template('childoflight.html')

@app.route('/ftl')
def ftl():
	return render_template('ftl.html')

@app.route('/Uncharted4')
def Uncharted4():
	return render_template('Uncharted4.html')

@app.route('/SuperMarioGalaxy')
def SuperMarioGalaxy():
	return render_template('SuperMarioGalaxy.html')

@app.route('/PokemonBlue')
def PokemonBlue():
	return render_template('PokemonBlue.html')

@app.route('/gearbox')
def gearbox():
	return render_template('gearbox.html')

@app.route('/ubisoft')
def ubisoft():
	return render_template('ubisoft.html')

@app.route('/subset')
def subset():
	return render_template('subset.html')

@app.route('/NaughtyDog')
def NaughtyDog():
	return render_template('NaughtyDog.html')

@app.route('/Nintendo')
def Nintendo():
	return render_template('Nintendo.html')

@app.route('/GameFreak')
def GameFreak():
	return render_template('GameFreak.html')

@app.route('/xbox360')
def xbox360():
	return render_template('xbox360.html')

@app.route('/pc')
def pc():
	return render_template('pc.html')

@app.route('/gamecube')
def gamecube():
	return render_template('gamecube.html')

@app.route('/PS4')
def PS4():
	return render_template('PS4.html')

@app.route('/Wii')
def Wii():
	return render_template('Wii.html')

@app.route('/GameBoy')
def GameBoy():
	return render_template('GameBoy.html')
	
if __name__ == '__main__':
	app.run('45.55.148.107','80') # Run application