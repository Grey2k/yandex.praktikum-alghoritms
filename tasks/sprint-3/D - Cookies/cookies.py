def main():
    kids_num = int(input())
    kids = list(map(int, input().strip().split()))[:kids_num]

    cookies_num = int(input())
    cookies = list(map(int, input().strip().split()))[:cookies_num]

    print(match_cookies(kids, cookies))


def match_cookies(kids, cookies):
    sorted_kids = sorted(kids)
    sorted_cookies = sorted(cookies)

    if len(sorted_kids) == 0:
        return 0

    if len(sorted_cookies) == 0:
        return 0

    pleasured = 0

    while len(sorted_kids) > 0:
        kid = sorted_kids.pop()
        cookie = sorted_cookies.pop()

        if cookie >= kid:
            pleasured += 1
        else:
            sorted_cookies.append(cookie)

        if len(sorted_cookies) == 0:
            return pleasured

    return pleasured


if __name__ == '__main__':
    main()
