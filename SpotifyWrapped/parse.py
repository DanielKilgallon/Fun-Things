from html.parser import HTMLParser

# copy html from spotify website, past into temp.html, then parse using this script.

class MyHTMLParser(HTMLParser):
    counter = 0

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if not data.isspace():
            print(data.strip(), end='|')
            self.counter += 1
            if self.counter >= 5:
                self.counter = 0
                print('\n---')

parser = MyHTMLParser()
with open('temp.html', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    output = ''
    for line in lines:
        output += line
    parser.feed(output)