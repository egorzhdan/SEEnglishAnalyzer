import data
import stack_exchange


data.load_answers()
data.load_users()
data.load_badges()

answers = stack_exchange.Post.get_all()