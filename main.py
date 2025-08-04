import subprocess
from pathlib import Path
import questionary
from questionary import Choice
from rich.console import Console
from utils.diff import run_diff, display_diff

console = Console()


def edit_file(filename: Path):
    """用 Notepad3 编辑文件"""
    filename.write_text("", encoding="utf-8")
    console.print(f"[cyan]正在编辑：{filename}（保存后关闭编辑器，按回车继续）[/cyan]")
    subprocess.Popen(["Notepad3.exe", str(filename)]).wait()
    input("按回车继续...")
    return filename.read_text(encoding="utf-8").strip()


def get_texts(mode: str):
    """根据模式获取两个文本"""
    if mode == "input":
        text1 = questionary.text("请输入原始文本：").ask()
        text2 = questionary.text("请输入对比文本：").ask()
    else:  # mode == "edit"
        text1 = edit_file(Path("text1.tmp"))
        text2 = edit_file(Path("text2.tmp"))
    return text1, text2


def main():
    console.print("[bold cyan]📄 文本差异对比工具（CLI版）[/bold cyan]")

    # 选择输入模式
    mode = questionary.select(
        "选择输入模式：",
        choices=[
            Choice(title="直接输入文本", value="input"),
            Choice(title="用 Notepad3 编辑文件", value="edit"),
        ],
    ).ask()

    text1, text2 = get_texts(mode)

    if not text1 or not text2:
        console.print("[yellow]⚠ 请确保两个文本都已填写内容[/yellow]")
        return

    # 选择对比方式
    diff_type = questionary.select(
        "选择对比方式：",
        choices=[
            Choice(title="按词对比", value="diffWords"),
            Choice(title="按字符对比", value="diffChars"),
            Choice(title="按行对比", value="diffLines"),
        ],
    ).ask()

    diff_result = run_diff(text1, text2, diff_type)
    console.print("\n[bold magenta]对比结果：[/bold magenta]")
    display_diff(diff_result)


if __name__ == "__main__":
    main()
