def original_dfa4(input_string):
    transitions = {
        '1': {'0': '2', '1': '4'}, '2': {'0': '3', '1': '4'},
        '3': {'0': '6', '1': '3'}, '4': {'0': '5', '1': '1'},
        '5': {'0': '6', '1': '1'}, '6': {'0': '3', '1': '6'}
    }
    current_state = '1'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'3', '6'}

def minimized_dfa4(input_string):
    transitions = {
        '{1, 4}': {'0': '{2, 5}', '1': '{1, 4}'},
        '{2, 5}': {'0': '{3, 6}', '1': '{1, 4}'},
        '{3, 6}': {'0': '{3, 6}', '1': '{3, 6}'}
    }
    current_state = '{1, 4}'
    for char in input_string:
        if char not in ['0', '1']: return False
        current_state = transitions[current_state][char]
    return current_state in {'{3, 6}'}

test_inputs = ["0", "00", "101001", "1010101010100"]
print("\n--- DFA 4 Tests ---")
for t in test_inputs:
    print(f"Input '{t}': Original={original_dfa4(t)} | Minimized={minimized_dfa4(t)}")