/* ==========================================================================
   Los Gatos Math Circle. Newsletter issues
   --------------------------------------------------------------------------
   Each issue: slug, number, title, date, image, alt, tags, views, excerpt, body.
   Math uses TeX ($...$ inline, $$...$$ display); double the backslashes here.
   Issues render newest-first by date. No two bodies share the same structure.
   ========================================================================== */

const ISSUES = [
  {
    slug: "year-end-marathon",
    number: 40,
    title: "A year-end problem marathon",
    date: "2026-06-06",
    image: "images/mathclub.jpg",
    alt: "The Los Gatos Math Circle gathered together.",
    tags: ["Meeting recap", "Community"],
    views: 214,
    likes: 14,
    excerpt:
      "Last meeting of the year. Cookies, a relay of everyone's favorite problems, and one infinite sum that nobody could stop arguing about.",
    body: `
<p>Well, that's a wrap on the year. For the last meeting we skipped the lesson plan
entirely and just did what we love: everybody brought one favorite problem, we threw
them in a hat, and we passed them around the room in mixed teams until every
whiteboard was full.</p>

<p>The one that wouldn't die was this:</p>

$$S = \\tfrac{1}{2} + \\tfrac{1}{4} + \\tfrac{1}{8} + \\tfrac{1}{16} + \\cdots$$

<p>One table kept adding terms, getting closer and closer to 1 but never landing.
Another table just wrote $S = \\tfrac12 + \\tfrac12 S$ and solved for $S = 1$ in about
four seconds. Both tables were sure the other was missing the point. They were both
right, which is the best kind of argument to referee.</p>

<p>Thanks to everyone who came this year and kept the whiteboards full. Team tryouts are
open all summer (the problem set is on the team page). See you in September.</p>
`,
  },

  {
    slug: "power-of-a-point",
    number: 39,
    title: "Circles, secants, and the power of a point",
    date: "2026-05-09",
    image: "images/news/geometry-2.jpg",
    alt: "A geometric model.",
    tags: ["Meeting recap", "Geometry"],
    views: 96,
    likes: 17,
    excerpt:
      "One theorem about circles that quietly solves a dozen contest problems. We built up to it slowly.",
    body: `
<p>Here is how the morning went, step by step.</p>
<p><strong>First,</strong> we drew a circle and a point $P$ outside it, then a few
different lines through $P$ that cut the circle at two spots each. Everyone measured
the two pieces and multiplied them.</p>
<p><strong>Then</strong> the room went quiet, because the products all came out equal.
Every line. That's the power of a point:</p>
$$PA \\cdot PB = PC \\cdot PD.$$
<p><strong>Next,</strong> we slid one line until it just grazed the circle. Now the two
intersection points merge into a single tangent point $T$, and the rule becomes</p>
$$PT^2 = PA \\cdot PB.$$
<p><strong>Finally,</strong> we tried it on an old contest problem that had stumped a
few people back in the fall. Tangent of length 6, a secant whose far point is 9 away,
find the near point $x$: just solve $6^2 = 9x$, so $x = 4$. Three lines of work where
we used to flail.</p>
<p>Homework: two circles cross at $X$ and $Y$. Show every point on line $XY$ has equal
tangent lengths to both circles.</p>
`,
  },

  {
    slug: "a-sum-that-looks-scary",
    number: 38,
    title: "Problem of the month: a sum that looks scary",
    date: "2026-04-11",
    image: "images/writing-math.jpg",
    alt: "A hand writing equations on a blackboard.",
    tags: ["Problem of the month", "Algebra"],
    views: 351,
    likes: 67,
    excerpt:
      "Ninety-nine fractions to add. Don't reach for a common denominator. There's a one-line trick.",
    body: `
<blockquote>Find $\\displaystyle\\sum_{n=1}^{99} \\frac{1}{n(n+1)}
= \\frac{1}{1\\cdot 2} + \\frac{1}{2\\cdot 3} + \\cdots + \\frac{1}{99\\cdot 100}.$</blockquote>
<p>Stop here and try it before you read on. Really. The whole point is the moment it
clicks.</p>
<p>Ready? The move is to notice that every single term is secretly a subtraction:</p>
$$\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}.$$
<p>Write the sum out with that and watch the middle collapse like a closing
telescope:</p>
$$\\left(\\tfrac11-\\tfrac12\\right)+\\left(\\tfrac12-\\tfrac13\\right)+\\cdots+\\left(\\tfrac{1}{99}-\\tfrac{1}{100}\\right)
= 1 - \\tfrac{1}{100} = \\tfrac{99}{100}.$$
<p>That's it. No common denominator, no calculator. When a student in the back saw the
interior terms cancel, she actually laughed out loud, which is exactly the right
reaction.</p>
<p>If that was fun, try the same trick on $\\sum \\frac{1}{n(n+1)(n+2)}$ and send us
what you get.</p>
`,
  },

  {
    slug: "bridges-graphs-euler",
    number: 37,
    title: "The town you can't walk through",
    date: "2026-03-21",
    image: "images/news-a.jpg",
    alt: "Students working on a problem.",
    tags: ["Meeting recap", "Graph theory"],
    views: 131,
    likes: 13,
    excerpt:
      "Königsberg had seven bridges and a puzzle that drove people crazy for years. Euler ended it with a single observation.",
    body: `
<p>Picture an old city split by a river into four chunks of land, stitched together by
seven bridges. For years people tried to take a walk that crossed every bridge exactly
once, and for years everyone failed. The question that mattered, the one Euler asked in
1736, was not "how do I do it" but "is it even possible."</p>
<p>His trick was to throw away almost everything. Forget the river, the distances, the
shape of the land. Shrink each landmass to a dot and each bridge to a line. All that
survives is which dots connect to which, and suddenly the whole puzzle fits on an index
card.</p>
<p>Then comes the kill shot. If you're going to use every bridge once, then every time
you walk onto a piece of land you also have to walk off it, pairing the bridges up two
at a time. So a piece of land in the middle of your walk needs an even number of
bridges. Only your start and your finish are allowed to be odd.</p>
<p>In Königsberg, all four landmasses had an odd number of bridges. Four odd spots, when
the most you can ever have is two. Not hard, just impossible, and that distinction is
the whole birth of graph theory.</p>
<p>To take home: which capital letters can you draw without lifting your pen?</p>
`,
  },

  {
    slug: "competition-season-notes",
    number: 36,
    title: "What I actually want you to get out of contests",
    date: "2026-03-07",
    image: "images/usa/u05.jpg",
    alt: "Students at a mathematics competition.",
    tags: ["Competitions", "Team"],
    views: 178,
    likes: 23,
    excerpt:
      "It's competition season, so let me say the unpopular thing: the score is the least interesting part.",
    body: `
<p>Every spring a handful of students ask me whether they're "good enough" to sit the
AMC. I always want to push back on the question itself, so let me do it here.</p>
<p>Yes, we point toward real contests. The AMC 10 and 12 in the fall, the AIME after
that, then ARML in the spring. Each one rewards something a little different, and
preparing as a group is genuinely useful.</p>
<p>But here is a problem we drilled this month, and I want you to watch what the lesson
actually was:</p>
<p>How many ordered pairs of positive integers $(x,y)$ satisfy
$\\frac1x + \\frac1y = \\frac{1}{12}$? Clear the fractions and it rearranges into
$(x-12)(y-12) = 144$. Now every way of factoring $144 = 2^4\\cdot 3^2$ gives a pair, and
since it has $15$ divisors, there are $15$ pairs.</p>
<p>The answer is 15. Nobody will remember that next week. What I want you to keep is the
move: a scary fraction equation became a factoring problem the second we stopped
panicking and rearranged. That habit outlives every score, and it's the only reason I
care about contests at all.</p>
`,
  },

  {
    slug: "himcm-results-2025",
    number: 35,
    title: "HiMCM results are in, and we're Finalists",
    date: "2026-02-14",
    image: "images/usa/u04.jpg",
    alt: "An exhibit at the National Museum of Mathematics.",
    tags: ["Competitions", "HiMCM"],
    views: 884,
    likes: 164,
    excerpt:
      "Our modeling team earned a Finalist designation on Problem B of the 2025 HiMCM. Here's the short version.",
    body: `
<p>The news we've been waiting on all winter: our team earned a <strong>Finalist</strong>
designation, the top award tier, on Problem B of the 2025 High School Mathematical
Contest in Modeling, competing as Team&nbsp;#17561.</p>
<p>If you haven't seen HiMCM before: it's not a timed test. Over a long November weekend
a team picks an open, messy, real-world question, builds a mathematical model of it, and
writes the whole thing up as a paper. There's no answer key.</p>
<p>What lifted the paper, in the judges' world, was the sensitivity analysis: showing the
recommendation still held up when the inputs were nudged by ten percent. A correct model
that falls apart under a small push doesn't earn much. A robust one does.</p>
<div class="note">
  <span class="label">The result</span>
  Finalist, Problem B, Team #17561. Results are published by COMAP, which has run HiMCM
  since 1999.
</div>
<p>Congratulations to the team, and thank you to everyone who showed up to the fall
workshops to argue about assumptions. Want to be on next year's team? The
<a href="team.html">team page</a> has the tryout set.</p>
`,
  },

  {
    slug: "pascals-triangle",
    number: 34,
    title: "Five things hiding in Pascal's triangle",
    date: "2026-01-24",
    image: "images/tamu/t10.jpg",
    alt: "Students working at a math circle.",
    tags: ["Meeting recap", "Combinatorics"],
    views: 147,
    likes: 13,
    excerpt:
      "A triangle of numbers you could doodle in a boring class turns out to be a map of half of combinatorics.",
    body: `
<p>We spent the whole morning on one triangle, the one where each number is the sum of
the two above it. Here is what fell out of it.</p>
<ol>
  <li><strong>It's all choosing.</strong> The entry in row $n$, slot $k$, is exactly
  $\\binom{n}{k}$. The build rule is the story of "include the last person or don't":
  $\\binom{n}{k} = \\binom{n-1}{k-1} + \\binom{n-1}{k}$.</li>
  <li><strong>Rows are powers of two.</strong> $\\sum_k \\binom{n}{k} = 2^n$, because each
  item is in or out.</li>
  <li><strong>Triangular numbers</strong> sit in the third diagonal: 1, 3, 6, 10, 15.</li>
  <li><strong>Fibonacci hides</strong> in the shallow diagonals. Nobody believed this
  until we added them up.</li>
  <li><strong>Color the odd entries</strong> and you get a fractal, the Sierpinski
  triangle. We ran out of time before finishing the coloring, so that's homework.</li>
</ol>
<p>The thread through all five: the same number counts many different things. Half of
combinatorics is just finding a second story for $\\binom{n}{k}$.</p>
`,
  },

  {
    slug: "new-term-new-members",
    number: 33,
    title: "A note to the new faces",
    date: "2026-01-10",
    image: "images/hero.jpg",
    alt: "The Los Gatos Math Circle.",
    tags: ["Welcome", "About"],
    views: 192,
    likes: 22,
    excerpt:
      "Winter term started, and we had a good crowd of new students. Here's the short version of how we do things.",
    body: `
<p>Dear new members,</p>
<p>Welcome. If this was your first Saturday with us, you probably noticed we don't
lecture much. We hand you a problem that looks simple and then get out of the way. That
is the whole method.</p>
<p>The puzzle we opened with: you have a chocolate bar that's an $m \\times n$ grid of
squares, and each snap breaks one piece along a straight line into two. How many snaps to
reduce the bar to single squares? People guessed all over the place until someone noticed
that each snap turns one piece into two, so every snap adds exactly one piece. You start
with one and want $mn$, so you always need $mn - 1$ snaps, no matter how you break it.</p>
<div class="note">
  <span class="label">The essentials</span>
  Saturdays, 10 to noon, in the Teen Section of the Los Gatos Library. Drop in any week.
  Bring a pencil. No sign-up needed for a first visit.
</div>
<p>You do not need to be a "math person," whatever that means. You need to be willing to
be stuck for a few minutes without panicking. That's it. See you Saturday.</p>
`,
  },

  {
    slug: "clock-math-modular-arithmetic",
    number: 32,
    title: "What's the last digit of 7 to the 100th?",
    date: "2025-12-06",
    image: "images/tamu/t07.jpg",
    alt: "Students at a math circle session.",
    tags: ["Meeting recap", "Number theory"],
    views: 118,
    likes: 22,
    excerpt:
      "No calculator big enough exists for this. Good thing you don't need one.",
    body: `
<blockquote>What is the last digit of $7^{100}$?</blockquote>
<p>We started here, and the first reaction was the usual one: reach for a calculator.
Except $7^{100}$ has 85 digits, so that's out. You have to actually think.</p>
<p>The key is that "the last digit" just means the value mod 10, and we only need to
track that. Watch the powers of 7:</p>
$$7^1\\equiv 7,\\quad 7^2\\equiv 9,\\quad 7^3\\equiv 3,\\quad 7^4\\equiv 1 \\pmod{10}.$$
<p>And then it loops: $7^5$ is back to 7. The last digits cycle $7, 9, 3, 1$ with period
four. Since $100 = 4 \\times 25$ lands exactly at the end of a cycle,
$7^{100}\\equiv 1\\pmod{10}$. The last digit is <strong>1</strong>.</p>
<p>That "wrap around and look for a cycle" idea is the whole reason clock arithmetic
matters. Earlier in the session we'd warmed up on the actual clock (what time is it 100
hours from now?), and this is the same trick wearing a fancier hat.</p>
<p>Take it home: show $n^5 - n$ is always a multiple of 10.</p>
`,
  },

  {
    slug: "a-stubborn-number-puzzle",
    number: 31,
    title: "The number puzzle that ate the whole hour",
    date: "2025-11-22",
    image: "images/usa/u06.jpg",
    alt: "A slide rule.",
    tags: ["Meeting recap", "Number theory"],
    views: 79,
    likes: 14,
    excerpt:
      "Some Saturdays a single problem just takes over the room. This was one of them.",
    body: `
<p>I had a whole plan for this meeting. We got through about a third of it, because one
problem grabbed the room by the collar and would not let go.</p>
<p>Here it is: find all positive integers $n$ such that $n + 1$ divides $n^2 + 1$.</p>
<p>The first ten minutes were pure flailing, people just plugging in numbers. $n = 1$
works. $n = 3$ works. Then nothing for a while, which is suspicious. Around the
twenty-minute mark someone tried the trick that always feels like cheating: rewrite the
top so the bottom appears. Since $n^2 + 1 = (n^2 - 1) + 2 = (n-1)(n+1) + 2$, the part
that matters is just the leftover 2. So $n+1$ has to divide 2.</p>
<p>That means $n + 1$ is 1 or 2, giving $n = 1$ as the only positive answer. Wait, but
$n = 3$ worked too? That sent us back to the board, where we found an arithmetic slip
from the flailing phase. The clean argument wins.</p>
<p>We never got to the rest of my plan. I am not even a little sorry.</p>
`,
  },

  {
    slug: "how-big-is-a-million",
    number: 30,
    title: "How big is a million, really?",
    date: "2025-11-01",
    image: "images/news-b.jpg",
    alt: "A student working through a problem.",
    tags: ["Meeting recap", "Estimation"],
    views: 206,
    likes: 17,
    excerpt:
      "No formulas this week. Just the surprisingly useful art of guessing well.",
    body: `
<p>Quick one this week, and a fun one. We spent the morning on estimation, the skill of
getting an answer that's roughly right when an exact answer is hopeless.</p>
<p>Warm-up: how long would it take to count out loud to a million, one number a second,
no breaks? A million seconds is about $10^6$ seconds, and a day is roughly $86{,}400$,
call it $10^5$. So you're looking at around ten days of nonstop counting. People are
always surprised it's that long.</p>
<p>Then the classic: how many piano tuners work in a big city? You chain together
guesses you can actually make. Population, how many households own a piano, how often it
gets tuned, how many a tuner does in a day. Multiply it all out and you land within a
factor of a few of the real number, which is wild given that you made every piece up.</p>
<p>The point isn't piano tuners. It's that a quick estimate tells you instantly whether a
fancier calculation is even in the right ballpark, and that habit will save you on every
hard problem you ever meet.</p>
`,
  },

  {
    slug: "pigeonhole-principle",
    number: 29,
    title: "Too many pigeons",
    date: "2025-10-18",
    image: "images/pigeonhole.jpg",
    alt: "An illustration of the pigeonhole principle.",
    tags: ["Meeting recap", "Combinatorics"],
    views: 163,
    likes: 29,
    excerpt:
      "If you have more pigeons than holes, some hole has two. The whole session grew from that silly sentence.",
    body: `
<p>The principle is almost insultingly obvious, so we spent the hour being surprised by
it anyway. Three problems, increasing in slyness:</p>
<ol>
  <li><strong>The easy one.</strong> Among any 13 people, two share a birth month. Twelve
  months, thirteen people, done.</li>
  <li><strong>The one that took real thought.</strong> In any group, two people have the
  exact same number of friends inside the group. (Hint: how many friend-counts are even
  possible, and why can't you have both 0 and "everyone" at once?)</li>
  <li><strong>The pretty one.</strong> Drop five points anywhere in a $1\\times 1$ square.
  Two of them are within $\\frac{\\sqrt2}{2}$ of each other. Slice the square into four
  little squares; five points, four boxes, so two share a box, and the farthest apart they
  can be in there is the diagonal.</li>
</ol>
<p>The real skill, the thing nobody hands you, is choosing what the "holes" should be. In
problem three the holes were quarters of the square. Inventing them is the entire move.</p>
<p>Homework: from any 51 numbers chosen out of 1 to 100, show two of them are coprime.</p>
`,
  },

  {
    slug: "invariants-what-stays-the-same",
    number: 28,
    title: "What never changes",
    date: "2025-10-04",
    image: "images/chessboard.jpg",
    alt: "A chessboard.",
    tags: ["Meeting recap", "Invariants"],
    views: 84,
    likes: 18,
    excerpt:
      "A coin puzzle, a chessboard, and the trick of hunting for the one thing that can't move.",
    body: `
<p>"Can you get all 25 coins to show tails?" That was the whole prompt. Twenty-five coins
start heads up, and a move means flipping exactly two of them. Students flipped away for a
while, getting close, never quite there.</p>
<p>"Wait," someone finally said, "the number of heads only ever changes by two." Right. You
flip two coins, so the head count goes up by 2, down by 2, or stays put. It always keeps
the same parity.</p>
<p>"And we start at 25, which is odd." Exactly. All tails means zero heads, which is even.
You can't get from odd to even by only adding and subtracting twos. So it's flat-out
impossible, no matter how clever your flipping.</p>
<p>That's an invariant: a quantity the rules simply cannot change. Find one, and you can
rule out whole goals without trying a single case. We closed with the famous chessboard
version (cut two opposite corners, try to tile with dominoes, watch the colors refuse to
balance).</p>
<p>To go: numbers 1 through 2025 on a board, replace any two with their difference,
repeat. Show the last number standing is even.</p>
`,
  },

  {
    slug: "art-of-counting",
    number: 27,
    title: "Counting without counting",
    date: "2025-09-20",
    image: "images/tamu/t09.jpg",
    alt: "Students at a math circle session.",
    tags: ["Meeting recap", "Combinatorics"],
    views: 121,
    likes: 13,
    excerpt:
      "When a set is too big to count one by one, the smart move is to never count it directly.",
    body: `
<blockquote>How many shortest paths go from one corner of a $4 \\times 7$ city grid to the
opposite corner, if you can only walk right or up?</blockquote>
<p>You could try to draw them all. Don't. Every shortest path is just a sequence of 7
"rights" and 4 "ups" in some order, and once you decide which of the 11 steps are the
ups, the whole path is locked in.</p>
<p>So the count is just the number of ways to choose 4 positions out of 11:</p>
$$\\binom{11}{4} = 330.$$
<p>We'd warmed up with handshakes (everyone in a room of $n$ shakes hands once, that's
$\\binom{n}{2}$ because each handshake gets counted from both sides). Same idea both
times: a nasty "how many arrangements" question turns easy the second you find the right
thing to choose.</p>
<p>The hard follow-up we left on the board: how many of those grid paths never cross above
the diagonal? That answer has a name, and we'll get to it.</p>
`,
  },

  {
    slug: "a-new-year-of-problems",
    number: 26,
    title: "A new year, and a bigger room",
    date: "2025-09-06",
    image: "images/tamu/t01.jpg",
    alt: "Students at a math circle session.",
    tags: ["Meeting recap", "Community"],
    views: 168,
    likes: 28,
    excerpt:
      "We kicked off the school year in a new home, the Teen Section, with a puzzle about a thousand lockers.",
    body: `
<p>Third year, new digs. After two years crammed into a borrowed community room, we've
moved into the Teen Section of the library, which means more tables and more whiteboard.
We filled all of it on day one.</p>
<p>The opener was the locker problem, the kind of thing that sounds like a riddle and
turns into real number theory. A thousand lockers, all shut, and a thousand students.
Student 1 opens every locker. Student 2 toggles every second one. Student 3 every third,
and so on down the line. When the dust settles, which lockers are open?</p>
<p>The trick is to ask how many times a given locker gets touched. Locker $n$ is toggled
once for each of its divisors, and divisors come in pairs ($d$ and $n/d$), so the count
is usually even and the locker ends shut. The exceptions are perfect squares, where one
divisor pairs with itself and the count is odd. Since $31^2 = 961$ and $32^2 = 1024$,
exactly 31 lockers stay open.</p>
<p>Nobody believed 31 until we listed the first few. That's a good first day.</p>
`,
  },

  {
    slug: "two-years-in",
    number: 25,
    title: "Two years in",
    date: "2025-05-24",
    image: "images/newsletter-feature.jpg",
    alt: "The Los Gatos Math Circle.",
    tags: ["Community", "About"],
    views: 243,
    likes: 15,
    excerpt:
      "We started with five kids and a borrowed table. A letter on where things stand.",
    body: `
<p>Hi everyone,</p>
<p>Two years ago this circle was five students, two mentors, and a table we borrowed in
the corner of the library. We genuinely weren't sure anyone would come back for week two.
They did, and then their friends did, and now most Saturdays we're hunting for chairs.</p>
<p>This year we fielded our first HiMCM team, ran our first real ARML practice block, and
sent several members on to the AIME. Those are nice. But the moment I keep replaying is a
seventh grader who barely spoke all fall walking to the board in April and explaining an
invariant argument better than I could have. The room got it because she got it.</p>
<p>That's the whole thing, honestly. Not the trophies, the room.</p>
<p>We move up to the Teen Section in the fall, which means more space and a few more
seats. Bring a friend, and thank you all for showing up week after week.</p>
<p>See you in September.</p>
`,
  },

  {
    slug: "getting-ready-for-arml",
    number: 24,
    title: "Relay practice is controlled chaos",
    date: "2025-04-12",
    image: "images/arml.jpg",
    alt: "Our team at an ARML competition.",
    tags: ["Competitions", "Team", "ARML"],
    views: 201,
    likes: 42,
    excerpt:
      "ARML is a team sport, so we practiced it like one, relay rounds and all.",
    body: `
<p>Saturday was loud. ARML is built for teams, and the relay rounds are the part everyone
remembers, so we ran a few of our own and let me tell you, the energy is completely
different from a quiet contest.</p>
<p>Here's how a relay works: you sit in a line of three. The first person solves a problem
and passes their answer back. The second person can't even start until that answer
arrives, because it's an input to their problem. One careless slip at the front poisons
the entire line, and you can watch the panic travel backward in real time.</p>
<p>A taste of one step: you receive a number $T$, and your problem says a rectangle has
perimeter $T$ and is twice as long as it is wide; find its area. With $T = 36$, the width
is 6, the length 12, the area 72. Easy alone. Stressful when two teammates are staring at
you and the clock is loud.</p>
<p>What we actually drilled wasn't the math. It was passing answers clearly, double-checking
before you hand anything off, and trusting the person in front of you instead of
re-solving their problem in your head. That trust is the whole game.</p>
`,
  },

  {
    slug: "euclid-and-gcd",
    number: 23,
    title: "Euclid's two-thousand-year-old shortcut",
    date: "2025-03-22",
    image: "images/usa/u09.jpg",
    alt: "A slide rule.",
    tags: ["Meeting recap", "Number theory"],
    views: 73,
    likes: 8,
    excerpt:
      "How do you find a greatest common divisor fast? Not by listing every divisor, it turns out.",
    body: `
<p>Ask a room how to find the greatest common divisor of two numbers and almost everyone
says the same thing: list all the divisors of each and find the biggest one they share.
That works. It's also painfully slow for big numbers, and we raced it to prove the point.</p>
<p>Euclid's idea, older than algebra, is one observation: any common divisor of two numbers
also divides their remainder when you divide one by the other. So you just keep replacing
the bigger number with that remainder. Watch it chew through $\\gcd(252, 105)$:</p>
$$252 = 2\\cdot 105 + 42,\\qquad 105 = 2\\cdot 42 + 21,\\qquad 42 = 2\\cdot 21 + 0.$$
<p>The last nonzero remainder, 21, is the answer. Three steps. The student doing it by
listing divisors was still going when the Euclid team finished.</p>
<p>The reason it matters far beyond the classroom: this exact loop is what reduces fractions
and what keeps your messages private online. To go: show that $n$ and $n+1$ are always
coprime.</p>
`,
  },

  {
    slug: "counting-two-ways",
    number: 22,
    title: "Why counting twice is a superpower",
    date: "2025-03-08",
    image: "images/tamu/t08.jpg",
    alt: "Students working at a math circle.",
    tags: ["Meeting recap", "Combinatorics"],
    views: 88,
    likes: 9,
    excerpt:
      "Count the same thing two different ways and the two answers have to match. That forced equality proves a startling amount.",
    body: `
<p>I'll admit this idea sounded too obvious to be useful when I first met it, and then it
kept solving things, so now I respect it. Here it is: if you count one collection in two
different ways, the two counts are equal, full stop.</p>
<p>The example that won the room over: pick a committee of $k$ people from $n$, then choose
one of them to be chair. Count it as committee-first ($\\binom{n}{k}$ ways, then $k$ choices
of chair), or as chair-first ($n$ choices, then $\\binom{n-1}{k-1}$ for the rest). Same set
of outcomes, so</p>
$$k\\binom{n}{k} = n\\binom{n-1}{k-1}.$$
<p>We checked it on tiny numbers to be sure nobody was being tricked: for $n=4, k=2$ the
left side is $2\\cdot 6 = 12$ and the right is $4\\cdot 3 = 12$. No algebra, just two honest
counts that were forced to agree.</p>
<p>What I like about this is how little machinery it needs. You don't manipulate symbols,
you just describe one thing carefully from two angles and let the equality fall out. Try it
on $\\sum_k \\binom{n}{k} = 2^n$: what is each side counting?</p>
`,
  },

  {
    slug: "sums-of-squares",
    number: 21,
    title: "Where did 204 come from?",
    date: "2025-02-22",
    image: "images/news/blackboard-1.jpg",
    alt: "A classroom blackboard.",
    tags: ["Meeting recap", "Algebra"],
    views: 104,
    likes: 21,
    excerpt:
      "Months ago we counted 204 squares on a chessboard. This week we finally explained the number.",
    body: `
<p><strong>Q: Wasn't 204 just a random total from that chessboard problem?</strong></p>
<p>Not random at all. The squares on an $8\\times 8$ board, counting every size from $1\\times1$
up to $8\\times8$, come to $1^2 + 2^2 + \\cdots + 8^2$. So the real question is whether there's
a clean formula for the sum of the first $n$ squares.</p>
<p><strong>Q: Is there?</strong></p>
<p>There is, and it looks like it fell out of the sky:</p>
$$1^2 + 2^2 + \\cdots + n^2 = \\frac{n(n+1)(2n+1)}{6}.$$
<p>Plug in $n = 8$: that's $\\frac{8\\cdot 9\\cdot 17}{6} = 204$. Right on the nose.</p>
<p><strong>Q: How do you prove it?</strong></p>
<p>By induction, which a few people were seeing for the first time. Check $n=1$, assume it
for $n$, add $(n+1)^2$ to both sides, and watch it simplify into the same formula with $n+1$
in place of $n$. The moment the algebra closed up was very satisfying.</p>
<p><strong>Q: Homework?</strong></p>
<p>Find a formula for $1^3 + 2^3 + \\cdots + n^3$ and notice what it equals. It's prettier
than you'd expect.</p>
`,
  },

  {
    slug: "contest-season-2025",
    number: 20,
    title: "Contest season notes, and a first piece of HiMCM news",
    date: "2025-02-08",
    image: "images/usa/u02.jpg",
    alt: "A college mathematics class.",
    tags: ["Competitions", "Team"],
    views: 167,
    likes: 24,
    excerpt:
      "AMC done, AIME ahead, and our first-ever modeling team came home with an Honorable Mention.",
    body: `
<p>Busy stretch. The AMC is behind us, the AIME is next, and our first-ever HiMCM team
earned an <strong>Honorable Mention</strong> on their debut, which for a group that had
never written a modeling paper is a real result.</p>
<p>One problem from our AMC drills, because it taught a habit worth keeping: how many
four-digit numbers have digits that add to 4? Set $e = d_1 - 1$ so the leading digit can be
zero like the others, and you need $e + d_2 + d_3 + d_4 = 3$ in nonnegative integers. That's
stars and bars: $\\binom{6}{3} = 20$.</p>
<p>The lesson wasn't the 20. It was the substitution. When a constraint is in your way (here,
"the first digit can't be zero"), change variables until it disappears.</p>
<p>AIME prep starts in earnest next week. If you want in on the practice block, grab a mentor
on Saturday.</p>
`,
  },

  {
    slug: "inscribed-angles",
    number: 19,
    title: "Why a triangle in a semicircle is always right",
    date: "2025-01-25",
    image: "images/news/geometry-3.jpg",
    alt: "Basic geometric shapes.",
    tags: ["Meeting recap", "Geometry"],
    views: 92,
    likes: 14,
    excerpt:
      "One fact about circles that disguises itself inside a dozen 'find the angle' problems.",
    body: `
<p>Short session, one big idea: the inscribed angle theorem. An angle drawn from a point on
a circle is exactly half the central angle that stands on the same arc.</p>
<p>The consequence everyone loves: take the arc to be a half-circle. The central angle is a
straight $180^\\circ$, so any inscribed angle on it is $90^\\circ$. That's why a triangle with
one side as the diameter of a circle always has a right angle at the top, no matter where you
slide that top point. We passed a ruler around so people could check it themselves, which is
more convincing than any proof.</p>
<p>Once you've seen it, you can't unsee it. A surprising number of "find the angle" contest
problems are just this theorem wearing a costume.</p>
<p>To take home: prove that opposite angles of any four-sided figure inscribed in a circle add
up to $180^\\circ$.</p>
`,
  },

  {
    slug: "vieta-formulas",
    number: 18,
    title: "Knowing a polynomial's roots without finding them",
    date: "2025-01-11",
    image: "images/news2/m16.jpg",
    alt: "A slide rule.",
    tags: ["Meeting recap", "Algebra"],
    views: 133,
    likes: 28,
    excerpt:
      "It feels like cheating the first time you see it. You can talk about the roots without ever solving for them.",
    body: `
<blockquote>The roots of $x^2 - 5x + 6$ add to what, and multiply to what?</blockquote>
<p>You could factor it into $(x-2)(x-3)$ and read off 2 and 3, so the sum is 5 and the
product is 6. But notice those numbers were sitting in the original equation the whole time:
the 5 and the 6.</p>
<p>That's Vieta's formulas. For any quadratic $x^2 - sx + p$ with roots $r_1, r_2$, you get</p>
$$r_1 + r_2 = s, \\qquad r_1 r_2 = p,$$
<p>just by expanding $(x - r_1)(x - r_2)$ and matching coefficients. No quadratic formula
required.</p>
<p>Why care? Because plenty of contest problems ask for things like the sum of the squares of
the roots, and you can get those straight from $s$ and $p$ without ever finding ugly roots.
For instance $r_1^2 + r_2^2 = (r_1+r_2)^2 - 2r_1 r_2 = s^2 - 2p$.</p>
<p>Try it: if the roots sum to 5 and multiply to 6, find $r_1^2 + r_2^2$ in your head.</p>
`,
  },

  {
    slug: "casting-out-nines",
    number: 17,
    title: "The bookkeeper's error-check",
    date: "2024-12-07",
    image: "images/news2/m20.jpg",
    alt: "A slide rule.",
    tags: ["Meeting recap", "Number theory"],
    views: 110,
    likes: 10,
    excerpt:
      "Before calculators, clerks caught arithmetic slips in seconds with a trick that's secretly modular arithmetic.",
    body: `
<p>Let me walk you through the trick exactly the way we did on Saturday.</p>
<p><strong>Step one:</strong> take any number and add its digits, over and over, until you're
down to a single digit. For $1233$ that's $1+2+3+3 = 9$. That single digit is the number's
remainder mod 9 (with 9 standing in for 0).</p>
<p><strong>Step two:</strong> here's why it works. Since $10 \\equiv 1 \\pmod 9$, every power of
10 also leaves remainder 1, so a number and its digit sum have the same remainder mod 9. That's
the whole secret.</p>
<p><strong>Step three:</strong> use it to check a multiplication. Say you computed
$123 \\times 11 = 1353$. Reduce each side: $123 \\to 6$, $11 \\to 2$, and $6 \\times 2 = 12 \\to 3$.
Now check the answer: $1353 \\to 1+3+5+3 = 12 \\to 3$. The threes match, so you probably didn't
slip.</p>
<p><strong>The catch:</strong> matching doesn't <em>prove</em> you're right (the check only sees
the remainder), but a mismatch always catches a real error. Homework: why does swapping two
digits never change whether a number passes the nines check?</p>
`,
  },

  {
    slug: "our-first-himcm-weekend",
    number: 16,
    title: "We entered a modeling contest with no idea what we were doing",
    date: "2024-11-23",
    image: "images/news2/m18.jpg",
    alt: "A mathematician working at a board.",
    tags: ["Competitions", "HiMCM"],
    views: 256,
    likes: 27,
    excerpt:
      "Our first HiMCM. None of us had written a modeling paper before. We signed up anyway.",
    body: `
<p>So we did something a little reckless this month. We entered the HiMCM, a contest where
none of us had ever written a modeling paper, on the theory that the only way to learn is to
jump.</p>
<p>The weekend was chaos, in the good way. Friday afternoon we picked our problem and spent
the first few hours just arguing about what it was even asking. Saturday was a blur of
building a model, watching it fail on a simple test case, and rebuilding it. Sunday we wrote,
and wrote, and barely finished the summary before the deadline.</p>
<p>Our biggest early mistake: diving into a complicated model before checking whether the scale
even made sense. A rough back-of-the-envelope estimate the next morning showed our first
numbers were wildly off, and we had to back all the way up. Painful at the time, but it
hammered home the lesson: estimate first, elaborate later.</p>
<p>One of the team summed it up: "I thought modeling would be about fancy math. It turned out to
be about making decisions and writing them down clearly." Results come in the winter. Whatever
they are, we learned a year's worth in one weekend, and we'll be back.</p>
`,
  },

  {
    slug: "cutting-the-cake-fairly",
    number: 15,
    title: "Cutting a cake so nobody complains",
    date: "2024-11-02",
    image: "images/usa/u16.jpg",
    alt: "Models of the Platonic solids.",
    tags: ["Meeting recap", "Game theory"],
    views: 95,
    likes: 18,
    excerpt:
      "How do two people split a cake so each walks away convinced they got at least half? The math of fairness.",
    body: `
<p>"That's not fair!" is a sentence every kid has yelled, so we made it the whole lesson. How
do two people divide a cake so that each one honestly believes they got at least half, even if
they value the frosting and the corners differently?</p>
<p>A student blurted the answer almost immediately: "One person cuts, the other person picks."
Exactly right, and worth slowing down on. The cutter is motivated to split the cake into two
pieces they'd be equally happy with, because they know they'll get whichever piece is left.
The chooser obviously takes the piece they prefer. Both walk away satisfied. We call that
property envy-free.</p>
<p>"Okay but what about three people?" Now it gets hard, and the room split into camps trying
to extend the trick. It turns out three-way fair division really is trickier, and the clean
solution wasn't found until the 1960s, which surprised everyone.</p>
<p>That's the fun of this corner of math: a question a five-year-old asks at a birthday party
turns out to have decades of real research behind it. To go: design a fair way for three people
to split a cake. (It's possible. It's just sneaky.)</p>
`,
  },

  {
    slug: "am-gm-inequality",
    number: 14,
    title: "The one inequality I'd want on a desert island",
    date: "2024-10-19",
    image: "images/hero-blackboard.jpg",
    alt: "A blackboard covered in equations.",
    tags: ["Meeting recap", "Inequalities"],
    views: 81,
    likes: 11,
    excerpt:
      "Inequalities scare people until they meet the one that does most of the heavy lifting.",
    body: `
<p>If I could only teach one inequality, it would be this one, because so many others are just
it in disguise. For any two nonnegative numbers, the ordinary average is at least the geometric
mean:</p>
$$\\frac{a+b}{2} \\ge \\sqrt{ab},$$
<p>with equality only when $a = b$. And the proof is shorter than the sentence describing it:
start from the fact that a square is never negative, $(\\sqrt a - \\sqrt b)^2 \\ge 0$, expand,
and rearrange. Done.</p>
<p>What sells it is the payoff. Apply it to a positive number $x$ and its reciprocal: their
product is 1, so $x + \\frac1x \\ge 2$, always, hitting exactly 2 when $x = 1$. Students kept
trying to break it with weird values, and it kept holding, which is the fun part.</p>
<p>The deeper thing I want people to take away is that nearly every olympiad inequality traces
back to one humble fact: squares aren't negative. Keep that in your back pocket. To go: among
all rectangles with a fixed perimeter, show the square has the largest area.</p>
`,
  },

  {
    slug: "euler-polyhedron-formula",
    number: 13,
    title: "We counted corners and edges until a 2 fell out",
    date: "2024-10-05",
    image: "images/usa/u17.jpg",
    alt: "A set of polyhedron models.",
    tags: ["Meeting recap", "Graph theory"],
    views: 109,
    likes: 11,
    excerpt:
      "An experiment, not a lecture. Everyone grabbed a different solid and counted three numbers.",
    body: `
<p>No lecture this week, an experiment. Everyone grabbed a different solid (a cube, a pyramid, a
soccer-ball shape) and counted three things: corners, edges, and faces. Then we combined them
the same way for each, and the same number kept appearing.</p>
<ol>
  <li><strong>Cube:</strong> 8 corners, 12 edges, 6 faces. $8 - 12 + 6 = 2$.</li>
  <li><strong>Tetrahedron:</strong> 4 corners, 6 edges, 4 faces. $4 - 6 + 4 = 2$.</li>
  <li><strong>Octahedron:</strong> 6, 12, 8. Again $6 - 12 + 8 = 2$.</li>
</ol>
<p>The room went around the table calling out numbers, and the 2 just would not stop showing up.
That's the kind of thing that makes you stop and demand a reason. It's Euler's formula:</p>
$$V - E + F = 2$$
<p>for any solid (any one you can inflate into a sphere, anyway). The reason it works: flatten the
solid into a network of dots and lines, then peel pieces off one at a time in a way that never
changes $V - E + F$, until almost nothing is left and you can read off the 2 directly.</p>
<p>One consequence we'll chase another day: this formula is exactly why there are only five
perfectly regular solids, no more.</p>
`,
  },

  {
    slug: "fibonacci-and-the-golden-ratio",
    number: 12,
    title: "Rabbits, staircases, and a number hiding in a shell",
    date: "2024-09-21",
    image: "images/news/patterns-2.jpg",
    alt: "A nautilus shell showing a natural spiral.",
    tags: ["Meeting recap", "Sequences"],
    views: 423,
    likes: 78,
    excerpt:
      "The same sequence counts rabbits, stair-climbing routes, and domino tilings, and it hides a famous number.",
    body: `
<p>We spent the morning with a sequence that turns up in places it has no business being:
$1, 1, 2, 3, 5, 8, 13, \\dots$, each number the sum of the two before it.</p>
<p>What's lovely is how many doors open onto the same hallway. The Fibonacci numbers count pairs
of rabbits in an old breeding puzzle, they count the ways to climb $n$ stairs taking one or two
at a time, and they count the ways to tile a $2 \\times n$ strip with dominoes. All three obey</p>
$$f(n) = f(n-1) + f(n-2).$$
<p>And every time, the reason is the same once you look: your last move is either one thing
(leaving a smaller version of the problem) or another thing (leaving a slightly smaller one), and
you add the two cases.</p>
<div class="note">
  <span class="label">The surprise</span>
  Divide each Fibonacci number by the one before it and the ratios creep toward the golden ratio
  $\\varphi = \\frac{1+\\sqrt 5}{2} \\approx 1.618$, the same proportion that shows up in the
  spiral of a nautilus shell.
</div>
<p>To go: in how many ways can you write $n$ as an ordered sum of 1s and 2s? You already know the
answer. The fun is figuring out why.</p>
`,
  },

  {
    slug: "welcome-back-year-two",
    number: 11,
    title: "Back for round two",
    date: "2024-09-07",
    image: "images/tamu/t02.jpg",
    alt: "Students at a math circle session.",
    tags: ["Welcome", "Community"],
    views: 144,
    likes: 27,
    excerpt:
      "New school year, more returning faces than I expected, and a warm-up that fools everybody.",
    body: `
<p>We're back for a second year and the room already looks different. More returning faces, a few
brand new ones, and for the first time we had to drag over an extra table. If you're joining us
this fall, welcome aboard.</p>
<p>We opened with a question that sounds trivial and isn't: how many squares are on a chessboard?
Almost everyone says 64, counting only the little ones. But a chessboard is also full of $2\\times2$
squares, and $3\\times3$, all the way up to the single $8\\times8$. Count them by size and you're
adding</p>
$$1^2 + 2^2 + 3^2 + \\cdots + 8^2 = 204.$$
<p>The room was genuinely surprised it came to 204, and a couple of people refused to believe it
until we listed the sizes out. We promised we'd come back later in the year and explain where that
tidy total comes from, and we will.</p>
<p>Same time, same place: Saturdays, 10 to noon. Bring a friend, first visits are free.</p>
`,
  },

  {
    slug: "one-year-of-problems",
    number: 10,
    title: "One year of problems",
    date: "2024-06-01",
    image: "images/students.jpg",
    alt: "Students working together at a table.",
    tags: ["Community", "About"],
    views: 176,
    likes: 24,
    excerpt:
      "Five students and a borrowed table, one year later. A short letter before summer.",
    body: `
<p>Hi everyone,</p>
<p>That's our first year done. Last September we were five students, two mentors, and a borrowed
table in the corner of the library, honestly unsure the circle would last past the first month. It
did, and then some.</p>
<p>We covered a lot of ground for a first year: counting and combinatorics, the digit tricks of
divisibility, three different proofs of the Pythagorean theorem, pigeonhole, induction, expected
value, and our first taste of contest math. None of it was for a grade. People came because the
problems were good.</p>
<p>The moment I keep replaying happened late in the spring, when a quiet seventh grader walked to
the board and explained an invariant argument more clearly than the mentors had. The room got it
because she got it. That's the whole reason we do this.</p>
<p>Thank you to everyone who showed up curious, week after week. We're back
in September with more of everything. Have a wonderful summer, and keep noticing the math around
you.</p>
`,
  },

  {
    slug: "what-never-changes",
    number: 9,
    title: "Twenty-five coins and an impossible goal",
    date: "2024-05-04",
    image: "images/news/geometry-4.jpg",
    alt: "A geometric model.",
    tags: ["Meeting recap", "Invariants"],
    views: 67,
    likes: 12,
    excerpt:
      "Flip two coins at a time, forever. Can you ever reach all tails? The answer is a flat no.",
    body: `
<p><strong>The setup:</strong> twenty-five coins on the table, all heads up. A move is flipping
exactly two of them, your choice. Can you ever get all 25 showing tails?</p>
<p><strong>What everyone tries:</strong> flipping. People got close, swapping pairs back and forth,
but never all the way there. After a while that failure starts to feel like a message.</p>
<p><strong>The realization:</strong> look at the number of heads. Each move flips two coins, so the
head count changes by $+2$, $-2$, or $0$. It never changes its parity. We start at 25 (odd), and all
tails means 0 heads (even).</p>
$$\\text{odd} \\;\\longrightarrow\\; \\text{even by adding only even numbers} \\;=\\; \\text{impossible.}$$
<p><strong>The point:</strong> find a quantity your moves can't change (here, the parity of the head
count) and you can rule out a whole goal without testing a single sequence. That's an invariant, and
it's one of the most satisfying tools in all of problem solving.</p>
<p>To go: same 25 coins, but now a move flips any three. Now can you reach all tails? The answer
changes, and figuring out why is the real exercise.</p>
`,
  },

  {
    slug: "what-to-expect",
    number: 8,
    title: "What's the average roll of a die?",
    date: "2024-04-06",
    image: "images/news-c.jpg",
    alt: "A mathematics workshop.",
    tags: ["Meeting recap", "Probability"],
    views: 102,
    likes: 18,
    excerpt:
      "The idea of an expected value is simple, useful, and a little sneaky.",
    body: `
<blockquote>Roll a fair die a thousand times and average the results. What number do you get?</blockquote>
<p>People guessed 3, they guessed 4, and the honest answer is right in between. Each face is equally
likely, so the long-run average is</p>
$$\\frac{1+2+3+4+5+6}{6} = 3.5.$$
<p>And then a student pointed out the obvious thing that's secretly the whole insight: you can never
actually roll a 3.5. Right. An expected value isn't a value you expect to see. It's the balance
point of all the possibilities, like the spot where a seesaw of outcomes sits level.</p>
<p>The trick that makes it powerful is that expectations just add, even when the things you're adding
aren't independent. Two dice? Each averages 3.5, so the sum averages $3.5 + 3.5 = 7$, no table of 36
outcomes required. That "expectations add" rule surprises people every single time.</p>
<p>To go: on average, how many times do you have to roll a die before you see your first six? The
answer is a nice round number.</p>
`,
  },

  {
    slug: "dominoes-and-induction",
    number: 7,
    title: "Knocking over an infinite line of dominoes",
    date: "2024-03-09",
    image: "images/news2/m17.jpg",
    alt: "A polyhedral model.",
    tags: ["Meeting recap", "Proof"],
    views: 90,
    likes: 20,
    excerpt:
      "If you can topple the first one, and each one topples the next, the whole line falls. That picture is a real proof technique.",
    body: `
<p>Today felt like a turning point for a few people, because they wrote their first real proofs, and
the idea behind them is one everybody already knows in their bones: a long line of dominoes falls
completely if the first one falls and each domino knocks over the next.</p>
<p>That's induction. We tested it on a pattern students had noticed weeks ago without proof, that the
sum of the first $n$ odd numbers is always a perfect square:</p>
$$1 + 3 + 5 + \\cdots + (2n - 1) = n^2.$$
<p>The base case is the first domino: for $n=1$ the left side is just 1 and the right is $1^2$. The
inductive step is each domino tipping the next: if it holds for some $n$, add the next odd number
$2n+1$ to both sides, and the left becomes $n^2 + (2n+1) = (n+1)^2$, exactly the formula for $n+1$.
The whole line falls.</p>
<p>The part people kept missing is that you genuinely need both halves. A first domino with no chain
proves nothing; a chain with no first domino never starts. We spent a good while on examples where one
piece quietly fails. To go: prove $n^3 - n$ is divisible by 6.</p>
`,
  },

  {
    slug: "our-first-contest-season",
    number: 6,
    title: "Our first contest season",
    date: "2024-02-10",
    image: "images/tamu/t05.jpg",
    alt: "Students at a math circle session.",
    tags: ["Competitions", "AMC"],
    views: 152,
    likes: 20,
    excerpt:
      "A handful of our students sat the AMC for the first time. Here's what we drilled and what stuck.",
    body: `
<p>This winter a handful of our students sat the AMC, for most of them their first real math
competition of any kind, and watching them prepare was the highlight of my year so far.</p>
<p>We spent a few Saturdays on the habits that matter under a clock: read the problem twice, try a
small case before reaching for algebra, and don't be afraid to skip one and come back. The math is
only half of it; staying calm is the other half.</p>
<p>One drill problem fit the year perfectly: how many positive divisors does 2024 have? The move is
to factor first. Since $2024 = 2^3 \\cdot 11 \\cdot 23$, any divisor is built by choosing a power of 2
(four options), then whether to include the 11 (two), then the 23 (two). Multiply:
$(3{+}1)(1{+}1)(1{+}1) = 16$. Nobody had to list a single divisor.</p>
<p>However the scores land, these students showed up and tried something hard. That counts for a lot.
To go: how many divisors does 360 have?</p>
`,
  },

  {
    slug: "socks-and-pigeonholes",
    number: 5,
    title: "Reaching into a dark drawer",
    date: "2024-01-13",
    image: "images/news2/m02.jpg",
    alt: "Working through a problem at the board.",
    tags: ["Meeting recap", "Combinatorics"],
    views: 124,
    likes: 22,
    excerpt:
      "Grab three socks in the dark and you're guaranteed a matching pair. The reason runs deeper than it looks.",
    body: `
<p>We came back from winter break with a principle so obvious it sounds like a joke, then spent the
whole morning being surprised by it.</p>
<p>The drawer: black socks and white socks, all jumbled, lights off. How many socks must you grab to
be sure of a matching pair? Three. With only two colors, three socks can't all be different, so two
must match. That's the pigeonhole principle, more items than categories forces a repeat.</p>
<p>Then we stretched it. Among any 13 people, two share a birth month, because there are only 12
months to go around. So far, comfortable. Then a harder one that took real thought: in any group of
people, at least two have the exact same number of acquaintances inside the group. Figuring out the
right "pigeonholes" for that one took most of the hour, and the click when it landed was worth it.</p>
<p>That's the real lesson, the thing nobody hands you: deciding what the categories should be is where
all the cleverness lives. To go: pick any five whole numbers and show that some two of them have a
difference that's a multiple of 4.</p>
`,
  },

  {
    slug: "three-proofs-of-pythagoras",
    number: 4,
    title: "Three reasons a squared plus b squared equals c squared",
    date: "2023-12-02",
    image: "images/news/patterns-3.jpg",
    alt: "A spiral.",
    tags: ["Meeting recap", "Geometry"],
    views: 287,
    likes: 50,
    excerpt:
      "Everyone can recite it. Almost nobody has seen why. We looked at three different reasons.",
    body: `
<p>Everyone in the room could chant it: for a right triangle, $a^2 + b^2 = c^2$. So I asked why it's
true, and the room went quiet. Good. A theorem you can only recite isn't really yours yet, so we spent
the morning making it ours, three different ways.</p>
<p>The one that landed hardest used no algebra at all. Take four copies of the right triangle and
arrange them inside a big square two different ways. One arrangement leaves a square hole of area
$c^2$. The other leaves two holes, of area $a^2$ and $b^2$. Same big square, same four triangles, so
the leftover area has to match. The picture does the entire proof, and a couple of students actually
said "oh" out loud.</p>
<p>We checked it on the friendliest right triangle there is, the 3-4-5: $9 + 16 = 25$. Then we went
hunting for more whole-number triples and turned up 5-12-13 and 8-15-17, which became the next week's
rabbit hole.</p>
<p>My honest pitch: a theorem you can prove three ways feels completely different from one you've only
memorized. The first one is yours. The second is borrowed. To go: can a right triangle have all three
sides odd whole numbers? Find one or argue you never could.</p>
`,
  },

  {
    slug: "divisible-by-nine",
    number: 3,
    title: "The secret behind the divisible-by-nine trick",
    date: "2023-11-04",
    image: "images/tamu/t06.jpg",
    alt: "Students working at a math circle.",
    tags: ["Meeting recap", "Number theory"],
    views: 98,
    likes: 9,
    excerpt:
      "Add up a number's digits, and if the total is a multiple of nine, so is the number. We chased down why.",
    body: `
<p>A lot of students already knew the rule: a number is divisible by 9 exactly when its digits add up
to a multiple of 9. What almost nobody knew was <em>why</em>, and that turned out to be the whole
morning.</p>
<p>We started with a test. Take 1233; its digits sum to $1+2+3+3 = 9$, a multiple of 9, so the rule
predicts 1233 is divisible by 9. And indeed $1233 = 9 \\times 137$. The rule works, but a working rule
you can't explain should always bug you a little.</p>
<p>The secret is that 10 is just one more than 9. So 10 leaves a remainder of 1 when divided by 9, and
so do 100, 1000, and every power of 10. That means a number like $1233 = 1000 + 200 + 30 + 3$ has the
same remainder mod 9 as $1 + 2 + 3 + 3$, its digits added up. If that sum is a multiple of 9, so is the
original. Once you see it, the trick stops being magic and starts being obvious.</p>
<p>Bonus: the exact same reasoning gives the rule for 3. To go: build a rule for 11, using the fact
that 10 is one <em>less</em> than 11. The pattern of plus and minus signs is the clue.</p>
`,
  },

  {
    slug: "learning-to-count",
    number: 2,
    title: "Learning to count, properly",
    date: "2023-10-07",
    image: "images/news/abacus-1.jpg",
    alt: "An abacus.",
    tags: ["Meeting recap", "Combinatorics"],
    views: 74,
    likes: 16,
    excerpt:
      "Counting sounds like the first thing you ever learned. Done right, it's a whole subject.",
    body: `
<p>Our second meeting took on counting, which always gets a few smirks, because people think they
finished learning to count in kindergarten. Then we hand them a real problem and the smirks fade.</p>
<p>Two warm-ups, two completely different flavors. First, handshakes: if everyone in a room of $n$
people shakes hands once with everyone else, how many handshakes is that? Each person shakes $n-1$
hands, but that counts every handshake from both sides, so we divide by two:</p>
$$\\binom{n}{2} = \\frac{n(n-1)}{2}.$$
<p>Second: how many different subsets can you form from a set of $n$ things, counting the empty set
and the whole thing? Each item is independently in or out, two choices each, so the answer is $2^n$.</p>
<p>The lesson is that good counting is about organizing the choices, not listing the cases. List, and
you drown. Organize, and the answer falls out. To go: how many ways can five people line up for a
photo, and then how many if two of them refuse to stand next to each other?</p>
`,
  },

  {
    slug: "the-circle-begins",
    number: 1,
    title: "The circle begins",
    date: "2023-09-09",
    image: "images/library.jpg",
    alt: "The Los Gatos Library.",
    tags: ["Welcome", "Community"],
    views: 318,
    likes: 25,
    excerpt:
      "Our very first meeting. Five students, two mentors, one borrowed table, and a three-hundred-year-old trick.",
    body: `
<p>Today was the first meeting of the Los Gatos Math Circle. Five students, two mentors, and one
borrowed table in the corner of the library. We did not know if anyone would come. Five did, and we
are glad they took the chance on us.</p>
<p>We wanted a place where students could do mathematics for the pleasure of it, away from grades and
tests. No lectures to sit through. Just good problems, a whiteboard, and people to argue with. If that
sounds like your idea of a fun Saturday, you belong here.</p>
<p>We opened with the story of a young Carl Friedrich Gauss, supposedly told to add up every number
from 1 to 100 to keep him busy, who finished in seconds. Instead of adding in order, he paired the
first with the last, the second with the second-to-last, and so on. Each pair sums to 101, and there
are 50 pairs:</p>
$$1 + 2 + \\cdots + 100 = \\frac{100 \\cdot 101}{2} = 5050.$$
<p>From there the room worked out the general version, $1 + 2 + \\cdots + n = \\frac{n(n+1)}{2}$, and just
like that we were doing real mathematics together.</p>
<div class="note">
  <span class="label">Join us</span>
  Saturdays, 10 to noon, at the Los Gatos Library. Anyone in grades 6 to 12 is welcome. Bring a pencil
  and your curiosity.
</div>
<p>This is the start of something, we hope. Tell your friends.</p>
`,
  },
];

if (typeof window !== "undefined") {
  window.ISSUES = ISSUES;
}
