"""Render the training plan in program.py to a narrated 1080p MP4.

Requirements: pip install pillow imageio-ffmpeg ; apt install espeak-ng mbrola mbrola-us2
Usage: python3 make_video.py [output.mp4]
"""
import os
import subprocess
import sys
import tempfile
import wave

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

from program import SLIDES, WEEKS

W, H = 1920, 1080
BG = (16, 18, 22)
PANEL = (30, 34, 42)
ACCENT = (255, 106, 26)
TEXT = (240, 240, 240)
MUTED = (160, 166, 176)
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
VOICE = os.environ.get("VOICE", "mb-us2")
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def font(size, bold=True):
    return ImageFont.truetype(FONT_B if bold else FONT_R, size)


def base(idx, total):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 24, H], fill=ACCENT)
    # progress bar
    d.rectangle([0, H - 10, W, H], fill=PANEL)
    d.rectangle([0, H - 10, int(W * (idx + 1) / total), H], fill=ACCENT)
    d.text((W - 60, H - 50), "HARE SCRAMBLE  |  4-WEEK PLAN", font=font(22), fill=MUTED, anchor="rs")
    return img, d


def header(d, title):
    d.text((110, 90), title, font=font(72), fill=TEXT)
    d.rectangle([110, 190, 330, 198], fill=ACCENT)


def render(slide, idx, total):
    img, d = base(idx, total)
    k = slide["kind"]
    if k == "title":
        d.multiline_text((W // 2, 430), slide["title"], font=font(130), fill=TEXT,
                         anchor="mm", align="center", spacing=20)
        d.rectangle([W // 2 - 180, 600, W // 2 + 180, 610], fill=ACCENT)
        d.text((W // 2, 680), slide["sub"], font=font(44, False), fill=MUTED, anchor="mm")
    elif k == "section":
        d.text((W // 2, 460), slide["title"], font=font(150), fill=ACCENT, anchor="mm")
        d.text((W // 2, 610), slide["sub"], font=font(46, False), fill=TEXT, anchor="mm")
    elif k == "bullets":
        header(d, slide["title"])
        y = 280
        for item in slide["items"]:
            d.rectangle([120, y + 18, 140, y + 38], fill=ACCENT)
            d.text((180, y), item, font=font(50, False), fill=TEXT)
            y += 130
    elif k == "schedule":
        header(d, slide["title"])
        y = 225
        for day, name, detail in slide["rows"]:
            race = day == "SUN"
            d.rounded_rectangle([110, y, W - 110, y + 96], radius=14,
                                fill=ACCENT if race else PANEL)
            d.text((150, y + 48), day, font=font(46), fill=BG if race else ACCENT, anchor="lm")
            d.text((340, y + 48), name, font=font(46), fill=BG if race else TEXT, anchor="lm")
            d.text((860, y + 48), detail, font=font(40, False), fill=BG if race else MUTED, anchor="lm")
            y += 106
    elif k == "table":
        header(d, slide["title"])
        cols = slide["cols"]
        first = 360
        colw = (W - 220 - first) // (len(cols) - 1)
        xs = [110] + [110 + first + i * colw for i in range(len(cols) - 1)]
        y = 290
        for i, c in enumerate(cols):
            d.text((xs[i] + 20, y), c, font=font(40), fill=ACCENT)
        y += 90
        fs = 40 if max(len(c) for r in slide["rows"] for c in r) < 12 else 34
        for r in slide["rows"]:
            d.rounded_rectangle([110, y - 10, W - 110, y + 100], radius=12, fill=PANEL)
            for i, c in enumerate(r):
                d.text((xs[i] + 20, y + 45), c, font=font(fs, i == 0),
                       fill=TEXT if i else ACCENT, anchor="lm")
            y += 130
    elif k == "exercise":
        d.rounded_rectangle([110, 80, 260, 190], radius=16, fill=ACCENT)
        d.text((185, 135), slide["tag"], font=font(64), fill=BG, anchor="mm")
        d.text((300, 135), slide["title"], font=font(66), fill=TEXT, anchor="lm")
        # week boxes
        bw = (W - 220 - 3 * 30) // 4
        for i, (lab, val) in enumerate(zip(WEEKS, slide["weeks"])):
            x = 110 + i * (bw + 30)
            d.rounded_rectangle([x, 250, x + bw, 450], radius=16, fill=PANEL)
            d.text((x + bw // 2, 300), lab, font=font(32), fill=ACCENT, anchor="mm")
            fs = 44 if len(val) <= 14 else 34
            d.text((x + bw // 2, 385), val, font=font(fs), fill=TEXT, anchor="mm")
        d.text((110, 490), slide["rest"], font=font(38), fill=MUTED)
        d.text((110, 570), "COACHING CUES", font=font(36), fill=ACCENT)
        y = 640
        for c in slide["cues"]:
            d.rectangle([120, y + 16, 136, y + 32], fill=ACCENT)
            d.text((170, y), c, font=font(44, False), fill=TEXT)
            y += 88
    return img


def tts(text, path):
    subprocess.run(["espeak-ng", "-v", VOICE, "-s", "150", "-p", "45", "-w", path, text],
                   check=True, capture_output=True)
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()


def main():
    out = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "hare_scramble_4wk_plan.mp4")
    tmp = tempfile.mkdtemp()
    parts = []
    for i, s in enumerate(SLIDES):
        png, wav, mp4 = (os.path.join(tmp, f"{i:02d}.{e}") for e in ("png", "wav", "mp4"))
        render(s, i, len(SLIDES)).save(png)
        dur = tts(s["say"], wav) + 1.2
        subprocess.run([
            FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-i", wav,
            "-af", "adelay=400|400,apad", "-t", f"{dur:.2f}",
            "-vf", f"fade=in:0:12,fade=out:st={dur - 0.4:.2f}:d=0.4,format=yuv420p",
            "-r", "30", "-c:v", "libx264", "-tune", "stillimage", "-preset", "medium",
            "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-ac", "2", mp4,
        ], check=True)
        parts.append(mp4)
        print(f"slide {i + 1}/{len(SLIDES)}  {dur:5.1f}s  {s['title'].splitlines()[0]}")
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", "-movflags", "+faststart", out], check=True)
    # thumbnail
    render(SLIDES[0], 0, len(SLIDES)).save(os.path.splitext(out)[0] + "_thumbnail.png")
    print("wrote", out)


if __name__ == "__main__":
    main()
