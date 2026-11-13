# claude-svg-diagramming-skill

A Claude Code skill for creating, editing, validating, and optimizing accessible SVG diagrams and vector illustrations.

## Overview

This skill helps turn structured information into clear, maintainable vector graphics. It covers diagram planning, semantic SVG construction, layout, visual consistency, accessibility, SVG security, validation, and conservative optimization.

## Use Cases

- Architecture, flow, sequence, state, and process diagrams.
- Technical illustrations, schematics, maps, and vector infographics.
- SVG icons, symbol sets, and reusable vector components.
- Repairing, reviewing, sanitizing, and optimizing SVG files.

## Installation

```bash
git clone https://github.com/Brajesh31/claude-svg-diagramming-skill.git ~/.claude/skills/svg-diagramming
```

## Workflow

1. Define the audience, takeaway, diagram type, target dimensions, renderer, and editability needs.
2. Select a suitable diagram grammar and plan the reading direction, grid, spacing, and connector routing.
3. Construct semantic SVG using `viewBox`, logical `<g>` groups, reusable `<defs>`, and appropriate markers.
4. Add titles and descriptions for informative graphics.
5. Apply consistent typography, contrast, and visual semantics.
6. Validate the SVG and review it at realistic display sizes.
7. Optimize conservatively and disclose renderer limitations.

## Validation

Run the included validator:

```bash
python scripts/validate_svg.py path/to/diagram.svg
```

The validator checks structural issues such as malformed XML, duplicate IDs, unresolved local references, and missing metadata. A successful parse does not prove that an SVG is safe.

## Supporting Resources

| Path | Purpose |
|---|---|
| `resources/svg-patterns.md` | Reusable SVG diagram and illustration patterns |
| `resources/accessibility-checklist.md` | Accessibility requirements for SVG graphics |
| `resources/visual-review-checklist.md` | Visual and layout review criteria |
| `scripts/validate_svg.py` | SVG structure validation |
| `scripts/optimize_svg.py` | SVG optimization |

## Security

Treat imported SVG as untrusted XML. Do not execute embedded scripts or event handlers. Avoid external entities and unexpected remote assets. Escape untrusted text with an XML library before inserting it.

## Creator and maintainer

Created and maintained by **Brajesh Kumar**.
