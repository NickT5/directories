import os
import datetime


def next_weekday_date(start_day: datetime.date, weekday: int = 0):
    """
    return the date of the next weekday beginning from the start_date.
    For example: if start day is 2020-06-14 and weekday is 0, then the date that will be returned is 2020-06-15 which
    is a monday.
    :param start_day: the day which to start from
    :type start_day: datetime.date
    :param weekday: which weekday should be returned
        weekday: 0 ~ monday
        weekday: 6 ~ sunday
    :type weekday: int
    :return: the next weekday date 
    :rtype datetime.date
    """
    return start_day + datetime.timedelta(days=-start_day.weekday() + weekday, weeks=1)


def get_mondays_this_year(start_day: datetime.date):
    """
    return all monday dates starting from start_day until the end of the year of start_day.
    :param start_day: the day which to start from
    :type start_day: datetime.date
    :return: 
    :rtype: list of datetime.date objects
    """
    mondays = []

    current_day = start_day
    while(current_day.year <= start_day.year):
        mondays.append(current_day)
        current_day = next_weekday_date(current_day)
    
    return mondays
    
def create_dirs(root_dir, parent_dir, mondays, chargers):

    # switch directory and create parent directory
    try:
        os.chdir(root_dir)
        os.mkdir(parent_dir)
    except FileExistsError:
        pass
    finally:
        os.chdir(parent_dir)

    # create dirs and subdirs
    for m in mondays:
        for c in chargers:
            os.makedirs(f"{m}/{c}", exist_ok=True)



def main():
    print("Starting")
    root_dir = "C:\\Users\\nick\\Documents\\projects\\directories"
    parent_dir = "Diagnostics"

    chargers = ["10_10_10_105", "10_10_10_106", "10_10_10_107",
                "10_10_10_110", "10_10_10_111", "10_10_10_112",
                "10_10_10_115", "10_10_10_116", "10_10_10_117",
                "10_10_10_120", "10_10_10_121", "10_10_10_122",
                "10_10_10_150", "10_10_10_151",
                "8100003"]


    start_date = datetime.date(2020, 6, 15)
    mondays = get_mondays_this_year(start_day=start_date)
    create_dirs(root_dir, parent_dir, mondays, chargers)
    print("Done")

if __name__ == "__main__":
    main()