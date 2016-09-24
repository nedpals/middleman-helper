import io
import os
import datetime
import re

# Middleman Helper Init
init = 1

# Does site have blog dir?
blog_dir = 1

# Main console
print "Middleman Helper v0.2.1-alpha".center(60, ' ')
print "by Ned Palacios".center(60,' ')
print "https://github.com/nedpals/middleman-helper".center(60,' ')
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
    elif cmd == "make article":
        a_title = raw_input('Title: ')
        re_phrase = re.sub('([^\s\w]|_)+', '',a_title).lower().replace(' ','-')
        today = str(datetime.date.today())
        filename = today + '-' + re_phrase + '.html.markdown'
        if blog_dir == 1:
            savedir = os.path.abspath(r'source\blog')
        else:
            savedir = os.path.abspath('source')
        savefile = os.path.join(savedir, filename)
        with open(savefile, "w+") as file:
            file.write("---\n")
            file.write("# File created using Middleman Helper\n")
            file.write("title: " + a_title + "\n")
            file.write("date: " + today + "\n")
            file.write("tags: \n")
            file.write("---\n")
            file.write("\n")
            file.close()
        print 'Creating "%s"...' % filename
        print 'Done.'
    elif cmd == "exit" or cmd == "x":
        exit()
    else:
        print "'%s' command not found" % cmd
    
