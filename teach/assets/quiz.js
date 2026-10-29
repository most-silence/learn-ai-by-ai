/* ═══════════════════════════════════════════════════════════
   quiz.js — 可复用测验组件
   用法：
     <div class="quiz" data-answer="2">
       <p class="quiz-q">题干</p>
       <ul class="quiz-opts">
         <li>选项 A</li><li>选项 B</li><li>选项 C</li><li>选项 D</li>
       </ul>
       <p class="quiz-why" hidden>解析文字</p>
     </div>
   data-answer 为正确选项的 0 基下标。
   点击即判分，立即反馈（紧凑反馈环）。
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var STYLE = ''
    + '.quiz{margin:2rem 0;padding:1.2rem 1.4rem;border:1px solid var(--rule);background:#faf8f3}'
    + '.quiz-q{font-weight:600;margin:0 0 .8rem}'
    + '.quiz-opts{list-style:none;margin:0;padding:0}'
    + '.quiz-opts li{padding:.55rem .8rem;margin:.35rem 0;border:1px solid var(--rule);'
    + 'background:#fff;cursor:pointer;transition:background .12s,border-color .12s}'
    + '.quiz-opts li:hover{border-color:var(--ink-faint)}'
    + '.quiz-opts li.correct{background:var(--good-bg);border-color:var(--good);font-weight:600}'
    + '.quiz-opts li.wrong{background:var(--bad-bg);border-color:var(--bad)}'
    + '.quiz-opts li.correct::after{content:" ✓";color:var(--good)}'
    + '.quiz-opts li.wrong::after{content:" ✗";color:var(--bad)}'
    + '.quiz-opts li.locked{cursor:default}'
    + '.quiz-why{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--rule);'
    + 'font-size:.9rem;color:var(--ink-soft)}';

  function injectStyle() {
    if (document.getElementById('quiz-style')) return;
    var s = document.createElement('style');
    s.id = 'quiz-style';
    s.textContent = STYLE;
    document.head.appendChild(s);
  }

  function initQuiz(quiz) {
    var answer = parseInt(quiz.getAttribute('data-answer'), 10);
    var opts = quiz.querySelectorAll('.quiz-opts li');
    var why = quiz.querySelector('.quiz-why');
    var done = false;

    Array.prototype.forEach.call(opts, function (li, i) {
      li.addEventListener('click', function () {
        if (done) return;
        done = true;
        Array.prototype.forEach.call(opts, function (o) { o.classList.add('locked'); });
        opts[answer].classList.add('correct');
        if (i !== answer) li.classList.add('wrong');
        if (why) why.hidden = false;
      });
    });
  }

  function init() {
    injectStyle();
    Array.prototype.forEach.call(document.querySelectorAll('.quiz'), initQuiz);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
