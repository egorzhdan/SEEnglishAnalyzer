import data
import html_builder


print("Enter count of answers to include in the result:", end=" ", flush=True)
count = int(input())

data.load_answers()
data.load_users()
data.load_badges()

html_builder.run(count)
