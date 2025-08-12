# Installation

## Requirements

- Python 3.8 or higher
- pip package manager

## Installation Methods

### From GitHub

```bash
pip install git+https://github.com/prakashgbid/osa-deep-reasoner.git
```

### From Source

```bash
git clone https://github.com/prakashgbid/osa-deep-reasoner.git
cd osa-deep-reasoner
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/prakashgbid/osa-deep-reasoner.git
cd osa-deep-reasoner
pip install -e ".[dev]"
```

## Verify Installation

```python
import deep_reasoner
print(deep_reasoner.__version__)
```
