def mutation(s,pos,var_to_add):
    l=list(s)
    l[pos]=var_to_add
    mutated_string=''.join(l)
    return mutated_string
