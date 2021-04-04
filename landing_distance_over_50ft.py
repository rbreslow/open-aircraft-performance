import math

def step_one(palt, oat):
    # TODO: We're off by around 15-20ft compared to ForeFlight's calculation at
    # KPNE. Who is more accurate? Does it matter?
    return (0.00012178 * palt + 2.85562) * oat + (0.034075 * palt + 1672.9)

def step_two(res, weight):
    # TODO: Explain why we think this ratio makes sense. Also, Leijurv is based.
    return ((1.0/3000) * res - 0.3) * weight + 900

def step_three(res, wind):
    if wind > 0:
        return ((7E-06 * pow(res, 2)) - (0.029 * res) + 10.302) * wind + res
    elif wind < 0:
        return res - ((-9E-06 * pow(res, 2)) + (0.0581 * res) - 6.3043) * wind
    else:
        return res

def landing_distance_over_50ft(palt, oat, weight, wind):
    one = step_one(palt, oat)
    two = step_two(one, weight)
    three = step_three(two, wind)

    print(f"\nStep One: { one }")
    print(f"Step Two: { two }")
    print(f"Step Three: { three }")

    return three


if __name__ == "__main__":
    palt = int(input("Landing pressure altitude: "))
    oat = int(input("Landing OAT: "))
    weight = int(input("Landing weight: "))
    wind = int(input("Surface wind: "))

    distance = landing_distance_over_50ft(palt, oat, weight, wind)
    print(f"\nTotal Distance Over 50 ft. Barrier (Standard Brakes): {round(distance):,}'")
