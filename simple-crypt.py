import simplecrypt
import multiprocessing


def decrypt(data, password):
    try:
        res = simplecrypt.decrypt(password, data)
        print(res)
    except simplecrypt.DecryptionException:
        print("Password: {} is wrong".format(password))


def main():
    with open("encrypted.bin", "rb") as ef, open("passwords.txt", "r") as pwd:
        data = ef.read()
        processes = []

        for p in pwd:
            password = p.rstrip()
            t = multiprocessing.Process(target=decrypt, args=(data, password))
            processes.append(t)
            t.start()

        for t in processes:
            t.join()


if __name__ == "__main__":
    main()