import os, shutil

# Copy the summary next to this program into the output directory.
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
OUT = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Post-copy check: the output must be an exact, non-empty copy.
    with open(SRC, "rb") as f:
        src = f.read()
    with open(OUT, "rb") as f:
        out = f.read()
    assert out == src and len(out) > 0
    text = src.decode("utf-8")
    # The competition allows 1 to 2,000 Unicode code points.
    assert 1 <= len(text) <= 2000


if __name__ == "__main__":
    main()
