---
layout: archive
title: "CV"
permalink: /cv/
page_class: cv-page
lede: "Senior Principal Researcher & Technical Lead at Huawei Canada, working on LLM post-training and agentic learning. Greater Toronto Area, Canada."
author_profile: true
redirect_from:
  - /resume
---

<div class="cv-actions">
  <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>
  <a href="{{ site.author.googlescholar }}">Google Scholar</a>
  <a href="https://github.com/{{ site.author.github }}">GitHub</a>
  <a href="https://www.linkedin.com/in/{{ site.author.linkedin }}/">LinkedIn</a>
  <button type="button" class="cv-print" onclick="window.print()">Print or save as PDF</button>
</div>

<section class="cv-section prose" markdown="1">
## Summary

<div markdown="1">
Research and technical leader with industrial-scale LLM post-training experience across thousands of Ascend NPUs. I lead a team spanning data, environments, SFT/RL and evaluation, and combine post-training research with distributed-systems engineering, with publications at EMNLP, AACL-IJCNLP, ICSE and ASE.
</div>
</section>

<section class="cv-section prose" markdown="1">
## Experience

<div markdown="1">
<div class="cv-entry" markdown="1">
<div class="cv-entry__head"><h3>Huawei Canada, Centre for Software Excellence</h3><span class="cv-entry__when">Dec 2022 – present</span></div>
<p class="cv-entry__role">Senior Principal Researcher &amp; Technical Lead, May 2026 – present<br>Senior Researcher → Principal Researcher, Dec 2022 – Apr 2026</p>

- **Industrial-scale post-training.** Lead about 20 researchers and engineers across Pangu code-model SFT and RL for 8B–718B models, coordinating data curation, environments, NPU training and agent evaluation.
- **SFT data curation.** Contributed to [MindForge](https://openreview.net/forum?id=QW1ubMMaGA), an automated SFT data pipeline spanning source-free environments, teacher rollouts, build-validity filtering, infrastructure-failure recovery and reasoning repair. Fine-tuning Qwen3.6-27B on 973 curated trajectories raised the ProgramBench average test pass rate from 37.98% to 49.51%, with gains on seven more SE benchmarks.
- **End-to-end agent learning.** Led [RepoForge](https://arxiv.org/abs/2508.01550), integrating repository mining, 7,304 executable environments, teacher trajectories, SFT and RL. Its 8B agent reached 17.4% on SWE-bench Verified, leading the ≤8B non-thinking category at its August 2025 release.
- **Data-centric capability improvement.** Co-authored an industrial study that increased usable teacher supervision 2.84× under the same teacher and attempt budget, improving held-out LiveCodeBench v6 pass@1 by 6.11 points and CodeForces by 2.59 points while keeping AIME/MATH regression suites within tolerance.
- **Cross-scaffold generalization.** Built trajectory collection, filtering and distillation pipelines across Claude Code, OpenCode and OpenHands; co-authored DCAS on planning-aware fine-tuning that improves performance on scaffolds not seen in training.
- **Data quality.** Designed SPICE for issue-clarity, test-coverage and effort labeling, at roughly 19,000× lower cost than estimated manual annotation in a 1,000-instance comparison.
- **Trustworthy evaluation.** Designed SWE-agent evaluations across bug fixing, feature implementation, code editing and architecture; co-authored SWE-Effi and When Elo Lies on resource-bounded performance and Codeforces evaluation bias.
- **Distributed systems and open source.** Led heterogeneous-computing research across Ascend NPUs and NVIDIA GPUs, including Ray on 10,000 NPUs. The team contributed 50+ upstream pull requests to Ray for cluster scalability, stability and performance.
</div>

<div class="cv-entry" markdown="1">
<div class="cv-entry__head"><h3>Huawei Canada</h3><span class="cv-entry__when">Apr 2020 – Dec 2022</span></div>
<p class="cv-entry__role">Research Intern → Senior Researcher</p>

Researched reproducible deep learning, build systems and code clones; published in ICSE, TSE, TOSEM and ICSE-SEIP, including first-author work on training reproducible deep learning models.
</div>

<div class="cv-entry" markdown="1">
<div class="cv-entry__head"><h3>Baidu, Cloud Testing Group</h3><span class="cv-entry__when">Aug – Dec 2017</span></div>
<p class="cv-entry__role">Research Intern</p>

Built a log-based code-coverage estimation prototype evaluated on five industrial projects; published at ASE 2018.
</div>

<div class="cv-entry" markdown="1">
<div class="cv-entry__head"><h3>IBM Canada, Platform Symphony</h3><span class="cv-entry__when">Jan – Aug 2016</span></div>
<p class="cv-entry__role">Research Partner</p>

Built a Hadoop/Python framework to analyze distributed-system logs and detect logging anti-patterns and problematic message sequences.
</div>
</div>
</section>

<section class="cv-section prose" markdown="1">
## Education

<div markdown="1">
<div class="cv-entry" markdown="1">
<div class="cv-entry__head"><h3>York University</h3><span class="cv-entry__when">Sep 2014 – Oct 2020</span></div>
<p class="cv-entry__role">Ph.D. (2020) and M.A.Sc. (2017), Computer Engineering</p>

Advised by [Zhen Ming (Jack) Jiang](https://www.eecs.yorku.ca/~zmjiang/). NSERC Canada Graduate Scholarship – Doctoral (CGS-D).
</div>

<div class="cv-entry" markdown="1">
<div class="cv-entry__head"><h3>University of Science and Technology of China</h3><span class="cv-entry__when">Sep 2010 – Jun 2014</span></div>
<p class="cv-entry__role">B.E., Computer Science</p>
</div>
</div>
</section>

<section class="cv-section prose" markdown="1">
## Talks and service

<div markdown="1">
{% assign talks = site.talks | sort: "date" | reverse %}
{%- for talk in talks %}
- [{{ talk.title }}]({{ talk.url | relative_url }}). {{ talk.venue }}{% if talk.role %}. {{ talk.role }}{% endif %}.
{%- endfor %}
- Program Committee, ASE 2024 (Research Papers).
- Curriculum Committee, AIware Leadership Bootcamp 2024, AIware Bootcamp Mini 2025 and AIware Bootcamp Europe 2025.
- Reviewer, IEEE Transactions on Software Engineering (2021–2025).
</div>
</section>

<section class="cv-section prose" markdown="1">
## Publications

<div markdown="1">
{% assign pubs = site.publications | sort: "date" | reverse %}
{% assign theses = pubs | where_exp: "p", "p.venue contains 'thesis'" %}{{ pubs.size | minus: theses.size }} papers and preprints and {{ theses.size }} theses, listed on the [publications page]({{ '/publications/' | relative_url }}) and [Google Scholar]({{ site.author.googlescholar }}).
</div>
</section>

<section class="cv-section prose" markdown="1">
## Technical focus

<div markdown="1">
- **Training:** SFT; RLVR; multi-turn, execution-feedback RL; teacher-trajectory distillation.
- **Data, evaluation and systems:** data curation and labeling; agent evaluation; Ray; distributed training; heterogeneous NPU/GPU computing.
- **Research interests:** domain adaptation, continual learning, and learning from software execution feedback.
</div>
</section>
