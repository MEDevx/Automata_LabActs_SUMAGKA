def original_dfa1(input_string):
    transitions = {
        'A': {'0': 'B', '1': 'C'}, 'B': {'0': 'B', '1': 'D'},
        'C': {'0': 'B', '1': 'C'}, 'D': {'0': 'B', '1': 'E'},
        'E': {'0': 'B', '1': 'C'}
    }
    current_state = 'A'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'E'}

def minimized_dfa1(input_string):
    transitions = {
        'AC': {'0': 'B', '1': 'AC'}, 'B': {'0': 'B', '1': 'D'},
        'D': {'0': 'B', '1': 'E'}, 'E': {'0': 'B', '1': 'AC'}  
    }
    current_state = 'AC'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'E'}

test_inputs = ["1", "1011", "011011", "1011010111011"]
print("--- DFA 1 Tests ---")
for t in test_inputs:
    print(f"Input '{t}': Original={original_dfa1(t)} | Minimized={minimized_dfa1(t)}")