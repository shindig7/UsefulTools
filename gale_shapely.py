# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:49:19 2019

@author: MS92789
"""
from numpy.random import randint, choice

class Person(object):
    def __init__(self, gender):
        self.number = randint(1,1000)
        self.gender = gender
        self.preferences = {}
        self.match = None
        self.Phi = 100000
        
    def set_preferences(self, population):
        mini = [(p, abs(p.number - self.number)) for p in population]
        for i, (p, k) in enumerate(sorted(mini, key=lambda k: k[1])):
            self.preferences[p] = i+1
            
    def set_phi(self):
        if self.match:
            self.Phi = self.preferences[self.match]
        else:
            self.Phi = 100000
            
    def switch_partners(self, other_person):
        self.match, other_person.match = other_person.match, self.match
        self.set_phi()
        other_person.set_phi()
            
    def __str__(self):
        return "Person, Gender {}, Number {}".format(self.gender, self.number)
    
    def __repr__(self):
        return "Person, Gender {}, Number {}".format(self.gender, self.number)
            

def get_random_pairs(males, females):
    for m in males:
        m.match = females.pop(females.index(choice(females)))
        m.set_phi()


def matchmaker(pair_list, prev_phi, n):
    print(f"Iteration {n}...")
    new_matches = []
    for m1, f1 in pair_list:
        for m2, f2 in pair_list:
            if m1 == m2:
                continue
            else:
                if m1.preferences[f2] < m1.preferences[f1] and m2.preferences[f1] < m2.preferences[f2]:
                    print(f"{m1} prefers {f2} and {m2} prefers {f1}, switching...")
                    new_matches.append((m1, f2))
                    new_matches.append((m2, f1))
                else:
                    continue
    phi = sum([m.preferences[f] for m, f in new_matches])
    print(f"Phi: {phi}, previously: {prev_phi}")
    if phi == prev_phi:
        return new_matches
    else:
        matchmaker(new_matches, phi, n+1)


POP_NUM = 2000

males = [Person('M') for _ in range(int(POP_NUM / 2))]
females = [Person('F') for _ in range(int(POP_NUM / 2))]


for m in males:
    m.set_preferences(females)

for f in females:
    f.set_preferences(males)
    

get_random_pairs(males, females)


prev_phi = 0
phi = sum([m.Phi for m in males])
i =1 
while phi != prev_phi:
    print(f"Iteration: {i}\tPrev_Phi: {prev_phi}\tPhi: {phi}\n")
    i += 1
    for m1 in males:
        for m2 in males:
            if m1 == m2:
                continue
            else:
                if m1.preferences[m2.match] < m1.Phi and m2.preferences[m1.match] < m2.Phi:
                    print(f"{m1} prefers {m2.match} and {m2} prefers {m1.match}, switching...")
                    m1.switch_partners(m2)
                else:
                    continue

    prev_phi = phi
    phi = sum([m.Phi for m in males])
    print()

print(f"Final:\tPrev_Phi: {prev_phi}\tPhi: {phi}")

#best_matches = matchmaker(random_pairs, len(males)**len(males), 1)
        
#for m, f in best_matches:
#    print(m, f)


