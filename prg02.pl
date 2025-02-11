% Logic gates definitions based on truth tables
and_gate(0, 0, 0).
and_gate(0, 1, 0).
and_gate(1, 0, 0).
and_gate(1, 1, 1).

or_gate(0, 0, 0).
or_gate(0, 1, 1).
or_gate(1, 0, 1).
or_gate(1, 1, 1).

xor_gate(0, 0, 0).
xor_gate(0, 1, 1).
xor_gate(1, 0, 1).
xor_gate(1, 1, 0).

% 2-bit adder circuit
circuit(A1, A0, B1, B0, S1, S0, CarryOut) :-
    % First half adder (for the least significant bit)
    xor_gate(A0, B0, HalfSum0),
    and_gate(A0, B0, HalfCarry0),

    % Second half adder
    xor_gate(A1, B1, HalfSum1),
    and_gate(A1, B1, HalfCarry1),

    % Combining the two half adders
    xor_gate(HalfSum1, HalfCarry0, S1),
    and_gate(HalfSum1, HalfCarry0, TempCarry),

    % Final Carry Out
    or_gate(TempCarry, HalfCarry1, CarryOut),

    % Sum
    S0 = HalfSum0.

% Optional code for printing
pmath(A, B, C, D, E, F, G) :-
    write(A), write(B), write(" + "), write(C), write(D),
    write(" = "), write(E), write(F), write(" with a carry of "), writeln(G).

% Test the circuit with specific inputs
test_circuit :-
    circuit(0, 0, 0, 0, S1, S0, C), pmath(0, 0, 0, 0, S1, S0, C),
    circuit(0, 0, 0, 1, S1, S0, C), pmath(0, 0, 0, 1, S1, S0, C),
    true.
