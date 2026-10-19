# Skier VTuber Avatar

A 2D, browser-based VTuber avatar: a bearded skier dude in an orange pom beanie, mirrored goggles, and a teal ski jacket with a lift ticket on the zipper. One self-contained file (`index.html`), no install, no internet needed.

## Run it

Open `index.html` in Chrome or Edge, then click **Enable mic**.

| Input | Action |
|---|---|
| Talk into mic | Mouth opens with your voice level |
| Hold `Space` | Talk without a mic |
| Move mouse | Head and eyes follow the cursor |
| `1` `2` `3` `4` | Stoked, Chill, Shook, Send it (goggles drop over eyes) |
| `S` | Toggle shaka glove |
| `B` | Background: snowy mountain scene / green screen / transparent |
| `H` | Hide or show the control panel |

Idle animation is automatic: blinking, breathing, head sway, swinging lift ticket, falling snow.

URL options: `index.html?bg=green&ui=0` starts on green screen with the panel hidden.

## Use in OBS

1. Open `index.html?bg=green&ui=0` in Chrome and enable the mic.
2. In OBS add a **Window Capture** of that Chrome window.
3. Right-click the source, **Filters**, add **Chroma Key** (green).
4. Keep that browser window open while streaming (it can sit behind other windows on most systems).

Tune **Sensitivity** and **Noise gate** in the panel so the mouth stays shut when you are not speaking.
