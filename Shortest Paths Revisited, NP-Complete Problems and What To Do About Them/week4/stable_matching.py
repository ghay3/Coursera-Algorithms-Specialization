def stable_matching(man2favor, woman2favor):
    man2woman, woman2man = {}, {}

    while len(man2woman) != len(man2favor):
        man = [man for man in man2favors.keys() - man2woman.keys()][0]
        mfavor = man2favor[man]

        woman = mfavor[0]
        while woman in woman2man:
            wfavor = woman2favor[woman]
            if wfavor.index(man) < wfavor.index(woman2man[woman]):
                break
            else:
                woman = mfavor[mfavor.index(woman) + 1]

        if woman in woman2man:
            old_man = woman2man[man]

            del man2woman[old_man]
            man2woman[man] = woman
            woman2man[woman] = man
            man2favor[old_man].remove(woman)
        else:
            man2woman[man] = woman
            woman2man[woman] = man

    return man2woman, woman2man


if __name__ == '__main__':
    man2favors = {
        'a': ['d', 'e', 'f'],
        'b': ['d', 'e', 'f'],
        'c': ['d', 'e', 'f']
    }
    woman2favors = {
        'd': ['a', 'b', 'c'],
        'e': ['b', 'c', 'a'],
        'f': ['c', 'a', 'b']
    }
    result = stable_matching(man2favors, woman2favors)
    print(result)