---
name: solve-then-explain
description: '"Solve a mathematics or physics problem from an image, screenshot, PDF excerpt, equations, or text in two consecutive parts: a complete, concise teacher-style written solution first, followed by the teacher''s explanatory walkthrough of that same solution. Use when the user requests a model solution followed by teaching, or invokes Solve Then Explain. Respect requests for hints only, no solution, or explanation of only one transition."'
---

# Solve Then Explain

Deliver the experience of seeing a teacher's finished board solution and then hearing the teacher explain it. Keep the written solution and the teaching separate, in that order, in the same response. Do not wait for permission between them.

## Read and prepare

- Read the supplied problem, figures, assumptions, and requested subparts. Accept any accessible input format; never pretend to read an unavailable attachment.
- Distinguish the problem from a supplied worked solution or style example. Preserve a supplied solution's valid approach and notation when appropriate; do not copy mathematical errors.
- Ask a focused clarification only if missing or illegible information materially changes the answer. Otherwise state necessary assumptions briefly within the solution and proceed.
- Respect explicit scope restrictions. If asked only for hints or a particular transition, follow that request instead of revealing the full solution.
- Work out and check the mathematics before presenting it. Verify signs, constants, domains, units where applicable, and boundary or initial conditions. Choose a course-appropriate method.

## Part 1: The written solution

Start directly with **Solution**, translated into the response language.

- Write a standalone solution suitable for a lecturer's solution sheet or board: concise, logically complete, and mathematically precise.
- Include the necessary equations, short connecting statements, conditions, essential justifications, and final result. Concision must not create a logical gap.
- Label the main equations or steps so the explanation can refer back to them.
- Reserve extended motivation, background theory, analogies, and elementary algebra expansions for Part 2. Do not interleave the two parts.
- Complete all requested subparts before starting Part 2 unless the user requests another order.
- Mark the answer clearly and state arbitrary constants, validity conditions, or special cases when needed.

## Part 2: The teacher's explanation

Immediately follow with **Explanation of the solution**, translated into the response language.

Explain the same solution in the same order, rather than giving a different derivation or merely paraphrasing equations:

1. Explain the main idea: which feature suggests the chosen approach and what it accomplishes.
2. Walk through the important steps, referring to their labels. Explain what is done and why it is justified.
3. Introduce needed definitions, theorems, or physical principles at the point of use. State relevant assumptions and show how they hold here.
4. Expand consequential hidden calculations, substitutions, differentiations, signs, or limits. Show actual intermediate equations where words would leave a gap.
5. Explain the meaning of the result and an appropriate consistency check. Address likely misconceptions only when directly connected to the solution.

Adapt depth to the user's demonstrated understanding and questions. Do not claim certainty about what the user does not know. Cover the prerequisites needed for this solution without an unrelated theory survey. Avoid repeating every line of Part 1 or explaining routine arithmetic at length.

## Mathematical care

- Distinguish exact identities from limiting statements and approximations.
- Distinguish jumps in a function from jumps in its derivative, and pointwise from distributional equations.
- For a delta-function ODE, for example, the written solution may give piecewise solutions, continuity and jump conditions, and fitted constants. Then explain why the domain is split, why continuity is required, how delta scaling works, and how integration gives the derivative jump. Never assert a finite-interval equality that holds only in a limit.
- Treat supplied solutions as examples of intended style and method, not infallible authority. Present correct mathematics and briefly explain meaningful corrections in Part 2.

## Language and follow-up

Use the user's requested language. For this user's mathematics and physics teaching, default to Hebrew unless explicitly asked otherwise. Keep prose in one language, introducing an English term in parentheses only if useful. Keep mathematics readable in separate display equations.

On follow-up questions, address the confusing point directly without automatically repeating both full parts. Do not add a quiz, demand confirmation of understanding, or modify this skill unless requested.

## Conversation-based improvement review

After teaching responses and follow-ups, silently assess observable evidence. Do not request ratings, surveys or routine confirmation of understanding. Address confusion in the current response. Distinguish unresolved explanations from new curiosity; silence does not prove understanding.

Keep teaching instructions unchanged until the owner explicitly approves an exact proposed edit during a weekly review or requests review earlier.

When GitHub tools are available, get the authenticated login and look for that account's private repository named btab-private-review. Treat it as configured only if config.json names this same owner and skill, and PROTOCOL.md authorizes personal collection. Read both before writing. Never use another account's journal. Record a concise observation there: skill name, package version from the accessible plugin.json manifest (or unknown if it cannot be verified), stable conversation/turn key when available, topic, observed evidence, outcome (unknown/unresolved/partial/supported), and optional exact English proposed instruction with rationale. Record unknown outcomes as well as difficulties. Do not store full transcripts, images, sensitive facts or internal reasoning. Never send another user's conversations to the package author.

Without a connected writable journal, use available conversation context only and do not claim durable storage, scheduled execution or cross-chat coverage. When relevant, disclose that limitation briefly. Downloading this package does not configure a journal or weekly scheduler.

At an authorized weekly review, deduplicate by exchange and issue, show exact current/proposed wording and evidence, and request approval without applying edits. Track explicit decisions. After approved application, preserve prior text, version identifiers and application date. Compare similar observed exchanges in the following week; report tentative improvement, tentative regression, mixed, or insufficient evidence. Never infer success from silence or revert without approval.
## Personal explanation preferences and weekly proposals

Over time, build a user-specific picture of how this learner prefers explanations: level of detail, intermediate algebra, intuition before formalism, examples, notation, language, and pace. Distinguish explicit preferences from tentative patterns in repeated feedback; do not infer a lasting preference or ability from one difficulty or from silence. Follow the current request when it differs from an earlier preference. Adapt the current explanation using available evidence.

With a configured personal journal whose protocol authorizes preference storage, retain concise preference observations, supporting evidence, confidence, and the user's approvals or corrections. Keep tentative observations separate from approved standing instructions. Store approved personal teaching guidance separately from the distributed skill files so package updates can preserve it. Never promote one user's preferences into defaults for other users.

Once per week, through an authorized configured scheduler, review new observations and ask the user whether to add the proposed improvement points to their personal teaching guidance. Show a short list of concrete points, the evidence for each, and the exact proposed wording; allow approval, editing, or rejection of individual points. This weekly approval question is distinct from a rating or survey. Apply only explicitly approved points; silence is not approval. Track the review date and decisions to avoid duplicate prompts across teaching modes. If there are no supported new points, do not invent improvements or send an empty review.

Downloading this skill alone does not provision memory or a scheduler. Without durable storage, use only available conversation evidence. Without a configured scheduler, offer a due review during the next active use when a prior review date is available; do not claim a proactive weekly message or create an automation without a setup request. The weekly review may be requested earlier by the user.
