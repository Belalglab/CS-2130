% Belal Glab
% 01/16/2024
% Facts
direct_flight(dgz, qyy).
direct_flight(dgz, azi).
direct_flight(qyy, csi).
direct_flight(azi, tva).
direct_flight(csi, ppg).
direct_flight(tva, brw).
direct_flight(brw, csi).

% Rules
route(Origin, Destination, Stops) :-
    find_route(Origin, Destination, 0, Stops).

find_route(Origin, Destination, Stops, Stops) :-
    direct_flight(Origin, Destination).

find_route(Origin, Destination, CurrentStops, TotalStops) :-
    direct_flight(Origin, Transit),
    Origin \= Destination,
    Transit \= Destination,
    NewStops is CurrentStops + 1,
    find_route(Transit, Destination, NewStops, TotalStops).
