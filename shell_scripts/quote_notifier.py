import subprocess
import random
import os


quotes = ['The best preparation for tomorrow is doing your best today',
        "  Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible",
          "My mission in life is not merely to survive, but to thrive; and to do so with some passion,some compassion, some humor, and some style.","Winning isn't everything, it is the only thing.",
          " You must do the things you think you cannot do.",
          "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.",
          "No matter what people tell you, words and ideas can change the world.",
          "No matter what people tell you, words and ideas can change the world.",
          "If you always put limit on everything you do, physical or anything else. It will spread into your work and into your life. There are no limits. There are only plateaus, and you must not stay there, you must go beyond them.",
          "When you get into a tight place and everything goes against you, till it seems as though you could not hang on a minute longer, never give up then, for that is just the place and time that the tide will turn.",
          "Out of difficulties grow miracles",
          "With self-discipline most anything is possible.",
          "The power of imagination makes us infinite.",
          "Somewhere, something incredible is waiting to be known.",
          "It is in your moments of decision that your destiny is shaped.",
          "In order to succeed, we must first believe that we can.",
          "Don't watch the clock; do what it does. Keep going.",
          "Never complain and never explain.",
          "Start where you are. Use what you have. Do what you can.",
          "You have to learn the rules of the game. And then you have to play better than anyone else."

]


title = "Quote :"
def choose() :
    l = len(quotes)
    #print(l)
    num = random.randint(0,l)
    #print(num)
    quote = quotes[num]
   #os.system('notify-send "'+title+'" "'+quote+'"')
    os.system('DISPLAY=:5.5 notify-send "'+title+'" "'+quote+'"')
  


choose()
