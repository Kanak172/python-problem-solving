class Solution:
    __slots__ = ()
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        width = 0
        line = []

        for word in words:
            if (len(word) + width + len(line)) <= maxWidth:
                width += len(word)
                line.append(word)
                continue
            if len(line) == 1:
                lines.append("{0: <{width}}".format(" ".join(line), width=maxWidth))
            else:
                space, extra = divmod(
                    maxWidth - width,
                    len(line) - 1
                )
                i = 0

                while extra > 0:
                    line[i] += " "
                    extra -= 1
                    i += 1

                lines.append(
                    (" " * space).join(line)
                )
            line = [word]
            width = len(word)

        lines.append(
            "{0: <{width}}".format(" ".join(line), width = maxWidth)
        )

        return lines

