from math import erfc, floor
from scipy.stats import chi2

def frequency_test(bits):
    """
    Частотный тест
    :param bits:бинарная последовательность
    :return:p_value
    """
    n = len(bits)
    count = sum(1 if b == '1' else -1 for b in bits)
    s_obs = abs(count) / (n ** 0.5)
    p_value = erfc(s_obs / (2 ** 0.5))
    return p_value

def runs_test(bits):
    """
    Тест на одинаковые подряд идущие биты
    :param bits: бинарная последовательность
    :return: p_value
    """
    n = len(bits)
    pi = bits.count('1') / n
    if abs(pi - 0.5) >= (2 / n) ** 0.5:
        return 0.0
    runs = 1 + sum(1 for i in range(1, n) if bits[i] != bits[i-1])
    numerator = abs(runs - 2 * n * pi * (1 - pi))
    denominator = 2 * (2 * n) ** 0.5 * pi * (1 - pi)
    p_value = erfc(numerator / denominator)
    return p_value

def longest_run_test(bits, config):
    """
    Тест на самую длинную последовательность единиц в блоке
    :param bits: бинарная последовательность
    :param config: словарь с нужными значениями
    :return: средняя макс длину по всем блокам
    """
    M = config["block_size"]
    pi = config["pi"]
    n = len(bits)
    N = floor(n / M)
    if N == 0:
        raise ValueError("Sequence too short for M=8")
    blocks = [bits[i * M:(i + 1) * M] for i in range(N)]
    v = [0] * 4
    for block in blocks:
        runs = [len(run) for run in block.split('0')]
        max_run = max(runs)
        match max_run:
            case _ if max_run <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1
    chi2_stat = sum((v[i] - N * pi[i]) ** 2 / (N * pi[i]) for i in range(4))
    p_value = chi2.sf(chi2_stat, df=3)
    return p_value


