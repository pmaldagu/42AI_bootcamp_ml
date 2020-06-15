from TinyStatistician import TinyStatistician

if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    print(tstat.median(a))
    print(tstat.quartile(a, 25))
    print(tstat.quartile(a, 75))
    print(tstat.var(a))
    print(tstat.std(a))
