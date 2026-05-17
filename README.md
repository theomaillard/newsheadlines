# newsheadlines

Python package to fetch the latest news headlines from major news outlets by parsing their webpages.

> ℹ️ Every response is cached for 10 minutes before a new request is made.

## Installation

The latest version can be installed via pip:

```shell
pip install newsheadlines
```

## Documentation

### `class Headline`

A dataclass representing a single news headline.

| Field    | Type          | Description                            |
| -------- | ------------- | -------------------------------------- |
| `title`  | `str`         | The headline text                      |
| `source` | `str`         | Source identifier (e.g. `"bbc"`)       |
| `url`    | `str \| None` | Link to the full article, if available |

### `newsheadlines.all(source_name)`

Returns a list of all `Headline` objects from the given source.

#### **Parameters**

- `source_name (str)` - one of the supported source keys (case-insensitive)

#### **Returns**

- `list[Headline]`

#### **Example**

```python
import newsheadlines

headlines = newsheadlines.all("bbc")

for h in headlines:
    print(h.title)
    print(h.url)
    print(h.source)
```

### `newsheadlines.main(source_name)`

Returns only the top/main Headline from the given source.

#### **Parameters**

- `source_name (str)` - one of the supported source keys (case-insensitive)

#### **Returns**

- `Headline`

#### **Example**

```python
import newsheadlines

headline = newsheadlines.main("bbc")

print(headline.title)
print(headline.url)
print(headline.source)
```

## Available sources

| Key             | Source             |
|:---------------:|:------------------:|
| `"apnews"`      | AP News            |
| `"bbc"`         | BBC News           |
| `"cnn"`         | CNN                |
| `"nyt"`         | The New York Times |
| `"theguardian"` | The Guardian       |