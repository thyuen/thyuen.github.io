---
title: "zkMatrix: Batched Short Proof for Committed Matrix Multiplication"
collection: talks
type: "Invited Talk"
permalink: /talks/2024-acisp
venue: "The 29th Australasian Conference on Information Security and Privacy (ACISP 2024)"
date: 2024-07-16
location: "Sydney, Australia"
---

Matrix multiplication is a common operation in applications like machine learning and data analytics. To demonstrate the correctness of such an operation in a privacy-preserving manner, we propose zkMatrix, a zero-knowledge proof for the multiplication of committed matrices. Among the succinct non-interactive zero-knowledge protocols that have an O(log n) transcript size and O(log n) verifier time, zkMatrix stands out as the first to achieve O(n^2) prover time and O(n^2) RAM usage for multiplying two n×n matrices. Significantly, zkMatrix distinguishes itself as the first zk-SNARK protocol specifically designed for matrix multiplication. By batching multiple proofs together, each additional matrix multiplication only necessitates O(n) group operations in prover time.

[More information here](https://www.acisp24.com/copy-of-program-schedule)
