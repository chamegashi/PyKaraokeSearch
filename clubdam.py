from PyKaraokeSearch import search_clubdam, ClubDamSearchQuery

if __name__ == '__main__':
    import json
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str)
    parser.add_argument('-o', '--output_path', type=str)
    parser.add_argument('-t', '--timeout', type=float)
    args = parser.parse_args()

    keyword = args.keyword
    output_path = args.output_path
    timeout = args.timeout

    result = search_clubdam(ClubDamSearchQuery(keyword=keyword), timeout=timeout)

    with open(output_path if output_path else 0, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)
