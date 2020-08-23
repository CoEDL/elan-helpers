from os import scandir, chdir
from pathlib import Path
from shutil import move, rmtree


def flatten(root_path: str, absolute_root: str) -> None:
    """
    Flatten a tree of files and give the files the names of the enclosing
    files separated by underscores.
    WARNING: operates in place and will destroy exiting file structure.
    :param root_path: the local root (at the start this will match the
    absolute root)
    :param absolute_root: the root directory of the tree you want to flatten
    """
    path = Path(root_path)
    stack = set(scandir(root_path))
    while stack:
        entry = stack.pop()
        entry_path = Path(entry.path)
        if ".DS_Store" in entry.name or not entry_path.exists() and entry_path.is_file():
            if entry_path.exists():
                entry_path.unlink()
            continue
        if entry_path.is_dir():
            flatten(entry.path, absolute_root)
            if root_path != absolute_root:
                stack = stack.union(filter(lambda x: x.is_file(),
                                        list(scandir(root_path))))
            rmtree(entry.path)
        elif entry_path.exists() and entry_path.is_file():
            target_file = f"{path.parent.resolve()}/{path.name}_{entry.name}"
            move(entry.path, target_file)


if __name__ == "__main__":
    target = "wav"
    # chdir(target)
    flatten(target, target)
