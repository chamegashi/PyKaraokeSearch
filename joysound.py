from typing import get_args

from PyKaraokeSearch import search_joysound, JoySoundSearchQuery
from PyKaraokeSearch import JoySoundSearchQueryField as QF

if __name__ == '__main__':
    import json
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('songname', type=str)
    parser.add_argument('-m', '--match', type=str, default='partial', choices=get_args(QF.Match))
    parser.add_argument('-o', '--output_path', type=str)
    parser.add_argument('-t', '--timeout', type=float)
    args = parser.parse_args()

    songname = args.songname
    match = args.match
    output_path = args.output_path
    timeout = args.timeout

    result = search_joysound(JoySoundSearchQuery(
        filters=[
            QF.Filter(
                kind='song',
                word=songname,
                match=match,
            ),
        ],
    ), timeout=timeout)

    with open(output_path if output_path else 0, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)
