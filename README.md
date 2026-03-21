# anatomyfyi

[![PyPI version](https://agentgif.com/badge/pypi/anatomyfyi/version.svg)](https://pypi.org/project/anatomyfyi/)
[![Python](https://img.shields.io/pypi/pyversions/anatomyfyi)](https://pypi.org/project/anatomyfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/anatomyfyi/)

Python API client for human anatomy data. Look up 14,692 anatomical structures across 12 body systems, explore organ relationships, trace nerve pathways, and query muscle attachments — all from [AnatomyFYI](https://anatomyfyi.com/), a comprehensive anatomical reference covering systems from the skeletal framework to the nervous system.

Built on the AnatomyFYI database of 14,692 structures with Terminologia Anatomica identifiers, hierarchical parent-child relationships, and cross-system associations used by medical students, anatomists, and health-tech developers worldwide.

> **Explore the interactive anatomy reference at [anatomyfyi.com](https://anatomyfyi.com/)** — browse by [body system](https://anatomyfyi.com/systems/), search structures, and explore organ relationships.

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/anatomyfyi/main/demo.gif" alt="anatomyfyi demo — human anatomy lookup, body systems, and organ relationships in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Body Systems](#body-systems)
  - [Structure Lookup](#structure-lookup)
  - [Organ Relationships](#organ-relationships)
  - [Anatomical Planes and Directions](#anatomical-planes-and-directions)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Anatomy](#learn-more-about-anatomy)
- [Also Available](#also-available)
- [Health FYI Family](#health-fyi-family)
- [License](#license)

## Install

```bash
pip install anatomyfyi                # Core (zero deps)
pip install "anatomyfyi[cli]"         # + Command-line interface
pip install "anatomyfyi[mcp]"         # + MCP server for AI assistants
pip install "anatomyfyi[api]"         # + HTTP client for anatomyfyi.com API
pip install "anatomyfyi[all]"         # Everything
```

## Quick Start

```python
from anatomyfyi.api import AnatomyFYI

with AnatomyFYI() as api:
    # List all body systems (skeletal, muscular, nervous, etc.)
    systems = api.list_systems()
    for system in systems:
        print(f"{system['name']}: {system['structure_count']} structures")

    # Get detailed info on a specific structure
    heart = api.get_structure("heart")
    print(heart["name"])         # Heart
    print(heart["system"])       # Cardiovascular System
    print(heart["latin_name"])   # Cor

    # Search across all anatomical structures
    results = api.search("femoral")
    for r in results:
        print(f"{r['name']} ({r['system']})")
```

## What You Can Do

### Body Systems

The human body is organized into 12 major organ systems, each performing distinct physiological functions. AnatomyFYI catalogs structures within every system, from the 206 bones of the skeletal system to the complex neural networks of the nervous system.

| System | Key Structures | Focus |
|--------|---------------|-------|
| Skeletal | Bones, joints, cartilage | 206 bones, axial vs appendicular |
| Muscular | Skeletal, smooth, cardiac muscle | 600+ muscles, origins & insertions |
| Nervous | Brain, spinal cord, nerves | Central & peripheral nervous system |
| Cardiovascular | Heart, arteries, veins | Blood circulation, cardiac cycle |
| Respiratory | Lungs, bronchi, alveoli | Gas exchange, breathing mechanics |
| Digestive | Stomach, intestines, liver | Nutrient absorption, GI tract |
| Endocrine | Glands, hormones | Pituitary, thyroid, adrenal regulation |
| Lymphatic | Lymph nodes, spleen, thymus | Immune defense, fluid balance |
| Urinary | Kidneys, bladder, ureters | Filtration, waste elimination |
| Reproductive | Gonads, uterus, accessory organs | Male and female systems |
| Integumentary | Skin, hair, nails | Protection, thermoregulation |
| Special Senses | Eyes, ears, nose | Vision, hearing, olfaction |

```python
from anatomyfyi.api import AnatomyFYI

with AnatomyFYI() as api:
    # Browse all body systems
    systems = api.list_systems()
    for s in systems:
        print(f"{s['name']}: {s['structure_count']} structures")

    # Get all structures in the nervous system
    nervous = api.get_system("nervous")
    print(nervous["description"])
```

Learn more: [Body Systems](https://anatomyfyi.com/systems/) · [Glossary](https://anatomyfyi.com/glossary/)

### Structure Lookup

Each of the 14,692 structures in the database includes its Terminologia Anatomica name (the international standard for anatomical nomenclature), Latin equivalent, parent system, and hierarchical position within the body.

```python
from anatomyfyi.api import AnatomyFYI

with AnatomyFYI() as api:
    # Detailed structure lookup with Latin name and hierarchy
    femur = api.get_structure("femur")
    print(femur["name"])         # Femur
    print(femur["latin_name"])   # Os femoris
    print(femur["system"])       # Skeletal System
    print(femur["region"])       # Lower Limb
```

Learn more: [Anatomical Structures](https://anatomyfyi.com/structures/) · [Guides](https://anatomyfyi.com/guides/)

### Organ Relationships

Anatomy is fundamentally about relationships — how structures connect, supply, innervate, and depend on each other. The cardiovascular system supplies every organ, the nervous system innervates every muscle, and the lymphatic system drains every tissue.

```python
from anatomyfyi.api import AnatomyFYI

with AnatomyFYI() as api:
    # Explore relationships of a structure
    heart = api.get_structure("heart")
    print(heart["blood_supply"])   # Coronary arteries
    print(heart["innervation"])    # Cardiac plexus
```

Learn more: [Organ Relationships](https://anatomyfyi.com/guides/) · [Glossary](https://anatomyfyi.com/glossary/)

### Anatomical Planes and Directions

All anatomical descriptions reference the **anatomical position** (standing upright, palms forward) and use three cardinal planes — sagittal (left/right), coronal (front/back), and transverse (upper/lower). Directional terms like anterior/posterior, medial/lateral, and proximal/distal provide unambiguous spatial references.

| Plane | Division | Clinical Use |
|-------|----------|-------------|
| Sagittal | Left / Right | MRI brain scans |
| Coronal | Anterior / Posterior | Chest X-rays |
| Transverse | Superior / Inferior | CT cross-sections |

```python
from anatomyfyi.api import AnatomyFYI

with AnatomyFYI() as api:
    # Search for structures by anatomical region
    results = api.search("anterior")
    for r in results[:5]:
        print(f"{r['name']} — {r['system']}")
```

Learn more: [Anatomical Terminology](https://anatomyfyi.com/glossary/) · [API Documentation](https://anatomyfyi.com/developers/)

## Command-Line Interface

```bash
pip install "anatomyfyi[cli]"

anatomyfyi systems                        # List all body systems
anatomyfyi structure heart                 # Structure details
anatomyfyi search "femoral artery"         # Search structures
anatomyfyi system nervous                  # All nervous system structures
```

## MCP Server (Claude, Cursor, Windsurf)

```bash
pip install "anatomyfyi[mcp]"
```

```json
{
    "mcpServers": {
        "anatomyfyi": {
            "command": "uvx",
            "args": ["--from", "anatomyfyi[mcp]", "python", "-m", "anatomyfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```python
from anatomyfyi.api import AnatomyFYI

with AnatomyFYI() as api:
    systems = api.list_systems()               # GET /api/v1/systems/
    structure = api.get_structure("heart")      # GET /api/v1/structures/heart/
    results = api.search("brachial")           # GET /api/v1/search/?q=brachial
```

### Example

```bash
curl -s "https://anatomyfyi.com/api/v1/structures/heart/"
```

```json
{
    "slug": "heart",
    "name": "Heart",
    "latin_name": "Cor",
    "system": "Cardiovascular System",
    "region": "Thorax"
}
```

Full API documentation at [anatomyfyi.com/developers/](https://anatomyfyi.com/developers/).

## API Reference

| Function | Description |
|----------|-------------|
| `api.list_systems()` | List all 12 body systems |
| `api.get_system(slug)` | System details with structure list |
| `api.list_structures()` | List all 14,692 structures |
| `api.get_structure(slug)` | Structure detail (system, region, Latin name) |
| `api.search(query)` | Search across all structures |

## Learn More About Anatomy

- **Browse**: [Body Systems](https://anatomyfyi.com/systems/) · [Structures](https://anatomyfyi.com/structures/)
- **Guides**: [Anatomy Guides](https://anatomyfyi.com/guides/) · [Glossary](https://anatomyfyi.com/glossary/)
- **API**: [REST API Docs](https://anatomyfyi.com/developers/) · [OpenAPI Spec](https://anatomyfyi.com/api/openapi.json)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install anatomyfyi` | [npm](https://www.npmjs.com/package/anatomyfyi) |
| **MCP** | `uvx --from "anatomyfyi[mcp]" python -m anatomyfyi.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Health FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — human body, medicine, and nutrition.

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| **anatomyfyi** | [PyPI](https://pypi.org/project/anatomyfyi/) | [npm](https://www.npmjs.com/package/anatomyfyi) | **14,692 anatomical structures, body systems, organs — [anatomyfyi.com](https://anatomyfyi.com/)** |
| pillfyi | [PyPI](https://pypi.org/project/pillfyi/) | [npm](https://www.npmjs.com/package/pillfyi) | Pill identification, FDA drug database — [pillfyi.com](https://pillfyi.com/) |
| drugfyi | [PyPI](https://pypi.org/project/drugfyi/) | [npm](https://www.npmjs.com/package/drugfyi) | Drug interactions, pharmacology, side effects — [drugfyi.com](https://drugfyi.com/) |
| nutrifyi | [PyPI](https://pypi.org/project/nutrifyi/) | [npm](https://www.npmjs.com/package/nutrifyi) | Nutrition data, food composition, dietary analysis — [nutrifyi.com](https://nutrifyi.com/) |

## License

MIT
