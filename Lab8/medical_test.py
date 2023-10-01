from itertools import product


def joint_prob(network, assignment):
    prob = 1
    for key, value in assignment.items():
        node = network[key]
        if not node['Parents']:
            prob *= node['CPT'][()] if value else 1 - node['CPT'][()]
        else:
            truth_tuple = ()
            for parents in node['Parents']:
                truth_tuple += (assignment[parents],)
            prob *= node['CPT'][truth_tuple] if value else 1 - node['CPT'][truth_tuple]
    return prob


def query(network, query_var, evidence):
    # If you wish you can follow this template

    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    # Initialise a raw distribution to [0, 0]
    raw_dist = {True: 0, False: 0}
    assignment = dict(evidence)  # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var: val for var, val in zip(hidden_vars, values)}
            # Update the assignment (we now have a complete assignment)
            for key, item in hidden_assignments.items():
                assignment[key] = item
            # Update the raw distribution by the probability of the assignment.
            p = joint_prob(network, assignment)
            raw_dist[query_value] += p
    norm = sum(raw_dist[p] for p in raw_dist)
    for key, p in raw_dist.items():
        raw_dist[key] = p / norm
    return raw_dist
# med_network = {
#         'Disease': {
#             'Parents': [],
#             'CPT': {
#                 (): 1/100000
#             }},
#
#         'Test': {
#             'Parents': ['Disease'],
#             'CPT': {
#                 (True,): 0.99,
#                 (False,): 0.01,
#             }},
#     }
network = {
        'Virus': {
            'Parents': [],
            'CPT': {
                (): 0.01
            }},
        'A': {
            'Parents': ['Virus'],
            'CPT': {
                (True,): 0.95,
                (False,): 0.1,
            }},

        'B': {
            'Parents': ['Virus'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},
    }
if __name__ == "__main__":
    # answer = query(med_network, 'Disease', {'Test': True})
    # print("The probability of having the disease\n"
    #       "if the test comes back positive: {:.8f}"
    #       .format(answer[True]))
    # answer = query(med_network, 'Disease', {'Test': False})
    # print("The probability of having the disease\n"
    #       "if the test comes back negative: {:.8f}"
    #       .format(answer[True]))

    answer = query(network, 'Virus', {'A': True})
    print("The probability of carrying the virus\n"
          "if test A is positive: {:.5f}"
          .format(answer[True]))
    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
          "if test B is positive: {:.5f}"
          .format(answer[True]))