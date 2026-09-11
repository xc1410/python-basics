def efootball(n=99):
    for i in range(1,n+1):
        if i%7==5:
            loss=5/i
            print(f"第{i}轮，loss={loss}")
    return loss

efootball(78)

