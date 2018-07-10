def solution(n):
    def move(a, b, c, n):
        if n == 1:
            return [[a, c]]
        moves = []
        moves.extend(move(a, c, b, n-1))
        moves.extend([[a, c]])
        moves.extend(move(b, a, c, n-1))
        return moves
    return move(1, 2, 3, n)