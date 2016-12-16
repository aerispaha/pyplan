"""
helper functions
"""

def identify_possible_next_ops(option_id):

    """
    given a alternative ID, return a list of possible next implementation levels.
        alt = alternative, the major category of an SFR solution. AKA a
        "segment category"

        degree = the level of implementation of the alternative. E.g.
        3rd implementation scenario of Mifflin alternative

    requires that the alternative ID "buckets" are sorted alphabetically in each
    alternative ID.
    """
    alt_buckets = {'M':0, 'R':0, 'W':0}
    #first, find the alts that are currently not implemented at all
    possibles = []
    possibles += [{x:1} for x in alt_buckets.keys() if x not in filter(str.isalpha, option_id)]

    #iterate through option id's components
    for op in option_id.split('_'):

        #parse the passed in option into its buckets
        alt_name = filter(str.isalpha, op)
        alt_degree = int(filter(str.isdigit, op))
        alt_buckets.update({alt_name:alt_degree})

        #increment the option_id
        nxt_degree = alt_degree + 1
        next_op = {alt_name:nxt_degree}
        possibles.append(next_op)


    results = [] # output list of potential next implementation scenarios
    for p in possibles:
        # "deep copy" the buckets dict
        d = {k:v for k,v in alt_buckets.items()} #{'M':1, 'R':1, 'W':0}
        d.update(p)

        #remove any genres with zero implementation
        d2 = { k:v for k, v in d.items() if v != 0 }

        #convert to id format, sort alphebetically
        string_alts = ['{}{}'.format(key, str(val).zfill(2)) for key, val in d2.iteritems()]
        reformatted_op = '_'.join(sorted(string_alts))
        results.append(reformatted_op)

    return results
