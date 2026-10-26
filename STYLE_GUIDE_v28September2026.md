# Armchair Quantum Physicist --- Writing Style Guide

## Purpose

This is the current house style for *The Armchair Quantum Physicist*. It
is an empirical guide: it describes the writing choices that repeatedly
survive Rob's own editing, rather than trying to imitate surface quirks
from older posts.

The strongest evidence is the latest human-edited prose, especially the
LightBeams work and subsequent controlled writing/editing exercises.
Older habits that no longer match the current writing process should not
be reproduced for authenticity.

> **Write like a physicist working through an argument with an
> interested reader. Let the physics provide the surprise.**

A second principle now sits beside it:

> **Earn the next sentence.**

The reader should understand why a fact, equation, question, definition,
or conclusion appears *now*. Create the need for an idea before
supplying it. Do not announce surprise before showing something
surprising, answer a question the reader has not yet had reason to ask,
or add explanatory scaffolding when the connection is already clear.

------------------------------------------------------------------------

## 1. Core Voice

The voice is direct rather than theatrical; curious without being
breathless; technically precise without sounding like a textbook;
conversational without becoming chatty; and comfortable with genuine
uncertainty.

The writing should feel like a physicist reasoning with the reader, not
presenting a finished lecture from above.

A useful test is:

> **Would I actually say this sentence aloud while explaining the idea
> to another physicist or an interested reader?**

If not, simplify it.

------------------------------------------------------------------------

## 2. Earn the Next Sentence

This is the central organizing principle.

Before introducing something, ask why the reader needs it *at this
point*.

A good sequence often looks like:

**physical fact → immediate implication → new problem → idea needed to
solve it**

or:

**claim → concrete example → mechanism → consequence → consistency
check**

These are not templates. They describe how the reasoning tends to move.

For example, do not coldly introduce a second route to a result:

> There is another way to approach the problem. Instead of starting from
> quantum mechanics, we can start from information.

If the intellectual turn matters, first let the reader encounter the
question:

> This raises a different question: can we reach the same limit without
> assuming quantum mechanics?

The question is useful because it creates the need for what follows.

But do not manufacture such questions everywhere. If the next step is
already obvious, simply take it.

------------------------------------------------------------------------

## 3. Let the Reader Discover the Physics With Us

The prose develops an idea rather than announcing a polished conclusion.

A common section-level movement is:

**observation → question → explanation → consequence → next question**

Another characteristic move is:

**apparent conclusion → why it is incomplete → deeper idea**

For example:

> The doughnut-shaped intensity is easy to see, but it isn't the
> interesting part. The interesting part is hidden in the phase.

Or:

> So quantum mechanics tells us where Nature stops. But that is not
> quite the same as understanding why it stops there.

The important point is not the exact wording. The reader first reaches a
reasonable conclusion, then sees why another step is needed.

------------------------------------------------------------------------

## 4. Start From the Physics, Not the Classification

Prefer explaining what happens before naming or classifying it.

**AI-native**

> The key to the Hong--Ou--Mandel effect is quantum interference between
> indistinguishable two-photon pathways.

**How Rob naturally explains it**

> The HOM dip occurs because there are different 'histories' leading to
> the same outcome.

The second version starts with the mechanism the reader needs. Terms
such as *interference*, *pathway*, or *indistinguishability* can enter
once their role is clear.

Likewise, prefer:

> The beam carries orbital angular momentum: momentum related to
> rotation around the beam's propagation axis.

over an elaborate introduction whose main purpose is to deliver the term
elegantly.

Technical language should name an idea that the reader already needs,
not create the appearance of explanation.

------------------------------------------------------------------------

## 5. Result First --- But Only When the Result Has Been Earned

A strong preference remains to state what happens and then explain why.

**AI-native**

> Add and subtract them, and the result is unsurprising --- the same
> two-lobed pattern, just rotated by 45°.

**How Rob would write it**

> Adding or subtracting them does not create a fundamentally new beam.
> It simply rotates the same two-lobed pattern by 45°.

