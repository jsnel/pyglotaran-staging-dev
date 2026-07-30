# Compression pass

A reusable prompt for cutting length from a finished draft without losing content.

Use it as the **last** pass, after correctness and style reviews. Correctness reviews only add
text; this one only removes it. Run it as its own session with a fresh context — an agent that
wrote the draft will defend its own sentences.

---

## Parameters

Set these before running. Everything in `{{...}}` is substituted.

| Parameter | Meaning | Example |
|---|---|---|
| `{{TARGET_FILE}}` | The document to compress. Edited in place. | `docs/pyglotaran-architecture-chapter-draft.md` |
| `{{WORD_CEILING}}` | Hard maximum, excluding references. | `7500` |
| `{{REDUCTION_TARGET}}` | Minimum cut, as a fraction of the starting count. | `25%` |
| `{{CONTRACT_FILE}}` | Optional. Terminology or style rules that survive the cut. | `docs/architecture-chapter-work/00-editorial-contract.md` |
| `{{PROTECTED}}` | Optional. Content classes that must not be touched. | equations, figures, APA citations |

---

## The prompt

> You are compressing a finished draft. Your only job is to remove text. You are not reviewing
> it for correctness, and you are not improving it.
>
> **Target:** `{{TARGET_FILE}}`
> **Hard ceiling:** `{{WORD_CEILING}}` words, references excluded.
> **Minimum reduction:** `{{REDUCTION_TARGET}}` of the starting word count.
> **Binding rules that survive the cut:** `{{CONTRACT_FILE}}`
>
> ### Rules
>
> 1. You may delete. You may not add. The only permitted additions are the minimum words needed
>    to repair grammar where a deletion broke a sentence — typically a conjunction or a pronoun.
> 2. Every fact, number, equation, citation, source anchor, and terminological distinction in the
>    input must still be present in the output. Losing one is a failure, not a trade-off.
> 3. Do not rewrite a paragraph to say the same thing more briefly unless the rewrite is strictly
>    a deletion. Rewriting reintroduces the register you are removing.
> 4. Never introduce terminology forbidden by the binding rules. A deleted caveat must not be
>    replaced by the term it was warning against.
> 5. Protected, do not touch: `{{PROTECTED}}`.
>
> ### Delete on sight
>
> **Sentences with no content.** A sentence must carry a fact, an equation, a distinction, a
> citation, or a necessary transition. If it carries none, it goes.
>
> **Statements of what the document is not doing.** "No claim is made here about future
> interfaces." "The diagram does not assert a unique mechanism." "This is not a tutorial." Scope
> belongs in one place, stated once, near the top.
>
> **Negative definitions used as prose.** "X is not Y", "X rather than Y", "It must not be
> confused with Y" — where the distinction is already in a glossary or was already made. Keep the
> first occurrence of each distinction. Delete every later restatement.
>
> **Hedges on verified claims.** `may`, `can`, `might`, `is arguably`, `to some extent`,
> `does not by itself`, `primarily`, `in practice` — where the underlying claim is verified.
> Delete the hedge, keep the claim. Leave hedges where the evidence is genuinely uncertain; those
> are doing work.
>
> **Structural duplication.** Synopses that preview what later sections say. Section openers that
> restate the previous section's close. Conclusions that recap rather than conclude. Roadmap
> paragraphs longer than three sentences. Keep the first full statement of an idea, delete the
> echoes, regardless of which one reads better.
>
> **Double explanation.** Where a plain-language paragraph and a formal paragraph say the same
> thing, keep whichever the reader needs and delete the other. Do not keep both because the brief
> asked for plain language first.
>
> **Throat-clearing.** "It is important to note that", "It is worth emphasizing", "As we shall
> see", "Having established X, we now turn to Y." Cut to the content.
>
> **Discourse-marker inflation.** `therefore`, `thus`, `consequently`, `hence`, `moreover`,
> `furthermore` where the logical relation is already obvious from the order of sentences.
>
> ### Keep
>
> Anything load-bearing: claims, evidence, equations, worked examples, the first statement of each
> definition, qualifications that reflect real uncertainty, and transitions that a reader would
> stumble without. When a cut is genuinely borderline, keep the text and note it in the report
> rather than guessing.
>
> ### Procedure
>
> 1. Record the starting word count, excluding references.
> 2. Build an inventory of load-bearing content: every distinct claim, equation, citation, and
>    definition, with its location. This is your loss checklist.
> 3. **Structural pass.** Remove whole duplicated blocks — synopsis, recap openers, conclusion
>    restatement, repeated definitions. This is where most of the words are.
> 4. **Sentence pass.** Work through the remainder against the delete-on-sight list.
> 5. **Verify.** Check every item on the inventory against the compressed text. Restore anything
>    lost. Confirm no forbidden terminology entered.
> 6. Record the final word count. If it is above the ceiling, repeat step 4 on the longest
>    sections. If it is below the ceiling but the reduction is under target, say so rather than
>    cutting load-bearing text to hit a number.
>
> ### Report
>
> Return, and nothing else:
>
> - word count before and after, and the percentage cut;
> - the three largest structural deletions, one line each;
> - counts for the main deleted categories (empty sentences, negative definitions, hedges,
>   duplicated explanation);
> - anything you kept that you believe should go, and why you left it;
> - confirmation that the loss checklist is complete, or a list of what could not be preserved.

---

## Optional: calibrate against an exemplar

If the draft has a target register, measure it rather than describing it. Before step 3, add:

> Take three consecutive paragraphs from `{{EXEMPLAR}}`. Record median sentence length, hedges per
> hundred words, and median paragraph length. Report the same three numbers for the draft before
> and after. Do not imitate the exemplar's phrasing; match its density.

## Notes

- Run this on a copy or a clean working tree, so the diff is reviewable and revertible.
- A cut of 20–35% is normal for a draft written to a word target. Much more than that usually
  means the draft has a scope problem the compression pass cannot fix.
- If a fan-out of writing agents produced the draft, expect most of the reduction to come from
  the structural pass, not the sentence pass. Sibling sections re-establish shared context.
