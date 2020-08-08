from random import randint
import time

heads=0
tails=0
flips=int(input('How many flips would you like? '))
starttime=time.time()
while flips:
    if randint(0,1)==0:
        heads+=1
    else:
        tails+=1
    flips-=1
# Have to assign an endtime, time elapsed could change > 0.00 secs by finish of if statement,
# proving inaccurate, and not <0.00 secs.
print("Heads: %d\nPercentage of heads: %.2f%%" % (heads, (heads/(heads+tails))))
print("Tails: %d\nPercentage of tails: %.2f%%" % (tails, (tails/(heads+tails))))
print("Time elapsed: %.6f seconds" % (time.time()-starttime))