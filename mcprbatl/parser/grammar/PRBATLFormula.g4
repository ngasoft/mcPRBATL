grammar PRBATLFormula;

formulas : state_formula*;

state_formula : enclosed_state_formula | top_state_formula | proposition | atl_state_formula | not_state_formula | state_formula 'or' state_formula ;

enclosed_state_formula : '(' state_formula ')';
top_state_formula : 'T';
not_state_formula : 'not' state_formula;
// or_state_formula : '(' state_formula 'or' state_formula ')';
atl_state_formula : '<<' agents '^' bound '>>' ('prob' comp_op real_number)? path_formula;

proposition : NAME;

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

POSITIVE_NUMBER : [1-9][0-9]*;
NUMBER_0 : '0';
POSITIVE_REAL_NUMBER : POSITIVE_NUMBER ('.' [0-9]+)? | NUMBER_0 '.' [0-9]*[1-9];

NAME : [a-zA-Z][a-zA-Z0-9]*;

WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '#' ~[\r\n]* -> skip;