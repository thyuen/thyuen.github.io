---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Dr Tsz Hon Yuen (John Yuen) is an associate professor in the [Department of Software Systems & Cybersecurity](https://www.monash.edu/it/ssc) at [Monash University](https://www.monash.edu/). His research develops practical cryptographic and privacy-enhancing technologies for trustworthy digital systems, with particular interests in public-key cryptography, privacy-preserving protocols, blockchain, and digital finance.


He currently serves as the Associate Director (Technology) of the Fintech Impact Lab of Monash University, and the Deputy Course Director of the Master of Cybersecurity. 

Before joining Monash, Dr Yuen was an Assistant Professor in the [Department of Computer Science](https://www.cs.hku.hk/) at the [University of Hong Kong](https://www.hku.hk/). He was previously a Senior Researcher at the Shield Lab, Huawei Singapore Research Centre, and a member of Huawei's Cryptography Expert Group. He received his PhD from the University of Wollongong in 2010 and subsequently held a postdoctoral position at the University of Hong Kong.

<div class="home">
  <p class="home-actions">
    <a class="home-action" href="{{ '/publications/' | relative_url }}">View publications</a>
    <a class="home-action" href="#opportunities">Research opportunities</a>
  </p>

  <section class="home-section home-section--research" aria-labelledby="research-interest">
    <h2 id="research-interest">Research Interest</h2>
    <p>Dr Yuen's research focuses on:</p>
    <ul>
      <li><strong>Cryptography</strong>: public-key encryption, digital signatures, and zero-knowledge proofs.</li>
      <li><strong>Privacy-enhancing technologies</strong>: anonymous credentials, private set intersection, and privacy-preserving data sharing and computation.</li>
      <li><strong>Blockchain and digital finance</strong>: payment channels, confidential transactions, and security for digital assets.</li>
    </ul>
    <p>His work has appeared in leading venues including CRYPTO, EUROCRYPT, ASIACRYPT, ACM CCS, IEEE Symposium on Security and Privacy, USENIX Security, and IEEE Transactions on Computers. He received the Best Paper Award at ESORICS 2014 and is an inventor on more than ten patents. He has served on programme committees and as a reviewer for leading security and cryptography conferences and journals. He is also a founding member of the Central Bank Digital Currency Expert Group of the Hong Kong Monetary Authority.</p>
    <p>His career-long impact (2025) and single-year impact (2023–2025) are included in the <a href="https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/8">Stanford/Elsevier World’s Top 2% Scientists</a>, a citation-indicator database prepared by the Ioannidis team using Scopus data and published by Elsevier.</p>
  </section>

  {% assign featured_publications = site.publications | sort: "date" | reverse %}

  <section class="home-section home-section--featured" aria-labelledby="featured-publications">
    <h2 id="featured-publications">Featured publications</h2>
    <div class="home-featured-publications">
      {% for publication in featured_publications %}
        {% if publication.permalink == "/publication/2023-05-sp" or publication.permalink == "/publication/2024-08-usenix" or publication.permalink == "/publication/2025-12-asiacrypt" %}
          <article class="home-featured-publication">
            <h3><a href="{{ publication.url | relative_url }}">{{ publication.title }}</a></h3>
            {% if publication.venue %}<p class="home-featured-publication__venue">{{ publication.venue }}</p>{% endif %}
            {% if publication.excerpt and publication.excerpt != "" %}<p>{{ publication.excerpt | escape }}</p>{% endif %}
          </article>
        {% endif %}
      {% endfor %}
    </div>
    <p class="home-section__more">For the complete list, see <a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>
  </section>

  <section class="home-section home-section--opportunities" aria-labelledby="opportunities">
    <h2 id="opportunities">Opportunities</h2>
    <p>I am always interested in working with motivated students and collaborators on cryptography, privacy-enhancing technologies, blockchain security, and digital finance.</p>
    <p>Prospective PhD students, postdoctoral researchers, and research collaborators are welcome to email me with a brief introduction, CV, and a description of relevant research interests.</p>
  </section>

  <section class="home-section home-section--news" aria-labelledby="news">
    <h2 id="news">News</h2>
    <ul class="home-news">
      <li><time class="home-news__date" datetime="2026-09">Sep 2026:</time> <span>Two papers, <em>SuccinCT</em> and <em>HedgeSwap</em>, will appear at ESORICS 2026.</span></li>
      <li><time class="home-news__date" datetime="2026-08">Aug 2026:</time> <span><em>FlowShield</em> will appear at ICDM 2026.</span></li>
      <li><time class="home-news__date" datetime="2026-07">Jul 2026:</time> <span><em>OblivSage</em> will appear at ACISP 2026.</span></li>
      <li><time class="home-news__date" datetime="2026-06">Jun 2026:</time> <span><em>GumSwap</em> will appear at ICDCS 2026.</span></li>
    </ul>
  </section>

  <section class="home-section home-section--contact" aria-labelledby="contact">
    <h2 id="contact">Contact</h2>
    <address class="home-contact">Room 2.25, Alan Finkel Building for Technology and Design, Monash University, Clayton VIC 3168, Australia</address>
    <p class="home-contact">Email: john dot tszhonyuen at monash dot edu</p>
  </section>
</div>
