from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Todo List</title>
  <style>
    :root { --accent: #2563eb; --bg: #f9fafb; --card: #ffffff; }
    html,body{height:100%;margin:0;font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial}
    body{display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,var(--bg),#eef2ff);padding:24px}
    .wrap{width:100%;max-width:640px;background:var(--card);border-radius:12px;padding:20px;box-shadow:0 6px 18px rgba(15,23,42,0.08)}
    h1{margin:0 0 12px;font-size:20px;color:#0f172a}
    .controls{display:flex;gap:8px;margin-bottom:12px}
    .controls input{flex:1;padding:10px 12px;border:1px solid #e6edf3;border-radius:8px;font-size:14px}
    .controls button{padding:10px 14px;border-radius:8px;border:none;background:var(--accent);color:#fff;cursor:pointer}
    ul{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px}
    li{display:flex;justify-content:space-between;align-items:center;padding:10px;border-radius:8px;border:1px solid #eef2f7;background:#fff}
    .text{flex:1;margin-right:12px;color:#0f172a}
    .text.done{text-decoration:line-through;color:#64748b}
    .actions{display:flex;gap:8px}
    .btn{padding:6px 10px;border-radius:6px;border:none;cursor:pointer;font-size:13px}
    .btn.done{background:#10b981;color:#fff}
    .btn.del{background:#ef4444;color:#fff}
    .empty{color:#64748b;text-align:center;padding:18px;border-radius:8px;border:1px dashed #e6edf3}
    @media (max-width:480px){.controls{flex-direction:column}.controls button{width:100%}}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Todo List</h1>
    <div class="controls">
      <input id="taskInput" placeholder="Tambahkan tugas baru..." />
      <button id="addBtn">Tambah</button>
    </div>
    <ul id="todoList"></ul>
    <div style="height:6px"></div>
    <div style="display:flex;justify-content:space-between;align-items:center">
      <small style="color:#94a3b8">Data tersimpan di browser (localStorage)</small>
      <button id="clearAll" style="background:#efefef;border-radius:6px;padding:6px 10px;border:1px solid #e6edf3">Hapus Semua</button>
    </div>
  </div>

  <script>
    const KEY = 'todos_v1'
    const input = document.getElementById('taskInput')
    const addBtn = document.getElementById('addBtn')
    const listEl = document.getElementById('todoList')
    const clearAllBtn = document.getElementById('clearAll')

    function loadTodos(){
      try{ return JSON.parse(localStorage.getItem(KEY) || '[]') }catch(e){ return [] }
    }
    function saveTodos(todos){ localStorage.setItem(KEY, JSON.stringify(todos)) }

    function render(){
      const todos = loadTodos()
      listEl.innerHTML = ''
      if(!todos.length){
        const emp = document.createElement('div')
        emp.className = 'empty'
        emp.textContent = 'Belum ada tugas — tambahkan tugas baru.'
        listEl.appendChild(emp)
        return
      }
      todos.forEach(item =>{
        const li = document.createElement('li')
        const txt = document.createElement('div')
        txt.className = 'text' + (item.done ? ' done' : '')
        txt.textContent = item.text

        const actions = document.createElement('div')
        actions.className = 'actions'

        const doneBtn = document.createElement('button')
        doneBtn.className = 'btn done'
        doneBtn.textContent = item.done ? 'Batal' : 'Selesai'
        doneBtn.onclick = () => { toggleDone(item.id) }

        const delBtn = document.createElement('button')
        delBtn.className = 'btn del'
        delBtn.textContent = 'Hapus'
        delBtn.onclick = () => { removeTodo(item.id) }

        actions.appendChild(doneBtn)
        actions.appendChild(delBtn)

        li.appendChild(txt)
        li.appendChild(actions)
        listEl.appendChild(li)
      })
    }

    function addTodo(text){
      const todos = loadTodos()
      const id = Date.now() + Math.floor(Math.random()*1000)
      todos.push({ id, text: text.trim(), done: false })
      saveTodos(todos)
      render()
    }

    function toggleDone(id){
      const todos = loadTodos().map(t => t.id === id ? {...t, done: !t.done} : t)
      saveTodos(todos)
      render()
    }

    function removeTodo(id){
      const todos = loadTodos().filter(t => t.id !== id)
      saveTodos(todos)
      render()
    }

    addBtn.addEventListener('click', ()=>{
      const v = input.value
      if(!v.trim()) return alert('Masukkan tugas sebelum menambah')
      addTodo(v)
      input.value = ''
      input.focus()
    })

    input.addEventListener('keydown', (e)=>{
      if(e.key === 'Enter') addBtn.click()
    })

    clearAllBtn.addEventListener('click', ()=>{
      if(confirm('Hapus semua tugas?')){ localStorage.removeItem(KEY); render() }
    })

    // initial render
    render()
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    # Run the app on localhost port 5000
    app.run(debug=True)
