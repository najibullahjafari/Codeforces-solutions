def can_form_decks(deck_size, total_cards, k, a):
    needed_cards = 0
    for count in a:
        if count < deck_size:
            needed_cards += deck_size - count
        if needed_cards > k:
            return False
    return needed_cards <= k


def max_deck_size(n, k, a):
    total_cards = sum(a)
    left, right = 1, total_cards + k
    while left < right:
        mid = (left + right + 1) // 2
        if can_form_decks(mid, total_cards, k, a):
            left = mid
        else:
            right = mid - 1
    return left


t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    results.append(max_deck_size(n, k, a))

for result in results:
    print(result)
