---
permalink: /
title: "Hi, I am Boyuan, an SE / AI Researcher."
author_profile: true

---

## 👤 About Me

I am a Principal Researcher at Centre for Software Excellence, Huawei Canada.

My current research interests are building **Software Engineering-first LLMs**. Our team's target is to build the most cost-effective SE models (Sonnet is great, but expensive). 

In the past, I lead a research team working on Heterogeneous Computing. In particualr, we focused on building infrastructure for large scale clusters for FMWare (i.e., Software built on Foundational Models). I am also interested in software reproducibility, logging, and AI4SE.
I received my Ph.D degree in Software Engineering from York University, Canada, under supervision of Prof. [Zhen Ming (Jack) Jiang](http://www.cse.yorku.ca/~zmjiang/).

Many of our team's work is contributed to [Ray](https://ray.io), a popular open source distributed computing framework. For instance, We provided the native Ascend support for Ray. Our talk at Ray Summit 2024 is [here](https://youtu.be/TSAWC-ZZwv4?si=Ht30wHcPAr2h8Aca).

## 🆕 News

**2025-09-18**: New paper on evaluating SWE agents under resource constraints! We introduce SWE-Effi, new metrics that balance solution accuracy with resource consumption. We found that AI system effectiveness depends on scaffold-model integration, and identified challenges like the "token snowball" effect and "expensive failures" where agents consume excessive resources on unsolvable tasks. Check it out [here](https://arxiv.org/abs/2509.09853).

**2025-08-03**: Introducing RepoForge, an end-to-end pipeline for training SWE agents at scale! RepoForge-8B-Agent achieves 17.4% on SWE-Bench-Verified, establishing new SOTA for ≤8B non-thinking LLMs. We auto-generated 7,304 executable environments from real GitHub commits with zero manual intervention, achieved 14× storage reduction, and >70% faster evaluation. Check it out [here](https://arxiv.org/abs/2508.01550).

**2025-07-12**: New paper on automated dataset labeling for SWE! We present SPICE, a scalable pipeline for labeling SWE-bench-style datasets with annotations for issue clarity, test coverage, and effort estimation. SPICE reduces labeling cost from ~$100,000 (manual) to just $5.10 for 1,000 instances - that's 19,000× cheaper! Check it out [here](https://arxiv.org/abs/2507.09108).

**2025-06-23**: New preprint on CodeLLM model management! We present CACE (Context-Aware CodeLLM Eviction), a novel eviction strategy for self-hosted CodeLLM serving. Unlike traditional LRU-based approaches, CACE leverages context-aware factors including model load time, task-specific latency sensitivity, and future demand prediction. Our experiments show CACE significantly reduces Time-to-First-Token (TTFT) and end-to-end latency while lowering model evictions compared to state-of-the-art systems. Check it out [here](https://arxiv.org/abs/2506.18796).

**2025-03-28**: We released our recent work on performance enhancement for AI-Native Coding. This work focuses on the Service Level Agreement of LLM serving for coding tasks. We present Coding Assistant Task Orchestrator (CATO), the first SLA-aware algorithms for LLM serving that's been internally deployed into Huawei Cloud and on Ascend NPU clusters. CATO intelligently orchestrates CodeLLMs to meet diverse coding tasks' unique latency requirements while maximizing resource utilization. Compared to model-centric serving approaches (e.g., Ray Serve), we have achieved up to 41.4% improvement on goodput. Check it out [here](https://arxiv.org/pdf/2503.19876).

**2024-10-08**: New vision paper on the future of software engineering! We propose "SE 3.0", an AI-native paradigm shift from task-driven copilots to intent-first, conversation-oriented development with AI teammates. This paper outlines a roadmap of challenges to realize truly intelligent AI collaborators that understand software engineering principles and developer intents. Read it [here](https://arxiv.org/abs/2410.06107).


## 📚 Selected Publications ([Full List](https://scholar.google.com/citations?hl=en&user=HsUXC7oAAAAJ))

- **SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints**.\
  Zhiyu Fan, Kirill Vasilevski, Dayi Lin, <ins>Boyuan Chen</ins>, Yihao Chen, Zhiqing Zhong, Jie M. Zhang, Pinjia He, Ahmed E. Hassan.\
  [arXiv preprint arXiv:2509.09853](https://arxiv.org/abs/2509.09853)

- **RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale**.\
  Zhilong Chen, Chengzong Zhao, <ins>Boyuan Chen</ins>, Dayi Lin, Yihao Chen, Arthur Leung, Gopi Krishnan Rajbahadur, Gustavo A. Oliva, Haoxiang Zhang, Aaditya Bhatia, Chong Chun Yong, Ahmed E. Hassan.\
  [arXiv preprint arXiv:2508.01550](https://arxiv.org/abs/2508.01550)

- **SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation**.\
  Gustavo A. Oliva, Gopi Krishnan Rajbahadur, Aaditya Bhatia, Haoxiang Zhang, Yihao Chen, Zhilong Chen, Arthur Leung, Dayi Lin, <ins>Boyuan Chen</ins>, Ahmed E. Hassan.\
  [arXiv preprint arXiv:2507.09108](https://arxiv.org/abs/2507.09108)

- **Context-Aware CodeLLM Eviction for AI-assisted Coding**.\
  Kishanthan Thangarajah, <ins>Boyuan Chen</ins>, Shi Chang, Ahmed E. Hassan.\
  [arXiv preprint arXiv:2506.18796](https://arxiv.org/abs/2506.18796)

- **SLA-Awareness for AI-assisted coding**.\
  Kishanthan Thangarajah, Arthur Leung, <ins>Boyuan Chen</ins>, Ahmed E. Hassan.\
  [arXiv preprint arXiv:2503.19876](https://arxiv.org/pdf/2503.19876)

- **Towards AI-Native Software Engineering (SE 3.0): A Vision and a Challenge Roadmap**.\
  Ahmed E. Hassan, Gustavo A. Oliva, Dayi Lin, <ins>Boyuan Chen</ins>, Zhen Ming (Jack) Jiang.\
  [arXiv preprint arXiv:2410.06107](https://arxiv.org/abs/2410.06107)

- **Rethinking Software Engineering in the Era of Foundation Models: A Curated Catalogue of Challenges in the Development of Trustworthy FMware**.\
  Ahmed E. Hassan, Dayi Lin, Gopi Krishnan Rajbahadur, Keheliya Gallaba, Filipe Roseiro Cogo, <ins>Boyuan Chen</ins>, Haoxiang Zhang, Kishanthan Thangarajah, Gustavo Oliva, Jiahuei (Justina) Lin, Wali Mohammad Abdullah, and Zhen Ming (Jack) Jiang.\
  International Conference on the Foundations of Software Engineering (**FSE 2024**).
- **Rethinking Software Engineering in the Foundation Model Era: From Task-Driven AI Copilots to Goal-Driven AI Pair Programmers**.\
  Ahmed E Hassan, Gustavo A Oliva, Dayi Lin, <ins>Boyuan Chen</ins>, Zhen Ming (Jack) Jiang\
  [arXiv preprint arXiv:2404.10225](https://arxiv.org/pdf/2404.10225)
- **Towards training reproducible deep learning models**.\
  <ins>Boyuan Chen</ins>, Mingzhi Wen, Yong Shi, Dayi Lin, Gopi Krishnan Rajbahadur, Zhen Ming (Jack) Jiang\
  International Conference on Software Engineering (**ICSE 2022**)







