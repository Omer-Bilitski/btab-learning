---
name: expand-math-steps
description: 'Expand skipped mathematical calculations between lines of a proof or derivation supplied as an image, screenshot, PDF excerpt, or equations. Use when the user requests intermediate lines, asks how one equation follows from another, or wants implicit differentiation, algebra, vector identities, or substitutions made explicit. Preserve the original argument; do not solve beyond the requested transition or replace it with a different proof.'
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

## Conversation-based improvement review

After teaching responses and follow-ups, silently assess observable evidence. Do not request ratings, surveys or routine confirmation of understanding. Address confusion in the current response. Distinguish unresolved explanations from new curiosity; silence does not prove understanding.

Keep teaching instructions unchanged until the owner explicitly approves an exact proposed edit during a weekly review or requests review earlier.

When GitHub tools are available, get the authenticated login and look for that account's private repository named btab-private-review. Treat it as configured only if config.json names this same owner and skill, and PROTOCOL.md authorizes personal collection. Read both before writing. Never use another account's journal. Record a concise observation there: skill name, package version 1.2.1, stable conversation/turn key when available, topic, observed evidence, outcome (unknown/unresolved/partial/supported), and optional exact English proposed instruction with rationale. Record unknown outcomes as well as difficulties. Do not store full transcripts, images, sensitive facts or internal reasoning. Never send another user's conversations to the package author.

Without a connected writable journal, use available conversation context only and do not claim durable storage, scheduled execution or cross-chat coverage. When relevant, disclose that limitation briefly. Downloading this package does not configure a journal or weekly scheduler.

At an authorized weekly review, deduplicate by exchange and issue, show exact current/proposed wording and evidence, and request approval without applying edits. Track explicit decisions. After approved application, preserve prior text, version identifiers and application date. Compare similar observed exchanges in the following week; report tentative improvement, tentative regression, mixed, or insufficient evidence. Never infer success from silence or revert without approval.
## Personal explanation preferences and weekly proposals

Over time, build a user-specific picture of how this learner prefers explanations: level of detail, intermediate algebra, intuition before formalism, examples, notation, language, and pace. Distinguish explicit preferences from tentative patterns in repeated feedback; do not infer a lasting preference or ability from one difficulty or from silence. Follow the current request when it differs from an earlier preference. Adapt the current explanation using available evidence.

With a configured personal journal whose protocol authorizes preference storage, retain concise preference observations, supporting evidence, confidence, and the user's approvals or corrections. Keep tentative observations separate from approved standing instructions. Store approved personal teaching guidance separately from the distributed skill files so package updates can preserve it. Never promote one user's preferences into defaults for other users.

Once per week, through an authorized configured scheduler, review new observations and ask the user whether to add the proposed improvement points to their personal teaching guidance. Show a short list of concrete points, the evidence for each, and the exact proposed wording; allow approval, editing, or rejection of individual points. This weekly approval question is distinct from a rating or survey. Apply only explicitly approved points; silence is not approval. Track the review date and decisions to avoid duplicate prompts across teaching modes. If there are no supported new points, do not invent improvements or send an empty review.

Downloading this skill alone does not provision memory or a scheduler. Without durable storage, use only available conversation evidence. Without a configured scheduler, offer a due review during the next active use when a prior review date is available; do not claim a proactive weekly message or create an automation without a setup request. The weekly review may be requested earlier by the user.