**AI-native**

> Combine them with a quarter-cycle phase instead of a sign, and the
> result stops looking like a rotated two-lobed mode.

**How Rob would write it**

> The result changes if we introduce a quarter-cycle phase difference.

Then explain what changes.

But "result first" does **not** mean revealing an answer before the
reader knows the question. At the level of the whole argument, create
the problem first. At the level of an individual explanatory step, state
the result directly rather than staging a miniature demonstration.

------------------------------------------------------------------------

## 6. Build the Argument in Small Causal Steps

Do not optimize for information density.

If A makes B possible, and B can then lead to C, do not casually write A
→ C merely because the sentence flows well. Preserve distinct physical
claims.

From the LightBeams and analogue-gravity work, a characteristic
progression is:

> The group velocity becomes zero. The wave stalls. Dispersion can also
> allow other modes with the same frequency but a different wavelength.
> The incoming mode can be converted into these other modes.

The existence of another allowed mode and conversion into that mode are
not the same claim. Keeping them separate improves both physics and
pedagogy.

However, do **not** split a simple cause from its immediate consequence
merely to produce short sentences.

Prefer:

> Because the phase winds around the centre of the beam, the local
> momentum acquires an azimuthal component.

when cause and consequence form one natural thought.

The rule is:

> **Separate distinct conceptual steps; keep immediate cause and effect
> together when that is clearer.**

------------------------------------------------------------------------

## 7. Prefer Physical Language

Prefer things happening physically: light **blurs, spreads, twists,
pushes and rotates**; phase **winds**; modes **combine**; roots
**merge**; a wave **stalls**; a beam **broadens**.

Prefer:

> the group velocity becomes zero

when that is clearer to the intended reader than:

> the group velocity vanishes

Prefer:

> modes with the same frequency but a different wavelength

when the physical distinction matters more than compact expert shorthand
such as:

> modes at conserved laboratory frequency

This is not a ban on technical language. Use the technically natural
expression when it genuinely helps.

------------------------------------------------------------------------

## 8. Keep the Reader's Current Physical Vocabulary

Do not switch vocabulary merely because another variable or formulation
is more conventional.

If the paragraph has been discussing a wavelength becoming shorter,
continuing with *wavelength* may be clearer than suddenly switching to
*wavenumber*, even if the dispersion relation is normally written as
ω(k).

Introduce *k* when *k* becomes useful.

More generally:

> **Maintain conceptual continuity across sentences. Change vocabulary
> because the argument needs it, not because a more expert formulation
> is available.**

------------------------------------------------------------------------

## 9. Technical Language and Notation Must Earn Their Place

Give the physical idea before, or together with, the technical term.

Prefer:

> a quarter-cycle, or π/2, phase difference

rather than leading with a complex phase factor.

Once *Laguerre--Gaussian mode* has been introduced, *vortex beam* or
*doughnut beam* may be clearer in the rest of the explanation.

A new symbol or name should repay the reader's effort. Use one name for
one thing wherever possible.

Do not narrate the act of introducing terminology. Sometimes the
cleanest definition is simply:

> The beam carries OAM: momentum related to rotation around the beam's
> propagation axis.

------------------------------------------------------------------------

## 10. Equations Enter Because We Need Them

An equation should feel like the next step, not a formal ceremony.

**AI-native**

> To see this mathematically, let us now derive the corresponding
> expression.

**How Rob would write it**

> We can write this phase dependence as

> *E* ∝ eⁱφ.

or, when appropriate:

> Write the field in polar coordinates.

After an equation, do not mechanically paraphrase every symbol. Explain
what changed physically.

**AI-native**

> This expression shows the azimuthal dependence of the field.

**How Rob would write it**

> An explicit eⁱφ falls out. The phase completes a full turn if you walk
> once around the beam axis.

Boundary cases and simple examples are useful when they build intuition:
50% versus 100%, n = 0 before general n, or the simplest two-mode case
before the full family.

------------------------------------------------------------------------

## 11. Referential Clarity Beats Elegant Variation

