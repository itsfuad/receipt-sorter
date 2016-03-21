# receipt-sorter

Calculate per-merchant spending from exported expense rows.

Small, dependency-light Python 3 standard library utility. Original implementation and history generated for a retrospective development exercise.

## Quick start

```sh
python3 cli.py examples/input.txt --pretty
python3 -m unittest discover -p 'test*.py'
```

Pass `-` to read standard input, `--pick KEY` for one field, and `--out PATH` to save JSON.
