# imports
from datetime import datetime
from random import randint
# variables
world = '🌍🌎🌏'
python = 'Python 🐍'
fire = '🔥'

# Function definitions        
def roll_dice():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1, int(max))
    print(f'You rolled a {roll} {fire * roll}')

# Put code to run under here


print(f'Hello{world}')
print(f'welcome to {python}')
print(f'{111111111 * 111111111}')
print(f'The date and time is {datetime.now()}')
roll_dice()
print(f'I ❤️ ...')
print(f'... makes me 😃')
print(f'I would like to make ... with {python}')