document.addEventListener("DOMContentLoaded", function () {
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  var widget = document.getElementById("waWidget");
  var toggle = document.getElementById("waToggle");
  var closeBtn = document.getElementById("waClose");

  function openPanel() {
    widget.classList.add("open");
    toggle.setAttribute("aria-expanded", "true");
  }
  function closePanel() {
    widget.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
  }

  toggle.addEventListener("click", function () {
    widget.classList.contains("open") ? closePanel() : openPanel();
  });
  closeBtn.addEventListener("click", function (e) {
    e.stopPropagation();
    closePanel();
  });
  document.addEventListener("click", function (e) {
    if (widget.classList.contains("open") && !widget.contains(e.target)) {
      closePanel();
    }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closePanel();
  });
});
