from math import erfc

def frequency_test(bits):
    n = len(bits)
    count = sum(1 if b == '1' else -1 for b in bits)
    s_obs = abs(count) / (n ** 0.5)
    p_value = erfc(s_obs / (2 ** 0.5))
    return p_value

def runs_test(bits):
    n = len(bits)
    pi = bits.count('1') / n
    if abs(pi - 0.5) >= (2 / n) ** 0.5:
        return 0.0
    runs = 1 + sum(1 for i in range(1, n) if bits[i] != bits[i-1])
    numerator = abs(runs - 2 * n * pi * (1 - pi))
    denominator = 2 * (2 * n) ** 0.5 * pi * (1 - pi)
    p_value = erfc(numerator / denominator)
    return p_value

def longest_run_test(bits, block_size=128):
    n = len(bits)
    if n < block_size * 16:
        raise ValueError("Sequence too short")
    blocks = [bits[i:i+block_size] for i in range(0, len(bits), block_size)]
    max_runs = [max(len(s) for s in block.split('0')) for block in blocks]
    return sum(max_runs) / len(max_runs)

