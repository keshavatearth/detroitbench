# Source notes

## Complete game flowcharts

- [Reddit index: all 100% flowcharts with global stats](https://www.reddit.com/r/DetroitBecomeHuman/comments/99b65j/all_100_flowcharts_with_global_stats_included/)
- [The Hostage flowchart album](https://imgur.com/a/sHOIu4N)

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
