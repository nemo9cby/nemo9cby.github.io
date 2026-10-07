/* chenboyuan.com: navigation state, mobile menu and the photo lightbox. */
(function () {
  'use strict';

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  /* Overlay nav on the home hero turns solid once the hero scrolls away. */
  function initNav() {
    var nav = document.querySelector('[data-nav]');
    if (!nav) return;

    var hero = document.querySelector('[data-hero]');
    if (hero && nav.classList.contains('site-nav--overlay') && 'IntersectionObserver' in window) {
      /* Go solid a little before the hero's last strip slides under the nav,
         so the hero caption never sits behind the links. */
      var observer = new IntersectionObserver(function (entries) {
        nav.classList.toggle('is-solid', !entries[0].isIntersecting);
      }, { rootMargin: '-' + (nav.offsetHeight + 96) + 'px 0px 0px 0px' });
      observer.observe(hero);
    } else if (nav.classList.contains('site-nav--overlay')) {
      nav.classList.add('is-solid');
    }

    var toggle = nav.querySelector('[data-nav-toggle]');
    if (!toggle) return;

    function setOpen(open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
    }

    toggle.addEventListener('click', function () {
      setOpen(!nav.classList.contains('is-open'));
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', function (event) {
      if (nav.classList.contains('is-open') && !nav.contains(event.target)) setOpen(false);
    });
    /* Tabbing past the last link closes the panel so focus is never hidden behind it. */
    nav.addEventListener('focusout', function (event) {
      if (nav.classList.contains('is-open') && event.relatedTarget && !nav.contains(event.relatedTarget)) setOpen(false);
    });
  }

  /* Lightbox for [data-gallery] links. Without JS the links open the image itself. */
  function initLightbox() {
    var links = Array.prototype.slice.call(document.querySelectorAll('[data-gallery] [data-lightbox]'));
    if (!links.length || typeof HTMLDialogElement !== 'function') return;

    var dialog = document.createElement('dialog');
    dialog.className = 'lightbox';
    dialog.setAttribute('aria-label', 'Photograph');
    dialog.innerHTML =
      '<figure class="lightbox__frame">' +
      '<img class="lightbox__img" alt="">' +
      '<figcaption class="lightbox__caption"><strong></strong><span></span></figcaption>' +
      '</figure>' +
      '<button class="lightbox__btn lightbox__btn--prev" type="button" aria-label="Previous photograph">' + icon('m15 5-7 7 7 7') + '</button>' +
      '<button class="lightbox__btn lightbox__btn--next" type="button" aria-label="Next photograph">' + icon('m9 5 7 7-7 7') + '</button>' +
      '<button class="lightbox__btn lightbox__btn--close" type="button" aria-label="Close">' + icon('M6 6l12 12M18 6 6 18') + '</button>';
    document.body.appendChild(dialog);

    var img = dialog.querySelector('.lightbox__img');
    var title = dialog.querySelector('.lightbox__caption strong');
    var details = dialog.querySelector('.lightbox__caption span');
    var prev = dialog.querySelector('.lightbox__btn--prev');
    var next = dialog.querySelector('.lightbox__btn--next');
    var closeButton = dialog.querySelector('.lightbox__btn--close');
    var current = 0;
    var opener = null;

    prev.hidden = next.hidden = links.length < 2;

    function show(index) {
      current = (index + links.length) % links.length;
      var link = links[current];
      var thumb = link.querySelector('img');
      img.src = link.getAttribute('href');
      img.alt = thumb ? thumb.alt : '';
      if (thumb && thumb.style.backgroundColor) img.style.backgroundColor = thumb.style.backgroundColor;
      title.textContent = link.getAttribute('data-caption') || '';
      details.textContent = link.getAttribute('data-details') || '';
    }

    links.forEach(function (link, index) {
      link.addEventListener('click', function (event) {
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.button !== 0) return;
        event.preventDefault();
        opener = link;
        show(index);
        dialog.showModal();
        closeButton.focus();
        document.body.classList.add('has-lightbox');
      });
    });

    prev.addEventListener('click', function () { show(current - 1); });
    next.addEventListener('click', function () { show(current + 1); });
    closeButton.addEventListener('click', function () { dialog.close(); });

    dialog.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowLeft') show(current - 1);
      if (event.key === 'ArrowRight') show(current + 1);
    });
    /* Clicking the dark surround (not the photo or a button) closes it. */
    dialog.addEventListener('click', function (event) {
      if (event.target === dialog || event.target.classList.contains('lightbox__frame')) dialog.close();
    });
    dialog.addEventListener('close', function () {
      document.body.classList.remove('has-lightbox');
      img.removeAttribute('src');
      if (opener) opener.focus();
    });

    var touchX = null;
    dialog.addEventListener('touchstart', function (event) { touchX = event.touches[0].clientX; }, { passive: true });
    dialog.addEventListener('touchend', function (event) {
      if (touchX === null) return;
      var dx = event.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
      touchX = null;
    });
  }

  function icon(path) {
    return '<svg class="icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">' +
      '<path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="' + path + '"/></svg>';
  }

  /* Long news lists show the newest items first; the rest stay one click away. */
  function initNews() {
    var news = document.querySelector('.news .prose');
    if (!news) return;
    var items = news.querySelectorAll('.news-item');
    var visible = 7;
    if (items.length <= visible + 1) return;
    news.classList.add('is-collapsed');
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'news-more';
    button.textContent = 'Show ' + (items.length - visible) + ' earlier items';
    button.addEventListener('click', function () {
      news.classList.remove('is-collapsed');
      button.remove();
      items[visible].setAttribute('tabindex', '-1');
      items[visible].focus();
    });
    news.appendChild(button);
  }

  /* Talk videos: show our own poster; load the YouTube player only on request. */
  function initVideos() {
    Array.prototype.forEach.call(document.querySelectorAll('[data-video]'), function (box) {
      var link = box.querySelector('a');
      if (!link) return;
      link.addEventListener('click', function (event) {
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.button !== 0) return;
        event.preventDefault();
        var frame = document.createElement('iframe');
        frame.src = 'https://www.youtube-nocookie.com/embed/' + box.getAttribute('data-video') + '?autoplay=1';
        frame.title = box.getAttribute('data-video-title') || 'Video';
        frame.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
        frame.referrerPolicy = 'strict-origin-when-cross-origin';
        frame.allowFullscreen = true;
        box.replaceChild(frame, link);
        frame.focus();
      });
    });
  }

  /* Email links carry the address only as base64 parts (data-email="user|domain"). */
  function initEmail() {
    Array.prototype.forEach.call(document.querySelectorAll('[data-email]'), function (link) {
      link.addEventListener('click', function (event) {
        event.preventDefault();
        var parts = link.getAttribute('data-email').split('|').map(function (p) { return window.atob(p); });
        window.location.href = 'mailto:' + parts[0] + '@' + parts[1];
      });
    });
  }

  ready(function () {
    initNav();
    initLightbox();
    initNews();
    initVideos();
    initEmail();
  });
})();
