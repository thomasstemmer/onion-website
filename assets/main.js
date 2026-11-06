document.documentElement.classList.add('js');
document.querySelectorAll('[data-year]').forEach((year) => {
  year.textContent = String(new Date().getFullYear());
});
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('#nav-links');
function closeMenu(restoreFocus = false) {
  toggle?.setAttribute('aria-expanded', 'false');
  links?.classList.remove('open');
  if (restoreFocus) toggle?.focus();
}
toggle?.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  links?.classList.toggle('open', open);
});
links?.addEventListener('click', (event) => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') closeMenu(true);
});
document.addEventListener('click', (event) => {
  if (!event.target.closest('.nav-wrap')) closeMenu();
});
window.matchMedia('(min-width: 761px)').addEventListener('change', () => closeMenu());
// Ordinary links keep the current section without cookies or browser storage.
document.querySelectorAll('[data-language]').forEach((link) => {
  link.addEventListener('click', () => {
    const target = new URL(link.href);
    target.hash = window.location.hash;
    link.href = target.href;
  });
});
