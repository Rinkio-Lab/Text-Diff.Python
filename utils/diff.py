import json
from pathlib import Path
from py_mini_racer import py_mini_racer
from rich.console import Console
from rich.text import Text

console = Console()

# 初始化 JS 引擎并加载 diff.min.js
diff_js_path = Path(__file__).parent / "assets" / "js" / "diff.min.js"
if not diff_js_path.exists():
    console.print("[bold red]错误[/bold red]：找不到 diff.min.js 文件")
    raise FileNotFoundError("缺少 diff.min.js")

ctx = py_mini_racer.MiniRacer()
ctx.eval(diff_js_path.read_text(encoding="utf-8"))


def run_diff(text1: str, text2: str, diff_type: str):
    """调用 JS Diff 方法"""
    js_code = f"""
        JSON.stringify(Diff["{diff_type}"]({text1!r}, {text2!r}))
    """
    diff_json = ctx.eval(js_code)
    return json.loads(diff_json)


def display_diff(diff_result):
    """高亮显示对比结果"""
    output = Text()
    for part in diff_result:
        value = part["value"]
        if part.get("added"):
            output.append(value, style="bold green on #d4fcd4")  # 新增
        elif part.get("removed"):
            output.append(value, style="bold red on #ffe1e1 strike")  # 删除
        else:
            output.append(value)
    console.print(output)
