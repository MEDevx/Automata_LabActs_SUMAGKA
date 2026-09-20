def original_dfa2(input_string):
    transitions = {
        'A': {'0': 'B', '1': 'C'}, 'B': {'0': 'A', '1': 'D'},
        'C': {'0': 'E', '1': 'F'}, 'D': {'0': 'E', '1': 'F'},
        'E': {'0': 'E', '1': 'F'}, 'F': {'0': 'F', '1': 'F'}
    }
    current_state = 'A'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'C', 'D', 'E'}

def minimized_dfa2(input_string):
    transitions = {
        'AB': {'0': 'AB', '1': 'CDE'},
        'CDE': {'0': 'CDE', '1': 'F'},
        'F': {'0': 'F', '1': 'F'}
    }
    current_state = 'AB'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'CDE'}

test_inputs = ["1", "01", "0010", "0100000000"]
print("\n--- DFA 2 Tests ---")
for t in test_inputs:
    print(f"Input '{t}': Original={original_dfa2(t)} | Minimized={minimized_dfa2(t)}")