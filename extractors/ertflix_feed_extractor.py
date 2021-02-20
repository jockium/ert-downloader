import feedparser

def obtain_list(url):
    mylist = []
    d = feedparser.parse(url)
    for i in range(len(d.entries)):
        mylist.append(d.entries[i].link)

    print('found '+ str(len(d.entries)) +' links on page 1, continuing...')
    mypage = 2
    if "paged=" in url:
        checknext = 0  # do not try to add page reference if someone already gave a specific page url...
    else:
        checknext = 1

    while (checknext==1):
        linksfound = 0
        newurl = url+'?paged='+str(mypage)
        d = feedparser.parse(newurl)
        for z in range(len(d.entries)):
            mylist.append(d.entries[z].link)
            linksfound = z+1
        if (linksfound == 0):
            checknext = 0   #stop trying to find pages...
            print('no links found on page '+str(mypage))
        else:
            print('found '+ str(linksfound) +' links on page '+str(mypage)+', continuing...')
            mypage +=1

    return mylist
