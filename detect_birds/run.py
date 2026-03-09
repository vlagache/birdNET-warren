import tomllib
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

with open(HERE / "config.toml", "rb") as f:
    cfg = tomllib.load(f)

inf = cfg.get("Inference", {})
out = cfg.get("Output", {})
loc = cfg.get("Locale", {})

W = 60
print("=" * W)
print(f"{'BirdNET Analyzer':^{W}}")
print("=" * W)
print(f"  Input   {HERE / 'input'}")
print(f"  Output  {HERE / 'output'}")
print("-" * W)
species_filter = f"slist={inf.get('slist')}" if inf.get("slist") else f"lat={loc.get('lat')} lon={loc.get('lon')}"
params = (
    f"conf={inf.get('min_conf')}  "
    f"overlap={inf.get('overlap')}s  "
    f"merge={inf.get('merge_consecutive')}  "
    f"lang={loc.get('locale')}  "
    f"{species_filter}  "
    f"week={loc.get('week')}  "
    f"fmt={','.join(out.get('rtype', ['csv']))}"
)
print(f"  {params}")
print("=" * W)
print()

args = [
    sys.executable,
    "-m",
    "birdnet_analyzer.analyze",
    "--min_conf",
    str(inf.get("min_conf", 0.5)),
    "--overlap",
    str(inf.get("overlap", 0.0)),
    "--merge_consecutive",
    str(inf.get("merge_consecutive", 1)),
    "--rtype",
    *out.get("rtype", ["csv"]),
    "-l",
    loc.get("locale", "en"),
    "--week",
    str(loc.get("week", -1)),
    *(
        ["--slist", str(HERE / inf["slist"])]
        if inf.get("slist")
        else ["--lat", str(loc.get("lat", -1)), "--lon", str(loc.get("lon", -1))]
    ),
    "--output",
    str(HERE / "output"),
    "--show_progress",
    str(HERE / "input"),
]

subprocess.run(args)
