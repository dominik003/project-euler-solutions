def calc_next_sunday(last_sunday: (int, int, int)) -> (int, int, int):
    l_day, l_month, l_year = last_sunday

    days_in_month = get_days_in_month(l_month, l_year)
    if l_day + 7 > days_in_month:
        n_day = l_day + 7 - days_in_month
        n_month = (l_month % 12) + 1
        n_year = l_year + 1 if l_month == 12 and n_month == 1 else l_year
    else:
        n_day, n_month, n_year = (l_day + 7, l_month, l_year)

    return n_day, n_month, n_year


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_days_in_month(month: int, year: int) -> int:
    days_in_month = 0
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            days_in_month = 31
        case 4 | 6 | 9 | 11:
            days_in_month = 30
        case 2:
            if is_leap_year(year):
                days_in_month = 29
            else:
                days_in_month = 28
    return days_in_month


cur_sunday = (6, 1, 1901)
sunday_counter = 0
while (cur_sunday := calc_next_sunday(cur_sunday))[2] < 2001:
    if cur_sunday[0] == 1:
        sunday_counter += 1

print(sunday_counter)
