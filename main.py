import data
import html_builder


count = 200

data.load_answers()
data.load_users()
data.load_badges()

html_builder.run(count)
