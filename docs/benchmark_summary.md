# Benchmark Summary

This file summarizes the public-safe evidence-preservation and recovery results carried into the Build Week package.

## C40B / C41 / C43

| Lane | Rows | Exact recoveries | Evidence hits | Read |
|---|---:|---:|---:|---|
| SQ67 clean receipt lane | 150 | 150 | 150 | Clean receipt lane preserved all evidence rows. |
| Normal visible lane | 150 | 149 | 114 | Visible answers were often correct, but evidence preservation was weaker. |

Plain English:

```text
The clean lane kept 36 more proof rows on the same kind of work.
```

## Earlier Clean Route

| Run family | Result |
|---|---:|
| Earlier clean SQ67 recovery route | 450 / 450 |
| False controls | 0 / 1300 |

## C31E Blinded Carrier Gate

| Result | Count |
|---|---:|
| Exact expected outputs | 25 / 25 |
| Carrier-lane recoveries | 20 / 20 |
| Neither lanes returned NO_RECOVERY | 5 / 5 |
| False positives on Neither lane | 0 |

## H-Series Sealed Controls

| Gate | Machine/Profile | Result |
|---|---|---|
| H07 | operator-external canary | 3 / 3 hashes matched; zero plaintext hits |
| H08D | Tornado second-machine sealed batch | 3 / 3 hashes matched; zero plaintext hits; zero runner failures |
| H09 | Tornado N10 sealed batch | 10 / 10 hashes matched; zero plaintext hits; fail-closed behavior |

## C57 / C58 Model-Gate Summary

C57 and C58 compare GPT-5.5 and GPT-5.6-sol under the same harness.

### C57 World Bank N50

| Model | Lane | Rows | Full pass | Contract | Avg latency s | Total tokens |
|---|---|---:|---:|---:|---:|---:|
| gpt-5.5 | A | 50 | 50 | 50 | 66.437 | 3,529,758 |
| gpt-5.5 | V | 50 | 50 | 50 | 36.526 | 2,341,622 |
| gpt-5.5 | C | 50 | 50 | 50 | 36.340 | 2,298,169 |
| gpt-5.6-sol | A | 50 | 43 | 44 | 61.970 | 2,894,968 |
| gpt-5.6-sol | V | 50 | 40 | 41 | 29.277 | 1,520,556 |
| gpt-5.6-sol | C | 50 | 44 | 44 | 29.177 | 1,483,215 |

### C58 USGS N50

| Model | Lane | Rows | Full pass | Contract | Avg latency s | Total tokens |
|---|---|---:|---:|---:|---:|---:|
| gpt-5.5 | A | 50 | 0 | 47 | 196.058 | 33,122,337 |
| gpt-5.5 | B | 50 | 0 | 46 | 147.784 | 19,592,477 |
| gpt-5.5 | C | 50 | 50 | 50 | 74.935 | 8,421,682 |
| gpt-5.6-sol | A | 50 | 0 | 17 | 276.905 | 14,318,631 |
| gpt-5.6-sol | B | 50 | 0 | 22 | 251.012 | 16,432,861 |
| gpt-5.6-sol | C | 50 | 38 | 47 | 171.111 | 19,067,794 |

### C58 Failure / Timeout Table

| Model | Rows | Timeouts | Return 124 | Return 1 |
|---|---:|---:|---:|---:|
| gpt-5.5 | 150 | 7 | 7 | 0 |
| gpt-5.6-sol | 150 | 54 | 54 | 11 |

## Public-Safe Claim

The strongest claim is not that every source flatters SQ67 the same way. The stronger claim is narrower and more durable:

```text
RFL built a controlled evidence-preservation harness, verified one source where
the SQ67/5.5 lane held cleanly, then ran a second source that exposed both a
boundary and a much worse 5.6-sol stability profile.
```

