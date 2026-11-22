# Exact number table (Gate-1 verified)

All values exact rational numbers, M_Pl = H = 1. Mixed graphs:
ψ = (∏ C_e)·I. Scalar graphs: ψ as listed, Ω = 2^(n_e)·ψ.
Full-length fractions for the K4 points are in `numbers.json`.

## Scalar sector

| Graph | x | y | ψ |
|---|---|---|---|
| 2-site | (1,1) | 1 | 1/8 = 0.125 |
| 2-site | (1,1) | 3/5 | 25/128 ≈ 0.1953125 |
| 3-chain | (1,1,1) | (1,1) | 1/54 ≈ 0.0185185 |
| 3-chain | (1,1,2) | (2,3) | 1/900 ≈ 0.0011111 |
| banana (2 scalar edges) | (1,1) | 1 | 1/36 ≈ 0.0277778 |
| 4-chain P4 | (1,1,1,1) | 1 | 29/10368 ≈ 0.0027971 |
| star K1,3 | (1,1,1,1) | 1 | 3/1024 ≈ 0.0029297 |
| C3 | (1,1,1) | 1 | 1/270 ≈ 0.0037037 |
| C3 non-symmetric | (1,2,1) | (1,1,2) | 13/18432 ≈ 0.0007053 |
| C4 | (1,1,1,1) | 1 | 49/90720 ≈ 0.0005401 |
| C5 | (1,…,1) | 1 | 11/136080 ≈ 8.0835×10⁻⁵ |
| K4 | (1,1,1,1) | 1 | 1/30720 ≈ 3.2552×10⁻⁵ |
| 5-site tree | (1,2,1,2,1) | (1,2,1,3) | 16361/1524096000 ≈ 1.0735×10⁻⁵ |

## Mixed scalar/graviton sector

| Point | C (per edge / product) | I | ψ |
|---|---|---|---|
| AF1: 2-site, 1 graviton (y=3/5) | 16/625 | 1175/4096 | 47/6400 = 0.00734375 |
| AG1: 3-chain s(4/5)+h(3/5) | 64/625 | 688766875/14424044544 | 1102027/225375696 ≈ 0.0048897331 |
| AH1 A: 4-chain h-s-h (h: 3/5, s: 4/5) | 64/625 per edge | 758737690796875/34534001699979264 | 48559212211/210778818969600 ≈ 2.3037994×10⁻⁴ |
| AH1 B: 4-chain h-s-h (h: 4/5, s: 3/5) | 81/2500 per edge | 17594375438854421875/866492028129208504608 | 1126040028086683/52826826894022771200 ≈ 2.1315686×10⁻⁵ |
| AH1 one-graviton control (h,s,s), point A energies | 64/625 | 254665515625/22024235778048 | 407464825/344128684032 ≈ 0.0011840478 |
| AM3: banana 3 graviton lines + scalar (y=1) | C_a=C_b=261729/390625, C_c=8281/390625 | 106984911185419164612944232177734375/4880620871952230389627986414051262464 | 87715115175416272578476855360327/420456052020349860668375040000000000 ≈ 2.0861900×10⁻⁴ |
| AR3: banana 5 graviton lines + scalar (y=1) | product 39731381854054663912075472441344/9094947017729282379150390625 | (see numbers.json) | ≈ 0.12915382293763303 (full fraction in numbers.json) |
| AP2: K4, one graviton edge e03 (y=3/5), non-degenerate | 13954816/244140625 | 30530605861331271019334224912109375/33097473646401887218811697580109463552 | 472076440070248645009353519281/8953393797178488362083323661516800 ≈ 5.2725978×10⁻⁵ |
| AQ3: K4 claw+e12 (4 graviton edges, y=3/5), degenerate (common q⃗) | 256/625 per edge; product 4294967296/152587890625 | (see numbers.json) | ≈ 7.280907906583549×10⁻⁴ (full fraction in numbers.json) |
| AU1: K4 claw+e12, NON-degenerate (AT3 point) | e01 256/1875; e02 401408/1171875; e03 97536/390625; e12 5619712/31640625; product 18775163798879731712/9052455425262451171875 | (see numbers.json) | ≈ 3.103144950719409×10⁻⁵ (full fraction in numbers.json) |

Recorded independent numeric reads for AU1 ψ (vs the exact value):
tensor grid n=151: +0.555%; tensor partner n=201: +0.311%;
gap-variable path: −0.000014%. Gate-1 Monte Carlo (6M samples):
all representative integrals within z ≤ 1.21 of the exact values.

## Scalar swaps (graviton kernels replaced by scalar kernels at the
same edge energies; ψ of the resulting all-scalar graph)

| Point | ψ |
|---|---|
| AG1 swap | 625/17472 |
| AH1 A swap | 734375/86704128 |
| AH1 B swap | 4484375/674155872 |
| AP2 swap (e03 → scalar at y=3/5) | 34193925400390625/86339862368481705984 |
| AM3 swap | 15625/22503936 |
| AR3 swap | 1953125/640065355776 |
| AQ3 swap | 391927495390625/2172642315851943936 |

## AT3 rational construction (Wave 25; disproves the AR2
coplanarity obstruction over ℚ)

q⃗ = (3/5, 0, 0); s13 = (8/15, −8/15, −4/15);
s23 = (92/375, 56/75, 56/375); p1 = q⃗ − s13 = (1/15, 8/15, 4/15);
p2 = q⃗ − s23 = (133/375, −56/75, −56/375);
p3 = q⃗ + s13 + s23 = (517/375, 16/75, −44/375).
|s13| = |s23| = 4/5; |q⃗−s13| = 3/5; |q⃗−s23| = 21/25; |p3| = 7/5.
det[p3, −s13, −s23] = 224/3125 ≠ 0; no two of {p3, −s13, −s23}
parallel. s23 forces denominator 375 = 3·5³; none of the Wave-23
search denominators {125, 625, 3125} is a multiple of 375, so that
search space could not contain this point.
