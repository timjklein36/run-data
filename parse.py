from enum import Enum
import numpy
import matplotlib
import matplotlib.pyplot as plt
import seaborn

columns = ['PLACE', 'TIME', 'BIB#', 'LAST', 'FIRST', 'SEX', 'AGE', 'FINISH']


class Sex(Enum):
    n_a = 0
    female = 1
    male = 2


def get_sex(sym):
    if sym == 'M' or sym == 'm':
        return Sex.male
    elif sym == 'F' or sym == 'f':
        return Sex.female
    else:
        return Sex.n_a


class RaceTime(object):
    minutes: int
    seconds: int

    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.minutes * 60 + self.seconds

    def to_string(self):
        return '{}:{}'.format(
            str(self.minutes).zfill(2),
            str(self.seconds).zfill(2)
        )


class Runner(object):
    bib_number: int
    last_name: str
    first_name: str
    sex: Sex
    age: int

    def __init__(self, bib_number, last_name, first_name, sex, age):
        self.bib_number = bib_number
        self.last_name = last_name
        self.first_name = first_name
        self.sex = get_sex(sex)
        self.age = age


class Result(object):
    place: int
    time: RaceTime
    bib_number: int
    finish_note: str

    def __init__(self, place, time_min, time_sec, bib_no, note):
        self.place = place
        self.time = RaceTime(time_min, time_sec)
        self.bib_number = bib_no
        self.finish_note = note


def parse_data(raw_data):
    results = []
    runners = []
    for result in raw_data:
        result = result.split(',')
        time_list = result[1].split(':')
        results.append(
            Result(
                int(result[0]),
                int(time_list[0]),
                int(time_list[1]),
                int(result[2]),
                result[7]
            )
        )

        runners.append(
            Runner(
                int(result[2]),
                result[3],
                result[4],
                result[5],
                int(result[6])
            )
        )

    return results, runners


def main():
    with open('results.csv') as data:
        results, runners = parse_data(data)

    result_times = []

    for r in results:
        result_times.append(r.time.get_time())
    
    plt.plot(numpy.linspace(1, 128, 128), result_times)
    plt.show()


if __name__ == '__main__':
    main()
