from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

if __name__ == "__main__":
    n = int(input())
    html = '\n'.join(input() for _ in range(n))
    parser = MyHTMLParser()
    parser.feed(html)