Words such as *this*, *it*, *these*, *the same*, and *this distinction*
are useful when their reference is genuinely obvious.

Prefer the short form when it is unambiguous:

> Alice chooses which measurement to perform. This does not affect Bob's
> statistics.

Do not repeat *Alice's choice of measurement* merely to avoid the word
*this*.

But if the reference could reasonably point to more than one preceding
idea, repeat the noun.

Weak:

> This distinction is important.

Better when several distinctions are in play:

> This distinction between correlations in the measurement outcomes and
> communication is important.

The rule is:

> **Use the shortest unambiguous reference. Repeat the noun when
> repetition buys clarity.**

Do not avoid repetition merely because conventional editing advice says
repeated words are inelegant.

------------------------------------------------------------------------

## 12. Make Important Contrasts Explicit

When two cases are central to the reasoning, it is often clearer to
state both.

For example:

> Without knowing Alice's result, Bob sees only random outcomes. When
> Alice and Bob later compare their results, the correlations become
> visible.

This is often clearer than describing only one case and leaving the
complementary case implicit.

Useful structures include:

**with A / without A**

**case 1 / case 2**

**classically / quantum mechanically**

**what changes / what stays the same**

Do not mechanically duplicate every contrast. Use this when the
distinction carries the physics.

------------------------------------------------------------------------

## 13. Trust Previously Established Context

A paragraph does not need to be independently complete.

AI often restates background to create a perfectly self-contained
explanation. That can slow the argument.

If the previous section has already established what happens in the
nondispersive model, there is no need to repeat:

> In a nondispersive model there is nothing to stop this process. Real
> media behave differently.

The next paragraph can continue directly with dispersion.

Trust the reader to remember what has just been established.

------------------------------------------------------------------------

## 14. Paragraphs Make One Conceptual Move

A paragraph often performs one main job. Useful patterns include:

**result → reason → consequence**

**known thing → small change → surprising result**

**claim → example → mechanism → consequence → consistency check**

The HOM explanation naturally followed the last pattern:

-   different histories can lead to one outcome;
-   both photons transmitted and both reflected provide a concrete
    example;
-   quantum amplitudes add;
-   opposite amplitudes can cancel;
-   another outcome must then gain probability because total probability
    remains one.

This last step --- checking the conclusion against a broader constraint
--- is characteristic and useful.

Paragraphs are often two to four sentences, but length is not a rule.
The aim is not short prose. It is clear movement through the reasoning.

------------------------------------------------------------------------

## 15. Keep Sentence Rhythm Uneven

Most sentences are medium length, but natural variation matters more
than a target word count.

Longer explanations can sit next to short turns:

> The wave stalls.

> They are not the same.

> That coincidence is the remarkable part.

> But does that close the story? Not completely.

Short sentences should mark a real physical or conceptual turn. Do not
manufacture a punchline at the end of every paragraph.

Avoid making every paragraph follow:

> Statement. Explanation. Contrast. Punchline.

That regularity is a common AI signature.

Semicolons, parentheses and em dashes are natural when they clarify
relationships. Do not add them as decoration.

------------------------------------------------------------------------

## 16. Questions Must Create or Expose a Real Need

Questions are valuable when they make the reader encounter the problem
before the solution.

Good:

> This raises the obvious question: is the Gaussian the only shape that
> survives diffraction?

> Can we reach the same limit without assuming quantum mechanics?

The question should emerge from what the reader has just learned.

Avoid generic transitions:

> So what does this tell us?

> But what is really going on?

> Why should we care?

Do not ask a question simply because a section transition needs energy.

At the same time, do not remove a useful question merely because
declarative prose would be more concise. A well-earned question creates
*wonder*: the reader sees why the next idea is worth pursuing.

Use this deliberately, but not constantly.

------------------------------------------------------------------------

## 17. Transitions Are Plain

Natural connectors include **But, Yet, Now, So, Instead, Suppose, It
turns out, The surprise is, More generally, In practice** and **In
principle** when they express a real logical relationship.

