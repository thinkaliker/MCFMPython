# MCFMPython
This Python script connects to any specified Twitch IRC channel, parses for [Monstercat](http://twitch.tv/monstercat) FM's Twitch music streaming bot, and formats them for use in [Open Broadcast Software](http://obsproject.org) or any other streaming program that uses a text file to update the current song/artist.

Don't have Python? Try [MCFMIRCParser](http://github.com/thinkaliker/mcfmircparser).

##Feaures
Proides an easy way to connect to Twitch IRC and scrapes for Monstercat FM's bot. It will automatically update a text file with the currently playing song and artist.

##How to use

###Before you start
- Python 3.0+ is required. The location of the Python installation must also be added to the system PATH variable.
- You will need an OAuth key for the account you would like to use this script with. Go to [TwitchApps](http://twitchapps.com/tmi) and connect using the account you would like to use. It can be the same account you are streaming with. Keep this key in a safe place. Copy it to your clipboard - you will need it later.
- Go to [Monstercat's Twitch channel](http://twitch.tv/monstercat) and type `!join` to have the bot join your channel. Be sure to go to your channel and mod it so that any other bots do not time it out.

###Running
- Run `start.bat` by double clicking on it. Alternatively you can run it through the Python terminal.
- It will ask you where to save the currently playing text file. If it does not exist, this will automatically create it for you.
- It will ask you for the channel name you would like to join. Preface the channel name with `#`.
- It will ask you for a username. This should match the account you got an OAuth key for.
- It will ask you for the OAuth key. Copy your OAuth key, starting with "oauth:", right click and paste it. It will be hidden from sight.
- It should now connect if everything went right.
- You may need to type `!song` in your own chat so that it will show the currently playing song.
- Add the text file to your OBS/whatever scene and it will automatically update.
- To exit, simply close the window.

#Bugs/TODO
- Write to file
- Different output style selection
- Input validation?
