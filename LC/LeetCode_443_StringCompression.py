def compress(chars):
  count = 1
  for i in range(len(chars) -1, -1, -1):
    if i and chars[i-1] == chars[i]:
      count += 1
      chars.pop(i)
    else:
      if count > 1:
        for item in str(count)[::-1]:
          chars.insert(i+1, item)
        count = 1

print(compress(["a","a","b","b","b","c","c"]))