import webbrowser

# webbrowser.open("https:/www.python.org/")
# help(webbrowser)

chrome = webbrowser.get(using = 'google-chrome').open_new_tab("https:/www.python.org/")