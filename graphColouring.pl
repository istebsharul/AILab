% Helper predicate to check if it's safe to assign a color to a vertex
is_safe(V, Graph, Color, C) :-
    nth1(V, Graph, AdjacentVertices),
    check_adjacent_vertices(AdjacentVertices, Graph, Color, C).

check_adjacent_vertices([], _, _, _).
check_adjacent_vertices([AdjacentVertex|Rest], Graph, Color, C) :-
    nth1(AdjacentVertex, Color, AdjacentColor),
    AdjacentColor \= C,
    check_adjacent_vertices(Rest, Graph, Color, C).

% Backtracking predicate to color the vertices
color_vertices(_, [], _).
color_vertices(Graph, [Vertex|Rest], Color) :-
    member(C, Color),
    is_safe(Vertex, Graph, Rest, Color, C),
    color_vertices(Graph, Rest, [C|Color]).

% Main predicate to solve the graph coloring problem
graph_coloring(Graph, NumColors, Colors) :-
    length(Graph, NumVertices),
    length(Colors, NumVertices),
    color_vertices(Graph, [1|Rest], Colors),
    permutation(Colors, Colors),
    is_valid_coloring(Graph, Colors).

% Helper predicate to check if the coloring is valid
is_valid_coloring(_, []).
is_valid_coloring(Graph, [C|Rest]) :-
    check_adjacent_vertices(Rest, Graph, [C|Rest], C),
    is_valid_coloring(Graph, Rest).

% Example usage
graph([[0, 1, 1, 1],
       [1, 0, 1, 0],
       [1, 1, 0, 1],
       [1, 0, 1, 0]]).
num_colors(3).

solve(Colors) :-
    graph(Graph),
    num_colors(NumColors),
    graph_coloring(Graph, NumColors, Colors).

% Query
?- solve(Colors).