Often **because**, **so**, **but**, **this means**, and **after all**
are enough. The writing is strongly causal: each sentence should make
clear why the previous fact leads to the next one.

Do not force legacy phrases such as *"This triggers the question..."*,
*"In this post, we will discuss..."* or *"Interestingly enough..."*
merely because they appeared in older writing.

**AI-native**

> But here is where things get interesting.

**How Rob would write it**

> A vortex beam is different.

If the next sentence contains the interesting fact, delete the sentence
telling the reader that it is interesting.

------------------------------------------------------------------------

## 18. Do Not Narrate the Act of Explaining

AI prose frequently inserts scaffolding such as:

> To understand this...

> To make this more precise...

> Let us now consider...

> We started with X because...

> More generally, we can see that...

Often the explanation is clearer without it.

**AI-native**

> To make this more precise, write the field as...

**How Rob would write it**

> We can write this phase dependence as...

**AI-native**

> We started with HG₁₀ and HG₀₁ because they give the simplest example.
> More generally, the same construction can be applied to higher-order
> modes.

**How Rob would write it**

> For HG₁₀ and HG₀₁ the construction produces the simplest vortex. The
> same idea works for higher-order modes.

Use explanatory scaffolding only when it performs a real logical job.

------------------------------------------------------------------------

## 19. Do Not Manufacture Drama --- But Earned Emphasis Is Fine

The physics supplies the surprise.

Avoid *"and that changes everything"*, *"the answer is surprisingly
simple"*, artificial cliff-hangers, and repeated declarations that
something is remarkable or fascinating.

**AI-native**

> What happened next would finally settle the question.

**How Rob would write it**

> The experimental demonstration came a few years later.

But do not flatten every ending. A slightly more crafted sentence can be
useful when it genuinely closes a conceptual unit.

Factual body sentence:

> So the physics predicts a torque, but experimentally it remained below
> the detection limit.

Possible closing sentence:

> The effect was real. The measurement simply wasn't sensitive enough to
> see it.

The second is more crafted, but here the emphasis has been earned by the
preceding discussion.

The distinction is not **plain versus rhetorical**. It is **earned
versus manufactured**.

------------------------------------------------------------------------

## 20. Avoid Over-Engineered Summaries

AI prose likes elegant compression.

**AI-native**

> So the chain is complete: a stable transverse mode → a winding phase →
> sideways momentum → orbital angular momentum → mechanical rotation.

**How Rob would write it**

> We started with beam shapes that survive diffraction, and ended with a
> beam that can transfer angular momentum to matter.

**AI-native**

> Sometimes physics is exactly this: right idea, right setup, and nature
> simply won't hand you a clean number.

**How Rob would write it**

> In this case the physics was right, but the experiment never produced
> a clean enough signal.

Be suspicious of three-part rhetorical lists, mirrored clauses, arrow
chains, "X, Y and Z" climaxes and perfectly symmetrical closing
sentences.

But again, do not turn this into a ban on memorable writing. If a
conclusion has been earned, it may be given weight.

------------------------------------------------------------------------

## 21. Avoid Duplicate Explanation

Explanatory prose often says the same thing once physically and once
rhetorically.

> The transverse momenta cancel but leave angular momentum behind.

and:

> Opposite sides give no net sideways push, but their torques add.

These do essentially the same job. Keep the more physical explanation.

Ask:

> **Do two sentences in this paragraph perform the same explanatory
> job?**

If so, remove or combine one. Do not add a mini-summary after every
explanation.

------------------------------------------------------------------------

## 22. Analogies Are Tools, Not Decoration

Use an analogy when it explains a specific mechanism.

Good:

> ...just as a guitar string only supports certain standing-wave
> patterns.

Be cautious with vivid analogies that distort the physics:

> Think of the beam as a spinning corkscrew of light.

Use the analogy, make the intended connection, then return to the
physics.

------------------------------------------------------------------------

## 23. History Should Make Ideas Feel Earned

Historical material works when it explains how an idea or experiment
emerged:

> This mode converter was built and demonstrated in 1993 by
> Beijersbergen and colleagues in Leiden.

