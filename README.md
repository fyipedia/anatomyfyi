# anatomyfyi

Human anatomy and body systems API client — [anatomyfyi.com](https://anatomyfyi.com)

## Install

```bash
pip install anatomyfyi
```

## Quick Start

```python
from anatomyfyi.api import AnatomyFYI

with AnatomyFYI() as api:
    results = api.search("heart")
    print(results)
```

## License

MIT
