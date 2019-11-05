grammar CGSModel;

structure :
    BEGIN
        agents SEP
        resources SEP
        states SEP
        propositions SEP
        labellings SEP
        availables SEP
        costings SEP
        transitions
    END;


agents : POSITIVE_NUMBER;

resources : number;

states : '{' state (',' state)* '}';
state :  NAME;

propositions : '{' (proposition (',' proposition)*)? '}';
proposition :  NAME;

labellings : '{' (labelling (',' labelling)*)? '}';
labelling : proposition '->' states;

availables : '{' (available (',' available)*)? '}';
available : '(' state ',' POSITIVE_NUMBER ')' '->' POSITIVE_NUMBER;

costings : '{' (costing (',' costing)*)? '}';
costing : '(' state ',' POSITIVE_NUMBER ',' POSITIVE_NUMBER ')' '->' number;

transitions : '{' (transition (',' transition)*)? '}';
transition : '(' state ',' move ')' '->' states_distribution;

move : '(' (POSITIVE_NUMBER (',' POSITIVE_NUMBER)*)? ')';
states_distribution : '{' (state_dist (',' state_dist)*)? '}';
state_dist : state ':' POSITIVE_REAL_NUMBER;

number : NUMBER_0 | POSITIVE_NUMBER;
POSITIVE_NUMBER : [1-9][0-9]*;
NUMBER_0 : '0';
POSITIVE_REAL_NUMBER : POSITIVE_NUMBER ('.' [0-9]+)? | NUMBER_0 '.' [0-9]*[1-9];
NAME : [a-zA-Z][a-zA-Z0-9]*;
BEGIN : '{';
END : '}';
SEP : ',';

WS : [ \t\r\n]+ -> skip ;