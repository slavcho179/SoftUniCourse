from collections import deque

monster_armors = deque([int(x) for x in input().split(',')])
soldier_strikes = [int(x) for x in input().split(',')]

defeated_monster = 0

while soldier_strikes and monster_armors:
    curr_strike = soldier_strikes.pop()
    curr_armor = monster_armors.popleft()

    if curr_strike >= curr_armor:
        defeated_monster += 1
        curr_strike -= curr_armor

        if soldier_strikes:
            soldier_strikes[-1] += curr_strike
        if not soldier_strikes and curr_strike > 0:
            # The line `soldier_strikes.append(curr_strike)` is adding the remaining strike power to the soldier's strikes
            # list if there are no more strikes left. This is done to ensure that the soldier's remaining strike power is
            # not lost and can be used in future battles if needed.
            soldier_strikes.append(curr_strike)

    else:
        curr_armor -= curr_strike
        monster_armors.append(curr_armor)

if not monster_armors:
    print("All monsters have been killed!")
if not soldier_strikes:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {defeated_monster}")


