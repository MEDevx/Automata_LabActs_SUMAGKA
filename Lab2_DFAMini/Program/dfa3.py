def original_dfa3(input_string):
    transitions = {
        '1': {'0': '4', '1': '2'}, '2': {'0': '3', '1': '5'},
        '3': {'0': '4', '1': '5'}, '4': {'0': '1', '1': '5'},
        '5': {'0': '6', '1': '2'}, '6': {'0': '1', '1': '2'}
    }
    current_state = '1'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'3', '6'}

def minimized_dfa3(input_string):
    transitions = {
        '{1, 4}': {'0': '{1, 4}', '1': '{2, 5}'},
        '{2, 5}': {'0': '{3, 6}', '1': '{2, 5}'},
        '{3, 6}': {'0': '{1, 4}', '1': '{2, 5}'}
    }
    current_state = '{1, 4}'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'{3, 6}'}

test_inputs = ["0", "10", "10110", "1111111110"]
print("\n--- DFA 3 Tests ---")
for t in test_inputs:
    print(f"Input '{t}': Original={original_dfa3(t)} | Minimized={minimized_dfa3(t)}")