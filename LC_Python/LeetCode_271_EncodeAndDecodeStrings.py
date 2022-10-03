class Codec:
    def encode(self, strs):
      encodedStr = ""
      for word in strs:
        encodedStr += str(len(word)) + "#" + word
      return encodedStr

    def decode(self, s):
      decodedArr = []
      i = 0
      while i < len(s):
        j = i
        while s[j] != "#":
          j += 1
        wordLength = int(s[i:j])
        decodedArr.append(s[j+1:j + 1 + wordLength])
        i = j + 1 + wordLength
      return decodedArr

# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ["Hello","World"]
print(codec.decode(codec.encode(strs)))