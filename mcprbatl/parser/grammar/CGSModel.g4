grammar CGSModel;

structure :
    'Structure' NAME '='
    '{'
        agents ','
        resources ','
        gstates ','
        propositions ','
        labellings ','
        availables ','
        costings ','
        transitions
    '}';


agents : POSITIVE_NUMBER;

resources : number;

gstates : '{' gstate (',' gstate)* '}'; // "state" is clashed with antlr
gstate :  NAME;

propositions : '{' (proposition (',' proposition)*)? '}';
proposition :  NAME;

labellings : '{' (labelling (',' labelling)*)? '}';
labelling : proposition '->' gstates;

availables : '{' (available (',' available)*)? '}';
available : '(' gstate ',' POSITIVE_NUMBER ')' '->' POSITIVE_NUMBER;

costings : '{' (costing (',' costing)*)? '}';
costing : '(' gstate ',' POSITIVE_NUMBER ',' POSITIVE_NUMBER ')' '->' cost;

cost : '(' (number (',' number)*)? ')';

transitions : '{' (transition (',' transition)*)? '}';
transition : '(' gstate ',' move ')' '->' states_distribution;

move : '(' (positive_number (',' positive_number)*)? ')';
states_distribution : '{' (state_dist (',' state_dist)*)? '}';
state_dist : gstate ':' POSITIVE_REAL_NUMBER;

positive_number : POSITIVE_NUMBER;
number : NUMBER_0 | POSITIVE_NUMBER;

POSITIVE_NUMBER : [1-9][0-9]*;
NUMBER_0 : '0';
POSITIVE_REAL_NUMBER : POSITIVE_NUMBER ('.' [0-9]+)? | NUMBER_0 '.' [0-9]*[1-9];
NAME : [a-zA-Z][a-zA-Z0-9]*;

WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '#' ~[\r\n]* -> skip;