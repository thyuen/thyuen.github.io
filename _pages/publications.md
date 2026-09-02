---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
<p>
  A complete citation record is also available on
  <a href="{{ author.googlescholar }}" target="_blank" rel="noopener noreferrer">Google Scholar</a>.
</p>
{% endif %}

{% include base_path %}

<nav class="pub-year-nav" aria-label="Publication years">
  Browse by year:
  <a href="#2026">2026</a>
  <a href="#2025">2025</a>
  <a href="#2024">2024</a>
  <a href="#2023">2023</a>
  <a href="#earlier-work">Earlier work</a>
</nav>

{% assign recent_years = "2026,2025,2024,2023" | split: "," %}

{% for year in recent_years %}
  <h2 id="{{ year }}">{{ year }}</h2>

  {% for post in site.publications reversed %}
    {% capture post_year %}{{ post.date | date: "%Y" }}{% endcapture %}

    {% if post_year == year %}
      {% include archive-single.html %}
    {% endif %}
  {% endfor %}
{% endfor %}

<details class="pub-archive" id="earlier-work">
  <summary>Earlier work (2022–2012)</summary>

  {% assign previous_year = "" %}

  {% for post in site.publications reversed %}
    {% capture post_year %}{{ post.date | date: "%Y" }}{% endcapture %}

    {% unless recent_years contains post_year %}
      {% if post_year != previous_year %}
        <h3 id="year-{{ post_year }}">{{ post_year }}</h3>
        {% assign previous_year = post_year %}
      {% endif %}

      {% include archive-single.html %}
    {% endunless %}
  {% endfor %}
</details>
