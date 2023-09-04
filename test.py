def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_age():
    for age in range(1, 101):
        childhood_age = age // 14
        adult_age = childhood_age + age // 7
        marriage_age = adult_age + age // 6
        son_birth_age = marriage_age + 3

        if son_birth_age >= 7 and is_prime(son_birth_age ** 2 - son_birth_age):
            return marriage_age

    return None


age_at_marriage = find_age()
print("张先生结婚时的年龄是:", age_at_marriage, "岁")
