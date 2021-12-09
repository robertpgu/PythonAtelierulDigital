import datetime


def verify_length(cnp):
    if len(cnp) != 13:
        return False
    return True


def verify_gender(cnp):
    if cnp[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


def validate_date(prefix, year, month, day):
    try:
        datetime.datetime(int(prefix + year), int(month), int(day))
    except ValueError:
        return False
    else:
        return True


def validate_birthday(cnp):
    if cnp[0] in ['1', '2', '7', '8', '9']:
        return validate_date("19", cnp[1:3], cnp[3:5], cnp[5:7])
    elif cnp[0] in ['3', '4']:
        return validate_date("18", cnp[1:3], cnp[3:5], cnp[5:7])
    elif cnp[0] in ['5', '6']:
        return validate_date("20", cnp[1:3], cnp[3:5], cnp[5:7])


def verify_county_code(cnp):
    if 0 < int(cnp[7:9]) <= 46 or int(cnp[7:9]) in [51, 52]:
        return True
    return False


def verify_nnn(cnp):
    if cnp[9:12] != "000":
        return True
    return False


def verify_c(cnp):
    constant = "279146358279"
    result = 0
    for a, b in zip(constant, cnp):
        result += int(a) * int(b)
    result = result % 11
    if result == 10:
        if cnp[12] == '1':
            return True
        return False
    elif int(cnp[12]) == result:
        return True
    return False


def identify_gender(cnp):
    if cnp[0] in ['1', '3', '5', '7']:
        return "Sex barbatesc"
    elif cnp[0] == '9':
        return "Persoana straina"
    else:
        return "Sex femeiesc"


def identify_birth_year(cnp):
    if cnp[0] in ['3', '4']:
        return "18" + cnp[1:3]
    elif cnp[0] in ['5', '6']:
        return "20" + cnp[1:3]
    elif cnp[0] in ['1', '2', '7', '8', '9']:
        return "19" + cnp[1:3]


def identify_birth_day(cnp):
    day = cnp[5:7]
    return day


def identify_birth_month(cnp):
    month_v = cnp[3:5]
    dict_month = {"01": "Ianuarie",
                  "02": "Februarie",
                  "03": "Martie",
                  "04": "Aprilie",
                  "05": "Mai",
                  "06": "Iunie",
                  "07": "Iulie",
                  "08": "August",
                  "09": "Septembrie",
                  "10": "Octombrie",
                  "11": "Noiembrie",
                  "12": "Decembrie"}
    return dict_month[month_v]


if __name__ == '__main__':
    personal_cnp = input("Introduceti CNP-ul\n")

    if not verify_length(personal_cnp) or not personal_cnp.isdigit():
        print("CNP invalid")
    else:
        valid = True
        if not verify_gender(personal_cnp):
            print("CNP invalid")
            valid = False
        if not validate_birthday(personal_cnp) and valid:
            print("CNP invalid")
            valid = False
        if not verify_county_code(personal_cnp) and valid:
            print("CNP invalid")
            valid = False
        if not verify_nnn(personal_cnp) and valid:
            print("CNP invalid")
            valid = False
        if not verify_c(personal_cnp) and valid:
            print("CNP invalid")
            valid = False
        if valid:
            print("CNP valid")
            print(identify_gender(personal_cnp) + ", cu data de nastere in " + identify_birth_day(personal_cnp) + " " +
                  identify_birth_month(personal_cnp) + " " + identify_birth_year(personal_cnp))