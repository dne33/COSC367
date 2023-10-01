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



if __name__ == "__main__":
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
            }},
    }

    p = joint_prob(network, {'A': True})
    print("{:.5f}".format(p) == '0.20000')

    p = joint_prob(network, {'A': False})
    print("{:.5f}".format(p) == '0.80000')

    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }

    p = joint_prob(network, {'A': False, 'B': False})
    print("{:.5f}".format(p) == '0.27000')
    p = joint_prob(network, {'A': False, 'B': True})
    print("{:.5f}".format(p) == '0.63000')
    p = joint_prob(network, {'A': True, 'B': False})
    print("{:.5f}".format(p) == '0.02000')
    p = joint_prob(network, {'A': True, 'B': True})
    print("{:.5f}".format(p) == '0.08000')

    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
            }},

        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
            }},
        'Alarm': {
            'Parents': ['Burglary', 'Earthquake'],
            'CPT': {
                (True, True): 0.95,
                (True, False): 0.94,
                (False, True): 0.29,
                (False, False): 0.001,
            }},

        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},

        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
            }},
    }

    p = joint_prob(network, {'John': True, 'Mary': True,
                             'Alarm': True, 'Burglary': False,
                             'Earthquake': False})
    print("{:.8f}".format(p) == '0.00062811')