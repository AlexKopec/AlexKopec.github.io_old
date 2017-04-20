from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Coaches templates
@app.route('/coaches')
def coaches():
    return render_template('Coaches/Coaches.html')

@app.route('/coaches2')
def coaches2():
    return render_template('Coaches/Coaches2.html')

@app.route('/coaches/BillSelf')
def BillSelf():
    return render_template('Coaches/BillSelf.html')

@app.route('/coaches/DanaAltman')
def DanaAltman():
    return render_template('Coaches/DanaAltman.html')

@app.route('/coaches/FrankMartin')
def FrankMartin():
    return render_template('Coaches/FrankMartin.html')

@app.route('/coaches/JohnCalipari')
def JohnCalipari():
    return render_template('Coaches/JohnCalipari.html')

@app.route('/coaches/MarkFew')
def MarkFew():
    return render_template('Coaches/MarkFew.html')

@app.route('/coaches/RoyWilliams')
def RoyWilliams():
    return render_template('Coaches/RoyWilliams.html')

#Players Templates
@app.route('/players')
def players():
    return render_template('Players/Players.html')

@app.route('/players2')
def players2():
    return render_template('Players/Players2.html')

@app.route('/players/DillonBrooks')
def DillonBrooks():
    return render_template('Players/DillonBrooks.html')

@app.route('/players/FrankMasonIII')
def FrankMasonIII():
    return render_template('Players/FrankMasonIII.html')

@app.route('/players/JoelBerryII')
def JoelBerryII():
    return render_template('Players/JoelBerryII.html')

@app.route('/players/MalikMonk')
def MalikMonk():
    return render_template('Players/MalikMonk.html')

@app.route('/players/NigelWilliamsGoss')
def NigelWilliamsGoss():
    return render_template('Players/NigelWilliamsGoss.html')

@app.route('/players/SindariusThornwell')
def SindariusThornwell():
    return render_template('Players/SindariusThornwell.html')

#Teams Templates
@app.route('/teams')
def teams():
    return render_template('Teams/Teams.html')

@app.route('/teams2')
def teams2():
    return render_template('Teams/Teams2.html')

@app.route('/teams/Gonzaga')
def Gonzaga():
    return render_template('Teams/Gonzaga.html')

@app.route('/teams/Kansas')
def Kansas():
    return render_template('Teams/Kansas.html')

@app.route('/teams/Kentucky')
def Kentucky():
    return render_template('Teams/Kentucky.html')

@app.route('/teams/Oregon')
def Oregon():
    return render_template('Teams/Oregon.html')

@app.route('/teams/SC')
def SC():
    return render_template('Teams/SC.html')

@app.route('/teams/UNC')
def UNC():
    return render_template('Teams/UNC.html')

##########################################
if __name__ == '__main__':
    app.run('162.243.39.202', '80')
    #app.run()
