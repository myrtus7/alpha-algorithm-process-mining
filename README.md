# Alpha Algorithm Process Mining
Python implementation of the α-algorithm (van der Aalst et al., 2004): discovers a Petri net (workflow net) from an event log.

## Formal definition

Let $T$ be a set of tasks. $\sigma \in T^*$ is a workflow trace and $L \in \mathcal{P}(T^*)$ is a workflow log.

**Log-based ordering relations**  for $a, b \in T$:

- $a >_L b \iff \exists\, \sigma = t_1 t_2 t_3 \dots t_{n-1},\ \exists\, i \in \{1, \dots, n-2\} : \sigma \in L \wedge t_i = a \wedge t_{i+1} = b$ (directly follows)
- $a \rightarrow_L b \iff a >_L b \wedge b \not>_L a$ (direct causal relation)
- $a \;\#_L\; b \iff a \not>_L b \wedge b \not>_L a$ (never follow each other directly)
- $a \parallel_L b \iff a >_L b \wedge b >_L a$ (potential parallelism)

**Algorithm** 

1. $T_L = \{ t \in T \mid \exists \sigma \in L : t \in \sigma \}$
2. $T_I = \{ t \in T \mid \exists \sigma \in L : t = \mathit{first}(\sigma) \}$
3. $T_O = \{ t \in T \mid \exists \sigma \in L : t = \mathit{last}(\sigma) \}$
4. $X_L = \{ (A,B) \mid A \subseteq T_L \ \wedge\ B \subseteq T_L \ \wedge\ \forall a \in A, \forall b \in B : a \rightarrow_L b \ \wedge\ \forall a_1, a_2 \in A : a_1 \#_L a_2 \ \wedge\ \forall b_1, b_2 \in B : b_1 \#_L b_2 \}$
5. $Y_L = \{ (A,B) \in X_L \mid \forall (A',B') \in X_L : A \subseteq A' \wedge B \subseteq B' \Rightarrow (A,B) = (A',B') \}$
6. $P_L = \{ p_{(A,B)} \mid (A,B) \in Y_L \} \cup \{ i_L, o_L \}$
7. $F_L = \{ (a, p_{(A,B)}) \mid (A,B) \in Y_L, a \in A \} \cup \{ (p_{(A,B)}, b) \mid (A,B) \in Y_L, b \in B \} \cup \{ (i_L, t) \mid t \in T_I \} \cup \{ (t, o_L) \mid t \in T_O \}$
8. $\alpha(L) = (P_L, T_L, F_L)$

## Reference

W. M. P. van der Aalst, A. J. M. M. Weijters, L. Maruster, *Workflow Mining: Discovering Process Models from Event Logs*, IEEE Transactions on Knowledge and Data Engineering, 16(9):1128–1142, 2004. doi:[10.1109/TKDE.2004.47](https://doi.org/10.1109/TKDE.2004.47)
