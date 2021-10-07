import random


destinations = ['Polaris', 'Columbus', 'Granville', 'Dublin', 'Easton']
restaurants = ['Chilis', 'Chipotle', 'BiBiBop', 'Fancy Feast', 'Golden Dragon']
transportations = ['Drive', 'Uber', 'Train', 'Hike', 'Spaceship']
entertainments = ['Comedy Show', 'Local Tour', 'Amusement Park', 'Sports Game', 'Concert']


def random_generator(some_list):
    some_value = random.choice(some_list)
    return some_value

def random_trip():
    email = input('Please enter your email: ')
    dest = random_generator(destinations)
    rest = random_generator(restaurants)
    trans = random_generator(transportations)
    ent = random_generator(entertainments)
    prompt_of_list = input(f'Destination: {dest} \nRestaurant: {rest} \nTransport: {trans} \nEntertainment: {ent} \nTo confirm trip, please type "Confirm". If you would like to generate a new trip, please type "New". ')
    while prompt_of_list == 'Confirm' or prompt_of_list == 'New':
        if prompt_of_list == 'Confirm':
            print(f'Trip confirmed! An email with all details was sent to {email}!')
            return
        elif prompt_of_list == 'New':
            dest = random_generator(destinations)
            rest = random_generator(restaurants)
            trans = random_generator(transportations)
            ent = random_generator(entertainments)
            prompt_of_list = input(f'Destination: {dest} \nRestaurant: {rest} \nTransport: {trans} \nEntertainment: {ent} \nTo confirm trip, please type "Confirm". If you would like to generate a new trip, please type "New". ')
            return

random_trip()



