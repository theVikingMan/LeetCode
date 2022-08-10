import math

class Solution:
    def parse_tag(self, i, code):
        tag = ''
        while i < len(code):
            if code[i] == '<':
                return math.inf, ''
            if code[i] == '>':
                i += 1
                break
            tag += code[i]
            i += 1
        return i, tag

    def parse_cdata(self, index, code):
        i = index + len(('<![CDATA['))
        while i < len(code):
            if code[i:].startswith(']]>'):
                i += 3
                break
            i += 1

        return i

    def valid_tag(self, tag):
        if len(tag) > 9 or len(tag) < 1: return False
        if tag != tag.upper(): return False
        if not tag.isalpha(): return False
        return True

    def isValid(self, code: str) -> bool:
        if  len(code) < 7: return False
        if code[0] != '<' or code[-1] !='>': return False
        stack, C, i, first = [], len(code), 0, None

        while i < C:
            if code[i:].startswith('<![CDATA['):
                if not stack: return False
                i = self.parse_cdata(i, code)
                if i >= C: return False

            elif code[i:i + 2] == '</':
                i, tag = self.parse_tag(i + 2, code)
                if not self.valid_tag(tag): return False
                if not stack or stack[-1] != tag: return False
                stack.pop()

            elif code[i] == '<':
                i, tag = self.parse_tag(i + 1, code)
                if i >= C: return False
                if not self.valid_tag(tag): return False
                if first is None: first = tag
                elif not stack: return False
                stack.append(tag)

            elif code[i] == '>' and not stack:
                return False

            else:
                i += 1

        return len(stack) == 0

solution = Solution()
print(solution.isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))