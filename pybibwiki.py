import sys
from datetime import datetime

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 pybibwiki.py wiki_url')
    else:
        url = sys.argv[1]
        title = url[url.rfind('/')+1:]
        df = datetime.now()

        print('@misc{{wiki:{},\n  author = "Wikipedia",\n  title = "{{{}}} --- {{W}}ikipedia{{,}} The Free Encyclopedia",\n  year = "{}",\n  url = "{}",\n  note = "[Online; accessed {}]"\n}}'.format(title, title.replace('_', ' '), df.strftime('%Y'), url, df.strftime('%d-%B-%Y')))