History is part of the scientific argument, not decorative background.

Do not require a historical preamble for every concept. The question is
always whether the history helps the reader understand why the next idea
appeared.

------------------------------------------------------------------------

## 24. "We" and "I"

**We** is useful when author and reader are genuinely taking a step
together:

> We can build the higher-order versions...

> We started with beam shapes that survive diffraction...

Do not insert *we* into every paragraph as a voice marker.

**I** is appropriate for an actual personal judgement, recollection or
uncertainty:

> I wonder whether...

Avoid an impersonal academic voice when a direct statement is clearer.

------------------------------------------------------------------------

## 25. Uncertainty Should Be Real

The writing is comfortable leaving questions open:

> Perhaps Information Causality is telling us why Nature is not more
> quantum.

> Or perhaps Information Causality is seeing the shadow of something
> deeper.

Do not manufacture hedging to sound thoughtful. Conversely, do not make
a stronger claim than the evidence supports.

An open question can be rhetorically strong when the article has
genuinely arrived there:

> So we arrive at an intriguing possibility: Information Causality may
> be the principle that explains the quantum boundary. But is it really
> the final answer?

This works only if the preceding argument has created that question.

------------------------------------------------------------------------

## 26. Pull Quotes Can Be More Crafted

The body should remain comparatively plain. Pull quotes can carry a
memorable formulation:

> **The doughnut is what we see in the light intensity. The twist is
> hidden in the phase.**

> **Go even slightly beyond the quantum limit, and eventually there is a
> guessing game large enough for information theory to object.**

This lets the pull quote be sharp without forcing every paragraph to
compete with it.

------------------------------------------------------------------------

## 27. Titles, Subtitles and Section Headers

Titles should pose or imply the central puzzle rather than merely name
the subject:

-   *Why Doesn't a Laser Beam Lose Its Shape?*
-   *Why Isn't Nature More Quantum?*

Subtitles clarify the promise without explaining the whole article.

Section headers should tell the story. Prefer:

> **Diffraction Destroys Shapes --- Yet a Gaussian Survives**

> **The Doughnut Is Hiding a Twist**

over generic labels such as *Gaussian Beams* or *Orbital Angular
Momentum*.

Headers can be more crafted than body prose, but should describe the
conceptual move.

------------------------------------------------------------------------

## 28. Figures and Captions

A figure should have a job in the argument. The surrounding prose
establishes what the reader is about to learn from it.

A useful caption pattern is:

**what is shown → what differs → what the reader should notice**

The caption should stand on its own without repeating the entire
surrounding paragraph. Alt text describes what is visually present; it
is not a second caption.

------------------------------------------------------------------------

## 29. Openings and Endings

### Openings

Do not standardize openings into *"In this post, we will..."*.

Establish the puzzle quickly through a physical observation, game,
experiment, contradiction, or genuine question. Give the reader a reason
to continue before introducing machinery.

The opening should create a problem worth solving, not promise that
something interesting will eventually happen.

### Endings

Do not mechanically summarize the article.

A strong ending often states where the argument has arrived, identifies
what remains unresolved or what changes next, and leaves the reader with
the underlying question.

For a series it can point naturally forward:

> The next question is different: what changes when we actually apply
> quantum mechanics to the light itself?

> That is where the next post begins.

A closing sentence may be more polished or emphatic than ordinary body
prose if the article has earned it.

Open endings are characteristic, not mandatory. Do not force uncertainty
when the subject has a clean conclusion.

------------------------------------------------------------------------

## 30. Correct English, Not Artificial Imperfection

Spelling mistakes, missing articles, Dutch word order and accidental
grammatical errors are not style features.

Do not deliberately preserve or introduce errors for authenticity.

Preserve the author's **conceptual rhythm, explanatory choices,
preferred level of explicitness, and willingness to repeat a noun for
clarity** --- not typing mistakes.

------------------------------------------------------------------------

