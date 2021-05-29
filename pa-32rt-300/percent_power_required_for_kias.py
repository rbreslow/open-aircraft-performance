import math


def percent_power_required_for_kias(kias):
    """!\f$y = -168.73x^2 + 344.68x - 17.641\f$ where Y is Indicated Airspeed
    (KIAS) and X is Percent Power"""
    a = -168.73
    b = 344.68
    c = -17.641 - kias

    d = (b ** 2) - (4 * a * c)
    return (-b + math.sqrt(d)) / (2 * a)


if __name__ == "__main__":
    kias = int(input("Indicated Airspeed (KIAS): "))
    print(
        "{:.2%} Power will yield {} KIAS.".format(
            percent_power_required_for_kias(kias), kias
        )
    )
