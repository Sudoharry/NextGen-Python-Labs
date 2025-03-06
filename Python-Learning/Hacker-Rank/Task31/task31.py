from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr, value in attrs:
            if value is None:
                value = 'None'
            print(f"-> {attr} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr, value in attrs:
            if value is None:
                value = 'None'
            print(f"-> {attr} > {value}")

if __name__ == "__main__":
    parser = MyHTMLParser()
    n = int(input())
    html = '\n'.join(input() for _ in range(n))
    parser.feed(html)
