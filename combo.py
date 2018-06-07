import itertools

def allPermutations(items):
    n = len(items)
    for k in range(1,n+1):
        for combo in itertools.combinations(items,k):
            yield combo
            
with open("bashscript.sh", "w") as shell_script:
    a = allPermutations([1,2,3,4,5,6,7])
    for i in range(63):
        x = next(a)
        x = [str(_) for _ in x]
        shell_script.write("python modelo.py {} >> model_log.txt\n".format(" ".join(x)))