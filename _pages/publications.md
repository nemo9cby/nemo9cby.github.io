---
layout: archive
title: "Publications"
permalink: /publications/
lede: "Papers and preprints on LLM post-training for software engineering, AI systems, and empirical software engineering. The full, always-current list is on [Google Scholar](https://scholar.google.com/citations?user=HsUXC7oAAAAJ)."
author_profile: true
---

{% assign pubs = site.publications | sort: "date" | reverse %}
{% assign years = pubs | group_by_exp: "pub", "pub.date | date: '%Y'" %}
{% for year in years %}
<section class="list-section">
  <h2 class="list-section__title" id="y{{ year.name }}">{{ year.name }} <span class="list-section__count">{{ year.items.size }}</span></h2>
  <ol class="pub-list">
    {%- for pub in year.items %}
      {% include pub-item.html pub=pub %}
    {%- endfor %}
  </ol>
</section>
{% endfor %}
