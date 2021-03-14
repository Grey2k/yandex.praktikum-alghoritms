from functools import cmp_to_key


class ConferenceParticipants:
    def __init__(self):
        self.index = dict()
        self.participants = []

    @staticmethod
    def comparator(a, b):
        if a.get('count') > b.get('count'):
            return 1
        if a.get('count') < b.get('count'):
            return -1

        if a.get('id') > b.get('id'):
            return -1

        if a.get('id') < b.get('id'):
            return 1

        return 0

    def get_top(self, limit):
        """
        :var self.pa:
        """
        top = sorted(self.participants, key=cmp_to_key(ConferenceParticipants.comparator), reverse=True)[:limit]

        return [str(p.get('id')) for p in top]

    def add(self, p_id):
        if self.index.get(p_id) is None:
            self.participants.append({'id': p_id, 'count': 1})
            self.index[p_id] = len(self.participants) - 1
        else:
            # noinspection PyTypeChecker
            self.participants[self.index.get(p_id)]['count'] += 1


def main():
    n = int(input())
    ids = list(map(int, input().strip().split()))[:n]
    limit = int(input())

    participants = ConferenceParticipants()

    for participant_id in ids:
        participants.add(participant_id)

    print(' '.join(participants.get_top(limit)))


if __name__ == '__main__':
    main()
