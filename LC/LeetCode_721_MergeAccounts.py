import collections

def accountsMerge(accounts):
  # create adj list for EMAILS, not mapping them all to a common account
  graph = collections.defaultdict(set)
  emails_to_name = {}

  for acc in accounts:
    name = acc[0]

    # map them to a single home node email to make graph simpler
    for e in acc[1:]:
      graph[e].add(acc[1])
      graph[acc[1]].add(e)
      emails_to_name[e] = name

  seen = set()
  def dfs(email):
    if email in seen:
      return
    sub_res = [email]
    seen.add(email)
    for nei in graph[email]:
      if nei not in seen:
        sub_res += dfs(nei)
    return sub_res

  res = []
  for acc in accounts:
    if acc[1] not in seen:
      res.append([emails_to_name[acc[1]]] + sorted(dfs(acc[1])))

  return res

print(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))