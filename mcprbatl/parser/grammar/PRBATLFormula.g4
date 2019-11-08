grammar PRBATLFormula;

formulas : state_formula*;

state_formula : OPEN state_formula CLOSE | TOP | NOT state_formula | PROPOSITION | state_formula OR state_formula |
                OPEN_AGENT agents '^' bound CLOSE_AGENT (PROB comp_op real_number )? path_formula ;

agents : '{' (agent (',' agent)*)? '}';
agent: POSITIVE_NUMBER;

bound : '(' (bound_number (',' bound_number)*)? ')';
bound_number : infinite | number;
infinite : '*';

comp_op : LT_OP | LEQ_OP | GEQ_OP | GT_OP;

path_formula : next_formula | until_formula | neg_path_formula;
next_formula : 'Next' state_formula;
until_formula : state_formula (finite_until | infinite_until) state_formula;
finite_until : 'Until^' number ;
infinite_until : 'Until';
neg_path_formula : 'not' path_formula;

number : NUMBER_0 | POSITIVE_NUMBER;
real_number : NUMBER_0 | POSITIVE_NUMBER| POSITIVE_REAL_NUMBER;

LT_OP : '<';
GT_OP : '>';
LEQ_OP : '=<';
GEQ_OP : '>=';

OPEN : '(';
CLOSE : ')';
TOP : 'T';
NOT : 'not';
PROB : 'prob';
OR : 'or';
OPEN_AGENT : '<<';
CLOSE_AGENT : '>>';

POSITIVE_NUMBER : [1-9][0-9]*;
NUMBER_0 : '0';
POSITIVE_REAL_NUMBER : POSITIVE_NUMBER ('.' [0-9]+)? | NUMBER_0 '.' [0-9]*[1-9];

PROPOSITION : NAME;
NAME : [a-zA-Z][a-zA-Z0-9]*;

WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '#' ~[\r\n]* -> skip;