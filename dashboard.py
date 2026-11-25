
import streamlit as st
import pandas as pd
import os

from algorithms.graph import create_graph
from algorithms.topological_sort import topological_sort_bfs
from algorithms.dfs_sort import topological_sort_dfs
from algorithms.cycle_detection import detect_cycle

st.set_page_config(
    page_title="FlowPilot | Project Manager",
    page_icon="🚀",
    layout="wide"
)

# ---------- PREMIUM DARK THEME ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080d1b, #10182b);
    color: #e8edf7;
}

[data-testid="stSidebar"] {
    background: #0b1222;
    border-right: 1px solid #26334d;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

h1, h2, h3 {
    color: #f1f5ff !important;
}

p, label, li {
    color: #c2cde0;
}

.metric-card {
    background: linear-gradient(145deg, #17243d, #111b30);
    border: 1px solid #293c5e;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 8px 25px #00000030;
}

.metric-label {
    color: #9eacc5;
    font-size: 14px;
}

.metric-value {
    color: #ffffff;
    font-size: 30px;
    font-weight: 750;
    margin-top: 7px;
}

.panel {
    background: #111c31;
    border: 1px solid #263956;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 15px;
}

.section-caption {
    color: #8fa3c3;
    font-size: 13px;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #293c5e;
    border-radius: 12px;
}

.stButton button {
    border-radius: 10px;
}

hr {
    border-color: #263956;
}
</style>
""", unsafe_allow_html=True)


# ---------- PROJECT DATA ----------
tasks = [
    "Requirement Analysis",
    "System Design",
    "Frontend Development",
    "Backend Development",
    "Database Design",
    "Integration",
    "Testing",
    "Deployment"
]

dependencies = [
    ("Requirement Analysis", "System Design"),
    ("System Design", "Frontend Development"),
    ("System Design", "Backend Development"),
    ("System Design", "Database Design"),
    ("Frontend Development", "Integration"),
    ("Backend Development", "Integration"),
    ("Database Design", "Integration"),
    ("Integration", "Testing"),
    ("Testing", "Deployment")
]

graph = create_graph(tasks, dependencies)
bfs_order = topological_sort_bfs(graph)
dfs_order = topological_sort_dfs(graph)
has_cycle = detect_cycle(graph)


# ---------- SIDEBAR ----------
st.sidebar.markdown("# 🚀 FlowPilot")
st.sidebar.caption("SMART PROJECT EXECUTION")
st.sidebar.divider()

section = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Dependency Graph",
        "Algorithm Results",
        "Performance & Complexity"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Design and Analysis of Algorithms")


# ---------- HEADER ----------
st.markdown(
    "<div style='color:#8fa3c3; font-size:13px; letter-spacing:2px;'>"
    "PROJECT MANAGEMENT SYSTEM</div>",
    unsafe_allow_html=True
)
st.title("FlowPilot")
st.write("Manage task dependencies. Discover the ideal execution flow.")
st.divider()


# ---------- OVERVIEW ----------
if section == "Overview":

    st.subheader("Project Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""<div class="metric-card">
            <div class="metric-label">TOTAL TASKS</div>
            <div class="metric-value">{len(tasks)}</div>
            </div>""",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""<div class="metric-card">
            <div class="metric-label">DEPENDENCIES</div>
            <div class="metric-value">{len(dependencies)}</div>
            </div>""",
            unsafe_allow_html=True
        )

    with c3:
        status = "No Cycle" if not has_cycle else "Cycle Found"
        st.markdown(
            f"""<div class="metric-card">
            <div class="metric-label">CYCLE STATUS</div>
            <div class="metric-value">{status}</div>
            </div>""",
            unsafe_allow_html=True
        )

    st.write("")
    st.markdown("### Project Summary")
    st.markdown("""
    <div class="panel">
        <h3>🎯 Project Execution</h3>
        <p>FlowPilot represents project tasks as vertices and their
        dependencies as directed edges.</p>
        <p>It uses BFS-based Kahn's Algorithm and DFS Topological Sort
        to calculate valid task execution orders.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Execution Status")
    if has_cycle:
        st.error("A dependency cycle was detected. No valid execution order exists.")
    else:
        st.success("All dependencies are valid. Project execution is possible.")


# ---------- DEPENDENCY GRAPH ----------
elif section == "Dependency Graph":

    st.subheader("Dependency Graph")
    st.caption("Visual representation of tasks and their prerequisite relationships.")

    graph_image = "results/dependency_graph.png"

    if os.path.exists(graph_image):
        st.image(graph_image, use_container_width=True)
    else:
        st.warning("Graph image not found. Run main.py first.")

    st.markdown("""
    <div class="panel">
        <h3>How to read this graph</h3>
        <p>Each node represents a project task.</p>
        <p>Each directed arrow represents a dependency:
        the starting task must be completed before the next task.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------- ALGORITHM RESULTS ----------
elif section == "Algorithm Results":

    st.subheader("Algorithm Results")
    st.caption("Two approaches to finding a valid project execution order.")

    left, right = st.columns(2)

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### 🔵 BFS / Kahn's Algorithm")
        for i, task in enumerate(bfs_order, 1):
            st.write(f"**{i}.** {task}")
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### 🟣 DFS Algorithm")
        for i, task in enumerate(dfs_order, 1):
            st.write(f"**{i}.** {task}")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Cycle Detection")
    if has_cycle:
        st.error("Cycle detected! No valid execution order.")
    else:
        st.success("No cycle detected. Project execution is possible.")


# ---------- PERFORMANCE & COMPLEXITY ----------
elif section == "Performance & Complexity":

    st.subheader("Performance & Complexity")

    st.markdown("### Algorithm Complexity")

    complexity = pd.DataFrame({
        "Algorithm": [
            "BFS / Kahn's",
            "DFS Topological Sort",
            "Cycle Detection"
        ],
        "Time Complexity": [
            "O(V + E)",
            "O(V + E)",
            "O(V + E)"
        ],
        "Auxiliary Space": [
            "O(V)",
            "O(V)",
            "O(V)"
        ]
    })

    st.dataframe(
        complexity,
        hide_index=True,
        use_container_width=True
    )

    st.caption("V = Number of tasks (vertices) | E = Number of dependencies (edges)")

    st.divider()
    st.markdown("### 📈 Performance Comparison")

    csv_file = "results/performance_results.csv"

    if os.path.exists(csv_file):
        results = pd.read_csv(csv_file)

        st.dataframe(
            results,
            hide_index=True,
            use_container_width=True
        )

        bfs_col = next(
            (c for c in results.columns if "bfs" in c.lower()),
            None
        )
        dfs_col = next(
            (c for c in results.columns if "dfs" in c.lower()),
            None
        )

        if bfs_col and dfs_col:
            chart_data = results.set_index(results.columns[0])[
                [bfs_col, dfs_col]
            ]
            st.line_chart(chart_data)
    else:
        st.warning("Run benchmark.py to generate performance results.")


# ---------- FOOTER ----------
st.divider()
st.markdown(
    "<p style='text-align:center; color:#7185a6; font-size:12px;'>"
    "FLOWPILOT • SMART DEPENDENCY & PROJECT EXECUTION MANAGER"
    "</p>",
    unsafe_allow_html=True
)
