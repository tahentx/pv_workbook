def fake_bin(x: str) -> str:
    z = list(x)
    new = []
    for i in z:
        if int(i) >= 5:
            i = "1"
            new.append(i)
        elif int(i) < 5:
            i = "0"
            new.append(i)
    output = ''.join(new)
    print(output)

fake_bin("43529347502")
