def num_atoms(amount_of_element, atom_weight=196.97):
    avogadro_num = 6.022*10**23
    num_of_atoms = amount_of_element/atom_weight*avogadro_num
    return num_of_atoms

print(num_atoms(10))
    