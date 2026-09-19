(() => {
  const toggle = document.querySelector('[data-menu-toggle]');
  const navigation = document.querySelector('#main-nav');
  if (!toggle || !navigation) return;
  document.documentElement.classList.add('js');
  toggle.hidden = false;
  const setMenu = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
    toggle.querySelector('span').textContent = open ? toggle.dataset.closeLabel : toggle.dataset.openLabel;
  };
  toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setMenu(false);
      toggle.focus();
    }
  });
  window.matchMedia('(min-width: 64rem)').addEventListener('change', () => setMenu(false));
})();
