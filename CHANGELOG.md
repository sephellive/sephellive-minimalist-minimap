# Changelog

## 1.0.6 — 2026-09-13

- Added a supersampled hairline edge overlay to conceal the engine's remaining polygon corners.
- The overlay is limited to the final few pixels and does not create the broad border used in 1.0.4.

## 1.0.5 — 2026-09-13

- Removed the over-map dark mask and its visible border entirely.
- Enabled Modded Exes' native minimap geometry fix with `ratio_mode="1"` on both layouts.

## 1.0.4 — 2026-09-13

- Moved the smoothing mask from the background layer to the compass layer, which Anomaly renders above the map.
- The over-map alpha annulus now conceals the engine's visibly faceted circular clipping edge.

## 1.0.3 — 2026-09-13

- Replaced the faint vignette with a compensated soft alpha mask that hides Anomaly's polygonal `rounded` clip edge.
- Keeps a light edge shade while presenting a visually smooth circular map.

## 1.0.2 — 2026-09-13

- Removed the rigid decorative circle which did not align with Anomaly's map clipping.
- Reduced the inner vignette to a very light, line-free edge shade.
- Reduced and softened the player arrow.

## 1.0.1 — 2026-09-13

- Restored Anomaly's required `static_counter` node in both supported minimap layouts.

## 1.0.0 — 2026-09-13

- First standalone release.
- Clean circular minimap presentation with an anti-aliased rim and a restrained inner vignette.
- Original direction labels: orange `N`, neutral `E`/`S`/`W`; no coloured north sector or glow.
- Original player arrow and no external addon runtime dependency.
