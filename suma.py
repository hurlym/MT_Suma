from sys import argv, stdin
from automata.base.exceptions import AutomatonException
from automata.tm.dtm import DTM

# MAQUINA DE TURING QUE CALCULA SUMA AABBCCCC
transiciones = {
    'q0': {
        'a': ('q1', 'X', 'R'),
        'b': ('q2', 'Y', 'R')
    },
    'q1': {
        'b': ('q2', 'b', 'R'),
        'a': ('q1', 'a', 'R')
    },
    'q2': {
        'b': ('q2', 'b', 'R'),
        'Z': ('q2', 'Z', 'R'),
        'c': ('q3', 'Z', 'R')
    },
    'q3': {
        '~': ('q8', '~', 'L'),
        'c': ('q4', 'c', 'L')
    },
    'q4': {
        'Z': ('q4', 'Z', 'L'),
        'b': ('q5', 'b', 'L')
    },
    'q5': {
        'a': ('q6', 'a', 'L'),
        'b': ('q5', 'b', 'L'),
        'Y': ('q7', 'Y', 'R'),
        'X': ('q0', 'X', 'R')
    },
    'q6': {
        'a': ('q6', 'a', 'L'),
        'X': ('q0', 'X', 'R')
    },
    'q7': {
        'b': ('q2', 'Y', 'R')
    },
    'q8': {
        'Z': ('q8', 'Z', 'L'),
        'Y': ('q9', 'Y', 'L')
    },
    'q9': {
        'Y': ('q9', 'Y', 'L'),
        'X': ('q10', 'X', 'L')
    },
    'q10': {
        '~': ('qacc', '~', 'L'),
        'X': ('q10', 'X', 'L')
    }


}
maquina = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'qacc'},
    input_symbols={'a', 'b', 'c', 'X', 'Y', 'Z'},
    tape_symbols={'a', 'b', 'c', 'X', 'Y', 'Z', '~'},
    transitions=transiciones,
    initial_state='q0',
    final_states={'qacc'},
    blank_symbol='~'

)


def evaluar(w, debug=False):
    if debug:
        for c in maquina.read_input_stepwise(w):
            c.print()
        return True
    return maquina.accepts_input(w)


if __name__ == '__main__':
    for w in stdin:
        res = False
        try:
            res = evaluar(w.strip(), '--debug' in argv)  # strip saca el enter del final
        except AutomatonException as ex:
            print(ex.args)
        if (res):
            print('ACEPTA')
        else:
            print('RECHAZA')
