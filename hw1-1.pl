% Wadlo Wildcat
% HomeWork 1
% File: hw1.pl
% This is the pratice of the prolog program that creats a family tree
%
%

% biological female family members
female(ann).
female(beth).
female(liz).
female(sue).
female(mary).
female(carol).

% biological male family members
male(bob).
male(ted).
male(bill).
male(sam).
male(harry).
male(john).
male(matt).

% our rules come next
% parental relationships

parentof(beth,bill).
parentof(bill,jill).
parentof(bill,liz).
parentof(ann,jill).
parentof(ann,liz).
parentof(ann,ted).
parentof(lizz,matt).
parentof(matt,john).
parentof(bob,carol).
parentof(harry,sue).
parentof(harry,sam).
parentof(carol,sue).
parentof(carol,sam).
parentof(sue,marry).
parentof(mary,john).

% Our rules come next
childof(Child,Parent) :- parentof(Parent,Child).

siblings(Sib1, Sib2) :- parentof(Parent, Sib1),
                        parentof(Parent, Sib2).

sisterof(Sis, Sib) :- siblings(Sis, Sib),
                      female(Sis).
