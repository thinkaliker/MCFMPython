import socket
import string
import getpass
import os
import os.path
import re

def header():
    print("       __  ___                 __                       __      ________  ___   ", end='')
    print("      /  \/  /___  ____  _____/ /____  ______________ _/ /_    / ____/  \/  /   ", end='')
    print("     / /\_/ / __ \/ __ \/ ___/ __/ _ \/ ___/ ___/ __ `/ __/   / /_  / /\_/ /    ", end='')
    print("    / /  / / /_/ / / / (__  ) /_/  __/ /  / /__/ /_/ / /_    / __/ / /  / /     ", end='')
    print("   /_/  /_/\____/_/ /_/____/\__/\___/_/   \___/\__,_/\__/   /_/   /_/  /_/      ", end='\n')
    print("Created by thinkaliker                                  [http://thinkaliker.com]", end='')
    print("       and rhoCode                                          [http://rhocode.com]", end='')
    print("Source available on GitHub            [http://github.com/thinkaliker/MCFMPython]", end='')
    print("////////////////////////////////////////////////////////////////////////////////")

def belowline():
    print("Songs will appear below.")
    print("================================================================================")

def styleprompt():
    print("Text output styles")
    print("----------------------")
    print(" [1]  Artist // Song")
    print(" [2]  Song // Artist")
    print(" [3]  Artist - Song")
    print(" [4]  Song - Artist")

def fileprompt():
    print("Enter your text file output location (Somewhere on C:\ recommended)")

song=""
artist=""

header()

def styleSwitch(style):
  styles = {
    1 : (" " + artist + " // " + song + " "),
    2 : (" " + song + " // " + artist + " "),
    3 : (" " + artist + " - " + song + " "),
    4 : (" " + song + " - " + artist + " "),
    5 : (" " + artist.upper() + " // " + song.upper() + " "),
    6 : (" " + song.upper() + " // " + artist.upper() + " "),
    7 : (" " + artist.upper() + " - " + song.upper() + " "),
    8 : (" " + song.upper() + " - " + artist.upper() + " ")
  }
  return styles[style]

fileprompt()
fileloc = input("File path: ")

if (os.path.isfile(fileloc)) != 1:
    print("File does not exist. Creating.")
    open(fileloc, 'w+')

NICK=input("Enter your username: ")

CHANNEL=input("Enter the channnel you would like to join (eg. Monstercat): ")
CHANNEL="#" + CHANNEL

print("Right click and paste your oauth key beginning with \"oath:\""),
PASSWORD=getpass.getpass('(hidden):')


HOST="irc.twitch.tv"
PORT=6667
IDENT=NICK
REALNAME=NICK

readbuffer=""

def sendIRC(stuff, t):
    t.send(stuff.encode('utf-8'))

print("Connecting...")
s=socket.socket( )
s.connect((HOST, PORT))
sendIRC("PASS %s\r\n" % PASSWORD, s)
sendIRC("NICK %s\r\n" % NICK, s)
sendIRC("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), s)
sendIRC("JOIN %s\r\n" % CHANNEL, s)

substring=":monstercat!monstercat@monstercat.tmi.twitch.tv PRIVMSG " +CHANNEL+ " :Now Playing:"

styleprompt()

instyle = input("Style: ")
style = int(instyle)
caps = input("All caps? (y/n): ")
if caps == "y":
    style = style + 4

songartist = styleSwitch(style)
belowline()
sendIRC("PRIVMSG " + CHANNEL + " :!song\r\n", s)
currentsongartist=songartist
init = 1

while 1:
    readbuffer=(s.recv(1024)).decode("utf-8")
    if readbuffer.find(substring) != -1:
        song, artist=re.search('Now Playing: (.*) by (.*) - Listen', readbuffer).groups()

        songartist=styleSwitch(style)

        if (init or currentsongartist != songartist):
            init = 0

            print(songartist)
            f=open(fileloc, 'r+')
            f.seek(0)
            f.write(songartist)
            f.truncate()
            f.close()
            currentsongartist=songartist            
