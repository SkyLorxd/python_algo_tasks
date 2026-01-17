def solution(s: str) -> bool:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    bracket_seq = []

    for char in s:
        if char in '([{':
            bracket_seq.append(char)
        elif char in ')]}':
            if not bracket_seq:
                return False
            if bracket_seq[-1] != pairs[char]:
                return False
            bracket_seq.pop()

    return len(bracket_seq) == 0
