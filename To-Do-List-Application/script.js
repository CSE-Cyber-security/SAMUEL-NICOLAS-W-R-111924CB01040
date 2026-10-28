(function () {
  var KEY = "todo.tasks", MAX = 100, tasks = [], confirmId = null;
  var $ = function (id) { return document.getElementById(id); };
  var list = $("list"), input = $("in"), err = $("err");

  // Load saved tasks
  try {
    var raw = localStorage.getItem(KEY);
    if (raw) {
      var parsed = JSON.parse(raw);
      if (Array.isArray(parsed)) tasks = parsed.filter(function (t) { return t && typeof t.text === "string"; });
    }
  } catch (e) {}

  function save() { try { localStorage.setItem(KEY, JSON.stringify(tasks)); } catch (e) {} }

  function showErr(msg) {
    err.textContent = msg;
    if (msg) setTimeout(function () { if (err.textContent === msg) err.textContent = ""; }, 2500);
  }

  function add() {
    var v = input.value.trim();
    if (!v) { showErr("Please enter a task."); return; }
    if (v.length > MAX) { showErr("Tasks can be up to " + MAX + " characters."); return; }
    tasks.unshift({ id: Date.now() + Math.random(), text: v, done: false });
    input.value = ""; err.textContent = "";
    save(); render(); input.focus();
  }

  function render() {
    list.innerHTML = "";
    if (!tasks.length) {
      var e = document.createElement("div");
      e.className = "empty";
      e.textContent = "// no tasks yet";
      list.appendChild(e);
    }
    tasks.forEach(function (t) {
      var li = document.createElement("li");
      if (t.done) li.className = "done";

      var cb = document.createElement("input");
      cb.type = "checkbox"; cb.checked = t.done;
      cb.setAttribute("aria-label", "Mark complete");
      cb.onchange = function () { t.done = cb.checked; save(); render(); };

      var s = document.createElement("span");
      s.className = "t"; s.textContent = t.text;

      li.appendChild(cb); li.appendChild(s);

      if (confirmId === t.id) {
        var ask = document.createElement("div");
        ask.className = "ask";
        ask.appendChild(document.createTextNode("Delete?"));
        var yes = document.createElement("button");
        yes.className = "yes"; yes.textContent = "Yes";
        yes.onclick = function () {
          li.classList.add("out");
          setTimeout(function () {
            tasks = tasks.filter(function (x) { return x.id !== t.id; });
            confirmId = null; save(); render();
          }, 180);
        };
        var no = document.createElement("button");
        no.className = "no"; no.textContent = "No";
        no.onclick = function () { confirmId = null; render(); };
        ask.appendChild(yes); ask.appendChild(no); li.appendChild(ask);
      } else {
        var del = document.createElement("button");
        del.className = "del"; del.textContent = "×";
        del.setAttribute("aria-label", "Delete task");
        del.onclick = function () { confirmId = t.id; render(); };
        li.appendChild(del);
      }
      list.appendChild(li);
    });

    var done = tasks.filter(function (t) { return t.done; }).length;
    $("total").textContent = tasks.length;
    $("comp").textContent = done;
    $("clear").disabled = !done;
    $("bar").style.width = (tasks.length ? Math.round(done / tasks.length * 100) : 0) + "%";
  }

  $("addBtn").onclick = add;
  input.addEventListener("keydown", function (e) { if (e.key === "Enter") add(); });
  input.addEventListener("input", function () {
    if (input.value.length >= MAX) showErr("Maximum length reached (" + MAX + ").");
  });
  $("clear").onclick = function () {
    tasks = tasks.filter(function (t) { return !t.done; });
    save(); render();
  };

  render();
})();
