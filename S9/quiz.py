import random

l1 = ['US', 'UK', 'INDIA']
l2 = ['RUSSIA', 'PAKISTAN', 'CHINA']


def outer(fn: 'func') -> 'func':
    from datetime import datetime, timezone
    from functools import wraps
    import random
    country_amm_dict = {'US':{'soldier':2260000, 'tank':6289, 'fighter_jets':1840, 'aircraft_carrier':11, 'nueclear_weapon':6185},
               'UK':{'soldier':275660, 'tank':227, 'fighter_jets':480, 'aircraft_carrier':2, 'nueclear_weapon':215},
               'INDIA':{'soldier':3544000, 'tank':4292, 'fighter_jets':900, 'aircraft_carrier':1, 'nueclear_weapon':150},
               'RUSSIA':{'soldier':3013628, 'tank':12950, 'fighter_jets':1319, 'aircraft_carrier':1, 'nueclear_weapon':1572},
               'PAKISTAN':{'soldier':1204000, 'tank':2200, 'fighter_jets':497, 'aircraft_carrier':0, 'nueclear_weapon':160},
               'CHINA':{'soldier':2693000, 'tank':3500, 'fighter_jets':3010, 'aircraft_carrier':2, 'nueclear_weapon':320}}
    initial_strength = {k:v['soldier'] + (v['tank'] * 100) + (v['fighter_jets'] * 1000) + (v['aircraft_carrier'] * 10000) + (v['nueclear_weapon'] * 100000) for k,v in country_amm_dict.items()}

    @wraps(fn) # Passing docstring of assigned function to inner
    def inner(country):
        nonlocal country_amm_dict
        run_dt = datetime.now(timezone.utc)
        country_amm_dict[country]['soldier'] = country_amm_dict[country]['soldier'] * random.uniform(0.5, 1.5)
        country_amm_dict[country]['tank'] = country_amm_dict[country]['tank'] * random.uniform(0.5, 1.5)
        country_amm_dict[country]['fighter_jets'] = country_amm_dict[country]['fighter_jets'] * random.uniform(0.5, 1.5)
        country_amm_dict[country]['aircraft_carrier'] = country_amm_dict[country]['aircraft_carrier'] * random.uniform(0.5, 1.5)
        country_amm_dict[country]['nueclear_weapon'] = country_amm_dict[country]['nueclear_weapon'] * random.uniform(0.5, 1.5)

        result = fn(country, country_amm_dict, initial_strength)
        print(f'{run_dt}: called {fn.__name__}')
        return result
    return inner


@outer
def country_strength(country, country_amm_dict={}, initial_strength={}):
    strength = country_amm_dict[country]['soldier'] + (country_amm_dict[country]['tank'] * 100) + (country_amm_dict[country]['fighter_jets'] * 1000) + (country_amm_dict[country]['aircraft_carrier'] * 10000) + (country_amm_dict[country]['nueclear_weapon'] * 10000000)
    if ((strength/initial_strength[country])*100) > 10:
        return True
    else:
        print(f'{country} out of the war. Initial strength {initial_strength[country]} vs current strength {strength}')
        # del country_amm_dict[country]
        return False

# country_strength('CHINA')


def find_the_winner(l1, l2):
    winner = None
    if l1:
        l1_country = l1[random.choice(list(range(len(l1))))]
        still_in_war = country_strength(l1_country)
        if not still_in_war:
            l1.remove(l1_country)
            print(f'Country {l1_country} from group L1 is out of war')
        if not l1:
            if not winner:
                winner = 'L2'
    else:
        if not winner:
            winner = 'L2'

    if l2:
        l2_country = l2[random.choice(list(range(len(l2))))]
        still_in_war = country_strength(l2_country)
        if not still_in_war:
            l2.remove(l2_country)
            print(f'Country {l2_country} from group L2 is out of war')
        if not l1:
            if not winner:
                winner = 'L1'
    else:
        if not winner:
            winner = 'L1' 

    if winner:
        print(f'Winner is {winner}')

    return winner

def engage_in_war(l1, l2):
    l1_country = l1[random.choice(list(range(len(l1))))]
    l2_country = l2[random.choice(list(range(len(l2))))]
    print(f'{l1_country} vs {l2_country}')

    still_in_war = country_strength(l1_country)
    if not still_in_war:
        l1.remove(l1_country)
        print(f'Country {l1_country} is out of war')

    still_in_war = country_strength(l2_country)
    if not still_in_war:
        l2.remove(l2_country)
        print(f'Country {l2_country} is out of war')
    return l1, l2

def war_begins(l1, l2):
    while l1 and l2:
        l1, l2 = engage_in_war(l1, l2)
    print(f'Winner group is {l1 or l2}')
    return l1 or l2


war_begins(l1, l2)























































