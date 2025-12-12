from app.engine.graph import Graph, Node
import asyncio

# Node: extract_functions
async def extract_functions(state):
    code = state.get("code", "")
    funcs = []
    for part in code.split("def ")[1:]:
        name_line = part.splitlines()[0].strip().split("(")[0]
        funcs.append(name_line)
    state["functions"] = funcs
    log = {"node": "extract_functions", "functions_count": len(funcs)}
    return state, log

# Node: check_complexity
async def check_complexity(state):
    funcs = state.get("functions", [])
    complexity = {f: 1 + len(f) for f in funcs}
    state["complexity"] = complexity
    state["complexity_score"] = sum(complexity.values())
    log = {"node": "check_complexity", "complexity_score": state["complexity_score"]}
    return state, log

# Node: detect_issues
async def detect_issues(state):
    code = state.get("code", "")
    issues = []
    if "TODO" in code or "# TODO" in code:
        issues.append("contains TODO")
    if "print(" in code:
        issues.append("debug-print statements")
    state["issues"] = issues
    state["issues_count"] = len(issues)
    log = {"node": "detect_issues", "issues": issues}
    return state, log

# Node: suggest_improvements (looping)
async def suggest_improvements(state):
    quality = state.get("quality_score", 0)
    penalty = state.get("issues_count", 0) * 10
    boost = max(0, 50 - state.get("complexity_score", 0))
    quality = quality - penalty + boost
    quality = min(max(0, quality + 20), 100)
    state["quality_score"] = quality

    threshold = state.get("threshold", 80)
    if quality < threshold:
        # loop: ask to run suggest_improvements again
        state["next"] = "suggest_improvements"

    log = {"node": "suggest_improvements", "quality_score": quality, "threshold": threshold}
    return state, log

def build_code_review_graph():
    nodes = {
        "extract": Node("extract", extract_functions),
        "complexity": Node("complexity", check_complexity),
        "detect": Node("detect", detect_issues),
        "suggest_improvements": Node("suggest_improvements", suggest_improvements),
    }
    edges = {
        "extract": "complexity",
        "complexity": "detect",
        "detect": "suggest_improvements",
        "suggest_improvements": None
    }
    start = "extract"
    return Graph(nodes=nodes, edges=edges, start=start)
