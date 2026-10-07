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

{% if site.data.patents %}
<section class="list-section" id="patents">
  <h2 class="list-section__title">Patents <span class="list-section__count">{{ site.data.patents.size }}</span></h2>
  <ol class="pub-list">
    {%- for p in site.data.patents %}
    <li class="pub">
      <p class="pub__venue">{{ p.number }}<span>{{ p.status }}</span></p>
      <h3 class="pub__title"><a href="{{ p.url }}">{{ p.title }}</a></h3>
    </li>
    {%- endfor %}
  </ol>
</section>
{% endif %}
