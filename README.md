Readme for pyaudiogame


# About

pyaudiogame is a toolkit for creating audio games in python  
In just a few lines of code, you can have a game window running and a place for your game logic.  

# Where to download

You can download pyaudiogame from
[The Git Releases page](https://github.com/frastlin/PyAudioGame/releases)  
or, if you would like to get all the new updates  
[go here for the latest git version](https://github.com/frastlin/PyAudioGame)  
Also checkout  
[The official website for the latest news](http://frastlin.github.io/PyAudioGame/)

<h1>Requirements</h1>
Most of what you need is in requires/. Just go in there and run:  
python setup.py install  
and you will be good.  
The dependencies for this package are pygame, accessible_output2, and inputs.

# Code example
<pre>
#Hello world example
import pyaudiogame
spk = pyaudiogame.speech.speak

#First create a basic app
app = pyaudiogame.App("My hello world app")

#Now make some game logic
def logic(actions):
	"""Our game logic function that gets run every iteration of our app's running loop"""
	if actions['key'] == "space":
		spk("Hello world")

#Put our logic into the app
app.logic = logic

#Run our app
app.run()
</pre>  
<br/><br/>  

Now run the above code and press space to hear "Hello world"  
#Documentation
[See the documentation page](documentation/documentation.html)  
There you can find guides and the API.