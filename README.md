# How Many Tabs Do You Have Open?

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/e0426685-cloud/u-danu-how-many-tabs-do-you-have-open-d86e783d-entry/rank.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/e0426685-cloud/u-danu-how-many-tabs-do-you-have-open-d86e783d-entry/reward.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entry for the [make.fun](https://make.fun) bounty
["How Many Tabs Do You Have Open?"](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d).

## The entry

One number, digits only: the honest count of open browser tabs.

```
365
```

## How it works

`main.py` (Python standard library only) writes the entry text to
`/output/entry.txt` and verifies it byte for byte: digits only, 1–5
characters, valid UTF-8, world-readable (mode 0644) so the grader can
read it.

The gate checks live in one place, `validate_entry(text)`, which
returns a reason when a candidate fails and `None` when it passes.
The digit test is strict ASCII (`0`–`9` only): `str.isdigit()` would
also accept superscript or non-Latin digits, which are not the plain
digits the gate means. The same function validates the entry before
writing and re-validates what was actually written afterwards.

```sh
python3 main.py
cat /output/entry.txt
```

To check the entry without writing anything:

```sh
python3 main.py --check   # or: python3 main.py --dry-run
```

## License

MIT — see [LICENSE](LICENSE).
