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

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
