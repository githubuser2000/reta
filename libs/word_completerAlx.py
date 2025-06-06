from typing import Callable, Iterable, List, Mapping, Optional, Pattern, Union

from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text import AnyFormattedText

__all__ = [
    "WordCompleter",
]


class WordCompleter(Completer):
    """
    Simple autocompletion on a list of words.

    :param words: List of words or callable that returns a list of words.
    :param ignore_case: If True, case-insensitive completion.
    :param meta_dict: Optional dict mapping words to their meta-text. (This
        should map strings to strings or formatted text.)
    :param WORD: When True, use WORD characters.
    :param sentence: When True, don't complete by comparing the word before the
        cursor, but by comparing all the text before the cursor. In this case,
        the list of words is just a list of strings, where each string can
        contain spaces. (Can not be used together with the WORD option.)
    :param match_middle: When True, match not only the start, but also in the
                         middle of the word.
    :param pattern: Optional compiled regex for finding the word before
        the cursor to complete. When given, use this regex pattern instead of
        default one (see document._FIND_WORD_RE)
    """

    def __init__(
        self,
        words: Union[List[str], Callable[[], List[str]]],
        ignore_case: bool = False,
        display_dict: Optional[Mapping[str, AnyFormattedText]] = None,
        meta_dict: Optional[Mapping[str, AnyFormattedText]] = None,
        WORD: bool = False,
        sentence: bool = False,
        match_middle: bool = False,
        pattern: Optional[Pattern[str]] = None,
    ) -> None:

        assert not (WORD and sentence)

        self.words = words
        self.ignore_case = ignore_case
        self.display_dict = display_dict or {}
        self.meta_dict = meta_dict or {}
        self.WORD = WORD
        self.sentence = sentence
        self.match_middle = match_middle
        self.pattern = pattern

    def __eq__(self, obj) -> bool:
        return self.words == obj.words

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        # Get list of words.
        words = self.words
        if callable(words):
            words = words()

        # Get word/text before cursor.
        if self.sentence:
            word_before_cursor = document.text_before_cursor
        else:
            word_before_cursor = document.get_word_before_cursor(
                WORD=self.WORD, pattern=self.pattern
            )

        if self.ignore_case:
            word_before_cursor = word_before_cursor.lower()

        def word_matches(word: str) -> bool:
            """True when the word before the cursor matches."""
            if self.ignore_case:
                word = word.lower()

            if self.match_middle:
                return word_before_cursor[: len(word)] in word
            else:
                return word.startswith(word_before_cursor[: len(word)])

        for a in words:
            if word_matches(a):
                display = self.display_dict.get(a, a)
                display_meta = self.meta_dict.get(a, "")
                yield Completion(
                    a,
                    -len(word_before_cursor),
                    display=display,
                    display_meta=display_meta,
                )
