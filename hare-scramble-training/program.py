"""4-week in-season hare scramble (GNCC / national-style) training program.

Single source of truth for the video slides, narration, and the printable plan.
Each slide: kind, on-screen content, and the narration line read by the voiceover.
"""

TITLE = "4-Week In-Season Hare Scramble Training Plan"
SUBTITLE = "GNCC / National-style off-road racer program"

# Weekly progression labels
WEEKS = ["WK 1 BUILD", "WK 2 BUILD+", "WK 3 PEAK", "WK 4 TAPER"]

SLIDES = [
    {
        "kind": "title",
        "title": "RACE SEASON\nTRAINING PLAN",
        "sub": "4 Weeks  |  Hare Scramble  |  GNCC-Style Off-Road",
        "say": "Race season is here. This is a four week, in-season training plan built for "
               "hare scramble and G N C C style off-road racing. Strength, squats, balance, "
               "grip, and running, all built around a weekend race.",
    },
    {
        "kind": "bullets",
        "title": "THE GOAL",
        "items": [
            "Hold attack position for 2 to 3 hours without fading",
            "Stronger legs = less arm pump (grip the bike with your knees)",
            "Engine for long climbs, woods sections, and restarts",
            "Balance and reaction for roots, rocks, and off-camber",
            "Show up FRESH on race day, not sore",
        ],
        "say": "The goal is simple. Hold attack position for two to three hours without fading. "
               "Strong legs mean less arm pump, because you grip the bike with your knees, not your hands. "
               "Build an engine for climbs and woods sections, sharpen balance for roots and off-camber, "
               "and most important, show up fresh on race day. In season, we train to race, not to get sore.",
    },
    {
        "kind": "schedule",
        "title": "YOUR WEEK",
        "rows": [
            ("MON", "RECOVERY", "30-40 min easy spin or walk + mobility"),
            ("TUE", "STRENGTH A", "Squats, legs, grip, balance"),
            ("WED", "RUN: ENGINE", "Race-pace intervals"),
            ("THU", "STRENGTH B", "Upper body, pulling, core, balance"),
            ("FRI", "RUN: EASY", "20-25 min easy + strides"),
            ("SAT", "RIDE / REST", "Light practice ride or travel day"),
            ("SUN", "RACE DAY", "Warm-up routine, then send it"),
        ],
        "say": "Here is your week. Monday is recovery. Tuesday is Strength A, squats, legs, grip, and balance. "
               "Wednesday is your engine run with race-pace intervals. Thursday is Strength B, upper body, "
               "pulling, and core. Friday is an easy run. Saturday is a light ride, or rest and travel. "
               "Sunday is race day. If you race Saturday, shift everything one day earlier.",
    },
    {
        "kind": "table",
        "title": "HOW THE 4 WEEKS PROGRESS",
        "cols": ["", "WK 1", "WK 2", "WK 3", "WK 4"],
        "rows": [
            ["Focus", "Build", "Build+", "Peak", "Taper"],
            ["Effort (RPE)", "7", "7-8", "8", "6"],
            ["Volume", "Normal", "+1 set", "Lower reps", "Half"],
            ["Run intervals", "6 x 2 min", "8 x 2 min", "5 x 3 min", "4 x 1 min"],
        ],
        "say": "Here is how the month progresses. Week one, build, at an effort of seven out of ten. "
               "Week two, add a set. Week three is the peak, heavier weight with fewer reps. "
               "Week four is the taper, cut the volume in half so you are sharp for the biggest race of the block.",
    },
    {
        "kind": "bullets",
        "title": "PICKING YOUR WEIGHTS",
        "items": [
            "RPE 7 = you could do 3 more reps. RPE 8 = 2 more reps.",
            "Never grind a rep to failure in season",
            "Starting guide, goblet squat: 35-55 lb DB",
            "Starting guide, back squat: bar + 50-60% bodyweight",
            "Bar speed slows or form breaks = drop 10%",
        ],
        "say": "How to pick your weights. We use R P E, rate of perceived exertion. Seven means you could "
               "do three more reps. Eight means two more. Never grind to failure in season. "
               "If you are new to lifting, start with a thirty five to fifty five pound dumbbell goblet squat. "
               "If you back squat, start around the bar plus half your bodyweight and work up. "
               "If the bar slows down or your form breaks, drop the weight ten percent.",
    },
    {
        "kind": "bullets",
        "title": "WARM-UP  (EVERY SESSION, 8 MIN)",
        "items": [
            "2 min jump rope or easy bike",
            "10 bodyweight squats, 10 walking lunges",
            "10 leg swings each way, each leg",
            "10 arm circles + 10 band pull-aparts",
            "5 slow inchworms to push-up",
        ],
        "say": "Every session starts with this eight minute warm-up. Two minutes of jump rope or easy bike. "
               "Ten bodyweight squats and ten walking lunges. Leg swings front to back and side to side. "
               "Arm circles and band pull-aparts. Then five slow inchworms into a push-up.",
    },
    # ---------------- STRENGTH A ----------------
    {
        "kind": "section",
        "title": "STRENGTH A",
        "sub": "Tuesday  |  Legs, Squats, Grip, Balance  |  45-50 min",
        "say": "Strength A. Tuesday. Legs, squats, grip, and balance. About forty five to fifty minutes.",
    },
    {
        "kind": "exercise",
        "tag": "A1",
        "title": "BACK SQUAT or GOBLET SQUAT",
        "weeks": ["3 x 6 @ RPE 7", "4 x 5 @ RPE 7-8", "3 x 4 @ RPE 8", "2 x 5 @ RPE 6"],
        "rest": "Rest 2-3 min",
        "cues": [
            "Feet shoulder width, toes slightly out",
            "Big breath, brace like you're landing a jump",
            "Sit down between your hips, knees track over toes",
            "Drive up hard. Controlled down, fast up",
        ],
        "say": "A one. The back squat, or goblet squat. Week one, three sets of six. Week two, four sets of five. "
               "Week three, three sets of four, heavier. Week four, two sets of five, light. "
               "Rest two to three minutes. Big breath, brace like you are landing a jump, sit between your hips, "
               "and drive up fast. This is the base of your attack position.",
    },
    {
        "kind": "exercise",
        "tag": "A2",
        "title": "ROMANIAN DEADLIFT (DB or BAR)",
        "weeks": ["3 x 8", "3 x 8", "3 x 6", "2 x 6"],
        "rest": "Rest 90 sec",
        "cues": [
            "Soft knees, push hips straight back",
            "Weight close to legs, flat back",
            "Stop when hamstrings are loaded",
            "Squeeze glutes to stand. Protects your lower back on the bike",
        ],
        "say": "A two. Romanian deadlift. Three sets of eight for the first two weeks, three sets of six in week three, "
               "two sets of six in the taper. Soft knees, push your hips back, keep the weight close and your back flat. "
               "This builds the hamstrings and lower back that hold you in position through whoops and braking bumps.",
    },
    {
        "kind": "exercise",
        "tag": "A3",
        "title": "BULGARIAN SPLIT SQUAT",
        "weeks": ["3 x 8 / leg", "3 x 10 / leg", "3 x 8 / leg (heavier)", "2 x 6 / leg"],
        "rest": "Rest 60-90 sec",
        "cues": [
            "Rear foot on a bench, front foot 2 ft forward",
            "Drop straight down, torso slightly forward",
            "Front knee stays stable, no caving in",
            "Hold DBs when bodyweight gets easy",
        ],
        "say": "A three. Bulgarian split squat. Rear foot up on a bench, drop straight down, front knee stable. "
               "Eight per leg in week one, ten per leg in week two, heavier eights in week three, and six per leg to taper. "
               "Single leg strength is what saves you when you dab a foot or get kicked off line.",
    },
    {
        "kind": "exercise",
        "tag": "A4",
        "title": "FARMER CARRY (GRIP + ARM PUMP)",
        "weeks": ["3 x 40 yd", "4 x 40 yd", "3 x 50 yd (heavier)", "2 x 40 yd"],
        "rest": "Rest 60 sec",
        "cues": [
            "Heavy DBs or kettlebells, crush the handles",
            "Tall posture, shoulders packed down",
            "Short fast steps, don't let them swing",
            "Open and shake hands between sets",
        ],
        "say": "A four. Farmer carry. Grab heavy dumbbells, crush the handles, stand tall, and walk forty yards. "
               "Three rounds in week one, four in week two, heavier fifty yard carries in week three, two to taper. "
               "Grip endurance is your first line of defense against arm pump.",
    },
    {
        "kind": "exercise",
        "tag": "A5",
        "title": "BALANCE: ATTACK POSITION HOLD",
        "weeks": ["3 x 30 sec", "3 x 40 sec", "3 x 45 sec", "2 x 30 sec"],
        "rest": "Rest 30 sec",
        "cues": [
            "Stand on a pillow, BOSU, or balance board",
            "Get in attack position: knees bent, elbows up, chin over bars",
            "Hold a broomstick like handlebars",
            "Partner nudges you: react and recover",
        ],
        "say": "A five. Balance, attack position hold. Stand on a pillow, a BOSU, or a balance board. "
               "Knees bent, elbows up, chin over the bars, holding a broomstick like handlebars. "
               "Thirty seconds, building to forty five. Have a buddy nudge you so you practice reacting and recovering.",
    },
    {
        "kind": "exercise",
        "tag": "A6",
        "title": "BALANCE: SINGLE-LEG RDL REACH",
        "weeks": ["2 x 8 / leg", "3 x 8 / leg", "3 x 8 / leg (hold DB)", "2 x 6 / leg"],
        "rest": "Rest 30 sec",
        "cues": [
            "Stand on one leg, slight knee bend",
            "Hinge forward and reach toward the floor",
            "Hips stay square, back leg straight behind you",
            "Slow and controlled. No hopping",
        ],
        "say": "A six. Single leg R D L reach. Stand on one leg, hinge forward, and reach for the floor while your back "
               "leg goes straight behind you. Keep the hips square and move slowly. This builds the ankle and hip "
               "stability you need on roots, rocks, and off-camber.",
    },
    # ---------------- RUN: ENGINE ----------------
    {
        "kind": "section",
        "title": "RUN: ENGINE",
        "sub": "Wednesday  |  Race-Pace Intervals  |  30-40 min",
        "say": "Wednesday. The engine run. Race-pace intervals. Thirty to forty minutes.",
    },
    {
        "kind": "table",
        "title": "WEDNESDAY INTERVALS",
        "cols": ["", "WARM-UP", "WORK", "RECOVER", "COOL-DOWN"],
        "rows": [
            ["WK 1", "10 min easy", "6 x 2 min HARD", "2 min walk/jog", "5 min easy"],
            ["WK 2", "10 min easy", "8 x 2 min HARD", "2 min walk/jog", "5 min easy"],
            ["WK 3", "10 min easy", "5 x 3 min HARD", "2 min walk/jog", "5 min easy"],
            ["WK 4", "10 min easy", "4 x 1 min HARD", "2 min walk/jog", "5 min easy"],
        ],
        "say": "Here are your intervals. Ten minute easy warm-up every time. Week one, six rounds of two minutes hard "
               "with two minutes easy. Week two, eight rounds. Week three, five rounds of three minutes hard. "
               "Week four, just four one minute efforts to stay sharp. Five minute cool-down.",
    },
    {
        "kind": "bullets",
        "title": "WHY INTERVALS WORK FOR OFF-ROAD",
        "items": [
            "Hard = 8 out of 10. You can say 2-3 words, not a sentence",
            "Mimics a hill climb or passing push, then settling back in",
            "Hills or trails? Even better. Run the ups hard",
            "Bad knees? Same intervals on a bike or rower",
            "Recover = keep moving. Don't stop and sit",
        ],
        "say": "Hard means eight out of ten. You can say two or three words, but not a full sentence. "
               "This copies what happens in a race: a hard push up a climb or to make a pass, then settling back in. "
               "Run hills or trails if you have them. If your knees are beat up, do the same intervals on a bike or rower. "
               "During recovery, keep moving. Don't stop and sit.",
    },
    # ---------------- STRENGTH B ----------------
    {
        "kind": "section",
        "title": "STRENGTH B",
        "sub": "Thursday  |  Upper Body, Pull, Core, Balance  |  40 min",
        "say": "Strength B. Thursday. Upper body, pulling, core, and balance. About forty minutes.",
    },
    {
        "kind": "exercise",
        "tag": "B1",
        "title": "PULL-UPS (or LAT PULLDOWN)",
        "weeks": ["3 x max -2", "4 x max -2", "4 x 5 (add weight)", "2 x 5"],
        "rest": "Rest 90 sec",
        "cues": [
            "Full hang to chin over the bar",
            "Pull elbows down to your ribs",
            "Stop 2 reps before failure",
            "Can't do one? Band-assisted or pulldown 3 x 10",
        ],
        "say": "B one. Pull-ups. Full hang to chin over bar, pulling your elbows down to your ribs. "
               "Stop two reps before failure. Three sets in week one, four in week two, add a little weight for fives "
               "in week three, and two easy sets to taper. If you can't do a pull-up, use a band or a lat pulldown.",
    },
    {
        "kind": "exercise",
        "tag": "B2",
        "title": "DB BENCH PRESS or PUSH-UPS",
        "weeks": ["3 x 10", "4 x 10", "3 x 8 (heavier)", "2 x 8"],
        "rest": "Rest 60-90 sec",
        "cues": [
            "Shoulder blades pinched back and down",
            "Lower slow, press fast",
            "Push-ups: body in a straight plank",
            "Builds the push to muscle the bike out of ruts",
        ],
        "say": "B two. Dumbbell bench press or push-ups. Shoulder blades pinched, lower slow, press fast. "
               "Tens for the first two weeks, heavier eights in week three, and two sets of eight to taper. "
               "This is the strength you use to muscle the bike out of ruts and pick it up after a get-off.",
    },
    {
        "kind": "exercise",
        "tag": "B3",
        "title": "ONE-ARM DB ROW",
        "weeks": ["3 x 10 / arm", "3 x 12 / arm", "3 x 8 / arm (heavier)", "2 x 8 / arm"],
        "rest": "Rest 60 sec",
        "cues": [
            "Hand and knee on a bench, flat back",
            "Pull the DB to your hip, not your chest",
            "Pause 1 sec at the top",
            "Balances out all the pushing and bar-holding",
        ],
        "say": "B three. One-arm dumbbell row. Flat back, pull the weight to your hip, and pause at the top. "
               "Tens, then twelves, then heavier eights, then an easy taper week.",
    },
    {
        "kind": "exercise",
        "tag": "B4",
        "title": "GRIP: DEAD HANG + TOWEL HANG",
        "weeks": ["3 x max hang", "3 x max hang", "3 x towel hang", "2 x 30 sec"],
        "rest": "Rest 60 sec",
        "cues": [
            "Hang from the pull-up bar, relaxed shoulders",
            "Week 3: drape 2 towels over the bar, grip those",
            "Log your time. Beat it next week",
            "Stretch forearms after: palm up and palm down",
        ],
        "say": "B four. Grip. Dead hang from the pull-up bar as long as you can. In week three, hang from two towels "
               "draped over the bar, which is much harder. Log your time and beat it. Stretch your forearms afterward.",
    },
    {
        "kind": "exercise",
        "tag": "B5",
        "title": "CORE CIRCUIT",
        "weeks": ["2 rounds", "3 rounds", "3 rounds", "2 rounds"],
        "rest": "Minimal rest between moves",
        "cues": [
            "Pallof press: 10 / side (anti-rotation)",
            "Dead bug: 10 / side, low back glued down",
            "Side plank: 30 sec / side",
            "Front plank in attack position: 45 sec",
        ],
        "say": "B five. Core circuit. Pallof press, ten per side. Dead bug, ten per side. Side plank, thirty seconds each side. "
               "Then a front plank for forty five seconds. Two rounds, then three, then three, then two to taper. "
               "Your core connects your legs to the bars. When it quits, your arms take over, and that is where pump starts.",
    },
    {
        "kind": "exercise",
        "tag": "B6",
        "title": "BALANCE: LATERAL BOUND + STICK",
        "weeks": ["3 x 5 / side", "3 x 6 / side", "3 x 6 / side", "2 x 4 / side"],
        "rest": "Rest 45 sec",
        "cues": [
            "Jump sideways off one leg, land on the other",
            "STICK the landing for a 2-count",
            "Knee soft and tracking over toes",
            "Trains quick reactions for dabs and off-camber saves",
        ],
        "say": "B six. Lateral bound and stick. Jump sideways off one leg, land on the other, and stick it for a two count "
               "with a soft knee. Five per side, building to six. This trains fast reactions for dabs and saves.",
    },
    # ---------------- FRI / MON ----------------
    {
        "kind": "bullets",
        "title": "FRIDAY: EASY RUN + OPENERS",
        "items": [
            "20-25 min EASY run. Full conversation pace",
            "Then 4 x 20-sec strides (fast, relaxed, not sprinting)",
            "10 min mobility: hips, hamstrings, forearms",
            "Hydrate all day. Aim for clear urine by Friday night",
            "Bed early. Friday's sleep matters most for Sunday",
        ],
        "say": "Friday. Easy run, twenty to twenty five minutes at conversation pace. Then four strides of twenty seconds, "
               "fast but relaxed. Ten minutes of mobility for hips, hamstrings, and forearms. "
               "Hydrate all day, and get to bed early. Friday night's sleep matters most for Sunday's race.",
    },
    {
        "kind": "bullets",
        "title": "MONDAY: RECOVERY",
        "items": [
            "30-40 min easy bike, walk, or swim",
            "Foam roll: quads, hamstrings, calves, lats",
            "Forearm and wrist stretches, 2 min each",
            "Note any tweaks from the race. Adjust Tuesday",
            "Big protein + carbs to rebuild",
        ],
        "say": "Monday is recovery. Thirty to forty minutes of easy bike, walking, or swimming. Foam roll your legs and lats. "
               "Stretch your forearms and wrists. Write down any tweaks from the race and adjust Tuesday's session if needed. "
               "Eat plenty of protein and carbs to rebuild.",
    },
    {
        "kind": "bullets",
        "title": "RACE-DAY WARM-UP  (15 MIN)",
        "items": [
            "5 min easy jog or jump rope",
            "Leg swings + walking lunges, 10 each",
            "3 x 10-sec sprints to raise heart rate",
            "Forearm squeezes + wrist circles, 1 min",
            "Finish 10-15 min before the start. Stay warm",
        ],
        "say": "Race day warm-up, fifteen minutes. Five minutes of easy jogging or jump rope. Leg swings and walking lunges. "
               "Three short ten second sprints to get your heart rate up, so the first lap isn't a shock. "
               "Then forearm squeezes and wrist circles. Finish ten to fifteen minutes before the start, and stay warm.",
    },
    {
        "kind": "bullets",
        "title": "FUEL + HYDRATION",
        "items": [
            "Protein: about 0.8-1 g per lb of bodyweight daily",
            "Race morning: carb-heavy breakfast 3 hrs before",
            "Hydration pack: sip every lap, add electrolytes",
            "2+ hr races: 30-60 g carbs per hour (gel, chews, drink mix)",
            "Post-race: protein + carbs within 1 hour",
        ],
        "say": "Fuel and hydration. Get about point eight to one gram of protein per pound of bodyweight every day. "
               "Eat a carb-heavy breakfast three hours before your start. Sip from your hydration pack every lap with electrolytes. "
               "For races over two hours, take in thirty to sixty grams of carbs per hour. "
               "Get protein and carbs within an hour after you finish.",
    },
    {
        "kind": "bullets",
        "title": "RULES FOR RACE SEASON",
        "items": [
            "No heavy legs within 72 hours of a race",
            "Sore or beat up? Cut the session in half, don't skip it",
            "Crashed hard? Skip Strength A that week",
            "Sleep 8 hours. It's the best recovery tool you have",
            "Track your lifts and lap times. What gets measured improves",
        ],
        "say": "Rules for race season. No heavy leg work within seventy two hours of a race. If you are sore or beat up, "
               "cut the session in half instead of skipping it. If you crashed hard, skip Strength A that week and focus on recovery. "
               "Sleep eight hours. And track your lifts and lap times, because what gets measured improves.",
    },
    {
        "kind": "bullets",
        "title": "SAFETY FIRST",
        "items": [
            "This is general fitness info, not medical advice",
            "Check with your doctor before starting a new program",
            "Sharp pain, dizziness, or chest pain = stop immediately",
            "Learn squat form with light weight or a coach first",
            "Use a spotter or safety bars for heavy squats",
        ],
        "say": "A quick safety note. This is general fitness information, not medical advice. Check with your doctor before "
               "starting any new program. If you feel sharp pain, dizziness, or chest pain, stop right away. "
               "Learn squat form with light weight first, and use a spotter or safety bars when you go heavy.",
    },
    {
        "kind": "title",
        "title": "SEE YOU AT\nTHE FINISH",
        "sub": "Screenshot the weekly plan  |  Train smart  |  Race hard",
        "say": "That's the plan. Four weeks, built around your race weekend. Screenshot the weekly schedule, "
               "track your numbers, and I'll see you at the finish. Train smart, race hard.",
    },
]
