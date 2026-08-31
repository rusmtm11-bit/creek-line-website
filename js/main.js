// Creek Line Limited — site behaviour
// Mobile navigation, active link state, scroll-reveal, counters,
// process timeline progress and form handling.

document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Mobile navigation ---------- */
  const burger = document.querySelector('.burger');
  const navLinks = document.querySelector('.nav-links');

  if (burger && navLinks) {
    burger.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('active');
      burger.classList.toggle('open', isOpen);
      burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  document.querySelectorAll('.has-dropdown > a').forEach((link) => {
    link.addEventListener('click', (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  document.querySelectorAll('.nav-links a:not(.has-dropdown > a)').forEach((link) => {
    link.addEventListener('click', () => {
      navLinks && navLinks.classList.remove('active');
      burger && burger.classList.remove('open');
    });
  });

  /* ---------- Active nav link ---------- */
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a[href]').forEach((link) => {
    const href = link.getAttribute('href');
    if (href === currentPath) {
      link.classList.add('active');
    }
  });

  /* ---------- Scroll reveal ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach((el, i) => {
      if (el.closest('.stagger')) {
        el.style.setProperty('--i', i % 8);
      }
      observer.observe(el);
    });
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }

  /* ---------- Animated counters ---------- */
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    const runCount = (el) => {
      const target = parseFloat(el.getAttribute('data-count'));
      const suffix = el.getAttribute('data-suffix') || '';
      const duration = 1400;
      const start = performance.now();
      const step = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const value = Math.round(target * eased);
        el.textContent = value + suffix;
        if (progress < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };

    if ('IntersectionObserver' in window) {
      const countObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            runCount(entry.target);
            countObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      counters.forEach((el) => countObserver.observe(el));
    } else {
      counters.forEach(runCount);
    }
  }

  /* ---------- Process timeline progress ---------- */
  const timeline = document.querySelector('.timeline');
  if (timeline) {
    const steps = timeline.querySelectorAll('.timeline-step');
    const updateProgress = () => {
      const rect = timeline.getBoundingClientRect();
      const viewportH = window.innerHeight;
      const total = rect.height;
      const visible = Math.min(Math.max(viewportH * 0.6 - rect.top, 0), total);
      const pct = total > 0 ? (visible / total) * 100 : 0;
      timeline.style.setProperty('--progress', pct + '%');

      steps.forEach((step) => {
        const stepRect = step.getBoundingClientRect();
        if (stepRect.top < viewportH * 0.6) {
          step.classList.add('active');
        }
      });
    };
    updateProgress();
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => { updateProgress(); ticking = false; });
        ticking = true;
      }
    });
    window.addEventListener('resize', updateProgress);
  }

  /* ---------- Contact / quote forms: consent + fallback UX ---------- */
  document.querySelectorAll('form[data-form]').forEach((form) => {
    const consentCheckbox = form.querySelector('input[name="consent"]');
    const consentError = form.querySelector('.consent-error');

    form.addEventListener('submit', (e) => {
      if (consentCheckbox && !consentCheckbox.checked) {
        e.preventDefault();
        if (consentError) consentError.classList.add('visible');
        consentCheckbox.style.outline = '2px solid #c0392b';
        consentCheckbox.style.outlineOffset = '1px';
        consentCheckbox.addEventListener('change', () => {
          consentCheckbox.style.outline = '';
          if (consentError) consentError.classList.remove('visible');
        }, { once: true });
      }
    });
  });

});
