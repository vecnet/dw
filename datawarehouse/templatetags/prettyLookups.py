# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/
import re
from django import template

register = template.Library()

def replaceWithSpace(val, arg):
    """This method takes a string, called 'val', and replaces
    all instances of 'arg' with a space.
    """
    return val.replace(arg, ' ')                        # replace all instances of the argument with a space
register.filter('replaceWithSpace', replaceWithSpace)   # register the filter

def capitalizeAll(val):
    """This method takes a string, called 'val', and
    capitalizes every space separated word.
    """
    tmp = val.split(" ")                                # seperate words by spaces into a list
    return " ".join(i.capitalize() for i in tmp)        # capitalize each word in the list and rejoin them with a space
register.filter('capitalizeAll', capitalizeAll)         # register the filter

def prettyLookup(val):
    """This method replaces various characters in a string
    with spaces and then capitalizes all the words.
    """
    tmp = val                                           # make a copy of the string
    tmp = replaceWithSpace(tmp, "_")                    # replace underscores with spaces
    tmp = capitalizeAll(tmp)                            # capitalize the words
    if tmp.startswith('Lut'):                           # strip "lut" from the beginning of the word
        tmp = tmp[3:]
    return tmp                                          # return the string
register.filter('prettyLookup', prettyLookup)           # register the filter

def prettyModelName(val):
    """This method expects camel-cased names and returns
    capitalized words separated by spaces.
    """
    tmp = val
    if tmp.startswith('Lut'):                           # strip "lut" from the beginning of the word
        tmp = tmp[3:]
    tmp = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', tmp)
    #--------------- Special Case of renaming Species to Species Bionomics as per Natalie Meyers and Greg Madey
    if tmp == 'Species':
        tmp = 'Species Bionomics'
    if tmp == 'Entomological Endpoint':
        tmp = 'Entomological Parameters'
    if tmp == 'Intervention Itn Coverages Admin1':
        tmp = "ITN Coverage in Africa"
    if tmp == 'Intervention Irs Coverages Admin1':
        tmp = "IRS Coverage in Africa"
    return tmp
register.filter(prettyModelName)
