from pathlib import Path


def get_project_root(marker: str = "requirements.txt") -> Path:
    """
    根据标志文件查找项目根目录。
    默认在当前文件夹往上查找，直到找到 marker 文件为止。
    如果找不到，就返回当前文件所在的目录。
    """
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / marker).exists():
            return parent
    return p.parent  # fallback：没找到 marker，就用当前文件的上级目录


def ensure_dir(path: str) -> str:
    root_dir = get_project_root()
    temp_dir = root_dir / "temp_files"

    temp_dir.mkdir(parents=True, exist_ok=True)
    filepath_out = temp_dir / path

    # filepath_out.mkdir(parents=True, exist_ok=True)
    return str(filepath_out)  # 如果需要字符串形式
