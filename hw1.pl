% Waldo Wildcat
% Homework 1
% File: hw1.pl
% This is a practice Prolog program that creates a family tree
% Easy peasy... comments will be part of grade for all programming assignments!!

% Facts for females
female(ann).
female(beth).
female(liz).
female(sue).
female(jill).
female(mary).
female(carol).

% Facts for males
male(bob).
male(ted).
male(bill).
male(sam).
male(harry).
male(john).
male(matt).

% Parent-of relationships
parentof(beth, bill).
parentof(bob, bill).
parentof(bob, bob).
% Add other parentof relationships based on the family tree diagram

% Rules for childof
childof(Child, Parent) :- parentof(Parent, Child).

% Rules for siblings
siblings(Sib1, Sib2) :-
    parentof(Parent, Sib1),
    parentof(Parent, Sib2),
    Sib1 \== Sib2.

% Rules for sisterof
sisterof(Sis, Sib) :-
    siblings(Sis, Sib),
    female(Sis).

% Query examples
% Try running these queries in SWI-Prolog after saving your file
% File -> Consult -> Select your file

% Query: Is Matt female? (Should return false)
female(matt).

% Query: Is Bill the parent of Beth? (Should return false)
parentof(bill, beth).

% Query: Is Beth the parent of Bill? (Should return true)
parentof(beth, bill).

% Query: Who are the children of Ann? (Should return Jill, Liz, and Ted)
parentof(ann, Child).

% Query: Who are the siblings of Ted? (Should return Jill and Liz)
siblings(ted, Sib).

% Query: Who are the sisters of Ted? (Should return Jill and Liz)
sisterof(Sis, ted).
