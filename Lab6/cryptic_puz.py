
            csp.var_domains[x] = new_domain  # DX := NDX
    return csp


def generate_and_test(csp):



domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1': {0, 1}, 'c2': {0, 1}})  # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        lambda o, r, c1: o + o == r + 10 * c1,  # one of the constraints
        lambda w, u, c1, c2: c1 + w + w == u + 10 * c2,
        lambda t, o, c2, f: c2 + t + t == o + 10 * f,
        lambda t, w, o, f, u, r: len({t, w, o, f, u, r}) == 6,  # All numbers must be unique
        lambda t: t != 0,
        lambda f: f != 0
        # add more constraints
    })
