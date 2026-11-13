---
name: svg-diagramming
description: Create, edit, validate, and optimize accessible SVG diagrams and vector illustrations. Use for flowcharts, architecture diagrams, process maps, technical illustrations, icons, and SVG repair.
---

# SVG Diagramming

## Goal
Create maintainable, legible, accessible SVG graphics that communicate structure and relationships. Prefer native SVG, semantic grouping, reusable definitions, deterministic geometry, and standards-based features.

## Use this skill for
- Architecture, flow, sequence, state, and process diagrams.
- Technical illustrations, schematics, vector infographics, and maps.
- SVG icons, symbol sets, and reusable vector components.
- Repairing, reviewing, sanitizing, or optimizing SVG.
- Turning structured information into vector diagrams.

## Workflow
1. Understand the message: identify audience, key takeaway, diagram type, intended size, renderer, and editability needs. State assumptions when details are missing.
2. Choose a diagram grammar: directional lanes for sequences, grouped boundaries for architecture, explicit transitions for state diagrams, and aligned columns for comparisons.
3. Plan layout: establish reading direction, grid, spacing scale, hierarchy, margins, and connector routing before styling.
4. Construct semantic SVG: use `viewBox`, descriptive IDs, `<g>` for logical groups, `<defs>` for reusable definitions, and `<marker>` for arrowheads. Add `<title>` and `<desc>` for informative graphics.
5. Apply visual rules: consistent typography, restrained semantic colors, sufficient contrast, and more than color alone to communicate status or relationship.
6. Validate with `python scripts/validate_svg.py path/to/diagram.svg`. Fix malformed XML, duplicate IDs, unresolved local references, and missing metadata.
7. Review in a browser at intended display sizes. Inspect clipping, connector routing, scaling, focus states, and dark/light backgrounds where relevant.
8. Optimize conservatively. Reuse repeated shapes and remove unnecessary metadata only when safe.
9. Deliver the SVG source, dimensions, assumptions, validation results, and known renderer limitations.

## Diagram patterns
- Flowchart: consistent node shapes, labeled decision branches, directional connectors.
- Architecture: group by system boundary, responsibility, and trust zone.
- Sequence: time flows in one direction, lifelines are aligned, messages are labeled.
- State machine: distinct states, labeled transitions, explicit start and end.
- Concept map: relationship labels explain why nodes are connected.

## Engineering requirements
- Use `viewBox` for scalable coordinates.
- Prefer readable text over converting text to paths.
- Keep IDs unique and stable.
- Keep connectors behind nodes and away from labels.
- Ensure arrowheads and line styles have consistent meaning.
- Test at realistic output sizes.

## Accessibility
- Give informative standalone SVG `role="img"` and an accessible name.
- Associate title and description using `aria-labelledby`.
- Do not rely on color alone.
- Keep labels readable and high-contrast.
- Interactive elements must be keyboard accessible with visible focus.
- Hide decorative SVG from assistive technology where appropriate.

## Security
- Treat imported SVG as untrusted XML.
- Do not execute embedded scripts or event handlers.
- Avoid remote assets and external entities unless explicitly required.
- Escape untrusted text with an XML library before inserting it.
- A successful XML parse is not proof that an SVG is safe.

## Completion checklist
- Main idea is immediately apparent.
- Reading order and relationships are unambiguous.
- Labels do not overlap or clip.
- IDs are unique and local references resolve.
- XML is well formed.
- Accessibility metadata is present where appropriate.
- No unexpected external dependencies exist.
- The diagram renders in a standard browser.

## Supporting files
- `resources/svg-patterns.md`
- `resources/accessibility-checklist.md`
- `resources/visual-review-checklist.md`
- `scripts/validate_svg.py`
- `scripts/optimize_svg.py`

## Response format
Summarize the diagram purpose, provide the SVG, state assumptions and dimensions, report validation checks, and disclose anything not tested.
