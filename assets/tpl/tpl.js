/* Vix Assist website templates: small interactions */
(function () {
  "use strict";
  var nav = document.querySelector(".nav"), mb = document.querySelector(".menu");
  if (mb) mb.addEventListener("click", function () { nav.classList.toggle("open"); });
  var rv = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .12 });
    rv.forEach(function (el) { io.observe(el); });
  } else rv.forEach(function (el) { el.classList.add("in"); });
  // shop: add to cart
  var count = document.querySelector(".cart b"), n = 0;
  document.querySelectorAll(".add").forEach(function (b) {
    b.addEventListener("click", function () { n++; if (count) count.textContent = n; b.classList.add("done"); b.textContent = "Added ✓"; setTimeout(function () { b.classList.remove("done"); b.textContent = "Add to cart"; }, 1600); });
  });
  // demo forms
  document.querySelectorAll("form.form, form.search").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = f.parentNode.querySelector(".ok");
      if (ok) { f.style.display = "none"; ok.style.display = "block"; }
      else { var b = f.querySelector("button"); if (b) b.textContent = "This is a demo ✓"; }
    });
  });
})();
