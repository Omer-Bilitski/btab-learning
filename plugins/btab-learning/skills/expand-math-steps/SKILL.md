---
name: expand-math-steps
description: Expand skipped mathematical calculations between lines of a proof or derivation supplied as an image, screenshot, PDF excerpt, or equations. Use when the user requests intermediate lines, asks how one equation follows from another, or wants implicit differentiation, algebra, vector identities, or substitutions made explicit. Preserve the original argument; do not solve beyond the requested transition or replace it with a different proof.
---

# Expand Math Steps

Turn compressed mathematical reasoning into a readable derivation with explicit intermediate equations. Treat steps that seem obvious to a computer as potential gaps for the learner.

## Read and scope the input

1. Inspect the supplied image directly using an available image viewer. Use provided local copies when available. Read relevant equations, neighboring definitions, indices, arrows, dots, exponents, and equation numbers carefully.
2. Identify the transition the user requests. If the user asks generally to add detail, expand the visible derivation's skipped transitions. If they specify two lines or one operation, focus on that interval.
3. Preserve the source's notation and equation order. Define any added shorthand. Distinguish vector dot products from scalar multiplication and squared vector norms from componentwise squares.
4. If a crucial symbol is unreadable, request a clearer crop or transcription of that symbol. Do not invent missing expressions. Continue with any independently readable portion.

## Expand the mathematical work

- Write actual intermediate equations, not only descriptions such as “by differentiation” or “after simplification.”
- Use one meaningful mathematical operation per added line when that helps reveal the gap.
- Explicitly expand product rules, chain rules, sums, cancellations, index changes, substitutions, and vector identities relevant to the transition.
- State the rule and why it applies in a short sentence near the added equations.
- State assumptions needed for the step, including constant parameters, differentiability, fixed summation ranges, or permission to exchange limits and derivatives. Distinguish assumptions inferred from the context from those given explicitly.
- Explain substitutions separately from calculus. For example, first differentiate kinetic energy, then invoke Newton's second law, then substitute the force expression.
- Check algebra, factors, signs, indices, units where relevant, and scalar/vector consistency against both endpoints.
- If the source contains an error, identify it and show the corrected transition. Do not manufacture intermediate lines that justify an invalid equality.
- Avoid unrelated background or a complete alternative proof. Stop at the requested endpoint. On a request for further detail, subdivide the same transition rather than repeat the original explanation.

## Present the result

Respond in the user's language unless they request otherwise; the English language of this skill does not prescribe the response language. Keep mathematical expressions in separate display-math blocks when surrounding right-to-left prose could impair readability.

Briefly identify the transition, show the starting equation and inserted intermediate lines through the endpoint, then explain any remaining subtlety. Use standard rendered LaTeX. Retain equation numbers when useful and label additions as intermediate lines without impersonating source numbering. Do not edit the input image unless explicitly requested; by default, present the expanded derivation in the conversation.

## Reference example: time derivative of kinetic energy

For particles with time-independent masses and a fixed finite index set, start from

\[
K(t)=\sum_i\frac12m_i\lVert\mathbf v_i(t)\rVert^2
=\sum_i\frac12m_i\bigl(\mathbf v_i(t)\cdot\mathbf v_i(t)\bigr).
\]

Do not jump directly to the final derivative. Insert the product-rule calculation:

\[
\frac{dK}{dt}
=\sum_i\frac12m_i\frac{d}{dt}
\bigl(\mathbf v_i\cdot\mathbf v_i\bigr).
\]

\[
=\sum_i\frac12m_i
\left(\frac{d\mathbf v_i}{dt}\cdot\mathbf v_i
+\mathbf v_i\cdot\frac{d\mathbf v_i}{dt}\right).
\]

\[
=\sum_i\frac12m_i
\left(2\mathbf v_i\cdot\frac{d\mathbf v_i}{dt}\right)
=\sum_i m_i\mathbf v_i\cdot\frac{d\mathbf v_i}{dt}.
\]

Explain that dot-product symmetry makes the two terms equal and the factor of two cancels the one-half. The result is a scalar. If necessary, unpack the dot-product rule componentwise:

\[
\frac{d}{dt}(v_{ix}^2+v_{iy}^2+v_{iz}^2)
=2v_{ix}\dot v_{ix}+2v_{iy}\dot v_{iy}+2v_{iz}\dot v_{iz}.
\]

If the requested endpoint includes forces, add separately

\[
m_i\frac{d\mathbf v_i}{dt}=\mathbf F_i,
\qquad
\frac{dK}{dt}=\sum_i\mathbf v_i\cdot\mathbf F_i,
\]

then insert the source's expression for each force without changing its indices or signs. If masses vary with time, include the additional term
\(\sum_i\tfrac12\dot m_i\lVert\mathbf v_i\rVert^2\)
and do not use the constant-mass simplification silently.

## Personal explanation preferences

Adapt the current explanation to explicit preferences and available evidence about detail, intermediate algebra, intuition, examples, notation, language, and pace. Distinguish stated preferences from tentative patterns; one difficulty or silence does not establish a lasting preference or ability. Follow the current request when it differs from earlier preferences. Personal preferences belong to this learner and must not become defaults for other users.

Cross-chat persistence and weekly improvement proposals belong to the user's separately configured review task. This teaching skill uses available conversation evidence and does not write observations to external services or create scheduled tasks. Approved personal guidance should remain separate from distributed teaching instructions. Never claim proactive reviews or durable memory when those services are unavailable.
