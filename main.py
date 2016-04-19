import data
import html_builder


print("Enter count of questions to include in the result:", end=" ", flush=True)
count = int(input())

data.load_questions()
data.load_users()
data.load_badges()
data.load_links()

html_builder.run(count)
