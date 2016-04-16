import stack_exchange


class HtmlPage(object):
    def __init__(self):
        self.string = ""

    def start(self):
        self.string += '<!DOCTYPE html>' \
                       '<html lang="en">' \
                       '<head><meta charset="UTF-8">' \
                       '<title>English StackExchange Answers</title>' \
                       '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">' \
                       '</head><body>' \
                       '<div class="container">' \
                       '<h1 class="page-header">English StackExchange Answers</h1>'

    def finish(self):
        self.string += '</div></body></html>'

    def add_row(self, item):
        author = item.get_owner()
        self.string += '<div class="panel panel-default">' + \
                       '<div class="panel-heading">Author:&nbsp; <a href="http://english.stackexchange.com/users/' + \
                       author.identifier + '"><b>' + author.display_name + '</b> (' + str(author.class2_count) + \
                       ' silver badges) </a><br>Score:&nbsp; ' + str(item.score) + \
                       '</div>' + \
                       '<div class="panel-body">' + item.body + \
                       '</div></div>'

    def save(self, file):
        out = open(file, "w")
        out.write(self.string)
        out.close()


def run(count):
    print("Making HTML page...", end=" ", flush=True)
    html = HtmlPage()
    answers = stack_exchange.Post.get_all()
    html.start()
    i = 0
    for answer in answers:
        if answer.get_owner().class2_count >= 2:
            html.add_row(answer)

        i += 1
        if i >= count:
            break
    html.finish()
    print("done.")
    html.save("result.html")