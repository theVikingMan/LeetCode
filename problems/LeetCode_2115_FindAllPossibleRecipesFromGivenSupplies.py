import collections

def solution(recipes, ingredients, supplies):
  adjList = collections.defaultdict(list) # hold all of the ingredients and what that are a component of
  inDegress = collections.defaultdict(int) # count for number of ingredients to make that recipe

  for recp, ing in zip(recipes, ingredients): # loop over both the recipe and ingredients
    for i in ing:
      adjList[i].append(recp) # add the recipe that the ingrendent is a part of
      inDegress[recp] += 1 # increase how many ingredients are need to make the recipe

  S = supplies # rename Supplies
  L = [] # to solve one recipe built on another

  while S:
    oneIng = S.pop() # Analyze the first ingredient
    for component in adjList[oneIng]: # for every recipe that the ingrident can make
      inDegress[component] -= 1 # mark that we have one less ingredient to worry about
      if inDegress[component] == 0: # if we have found a recipes that has all ingreidents
        L.append(component) # Keeps track of completed recipes
        S.append(component) # Magic -> if a recipe is complete its now a supplies as we know we have it
  return L

print(solution(["bread","sandwich"],[["yeast","flour"],["bread","meat"]],["yeast","flour","meat"]))