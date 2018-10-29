#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import abspath, join, dirname
import random
import string
import sys


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
    'email': full_path('dist.email.providers'),
}

with open(FILES['email']) as f:
    email_providers = f.read().split('\n')

def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name


def get_first_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return u"%s %s" % (get_first_name(gender), get_last_name())


def get_user_name(f=None, l=None, n=1, p=False):
    user_name = ''

    # Verbs and nouns for namegen
    verbs = ['awkward','thin','thick','happy','sad','tall','short','malious','ravenous','smooth','loving','mean','weird','high','sober',"smart",'dumb','rich','poor','mega','music','lord']
    nouns = ['hacker','lumberjack','horse','unicorn','guy','girl','man','woman','male','female','men','women','duck','dog','sheep','zombie','tennis','doctor']
    # Not Safe For Work verbs and nouns to be added in later
    verbs_nfsw = ['drunk','shitfaced','rapie','high','drug_dealing','junkie','fucker_of']
    nouns_nfsw = ['rapist','fuck','pedophile','fucker']

    starts = ['Touches_','Loves_','Hates_','Licks_','Feels_']
    starts_nfsw = ["Gets_fucked_by_","Fucks_with_",'Humps_','Fucks_','Pimps_']

    if n == 1:
            nouns = nouns + nouns_nfsw
            starts = starts + starts_nfsw
    elif n == 2:
            nouns = nouns_nfsw
            starts = starts_nfsw

    # Set first and last so I can reuse this code in namegen
    first = f or get_first_name()
    last = l or get_last_name()

    # Random string generation
    char_set = string.ascii_uppercase + string.digits
    randstring = ''.join(random.sample(char_set*6, 6))

    # Numbers that may be added to the username
    numbers = ['one','two','three','four','five','seven','eight','nine','ten']

    if p:
            user_name = random.choice(starts) + random.choice(verbs) + '_' + random.choice(nouns) + 's'
    # Whats been done so far
    # first letter + last name
    # first 3 letters of first and all of last
    # 2-5th of first and first 6 of last
    # 1-2 of first and all of last
    # first 3 of first and 3-4 of last
    # first 3 of first and 1 of last
    # 2-4 of first and 0-3 of last
    # first 3 of first and 3-4 of last + numbers (spelled out)
    # first + random string
    # first + last but with first letter of first (john joe)
    # first 3 + last 3 but with first letter of first (joh joe)

    # How to generate the user name
    user_name_how = random.randint(1,18)

    # If the user has passed -p we skip this 
    if not p:

            # Code that generates username
            if user_name_how == 1:
                    user_name = first[0] + last
            elif user_name_how == 2:
                    user_name = first[0:2] + last[0:2]
            elif user_name_how == 3:
                    user_name = first[2:5] + last[0:5]
            elif user_name_how == 4:
                    user_name = first[1:2] + last
            elif user_name_how == 5:
                    user_name = first[0:2] + first[3:4]
            elif user_name_how == 6:
                    user_name = last[0:2] + last[1]
            elif user_name_how == 7:
                    user_name = first[2:4] + last[0:3]
            elif user_name_how == 8:
                    numbs = random.randint(10, 100)
                    numbs = str(numbs)
                    user_name = first[0] + last + " " + numbs
                    user_name = user_name.replace(" ", "")
            elif user_name_how == 9:
                    user_name = first + randstring
            elif user_name_how == 10:
                    first = first[:1].upper() + first[1:]
                    last = first[:1].upper() + last[1:]
                    user_name = first + last
            elif user_name_how == 11:
                    first = first[:1].upper() + first[1:]
                    last = first[:1].upper() + last[1:]
                    user_name = first[0:2] + last[0:2]
            elif user_name_how == 12:
                    user_name = first + random.choice(numbers)
            elif user_name_how == 13:
                    user_name = last[3:6] + last[0:2]
            elif user_name_how == 14:
                    user_name = random.choice(verbs) +'_'+ random.choice(nouns)
            elif user_name_how == 15:
                    user_name = first + random.choice(verbs) + random.choice(nouns) + last
            elif user_name_how == 16:
                    user_name = "The_one_and_only_" + first
            elif user_name_how == 17:
                    user_name = "The_one_and_only_" + first + "_the_" + random.choice(verbs) + "_" + last
            elif user_name_how == 18:
                    how = random.randint(1,2)
                    if how == 1:
                            user_name = random.choice(starts) + random.choice(verbs) + '_' + random.choice(nouns) + 's'
                    elif how == 2:
                            user_name = random.choice(starts) + random.choice(nouns) + 's'
            else:
                return None

    # If and how to repalce chars in the user name.
    replace_char = random.randint(1,10)

    # The code that replace chars in the user name
    if replace_char == 1:
            user_name = user_name.replace('i', '1')
            user_name = user_name.replace('a', '4')
            user_name = user_name.replace('e', '3')
            user_name = user_name.replace('l','|')
    elif replace_char == 2:
            user_name = user_name.replace('_', '-')
    elif replace_char == 3:
            user_name = user_name.replace('_', '7')
    elif replace_char == 4:
            user_name = user_name.replace('m','nn')
    else:
            user_name = user_name

    randstuff = random.randint(1,10)

    # This codes adds random stuff to the end of a username so it's more unique
    if randstuff == 1:
            user_name = user_name + randstring
    else:
            user_name = user_name

    return user_name


def get_email_address(username=None, domain=None):
    return (username or get_user_name()) + '@' + (domain or random.choice(email_providers))
