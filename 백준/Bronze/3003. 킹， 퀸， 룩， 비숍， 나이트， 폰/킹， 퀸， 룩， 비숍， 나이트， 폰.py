a, b, c, d, e, f = map(int, input().split())

chess_piece1 = [1, 1, 2, 2, 2, 8]
chess_piece2 = [a, b, c, d, e, f]

add_list = [chess_piece1[i] - chess_piece2[i] for i in range(len(chess_piece1))]
print(*add_list)
