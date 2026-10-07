---
layout: home
permalink: /
title: "Hi, I am Boyuan, an SE / AI Researcher."
author_profile: true
# Home page hero and the photo-filled statement (photo ids from _data/photos.yml)
hero:
  photo: DSC01521
  tagline: "Researcher at Huawei Canada, post-training language models for software engineering."
statement:
  - text: "Researcher,"
    photo: DSC01202
  - text: "Engineer,"
    photo: DSC01171
    position: "40% 45%"
  - text: "Photographer"
    photo: DSC01521
    position: "50% 30%"
---

## About Me

I am a Senior Principal Researcher and Technical Lead at the Centre for Software Excellence, Huawei Canada.

My current research focuses on building **Software Engineering-first LLMs**: post-training (SFT and RL) that teaches language models to work as software engineering agents, together with the data, environments and evaluations behind it. Our team's target is to build the most cost-effective SE models (Sonnet is great, but expensive).

Before that, I led a research team working on heterogeneous computing, building infrastructure for large-scale clusters for FMware (software built on foundation models). Much of our team's work went into [Ray](https://ray.io), the open-source distributed computing framework: we provided native Ascend support for Ray and scaled it to 10,000 NPUs, which we presented at [Ray Summit 2024](/talks/2024-10-02-ray-summit-10k-ascend-npus/). I am also interested in software reproducibility, logging, and AI for software engineering.

