# Lista 2 MD
## Questão 1

$(A - B) - C \subseteq A - C$

$$(A - B) - C \\
\equiv \\
\{x\mid (x \in A\land x\notin B) \land x\notin C\} \\
\equiv \\
\{x\mid (x\in A \land x \notin C) \land (x\notin B \land x \notin C) \} \text{  [distributiva]}\\
\equiv 
\\
\{x \mid (x \in A \land x \notin C)\land \overline{(x \in B \lor x \in C)}\} \text{  [de morgan]}
\\
\equiv 
\\
(A - C) \cap \overline{(B \cup C)}
\\
\therefore 
\\
(A - B) - C \equiv \boxed{(A - C) \cap \overline{(B \cup C)} \subseteq A - C}
\\
qed \square $$

## Questão 2
$(A - C) \cap (C - B) = \{\}$

$$ 
(A - C) \cap (C - B) \\
\equiv 
\\
\{x \mid (x \in A \land x \notin C ) \land (x \in C \land x \notin B)\}
\\
\equiv
\\
\{x \mid (x \in A \land x \in C) \land (x \in A \land x \notin B) \land (x \notin C \land x \in C) \land (x \notin C \land x \notin B)\}
\\
\equiv
\\
(A \cap C) \cap (A -B)\cap \emptyset \cap(\bar{C} \cap \bar{B})
\\
\equiv
\\
\emptyset  $$
