import questionary
from questionary import Choice
from rich.console import Console
from utils.diff import run_diff, display_diff

console = Console()


def main():
    console.print("[bold cyan]📄 文本差异对比工具[/bold cyan]")

    # 输入文本
    text1 = questionary.text("请输入原始文本：").ask()
    text2 = questionary.text("请输入对比文本：").ask()

    if not text1 or not text2:
        console.print("[yellow]⚠ 请确保两个文本都已输入[/yellow]")
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

    # 运行对比并显示结果
    diff_result = run_diff(text1, text2, diff_type)
    console.print("\n[bold magenta]对比结果：[/bold magenta]")
    display_diff(diff_result)


if __name__ == "__main__":
    main()