## 31. AI-Native vs. How Rob Would Write

  ------------------------------------------------------------------------------
  AI-native tendency                         How Rob would write
  ------------------------------------------ -----------------------------------
  Announces the surprise                     States the surprising physical fact

  Answers before creating the problem        Lets the reader encounter the
                                             question first

  "Here is where things get interesting"     "A vortex beam is different."

  Stages "Take X. Now do Y."                 States the result, then explains
                                             the cause

  Starts with terminology/classification     Starts with what physically happens

  Compresses A → B → C into one fluent       Separates physically distinct
  sentence                                   claims

  Chops every causal step into a short       Keeps immediate cause and effect
  sentence                                   together when natural

  Switches to expert vocabulary quickly      Keeps the reader's current physical
                                             vocabulary until a new term is
                                             useful

  Avoids repeated nouns for stylistic        Repeats a noun when a pronoun would
  elegance                                   be ambiguous

  Repeats full nouns even when unnecessary   Uses "this" or "it" when the
                                             reference is obvious

  Leaves the complementary case implicit     States both cases when the contrast
                                             carries the physics

  Rebuilds context in every paragraph        Trusts what the reader has just
                                             learned

  Narrates the act of explaining             Moves directly to the explanation
                                             or equation

  Abstract general case first                Uses the simplest concrete case
                                             first when helpful

  Polished three-part climax                 Plain statement of what happened

  Perfectly symmetrical summary              Uneven, conversational synthesis

  Generic rhetorical question                Question only when the argument
                                             creates a real need

  Explains every symbol after an equation    Says what the equation changes
                                             physically

  Adds a rhetorical summary after the        Stops when the explanation is
  explanation                                complete

  "Remarkably/fascinatingly/interestingly"   Lets the fact carry the interest
  cues                                       

  "To see this mathematically..."            Moves directly to the needed
                                             equation

  Historical drama                           Concrete historical fact

  Uniform paragraph endings with punchlines  Uses emphasis selectively,
                                             especially when closing a real
                                             conceptual unit

  Neat final verdict                         Often reopens the deeper question
                                             when one genuinely remains

  Mimics quirks/errors as "voice"            Uses clean English while preserving
                                             reasoning style
  ------------------------------------------------------------------------------

The goal is not to make AI prose rougher. It is to remove the ways AI
tends to **over-design, over-compress, or over-explain** an argument.

------------------------------------------------------------------------

## 32. Section Drafting Workflow

Before writing a section, record:

**Purpose** --- Why does this section exist in the story?

**Reader takeaway** --- What should the reader understand by the end?

**Starting point** --- What does the reader already know?

**Need** --- What question, inconsistency, or missing piece makes this
section necessary?

**Physical/conceptual steps** --- What few steps are needed, and which
of them are genuinely distinct claims?

**Figure or equation** --- What work does it perform?

**Bridge** --- What unresolved point naturally motivates the next
section?

Then draft interactively from Rob's own ideas, phrases and sentences.
Preserve useful wording from his input rather than automatically
replacing it with smoother AI prose.

During drafting, repeatedly ask:

> **Has the reader been given a reason to need the next sentence?**

------------------------------------------------------------------------

## 33. Review Checklist

Review in this order:

1.  **Need before answer** --- Has the text created the problem before
    supplying the solution?
2.  **Physics first** --- Is the physical idea clear before unnecessary
    terminology or classification?
3.  **Causal chain complete** --- Is any conceptual step missing because
    the prose compressed A → C?
4.  **Distinct claims separated** --- Are possibility, existence,
    conversion, observation, and interpretation kept distinct where
    necessary?
5.  **Immediate cause kept together** --- Has a simple causal relation
    been chopped up unnecessarily?
6.  **Result first where natural** --- Are there unnecessary staged
    constructions?
7.  **Referents clear** --- Is every *this*, *it*, *same*, *these*, or
    *this distinction* unambiguous?
8.  **Useful repetition allowed** --- Has clarity been sacrificed merely
    to avoid repeating a noun?
9.  **Context trusted** --- Is established background being needlessly
    repeated?
