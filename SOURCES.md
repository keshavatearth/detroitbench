# Source notes

## Opening-act expansion

Chapters 2–13 use the same local English transcript snapshot and the chapter
component templates under `source/src/app/chapters/components/chapter-contents/`.
The source is not distributed. Each executable chapter records source keys,
source paths and adaptation/omission notes. `scripts/audit_campaign.py` checks
that referenced translation keys resolve; it does not certify gameplay parity.

- [Detroit Become Text source snapshot](https://github.com/detroitbecometext/detroitbecometext.github.io/tree/932160cdbed5e5fa13fdc8168b0c6fd09161fe7d)
- [On the Run walkthrough and game flowchart screenshots](https://www.powerpyx.com/detroit-become-human-on-the-run-walkthrough-100/)

The On the Run pursuit and squat-investigation screenshots were inspected for
branch layout and control-flow distinctions on October 30, 2026. The new viewer
renders the authored CLI graph; it does not claim a pixel-identical or complete
copy of the original game's flowchart.

The research presentation was informed by
[Adam Holter's visual analysis portfolio](https://adam.holter.com/portfolio/)
and [interactive model dashboard](https://github.com/adamholter/ai-aggregator):
questions, visible assumptions, inspectable values and usable controls.
No assets, statistics, model rankings or code were copied from them.

## Complete game flowcharts

- [Reddit index: all 100% flowcharts with global stats](https://www.reddit.com/r/DetroitBecomeHuman/comments/99b65j/all_100_flowcharts_with_global_stats_included/)
- [The Hostage flowchart album](https://imgur.com/a/sHOIu4N)

The standalone `hostage-flow.html` viewer was rebuilt after visually inspecting
all three captures in that album. Local copies and exact source URLs are in
`references/hostage-flowchart/`. Its base graph preserves the game's compact
left-to-right branch groups and six ending positions; expanded CLI decisions
are accessible within the checkpoint and group details. Historical player
percentages are replaced by observed model counts. Unrecorded game nodes stay
explicitly unmapped.

Use these captures as structural evidence when converting the transcript into the
story graph. A visible flowchart node is a boundary candidate, but it is not
automatically a model decision:

- player-triggered and optional nodes become CLI actions;
- passive events and dialogue-only story beats are emitted as the result of the
  preceding action;
- conditional and locked nodes become state requirements;
- outcome nodes become recorded transitions or terminal endings.

This distinction is especially useful when the transcript contains several
paragraphs of story but the game offers no new interaction. Keep that material
in the replay without inventing an action for it. Each graph node should retain
the corresponding flowchart label and transcript keys so the split can be
audited later.

The screenshots' global percentages are historical descriptive data, not a
benchmark target or current population baseline. The post notes that values are
rounded down, can shift over time, and may only represent players who reached
and completed the relevant chapter.

## Transcript

- [Detroit Become Text](https://github.com/detroitbecometext/detroitbecometext.github.io)

Use the retained English transcript for exact dialogue and prose. Use the game
flowcharts to validate topology, interaction boundaries, prerequisites, and
outcomes when the transcript presentation is ambiguous.

## The Hostage interaction cadence

- [Recorded playthrough](https://www.youtube.com/watch?v=t3cLDDwLeJA)
- [GameFAQs chapter walkthrough](https://gamefaqs.gamespot.com/ps4/182637-detroit-become-human/faqs/75923/chapter-one-the-hostage)
- [PowerPyx 100% walkthrough](https://www.powerpyx.com/detroit-become-human-the-hostage-opening-walkthrough-100/)

Use these to check the order and number of successive prompts that the static
transcript groups together. The walkthrough sequences also confirm that a
spoken negotiation line is consumed rather than repeated in a later prompt.
