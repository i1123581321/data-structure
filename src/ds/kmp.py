def get_pmt(s: str) -> list[int]:
    """Get partial match table

    Args:
        s (str): pattern string

    Returns:
        list[int]: partial match table
    """
    n = len(s)
    if n == 0:
        return []
    result = [0] * n
    now = 0
    for i in range(1, n):
        while now > 0 and s[i] != s[now]:
            now = result[now - 1]
        if s[i] == s[now]:
            now += 1
        result[i] = now
    return result


def kmp(s: str, p: str) -> list[int]:
    ps = 0
    pp = 0
    pmt = get_pmt(p)
    result: list[int] = []
    while ps < len(s):
        if s[ps] == p[pp]:
            ps += 1
            pp += 1
        elif pp != 0:
            pp = pmt[pp - 1]
        else:
            ps += 1

        if pp == len(p):
            result.append(ps - pp)
            pp = pmt[pp - 1]
    return result
