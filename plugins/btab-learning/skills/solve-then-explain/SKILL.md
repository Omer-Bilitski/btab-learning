---
name: solve-then-explain
description: "Solve a mathematics or physics problem from an image, screenshot, PDF excerpt, equations, or text in two consecutive parts: a complete, concise teacher-style written solution first, followed by the teacher's explanatory walkthrough of that same solution. Use when the user requests a model solution followed by teaching, or invokes Solve Then Explain. Respect requests for hints only, no solution, or explanation of only one transition."
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

## Personal explanation preferences

Adapt the current explanation to explicit preferences and available evidence about detail, intermediate algebra, intuition, examples, notation, language, and pace. Distinguish stated preferences from tentative patterns; one difficulty or silence does not establish a lasting preference or ability. Follow the current request when it differs from earlier preferences. Personal preferences belong to this learner and must not become defaults for other users.

Cross-chat persistence and weekly improvement proposals belong to the user's separately configured review task. This teaching skill uses available conversation evidence and does not write observations to external services or create scheduled tasks. Approved personal guidance should remain separate from distributed teaching instructions. Never claim proactive reviews or durable memory when those services are unavailable.
