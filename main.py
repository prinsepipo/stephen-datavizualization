from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

import pandas as pd


MONTHS = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
]


def plot(x, y):
    global index
    fig, ax = plt.subplots()
    line, = ax.plot(x, y)

    y_copy = pd.Series(data=[None for i in range(len(y))], index=[i for i in range(len(y))])

    ax.set_xticks([
        '2020-01-01',
        '2020-02-01',
        '2020-03-01',
        '2020-04-01',
        '2020-05-01',
        '2020-06-01',
        '2020-07-01',
        '2020-08-01',
        '2020-09-01',
        '2020-10-01',
        '2020-11-01',
        '2020-12-01',
    ])

    def f(x, p):
        return MONTHS[p] + '2020'

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.tick_params('x', rotation=30)
    ax.get_yaxis().set_major_formatter('${x:1.0f}')
    ax.get_xaxis().set_major_formatter(f)

    index = 0

    def update(i):
        global index
        y_copy[index] = y.tolist()[index]
        index = min(index + 1, len(y_copy) - 1)
        line.set_ydata(y_copy)
        return line,

    anim = FuncAnimation(fig, update, interval=1)

    plt.show()


def main():
    data = pd.read_csv('bitcoin.csv')
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    data = data.loc[(data['Date'] >= '2020-01-01') & (data['Date'] < '2021-01-01'), ['Date', 'High']]

    plot(data['Date'], data['High'])


if __name__ == '__main__':
    main()
