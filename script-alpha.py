import io
import datetime
import re

# Middleman Helper Init
init = 1

# Main console
print "Middleman Helper v0.1-alpha".center(60, ' ')
print "by Ned Palacios".center(60,' ')
print "https://gitlab.com/nedpals/middleman-helper".center(60,' ')
print " "
print "Type 'help' to get a list of commands. ".center(60,' ')
while init == 1:
    print " "
    cmd = str(raw_input('middleman-helper >>> '))
    print " "
    if cmd == 'help' or cmd == 'h':
        print "Help"
        print "===="
        print " "
        print "still in progress"
    elif cmd == "test":
        phrase = raw_input('Enter phrase: ')
        p =  re.sub('([^\s\w]|_)+', '',phrase).replace(' ','-')
        d = str(datetime.date.today())
        title = d + '-' + p
        print "Expected blog post file: " + title + ".html.markdown"
    elif cmd == "exit" or cmd == "x":
        die()
    else:
        print "'%s' not found" % cmd
    
