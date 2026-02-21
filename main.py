from flask import Flask, request, redirect, session, render_template_string

app = Flask(__name__)
app.secret_key = "secret_key"

# ===============================
# In-memory storage (NO DATABASE)
# ===============================
organization = "Not Created"
projects = []
tasks = []
milestones = []
time_logs = []
comments = []
issues = []
documents = []
notifications = ["Welcome to Project Management Tools"]

# ===============================
# Module 1: Authentication
# ===============================
def authenticate(username, password):
    if username == "admin" and password == "admin":
        return "Admin"
    if username == "user" and password == "user": 
        return "Team Member"
    return None

# ===============================
# Dashboard Summary (Module 12)
# ===============================
def dashboard_data():
    return {
        "projects": len(projects),
        "tasks": len(tasks),
        "milestones": len(milestones),
        "issues": len(issues)
    }

# ===============================
# HTML Templates
# ===============================
login_html = """
<h2>Login</h2>
<form method="post">
<input name="username" placeholder="Username" required><br><br>
<input name="password" type="password" placeholder="Password" required><br><br>
<button>Login</button>
</form>
"""

dashboard_html = """
<h2>{{ role }} Dashboard</h2>
<p>Projects: {{ d.projects }}</p>
<p>Tasks: {{ d.tasks }}</p>
<p>Milestones: {{ d.milestones }}</p>
<p>Issues: {{ d.issues }}</p>

<a href="/organization">Organization</a> |
<a href="/projects">Projects</a> |
<a href="/tasks">Tasks</a> |
<a href="/milestones">Milestones</a> |
<a href="/time">Time</a> |
<a href="/collaboration">Collaboration</a> |
<a href="/issues">Issues</a> |
<a href="/documents">Documents</a> |
<a href="/reports">Reports</a> |
<a href="/notifications">Notifications</a> |
<a href="/logout">Logout</a>
"""

# ===============================
# Routes (ALL 12 MODULES)
# ===============================

# Module 1: Login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = authenticate(request.form["username"], request.form["password"])
        if role:
            session["role"] = role
            return redirect("/dashboard")
    return render_template_string(login_html)

# Module 12: Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template_string(
        dashboard_html,
        d=dashboard_data(),
        role=session.get("role")
    )

# Module 2: Organization
@app.route("/organization", methods=["GET", "POST"])
def org():
    global organization
    if request.method == "POST":
        organization = request.form["org"]
    return render_template_string("""
    <h2>Organization</h2>
    <form method="post">
    <input name="org" placeholder="Organization Name">
    <button>Create</button>
    </form>
    <p>Current Organization: {{ org }}</p>
    <a href="/dashboard">Back</a>
    """, org=organization)

# Module 3: Projects
@app.route("/projects", methods=["GET", "POST"])
def project_module():
    if request.method == "POST":
        projects.append(request.form["project"])
    return render_template_string("""
    <h2>Projects</h2>
    <form method="post">
    <input name="project" placeholder="Project Name">
    <button>Add</button>
    </form>
    <ul>{% for p in projects %}<li>{{ p }}</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, projects=projects)

# Module 4: Tasks
@app.route("/tasks", methods=["GET", "POST"])
def task_module():
    if request.method == "POST":
        tasks.append(request.form["task"])
    return render_template_string("""
    <h2>Tasks</h2>
    <form method="post">
    <input name="task" placeholder="Task Name">
    <button>Add</button>
    </form>
    <ul>{% for t in tasks %}<li>{{ t }}</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, tasks=tasks)

# Module 5: Milestones
@app.route("/milestones", methods=["GET", "POST"])
def milestone_module():
    if request.method == "POST":
        milestones.append(request.form["milestone"])
    return render_template_string("""
    <h2>Milestones</h2>
    <form method="post">
    <input name="milestone" placeholder="Milestone">
    <button>Add</button>
    </form>
    <ul>{% for m in milestones %}<li>{{ m }}</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, milestones=milestones)

# Module 6: Time Tracking
@app.route("/time", methods=["GET", "POST"])
def time_module():
    if request.method == "POST":
        time_logs.append(request.form["hours"])
    return render_template_string("""
    <h2>Time Tracking</h2>
    <form method="post">
    <input name="hours" placeholder="Hours Worked">
    <button>Log</button>
    </form>
    <ul>{% for h in time %}<li>{{ h }} hours</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, time=time_logs)

# Module 7: Collaboration
@app.route("/collaboration", methods=["GET", "POST"])
def collaboration_module():
    if request.method == "POST":
        comments.append(request.form["comment"])
    return render_template_string("""
    <h2>Collaboration</h2>
    <form method="post">
    <textarea name="comment"></textarea>
    <button>Post</button>
    </form>
    <ul>{% for c in comments %}<li>{{ c }}</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, comments=comments)

# Module 8: Issues
@app.route("/issues", methods=["GET", "POST"])
def issue_module():
    if request.method == "POST":
        issues.append(request.form["issue"])
    return render_template_string("""
    <h2>Issues</h2>
    <form method="post">
    <input name="issue" placeholder="Issue Description">
    <button>Add</button>
    </form>
    <ul>{% for i in issues %}<li>{{ i }}</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, issues=issues)

# Module 9: Documents
@app.route("/documents", methods=["GET", "POST"])
def document_module():
    if request.method == "POST":
        documents.append(request.form["doc"])
    return render_template_string("""
    <h2>Documents</h2>
    <form method="post">
    <input name="doc" placeholder="Document Name">
    <button>Upload</button>
    </form>
    <ul>{% for d in docs %}<li>{{ d }}</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, docs=documents)

# Module 10: Reports
@app.route("/reports")
def report_module():
    return render_template_string("""
    <h2>Reports</h2>
    <p>Total Projects: {{ p }}</p>
    <p>Total Tasks: {{ t }}</p>
    <p>Total Issues: {{ i }}</p>
    <a href="/dashboard">Back</a>
    """, p=len(projects), t=len(tasks), i=len(issues))

# Module 11: Notifications
@app.route("/notifications")
def notification_module():
    return render_template_string("""
    <h2>Notifications</h2>
    <ul>{% for n in notes %}<li>{{ n }}</li>{% endfor %}</ul>
    <a href="/dashboard">Back</a>
    """, notes=notifications)

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ===============================
# Run App
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
