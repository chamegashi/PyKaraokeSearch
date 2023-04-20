import datetime

"""_summary_
datetime type のものを string に変換
"""


def convertDateToString(date):
    return date.strftime('%Y-%m-%d_%H:%M:%S')
