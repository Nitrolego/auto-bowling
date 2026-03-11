subframe_2_hit = 0

frame_hit = 10
subframe_2_hit = 0

#frame 1
if frame_hit < 10:
    strike = False
    subframe_1 = frame_hit
else:
    strike = True
    subframe_1 = "X"

#how to not execute this when striked...
if subframe_2_hit < (10 - frame_hit):
    spare = False
    subframe_2 = subframe_2_hit
elif subframe_2_hit == (10 - frame_hit):
    spare = True
    subframe_2 = "/"

print("frame: " + str(subframe_1) + "|" + str(subframe_2))
print("strike: " + str(strike))
print("spare: " + str(spare))