I received my Ph.D. from York University, Canada, where I worked on software engineering under the supervision of Prof. [Zhen Ming (Jack) Jiang](https://www.eecs.yorku.ca/~zmjiang/).

## News

**2026-08-31**: New paper, now accepted to the EMNLP 2026 Industry Track! *LLM Post-Training as Brownfield Maintenance* treats industrial post-training as maintaining a deployed checkpoint through budgeted data-mixture patches, and distills what makes that hard. Check it out [here](https://arxiv.org/abs/2608.31102).

**2026-08-06**: New paper, now accepted to the ASE 2026 Industry Showcase! *DCAS* decouples CLI agent scaffolds from the models behind them: a model fine-tuned on planning-aware trajectories collected under Claude Code also improves under OpenCode and mini-swe-agent. Check it out [here](https://arxiv.org/abs/2608.06113).

**2026-07-29**: Introducing MindForge, which teaches small language models whole-life-cycle software engineering through source-free program synthesis. Fine-tuning Qwen3.6-27B on 973 curated trajectories lifts the ProgramBench average test pass rate from 37.98% to 49.51%. The [model](https://huggingface.co/centre-for-swe/MindForge-27B) and [training trajectories](https://huggingface.co/datasets/centre-for-swe/MindForge-27B-Training-Trajectories) are on Hugging Face. Check it out [here](https://arxiv.org/abs/2607.27146).

**2026-06-12**: New paper, now accepted to AACL-IJCNLP 2026! *Beyond Correctness* uses agentic judges to curate architecture-aware training data for code LLMs. Check it out [here](https://arxiv.org/abs/2606.14948).

**2026-04-16**: We presented a technical briefing on Software Engineering for Foundation Models (SE4FM) at ICSE 2026. Details [here](/talks/2026-04-16-icse-se4fm-briefing/).

**2026-02-05**: New paper on hidden biases in Codeforces-based evaluation of LLMs, now accepted to the ASE 2026 Industry Showcase. *When Elo Lies* shows that submission order alone can shift a model's Elo by 394 points. Check it out [here](https://arxiv.org/abs/2602.05891).

**2026-02-03**: New paper, now accepted to EMNLP 2026! *Beyond Tokens* speeds up reasoning models with semantic-aware speculative decoding, verifying whole semantic steps instead of single tokens (up to 2.7× faster on DeepSeek-R1-32B). Check it out [here](https://arxiv.org/abs/2602.03708).

**2025-11-05**: We gave a lightning talk at Ray Summit 2025 on boosting vLLM inference on Huawei NPUs with Ray Compiled Graphs. Watch it [here](/talks/2025-11-05-ray-summit-vllm-npu-compiled-graphs/).

**2025-09-18**: New paper on evaluating SWE agents under resource constraints! We introduce SWE-Effi, new metrics that balance solution accuracy with resource consumption. We found that AI system effectiveness depends on scaffold-model integration, and identified challenges like the "token snowball" effect and "expensive failures" where agents consume excessive resources on unsolvable tasks. Check it out [here](https://arxiv.org/abs/2509.09853).

**2025-08-03**: Introducing RepoForge, an end-to-end pipeline for training SWE agents at scale! RepoForge-8B-Agent achieves 17.4% on SWE-Bench-Verified, establishing new SOTA for ≤8B non-thinking LLMs. We auto-generated 7,304 executable environments from real GitHub commits with zero manual intervention, achieved 14× storage reduction, and >70% faster evaluation. Check it out [here](https://arxiv.org/abs/2508.01550).

**2025-07-12**: New paper on automated dataset labeling for SWE! We present SPICE, a scalable pipeline for labeling SWE-bench-style datasets with annotations for issue clarity, test coverage, and effort estimation. SPICE reduces labeling cost from ~$100,000 (manual) to just $5.10 for 1,000 instances - that's 19,000× cheaper! Check it out [here](https://arxiv.org/abs/2507.09108).

**2025-06-23**: New preprint on CodeLLM model management! We present CACE (Context-Aware CodeLLM Eviction), a novel eviction strategy for self-hosted CodeLLM serving. Unlike traditional LRU-based approaches, CACE leverages context-aware factors including model load time, task-specific latency sensitivity, and future demand prediction. Our experiments show CACE significantly reduces Time-to-First-Token (TTFT) and end-to-end latency while lowering model evictions compared to state-of-the-art systems. Check it out [here](https://arxiv.org/abs/2506.18796).

**2025-03-28**: We released our recent work on performance enhancement for AI-Native Coding. This work focuses on the Service Level Agreement of LLM serving for coding tasks. We present Coding Assistant Task Orchestrator (CATO), the first SLA-aware algorithms for LLM serving that's been internally deployed into Huawei Cloud and on Ascend NPU clusters. CATO intelligently orchestrates CodeLLMs to meet diverse coding tasks' unique latency requirements while maximizing resource utilization. Compared to model-centric serving approaches (e.g., Ray Serve), we have achieved up to 10% higher goodput and 41.1% higher resource utilization. Check it out [here](https://arxiv.org/pdf/2503.19876).

**2024-10-08**: New vision paper on the future of software engineering! We propose "SE 3.0", an AI-native paradigm shift from task-driven copilots to intent-first, conversation-oriented development with AI teammates. This paper outlines a roadmap of challenges to realize truly intelligent AI collaborators that understand software engineering principles and developer intents. Read it [here](https://arxiv.org/abs/2410.06107).


## Selected Publications

- **LLM Post-Training as Brownfield Maintenance: An Industrial Perspective on Dataware Engineering**.\
  Gopi Krishnan Rajbahadur, Amir M. Ebrahimi, <ins>Boyuan Chen</ins>, Ahmed E. Hassan.\
  EMNLP 2026, Industry Track (accepted). [arXiv:2608.31102](https://arxiv.org/abs/2608.31102)

- **Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States**.\
  Ximing Dong, Shaowei Wang, Dayi Lin, <ins>Boyuan Chen</ins>, Ahmed E. Hassan.\
  EMNLP 2026. [arXiv:2602.03708](https://arxiv.org/abs/2602.03708)

- **Beyond Correctness: Enhancing Architectural Reasoning in Code LLMs via Scalable Labeling with Agentic Judgment**.\
  Kirill Vasilevski, Ximing Dong, Benjamin Rombaut, Milad Soltany, Ruochen Deng, Jiahuei Lin, Arthur Leung, Dayi Lin, <ins>Boyuan Chen</ins>, Shaowei Wang, Ahmed E. Hassan.\
  AACL-IJCNLP 2026. [arXiv:2606.14948](https://arxiv.org/abs/2606.14948)

- **MindForge: Teaching Small Language Models Whole-Life-Cycle Software Engineering via Source-Free Program Synthesis**.\
  Yihao Chen, Shi Chang, Khaled Chawa, Feng Lin, <ins>Boyuan Chen</ins>, Shaowei Wang, Ahmed E. Hassan.\
  [arXiv:2607.27146](https://arxiv.org/abs/2607.27146)

- **When Elo Lies: Hidden Biases in Codeforces-Based Evaluation of Large Language Models in Practice**.\
  Shenyu Zheng, Ximing Dong, Xiaoshuang Liu, Gustavo A. Oliva, Chun Yong Chong, Dayi Lin, <ins>Boyuan Chen</ins>, Shaowei Wang, Ahmed E. Hassan.\
  ASE 2026, Industry Showcase. [arXiv:2602.05891](https://arxiv.org/abs/2602.05891)

- **DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds**.\
  Kishanthan Thangarajah, <ins>Boyuan Chen</ins>, Ahmed E. Hassan.\
  ASE 2026, Industry Showcase. [arXiv:2608.06113](https://arxiv.org/abs/2608.06113)

- **RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale**.\
  Zhilong Chen, Chengzong Zhao, <ins>Boyuan Chen</ins>, Dayi Lin, Yihao Chen, Arthur Leung, Gopi Krishnan Rajbahadur, Gustavo A. Oliva, Haoxiang Zhang, Aaditya Bhatia, Chong Chun Yong, Ahmed E. Hassan.\
  [arXiv:2508.01550](https://arxiv.org/abs/2508.01550)

- **SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation**.\
  Gustavo A. Oliva, Gopi Krishnan Rajbahadur, Aaditya Bhatia, Haoxiang Zhang, Yihao Chen, Zhilong Chen, Arthur Leung, Dayi Lin, <ins>Boyuan Chen</ins>, Ahmed E. Hassan.\
  ASE 2025. [Paper](https://doi.org/10.1109/ASE63991.2025.00192)

- **SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints**.\
  Zhiyu Fan, Kirill Vasilevski, Dayi Lin, <ins>Boyuan Chen</ins>, Yihao Chen, Zhiqing Zhong, Jie M. Zhang, Pinjia He, Ahmed E. Hassan.\
  [arXiv:2509.09853](https://arxiv.org/abs/2509.09853)

- **Towards Training Reproducible Deep Learning Models**.\
  <ins>Boyuan Chen</ins>, Mingzhi Wen, Yong Shi, Dayi Lin, Gopi Krishnan Rajbahadur, Zhen Ming (Jack) Jiang.\
  ICSE 2022. [Paper](https://doi.org/10.1145/3510003.3510163)

See all [publications](/publications/), or the full list on [Google Scholar](https://scholar.google.com/citations?hl=en&user=HsUXC7oAAAAJ).
