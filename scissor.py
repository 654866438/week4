
#又是考split.method，跟上周的一样啊

import sys


def main():
    args = sys.argv
    args_len = len(args)

    if args_len < 3:
        print('Not enough arguments.')
        return

    if args_len > 3:
        print('Too many arguments.')
        return

    pos = int(args[1])
    filename = args[2]

    f = open(filename, 'r')

    for line in f:
        fields = line.split()
        print(fields[pos-1])

    f.close()


if __name__ == '__main__':
    main()


