# SVG construction patterns

## Responsive root

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 1200 800"
     role="img"
     aria-labelledby="diagram-title diagram-description">
  <title id="diagram-title">Service architecture</title>
  <desc id="diagram-description">A browser client sends requests to an API that reads from a database.</desc>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10"
            refX="8" refY="5" orient="auto">
      <path d="M0 0 L10 5 L0 10 Z" fill="#334155"/>
    </marker>
  </defs>
</svg>
```

## Node

```xml
<g id="api-service">
  <rect x="420" y="240" width="220" height="100" rx="12"
        fill="#ffffff" stroke="#334155" stroke-width="2"/>
  <text x="530" y="295" text-anchor="middle"
        font-family="system-ui, sans-serif" font-size="20">API service</text>
</g>
```

## Connector

```xml
<path d="M250 290 H400" fill="none" stroke="#475569"
      stroke-width="2.5" marker-end="url(#arrow)"/>
```

## Layout guidance
- Decide reading direction first.
- Use a consistent gap between sibling nodes.
- Put connectors behind nodes.
- Keep long explanations outside dense nodes.
- Give major groups enough padding to read as boundaries.
- Use orthogonal routing for complex technical diagrams.
- Use a legend only when shape or line meaning is not self-evident.

## Safe text insertion
Use an XML library or XML escaping utilities for untrusted text. Never concatenate raw user content into SVG markup.
