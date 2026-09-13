# Sephellive Minimalist Minimap

A compact circular minimap for S.T.A.L.K.E.R. Anomaly and GAMMA. It preserves a
directional player arrow and a coloured `N`, removes the bright north sector,
and adds a smooth circular rim with a restrained inner vignette.

This is a standalone addon. It contains neither third-party scripts nor textures
and does not require SquareDOV, Modular Compass & Minimap Extension, or another
minimap addon to supply its files.

## Requirements

- S.T.A.L.K.E.R. Anomaly 1.5.3 / GAMMA.
- A 16:9 or 21:9 display profile.

The addon replaces `zone_map_16.xml` and `zone_map_21.xml`; do not enable it
alongside another mod that changes the same minimap layouts.

## Installation

Download the ZIP from the latest GitHub Release and install it in MO2 as a normal
mod. Put it below other minimap/HUD mods that replace `zone_map_16.xml` or
`zone_map_21.xml`. The archive starts with `gamedata/`; it has no extra wrapper
directory.

No FOMOD is included deliberately: this addon has one coherent visual preset and
no install-time choices. A FOMOD would add an unnecessary step without providing
any benefit.

## Releases

Every push to `master` runs GitHub Actions. The workflow packages `gamedata/`,
reads the version from `VERSION`, and creates or updates the matching GitHub
Release.

## Credits and rights

**Implementation, clean-room UI textures, configuration, and packaging:**
Sephellive.

The addon was conceived after using these projects:

- SquareDOV — Blackgrowl, RavenAscendant, Tronex, Strogglet15 and contributors.
- Modular Compass & Minimap Extension — lifestorock.
- Raven800's Compass Overlay — Raven800.

Their work remains the property of its respective authors. This addon does not
include, extract, modify, or redistribute their code, scripts, or textures.
SquareDOV's terms expressly restrict redistribution of its textures; that is why
this release uses newly created, independent UI assets instead of repackaging
those files. S.T.A.L.K.E.R. and S.T.A.L.K.E.R. Anomaly belong to their respective
rightsholders.

## License

The original files in this repository are available under the MIT License. No
rights are granted for S.T.A.L.K.E.R., S.T.A.L.K.E.R. Anomaly, or third-party
projects named above.
