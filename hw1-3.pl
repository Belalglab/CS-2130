% Wadlo Wildcat
% HomeWork 2
% File: hw1.pl and hw2.pl
% This is the pratice of the prolog program that creats a family tree
% Author: Belal Glab
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
% changes for homework two
% added the new follwing
% Author: Belal Glab
%

ancestor_of(A,B) :-parentof(A,B).
ancestor_of(A,B) :- parentof(A,C), ancestor_of(C,B).

% and the counting for the new generation
ancestor_gen(A,B,G) :- parentof(A,B), G is 1.
ancestor_gen(A,B,G) :- parentof(A,C), ancestor_gen(C,B,F), G is F + 1.

% Define the custom logic gate 'mygate'
mygate(0, 0, 0, 1).
mygate(0, 0, 1, 1).
mygate(0, 1, 0, 0).
mygate(0, 1, 1, 0).
mygate(1, 0, 0, 1).
mygate(1, 0, 1, 1).
mygate(1, 1, 0, 0).
mygate(1, 1, 1, 1).

% Define XOR and NAND gates
myxor(0, 0, 0).
myxor(0, 1, 1).
myxor(1, 0, 1).
myxor(1, 1, 0).

mynand(0, 0, 1).
mynand(0, 1, 1).
mynand(1, 0, 1).
mynand(1, 1, 0).

% Define the circuit combining XOR and NAND gates
mycircuit(X, Y, Z, F) :-
    myxor(X, Y, T1),
    myxor(T1, Z, T2),
    mynand(T1, T2, F),
    write(X), write(' '), write(Y), write(' '), write(Z), write(' '), write(F), write('\n').
