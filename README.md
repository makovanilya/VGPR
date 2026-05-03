# VGPR | Video Game Preservation Rating
**A consumer rights focused classification system for game availability and preservation after official support ends.**

> Aligned with the [Stop Killing Games](https://www.stopkillinggames.com) movement.
> campaign and EU consumer protection advocacy.  
> Spec version: `VGPR v1.0`

What publishers do when ending support for their games may vary vastly, ranging from honoring the purchases to not even letting players keep the game in their digital libraries.
This rating system serves to make that range clear and instantly understood.

## The Scale

| Rating | Meaning                                              |
|--------|------------------------------------------------------|
| p5     | No dead infrastructure dependency, fully playable    |
| p4     | Minor losses, community-sustainable                  |
| p3     | Notable content loss, core experience reachable      |
| p2     | Barely functional, broken without dead servers       |
| p1     | Deliberately destroyed, no recourse for consumer     |
| NR     | EoL not reached or pending review                   |

---

## Modifiers

### Preservation
| Tag   | Meaning                                          |
|-------|--------------------------------------------------|
| OS    | Source code officially released                  |
| SDK   | Full dev/modding toolkit released                |
| SRV   | Dedicated server binaries released               |
| SP    | Sunset patch issued, game made offline-capable  |
| ON    | Online-oriented, online is the core design intent         |
| DRM   | Always-online DRM with no gameplay justification           |
| DLS   | Delisted and cannot be legally acquired by new players       |

---

## Example Ratings

| Game           | Rating | Tags     |
|----------------|--------|----------|
| The Crew       | p1     | ON, DLS  |
| Anthem         | p1     | ON       |
| SimCity (2013) | p1     | DRM, DLS |
| Left 4 Dead 2  | p5     | SDK      |
| Quake          | p5     | OS       |

[→ See all ratings](ratings/)

---

## Using VGPR

Reference a rating in your own writing or project:

`[VGPR: p1, ON, DLS](https://github.com/yourname/game-eol-rating/blob/main/ratings/the-crew.md)`

Shield badges:

[![VGPR: p1](https://img.shields.io/badge/VGPR-p1-critical)](link)
[![VGPR: p5](https://img.shields.io/badge/VGPR-p5-brightgreen)](link)
[![VGPR: NR](https://img.shields.io/badge/VGPR-NR-lightgrey)](link)

---

## Contributing

- Submit a rating → [open an issue](../../issues)
- Dispute a rating → [open a discussion](../../discussions)
- Read the full rules → [CONTRIBUTION.md](CONTRIBUTION.md)

All ratings require sourced evidence. See [CRITERIA.md](CRITERIA.md) for exact definitions.

---

## Documents

| File | Purpose |
|------|---------|
| [CRITERIA.md](CRITERIA.md) | Full falsifiable criteria for every tier and modifier |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to submit and dispute ratings |
| [docs/faq.md](docs/faq.md) | Common questions |
| [CHANGELOG.md](CHANGELOG.md) | Spec version history |

---

## License

[CC0 1.0 Universal](LICENSE) — Public domain. 
Use freely, no attribution required.