10. **Vocabulary continuous** --- Has the prose switched to a more
    technical term before it is needed?
11. **No narration of explanation** --- Can "to understand this," "more
    generally," or similar scaffolding simply disappear?
12. **No manufactured suspense** --- Can a sentence announcing interest
    simply be deleted?
13. **Questions earned** --- Would the reader naturally recognize why
    the question matters?
14. **No duplicate explanation** --- Is the same point made twice?
15. **No artificial climax** --- Are rhetorical lists, symmetry, and
    punchlines doing real work?
16. **Minimal notation** --- Does every symbol earn its place?
17. **Equations interpreted physically** --- What did the equation
    actually show?
18. **Natural rhythm** --- Are sentence and paragraph lengths varied?
19. **Closure earned** --- If a paragraph ends emphatically, has the
    preceding argument earned it?
20. **Speak-it test** --- Would this sound natural in discussion with
    another physicist?
21. **Open question where appropriate** --- Does the ending respect what
    remains unresolved?
22. **Detector last** --- Detector scores are diagnostics, not writing
    objectives.

Do not rewrite passages merely because another wording is possible.

> **Prefer the smallest revision that fixes a real problem.**

------------------------------------------------------------------------

## 34. Compact Drafting Instruction

> Write in the Armchair Quantum Physicist style. Write like a physicist
> working through an argument with an interested reader. Let the physics
> provide the surprise and earn each new sentence: create the need for
> an idea before introducing it. Start from what physically or
> conceptually happens rather than from terminology or classification.
> Build the argument in small causal steps and do not compress distinct
> physical claims merely for smoother prose, while keeping an immediate
> cause and consequence together when they naturally form one thought.
> Preserve the reader's current physical vocabulary until a new term or
> symbol becomes useful. Use the shortest unambiguous reference; repeat
> a noun when that improves clarity. Trust context instead of rebuilding
> it in every paragraph. Introduce equations because they are needed and
> explain what they change physically. Use questions when they expose a
> problem the reader is now ready to ask, not as generic transitions.
> Avoid narration of the explaining process, manufactured suspense,
> duplicate explanations, over-engineered summaries and automatic
> rhetorical punchlines. Earned emphasis is allowed, especially at
> genuine conceptual turns and endings. Preserve useful wording from
> Rob's input rather than automatically smoothing it away.

------------------------------------------------------------------------

## 35. Compact Review Instruction

> Review this text for the Armchair Quantum Physicist style while
> preserving its physics and the author's existing voice. First check
> whether the argument creates the need for each important idea before
> supplying it. Look for missing causal steps, compressed distinct
> claims, ambiguous reference words, unnecessary changes of vocabulary,
> repeated background, narration of the explaining process, manufactured
> suspense, duplicate explanation, unearned questions, and overly
> polished summaries. Do not mechanically split cause from immediate
> consequence, eliminate useful repetition, or remove rhetoric that has
> been earned by the argument. Prefer the shortest unambiguous phrasing
> and the smallest revision that fixes a real problem. Treat AI-detector
> output as diagnostic evidence only, never as the writing objective.

------------------------------------------------------------------------

## 36. How This Guide Evolves

This document is empirical.

After each article:

-   retain patterns that repeatedly survive Rob's final editing;
-   distinguish deliberate editorial choices from typos or quick-draft
    habits;
-   add useful **AI-native vs. How Rob would write** examples;
-   test uncertain preferences with controlled A/B/C comparisons when
    useful;
-   do not turn a single preference into a rule too quickly;
-   revise rules when later edits reveal that they were too absolute;
-   remove rules that no longer describe the current prose;
-   do not turn frequently occurring words into mandatory catchphrases;
-   keep physics clarity above stylistic consistency.

The LightBeams work and the later writing experiments suggest that the
most stable fingerprint is not a collection of favourite phrases. It is
a way of reasoning on the page:

> **Create the need. State the physical fact. Make the causal link
> clear. Take one conceptual step at a time. Stop when the explanation
> is complete.**

The guide should become more accurate over time, not merely longer.
