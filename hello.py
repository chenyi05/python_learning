"""我的第一个上传到 GitHub 的 Python 文件。

运行方式：在文件夹里打开终端，输入  python hello.py
"""


def main():
    print("Hello, GitHub!")
    print("这是我上传的第一个仓库。")

    # 试试把学过的知识用上：列表 + 循环
    goals = [
        "学好 SQL 和数据库",
        "做出一个 AI Agent",
        "拿到英科医疗的 offer",
    ]
    print("\n我的目标：")
    for i, goal in enumerate(goals, start=1):
        print(f"  {i}. {goal}")


if __name__ == "__main__":
    main()
