from operator import itemgetter

import hug
import tqdm


class TrieNode:
    __slots__ = ('value', 'end_of_word', 'children', 'weight')

    def __init__(self, value: str, end_of_word=False):
        self.value = value
        self.end_of_word = end_of_word
        self.children = {}
        self.weight = -1

    def add(self, word_part: str, *, weight: int=-1) -> None:
        if len(word_part) == 0:
            self.end_of_word = True
            self.weight = weight
            return

        first_char = word_part[0]
        node = self.children.setdefault(first_char, TrieNode(first_char))
        node.add(word_part[1:], weight=weight)

    def find_all(self, word_part: str, path: str=""):
        if self.end_of_word:
            yield path + self.value, self.weight

        if len(word_part) > 0:
            char = word_part[0]
            node = self.children.get(char)

            if node is not None:
                yield from node.find_all(word_part[1:], path + self.value)
        else:
            for node in self.children.values():
                yield from node.find_all("", path + self.value)


with open('words.txt') as f:
    words = f.readlines()

root = TrieNode("")

print('Loading words')
for word in tqdm.tqdm(words):
    root.add(word.rstrip('\n'), weight=1)

del words


@hug.get('/autocomplete')
def autocomplete(string: str, hug_timer):
    split_words = string.split()
    last_word = split_words[-1]
    prefix = ' '.join(split_words[:-1])

    suggestions = root.find_all(last_word)

    full_suggestions = []

    for suggestion in suggestions:
        full_suggestions.append((
            '{}{}'.format((prefix + ' ') if prefix else '', suggestion[0]),
            suggestion[1],
        ))

    sorted_suggestions = sorted(
        full_suggestions,
        key=itemgetter(1),
        reverse=True,
    )

    return {
        'words': list(map(itemgetter(0), sorted_suggestions)),
        'time_taken': hug_timer,}