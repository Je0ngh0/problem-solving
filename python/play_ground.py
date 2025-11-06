from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET_DIR = ROOT / "class5"

HEADER_INPUT = "input = sys.stdin.readline"
HEADER_PRINT = "print = sys.stdout.write"
HEADER_IMPORT = "import sys"

def file_has_both_header_lines(text: str) -> bool:
    return HEADER_INPUT in text and HEADER_PRINT in text

def main():
    if not TARGET_DIR.exists():
        raise SystemExit(f"[ERROR] 대상 디렉토리 없음: {TARGET_DIR}")

    changed = []
    skipped = []

    for py in TARGET_DIR.rglob("*.py"):
        if py.is_symlink():
            continue

        try:
            text = py.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = py.read_text(encoding="utf-8", errors="ignore")

        # 이미 두 줄이 있으면 스킵
        if file_has_both_header_lines(text):
            skipped.append(py)
            continue

        lines = text.splitlines()
        insert_at = 1 if lines and lines[0].startswith("#!") else 0

        # 삽입할 블록 구성
        to_insert = []
        if HEADER_IMPORT not in text:
            to_insert.extend([HEADER_IMPORT, ""])
        to_insert.extend([HEADER_INPUT, HEADER_PRINT, ""])

        new_lines = lines[:insert_at] + to_insert + lines[insert_at:]
        new_text = "\n".join(new_lines)
        if not new_text.endswith("\n"):
            new_text += "\n"

        py.write_text(new_text, encoding="utf-8")
        changed.append(py)

    print(f"Updated {len(changed)} file(s). Skipped {len(skipped)} file(s).")
    if changed:
        print("\n[UPDATED]")
        for p in changed:
            print("  +", p)
    if skipped:
        print("\n[SKIPPED]")
        for p in skipped:
            print("  =", p)

if __name__ == "__main__":
    main()
