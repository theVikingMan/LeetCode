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
        if len(code) < 7: return False # check if input code is valid length
        if code[0] != '<' or code[-1] !='>': return False # need open + close tags
        stack, codeLen, i, first = [], len(code), 0, None

        while i < codeLen:
            if code[i:].startswith('<![CDATA['): # Option 1: cdata to validate
                if not stack: return False # need it to be enclosed by another tag
                i = self.parse_cdata(i, code) # basically validate it is closed propery
                if i >= codeLen: return False

            elif code[i:i + 2] == '</': # Option 2: closing tag to validate
                i, tag = self.parse_tag(i + 2, code) # extract tag
                if not self.valid_tag(tag): return False # validate that extracted tag
                if not stack or stack[-1] != tag: return False # Need top stack tag to match
                stack.pop()

            elif code[i] == '<': # Option 3: opening tag to validate
                i, tag = self.parse_tag(i + 1, code) # grab the tag
                if i >= codeLen: return False # see if we overdid it
                if not self.valid_tag(tag): return False # check grabbed tag
                if first is None:
                  first = tag
                elif not stack: # Not the first tag and we have closed the first tag
                  return False
                stack.append(tag)

            elif code[i] == '>' and not stack:
                return False

            else: # no tag, just content between tags
                i += 1

        return len(stack) == 0

solution = Solution()
print(solution.isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))