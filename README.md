# &lt;Addon Name&gt;

Short description of the addon.

This repository is a template for small, independent S.T.A.L.K.E.R. Anomaly addons. Replace the placeholders, add the addon files under `gamedata`, and develop the mod without a separate build system.

## Requirements

- S.T.A.L.K.E.R. Anomaly 1.5.3
- [Anomaly Modded Exes](https://github.com/themrdemonized/xray-monolith) when the addon uses DLTX or another engine extension
- Git LFS when the addon contains binary assets tracked by `.gitattributes`

## Installation

Download the ZIP from the latest GitHub Release and extract it directly into the S.T.A.L.K.E.R. Anomaly directory. The archive starts with `gamedata/`; it has no extra wrapper directory.

For a local checkout, run:

```powershell
./tools/install.ps1 -GamePath "D:\Stalker\Anomaly-Test"
```

The installer copies and updates this addon's files. It does not delete the game's existing `gamedata` or files belonging to other addons.

To download and install the latest GitHub Release instead of the local files:

```powershell
./tools/install.ps1 -GamePath "D:\Stalker\Anomaly-Test" -Latest
```

`-Latest` derives the repository from the `origin` remote. Public releases need no token. For a private repository, set `GH_TOKEN` or `GITHUB_TOKEN` to a token that can read the repository. Local installation never uses the GitHub API.

## Development

Create a repository from this template, then clone it:

```powershell
git clone https://github.com/<owner>/<repository>.git
cd <repository>
git lfs install
```

Put only the files shipped by the addon under `gamedata/`. Add standard Anomaly directories such as `textures`, `meshes`, `sounds`, or `shaders` only when the addon needs them. The tracked `.gitkeep` files only preserve the starter directories and are excluded from release ZIPs.

For DLTX, the filename must identify the original root LTX file: `mod_<base-file-name>_sep_<module>.ltx`. For example, a patch to `system.ltx` can be named `mod_system_sep_economy.ltx`. Place it beside the root file it patches. Do not use DLTX syntax unless the addon declares Modded Exes as a requirement.

## Branching

- `master` is stable and releasable.
- `feature/*` is for development and testing.

## Releases

Every push or merge to `master` runs GitHub Actions. The workflow packages `gamedata/`, creates version `v0.0.<run number>`, creates the matching Git tag and GitHub Release with generated notes, and uploads `<repository>-<version>.zip`.

Rerunning the same workflow keeps the same version and replaces the release asset instead of creating a conflicting tag.

## Git LFS

The template tracks common binary game assets (`.dds`, `.ogf`, `.object`, `.ogg`, `.wav`, `.tga`, and `.png`) with Git LFS. Install Git LFS before adding those files and ensure CI has access to the LFS objects. Text files such as LTX, Lua scripts, Markdown, YAML, and PowerShell remain in normal Git history.

## License

No license is selected by this template. Replace `LICENSE` with the license appropriate for your original work before publishing. Do not grant rights to game assets or third-party material you do not own.
