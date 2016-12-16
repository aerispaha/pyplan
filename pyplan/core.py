import pandas as pd
import .helpers as h


def most_efficient_sequence(data, benefit_col = 'Improved', cost_col ='Cost',
                            start_sequence = None):
    """
    given the cost / benefit summary data of segment combination models, return
    a dataframe with each option in sequence of most efficient projects. This
    method prioritizes max efficiency at each implementation phase.

    optionally passing in a start_sequence forces the sequence to begin at
    that point. start_sequence is a list.
    """

    #empty df to hold the implemenation sequence
    data.loc[:,'incr_benefit_cost'] = data[benefit_col] / data[cost_col]
    sequence = pd.DataFrame(columns=data.columns)

    #set the initial incremental values
    data.loc[:,'incr_benefit'] = data[benefit_col]
    data.loc[:,'incr_cost'] = data[cost_col]

    if start_sequence is None:
        #no starting point hard set, find the best overall starting point
        #first grab the index where incr_benefit_cost is max
        imax = data['incr_benefit_cost'].idxmax()
        best_nxt = data.ix[imax:imax] #look up single row df (so its not a series)
        sequence = sequence.append(best_nxt)
        print 'best_nxt start = {}'.format(best_nxt)
    else:
        #single row df of last (or only) item passed in
        best_nxt = data[data.Option_ID == start_sequence[-1]]

        #this copies the orginal data and changes the Option_ID column
        #to a Category type to allow sorting by Option_ID. This allows the
        #user's order of start_sequence to be honored in the resulting df
        df = data[:]
        sorter = start_sequence
        df.Option_ID = df.Option_ID.astype("category")
        df.Option_ID.cat.set_categories(sorter, inplace=True)
        df = df.loc[df.Option_ID.isin(sorter)].sort_values(["Option_ID"])
        df['incr_cost'] = df[cost_col].diff().fillna(df[cost_col])
        df['incr_benefit'] = df[benefit_col].diff().fillna(df[benefit_col])
        df['incr_benefit_cost'] = df.incr_benefit / df.incr_cost
        sequence = sequence.append(df)

    #get a df of all possible (logically) next options
    nxt_ids = h.identify_possible_next_ops(best_nxt.Option_ID.values[0])
    nxt_df = data[data['Option_ID'].isin(nxt_ids)]

    while len(nxt_df) > 0:

        #calculate the incremental cost/benefit data for each possible next
        #implementation level
        nxt_df.loc[:,'incr_cost'] = nxt_df.apply(lambda row: row[cost_col] - best_nxt.squeeze()[cost_col], axis=1)
        nxt_df.loc[:,'incr_benefit'] = nxt_df.apply(lambda row: row[benefit_col] - best_nxt.squeeze()[benefit_col], axis=1)
        nxt_df.loc[:,'incr_benefit_cost'] = nxt_df.incr_benefit / nxt_df.incr_cost

        #find the next implementation level with the highest benefit cost ratio
        #with respect to the current state of implementation. append to sequence
        best_nxt = nxt_df.ix[nxt_df['incr_benefit_cost'].idxmax()]
        sequence = sequence.append(best_nxt, ignore_index=True)

        #create a new dataframe with the possible next implementation levels
        nxt_ids = h.identify_possible_next_ops(best_nxt.Option_ID)
        nxt_df = data[data['Option_ID'].isin(nxt_ids)]

        #loop this process to build the sequence until no next options exist



    return sequence
