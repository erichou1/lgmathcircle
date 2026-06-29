#!/usr/bin/env python3
"""Generate js/meetings.js: the full Saturday meeting schedule (Fall 2023 to
Spring 2026) with breaks, plus a slide deck (MODULES) for every meeting."""
import datetime, json
from datetime import date, timedelta

# ---------------------------------------------------------------------------
# Slide-deck modules. Each: id -> {t: title, topic, s: [[heading, html], ...]}
# Math uses TeX ($...$ inline, $$...$$ display); json.dumps escapes backslashes.
# ---------------------------------------------------------------------------
M = {}
def mod(mid, t, topic, slides): M[mid] = {"t": t, "topic": topic, "s": slides}

# --- Welcomes / community ---
mod("welcome_gauss", "Welcome, and a famous sum", "Welcome", [
 ["Welcome to the circle", "<p>Glad you're here. We do math the way mathematicians actually do it: play with examples, make guesses, argue about them, and prove the ones that survive.</p><p>No grades. Just good problems and a whiteboard.</p>"],
 ["A quick story", "<p>Young Carl Friedrich Gauss was told to add every number from 1 to 100. He finished in seconds. How?</p>"],
 ["The trick", "<p>Pair the ends: $1+100$, $2+99$, $3+98$, ... Each pair sums to 101, and there are 50 pairs.</p>$$1+2+\\cdots+100 = \\frac{100\\cdot 101}{2} = 5050.$$"],
 ["The general rule", "<p>The same pairing gives a formula for any $n$:</p>$$1+2+\\cdots+n = \\frac{n(n+1)}{2}.$$<p>One good idea replaced a hundred additions.</p>"],
 ["Your turn", "<p>What is $1+2+\\cdots+200$? And what is $2+4+6+\\cdots+100$?</p>"],
])
mod("welcome_squares", "How many squares on a board?", "Welcome", [
 ["Back for a new year", "<p>Welcome back. Let's warm up with a question that sounds easy and isn't.</p>"],
 ["The question", "<p>How many squares are on an $8\\times 8$ chessboard? Most people say 64. But there are bigger squares too: $2\\times2$, $3\\times3$, all the way up to $8\\times8$.</p>"],
 ["Count by size", "<p>There are $8^2$ unit squares, $7^2$ of size two, and so on:</p>$$1^2+2^2+3^2+\\cdots+8^2 = 204.$$"],
 ["A promise", "<p>Why does the sum of squares come out so cleanly? We'll prove a formula for it later this year.</p>"],
])
mod("welcome_lockers", "The locker problem", "Welcome", [
 ["A new year of problems", "<p>Welcome to a new season. Here is a classic to start.</p>"],
 ["1000 lockers", "<p>1000 lockers, all closed, and 1000 students. Student 1 opens every locker. Student 2 toggles every 2nd. Student 3 every 3rd, and so on. Which lockers end up open?</p>"],
 ["Count the toggles", "<p>Locker $n$ is toggled once for each divisor of $n$. Most divisors come in pairs, so most lockers are toggled an even number of times and end closed.</p>"],
 ["The exceptions", "<p>Perfect squares have a repeated divisor, so they are toggled an odd number of times. Since $31^2=961$ and $32^2=1024$, exactly $31$ lockers stay open.</p>"],
])
mod("welcome_chocolate", "Breaking a chocolate bar", "Welcome", [
 ["New term, new faces", "<p>Welcome to everyone joining us this winter. A warm-up to get going.</p>"],
 ["The bar", "<p>You have an $m\\times n$ chocolate bar. Each snap breaks one piece along a line into two. How many snaps to reduce it to single squares?</p>"],
 ["The insight", "<p>Every snap turns one piece into two, so each snap adds exactly one piece. You start with 1 and want $mn$.</p>$$\\text{snaps} = mn - 1.$$"],
 ["Surprise", "<p>The order never matters. However you break it, the count is the same.</p>"],
])

# --- Counting / combinatorics ---
mod("counting", "Learning to count, properly", "Combinatorics", [
 ["Counting is a subject", "<p>You think you learned to count in kindergarten. Then we hand you a real problem.</p>"],
 ["Handshakes", "<p>In a room of $n$ people who each shake hands once, how many handshakes happen? Each person shakes $n-1$ hands, but that counts each twice:</p>$$\\binom{n}{2}=\\frac{n(n-1)}{2}.$$"],
 ["Subsets", "<p>How many subsets does a set of $n$ things have? Each item is in or out, independently:</p>$$2^n.$$"],
 ["The lesson", "<p>Good counting organizes the choices instead of listing the cases.</p>"],
 ["Try it", "<p>How many ways can five people line up? Then, how many if two of them refuse to stand next to each other?</p>"],
])
mod("counting_grid", "Counting without counting", "Combinatorics", [
 ["The idea", "<p>When a set is too big to count one item at a time, count it sideways.</p>"],
 ["Grid paths", "<p>How many shortest paths go from the bottom-left to the top-right of a $4\\times 7$ grid, moving only right or up?</p>"],
 ["Choose the ups", "<p>Every path is 7 rights and 4 ups in some order. Choosing which steps are ups fixes the path:</p>$$\\binom{11}{4}=330.$$"],
 ["Take-home", "<p>How many shortest paths from $(0,0)$ to $(8,8)$ never rise above the line $y=x$?</p>"],
])
mod("count_two_ways", "Count it two ways", "Combinatorics", [
 ["One idea", "<p>If you count the same thing two ways, the answers must match. That forced equality proves a lot.</p>"],
 ["A committee with a chair", "<p>Pick a committee of $k$ from $n$, then a chair. Count it as committee-then-chair, or chair-then-rest:</p>$$k\\binom{n}{k}=n\\binom{n-1}{k-1}.$$"],
 ["Check it", "<p>For $n=4,k=2$: left is $2\\cdot 6=12$, right is $4\\cdot 3=12$. No algebra needed.</p>"],
 ["Try it", "<p>Explain $\\sum_{k=0}^n \\binom{n}{k}=2^n$ by counting one set two ways.</p>"],
])
mod("stars_bars", "Stars and bars", "Combinatorics", [
 ["The setup", "<p>How many ways can you put $n$ identical balls into $k$ labeled boxes?</p>"],
 ["The picture", "<p>Lay out $n$ stars and $k-1$ bars to separate the boxes. Each arrangement is one distribution:</p>$$\\binom{n+k-1}{k-1}.$$"],
 ["Example", "<p>Nonnegative solutions of $a+b+c=10$: that's $\\binom{12}{2}=66$.</p>"],
 ["Try it", "<p>How many ways to make change for 25 using pennies, nickels, and dimes?</p>"],
])
mod("binomial", "The binomial theorem", "Algebra", [
 ["Expanding powers", "<p>What is $(x+y)^n$? The coefficients are exactly the binomial numbers.</p>"],
 ["The formula", "$$ (x+y)^n=\\sum_{k=0}^{n}\\binom{n}{k}x^{n-k}y^k. $$<p>The $\\binom{n}{k}$ counts how many ways to choose $k$ of the $n$ factors to contribute a $y$.</p>"],
 ["A neat corollary", "<p>Set $x=y=1$: $\\sum_k \\binom{n}{k}=2^n$. Set $x=1,y=-1$: the alternating sum is $0$.</p>"],
 ["Try it", "<p>Find the coefficient of $x^2$ in $(1+x)^{10}$.</p>"],
])
mod("pascal", "Pascal's triangle", "Combinatorics", [
 ["A triangle of numbers", "<p>Each entry is the sum of the two above it. It looks like a doodle; it's a map of counting.</p>"],
 ["The rule", "$$\\binom{n}{k}=\\binom{n-1}{k-1}+\\binom{n-1}{k}.$$<p>To choose $k$ from $n$, either include the last item or don't.</p>"],
 ["Hidden patterns", "<p>Rows sum to $2^n$. The shallow diagonals add up to Fibonacci numbers.</p>"],
 ["Try it", "<p>Prove the hockey stick: $\\sum_{i=r}^{n}\\binom{i}{r}=\\binom{n+1}{r+1}$.</p>"],
])

# --- Number theory ---
mod("div9", "The secret of dividing by nine", "Number theory", [
 ["A familiar rule", "<p>A number is divisible by 9 exactly when its digits add to a multiple of 9. But why?</p>"],
 ["Quick test", "<p>$1233\\to 1+2+3+3=9$, so 9 divides 1233. Indeed $1233=9\\times 137$.</p>"],
 ["Why it works", "<p>Because $10\\equiv 1\\pmod 9$, every power of 10 leaves remainder 1. So a number has the same remainder mod 9 as its digit sum.</p>"],
 ["Bonus", "<p>The same idea gives the rule for 3. Now find a rule for 11 using $10\\equiv -1\\pmod{11}$.</p>"],
])
mod("casting_nines", "Casting out nines", "Number theory", [
 ["An old check", "<p>Before calculators, clerks caught arithmetic errors fast with this trick.</p>"],
 ["Key fact", "<p>A number's remainder mod 9 equals its digit sum's remainder. Keep adding digits to a single number.</p>"],
 ["Checking a product", "<p>$123\\times 11=1353$. Check: $123\\to 6$, $11\\to 2$, $6\\times 2=12\\to 3$. And $1353\\to 12\\to 3$. They match.</p>"],
 ["A warning", "<p>Matching doesn't prove correctness, but a mismatch always reveals a real error.</p>"],
])
mod("modular", "Clock math: modular arithmetic", "Number theory", [
 ["Wrap-around", "<p>It's 10 o'clock; wait 5 hours and it's 3, not 15. Arithmetic that wraps around is one of our sharpest tools.</p>"],
 ["Notation", "<p>$a\\equiv b\\pmod m$ means $m$ divides $a-b$. You can add and multiply congruences like equations.</p>"],
 ["Last digit of $7^{100}$", "<p>Track powers mod 10: $7,9,3,1$ then repeat. Period 4, and $100=4\\cdot 25$, so $7^{100}\\equiv 1$. Last digit is 1.</p>"],
 ["Try it", "<p>Show $n^5-n$ is a multiple of 10 for every integer $n$.</p>"],
])
mod("euclid", "Euclid's algorithm for GCD", "Number theory", [
 ["A faster way", "<p>Listing divisors to find a gcd is slow. Euclid had a better idea 2000 years ago.</p>"],
 ["The loop", "<p>Replace the larger number with the remainder, repeat:</p>$$252=2\\cdot105+42,\\ 105=2\\cdot42+21,\\ 42=2\\cdot21+0.$$<p>So $\\gcd(252,105)=21$.</p>"],
 ["Why it matters", "<p>It reduces fractions and underlies the math that keeps online messages private.</p>"],
 ["Try it", "<p>Show consecutive integers $n$ and $n+1$ are always coprime.</p>"],
])
mod("primes", "Infinitely many primes", "Number theory", [
 ["A big claim", "<p>The primes never run out. Euclid proved it with a one-paragraph argument.</p>"],
 ["The proof", "<p>Suppose there were finitely many: $p_1,\\dots,p_k$. Consider $N=p_1p_2\\cdots p_k+1$. It leaves remainder 1 when divided by each $p_i$, so no listed prime divides it.</p>"],
 ["The punchline", "<p>So $N$ has a prime factor not on the list. Contradiction. The primes are infinite.</p>"],
 ["Try it", "<p>Are there infinitely many primes of the form $4k+3$? (Yes; adapt the idea.)</p>"],
])
mod("mod_inverse", "Inverses mod p", "Number theory", [
 ["Dividing in modular world", "<p>Mod a prime $p$, every nonzero number has a multiplicative inverse.</p>"],
 ["Fermat's little theorem", "$$a^{p-1}\\equiv 1\\pmod p\\quad(p\\nmid a).$$<p>So $a^{p-2}$ is the inverse of $a$.</p>"],
 ["Example", "<p>Mod 7, the inverse of 3 is $3^5=243\\equiv 5$, since $3\\cdot 5=15\\equiv 1$.</p>"],
 ["Try it", "<p>Solve $4x\\equiv 1\\pmod{9}$.</p>"],
])
mod("number_bases", "Counting in other bases", "Number theory", [
 ["Beyond base ten", "<p>We write numbers in base 10 by habit. Computers use base 2. The idea is the same.</p>"],
 ["What a base means", "<p>In base $b$, the digits are weights of powers of $b$:</p>$$1011_2 = 8+0+2+1 = 11.$$"],
 ["Converting", "<p>To write 23 in base 2, peel off powers of two: $23=16+4+2+1=10111_2$.</p>"],
 ["Try it", "<p>What is $100$ in base 7? And what base makes $44$ equal to $24$ in base ten?</p>"],
])
mod("diophantine", "Equations in whole numbers", "Number theory", [
 ["Integer solutions only", "<p>A Diophantine equation asks for whole-number solutions, which changes everything.</p>"],
 ["A linear one", "<p>$3x+5y=1$ has solutions because $\\gcd(3,5)=1$. One is $x=2,y=-1$; all others differ by multiples of $(5,-3)$.</p>"],
 ["A factoring trick", "<p>For $\\frac1x+\\frac1y=\\frac1{12}$, clear denominators to get $(x-12)(y-12)=144$. Each factor pair gives a solution.</p>"],
 ["Try it", "<p>Find all positive integer solutions of $\\frac1x+\\frac1y=\\frac12$.</p>"],
])

# --- Geometry ---
mod("pythagoras", "Three proofs of one theorem", "Geometry", [
 ["Everyone knows it", "<p>For a right triangle, $a^2+b^2=c^2$. But why is it true?</p>"],
 ["Rearrangement proof", "<p>Place four copies of the triangle inside a big square two ways. One leaves a hole of area $c^2$; the other leaves holes $a^2$ and $b^2$. Same square, so they're equal.</p>"],
 ["A friendly triangle", "<p>Check the 3-4-5: $9+16=25=5^2$. Then 5-12-13 and 8-15-17 appear too.</p>"],
 ["Try it", "<p>Can a right triangle have all three sides odd integers? Argue why not.</p>"],
])
mod("inscribed", "The inscribed angle theorem", "Geometry", [
 ["One fact, many problems", "<p>An angle on a circle is half the central angle on the same arc.</p>"],
 ["The clean case", "<p>An angle standing on a diameter is $\\frac{180^\\circ}{2}=90^\\circ$. Every triangle with a side as diameter has a right angle.</p>"],
 ["Why you want it", "<p>Many 'find the angle' problems are this theorem in disguise.</p>"],
 ["Try it", "<p>Show opposite angles of a cyclic quadrilateral add to $180^\\circ$.</p>"],
])
mod("power_point", "The power of a point", "Geometry", [
 ["A tidy theorem", "<p>From a point $P$, any line through a circle meets it at $A,B$ with $PA\\cdot PB$ constant.</p>"],
 ["Two forms", "$$PA\\cdot PB = PC\\cdot PD,\\qquad PT^2=PA\\cdot PB\\ \\text{(tangent)}.$$"],
 ["In action", "<p>Tangent length 6, far secant point 9 away: $6^2=x\\cdot 9$, so the near point is $x=4$.</p>"],
 ["Try it", "<p>Two circles meet at $X,Y$. Show any point on line $XY$ has equal tangent lengths to both.</p>"],
])
mod("euler_poly", "A formula for every solid", "Geometry", [
 ["An experiment", "<p>Count the corners $V$, edges $E$, and faces $F$ of any solid. Combine them.</p>"],
 ["Euler's formula", "$$V-E+F=2.$$<p>Cube: $8-12+6=2$. Tetrahedron: $4-6+4=2$. Always 2.</p>"],
 ["Why", "<p>Flatten the solid to a network and remove pieces without changing $V-E+F$. The leftover is 2.</p>"],
 ["Consequence", "<p>This is why there are exactly five regular (Platonic) solids.</p>"],
])
mod("graphs", "Bridges, graphs, and Euler", "Graph theory", [
 ["A walk you can't finish", "<p>Could you cross all seven bridges of Königsberg exactly once? Euler said no, and invented graph theory.</p>"],
 ["Throw away the map", "<p>Each landmass is a dot, each bridge an edge. Only the connections matter.</p>"],
 ["Count odd corners", "<p>A trail using every edge once needs 0 or 2 odd-degree vertices. Königsberg had 4 odd, so it's impossible.</p>$$\\sum_v \\deg(v)=2E.$$"],
 ["Try it", "<p>Which capital letters can you draw without lifting your pen?</p>"],
])
mod("picks", "Pick's theorem", "Geometry", [
 ["Area by dots", "<p>Draw a polygon on grid paper with corners on lattice points. Its area comes from counting dots.</p>"],
 ["The formula", "$$A = I + \\tfrac{B}{2} - 1,$$<p>where $I$ is interior dots and $B$ is boundary dots.</p>"],
 ["Example", "<p>A triangle with $B=4$ boundary and $I=0$ interior dots has area $0+2-1=1$.</p>"],
 ["Try it", "<p>Draw a pentagon on the grid and verify Pick's theorem against the shoelace area.</p>"],
])
mod("triangle_centers", "The many centers of a triangle", "Geometry", [
 ["More than one middle", "<p>A triangle has several natural centers, each where three special lines meet.</p>"],
 ["Four classics", "<p>Centroid (medians), incenter (angle bisectors), circumcenter (perpendicular bisectors), orthocenter (altitudes).</p>"],
 ["Euler line", "<p>Amazingly, the centroid, circumcenter, and orthocenter are always collinear, and the centroid splits the segment $2:1$.</p>"],
 ["Try it", "<p>Where is the circumcenter of a right triangle? (Hint: the midpoint of the hypotenuse.)</p>"],
])
mod("geometry_transforms", "Symmetry and transformations", "Geometry", [
 ["Moving figures", "<p>Translations, rotations, reflections, and their combinations preserve distance. They turn hard problems into easy ones.</p>"],
 ["A reflection trick", "<p>To find the shortest path from $A$ to a line and then to $B$, reflect $B$ across the line and draw a straight segment.</p>"],
 ["Why it helps", "<p>Symmetry often reveals equal lengths and angles you couldn't otherwise see.</p>"],
 ["Try it", "<p>A ball bounces off a wall. Use reflection to find where it must hit to reach a target.</p>"],
])

# --- Pigeonhole / invariants / proof ---
mod("pigeonhole_socks", "Socks, birthdays, pigeons", "Combinatorics", [
 ["An obvious idea", "<p>More pigeons than holes means some hole holds two. Simple, and powerful.</p>"],
 ["The drawer", "<p>Black and white socks in the dark: grab 3 and two must match. Two colors, three socks.</p>"],
 ["Stretch it", "<p>Among 13 people, two share a birth month. Among any group, two people have the same number of friends inside it.</p>"],
 ["Try it", "<p>Pick any five integers. Show two have a difference divisible by 4.</p>"],
])
mod("pigeonhole", "Pigeonhole: too many pigeons", "Combinatorics", [
 ["The principle", "<p>Put more items than categories and a category repeats. The craft is choosing the categories.</p>"],
 ["Five points", "<p>Drop five points in a unit square. Cut it into four half-squares; two points share one, so they're within</p>$$\\tfrac{\\sqrt2}{2}.$$"],
 ["The real skill", "<p>Nobody hands you the boxes. Inventing them is the whole move.</p>"],
 ["Try it", "<p>From 51 numbers chosen out of 1..100, show two are coprime and two differ by 1.</p>"],
])
mod("invariants", "What never changes", "Invariants", [
 ["Look for the constant", "<p>When a process keeps changing, find the one quantity that never does.</p>"],
 ["Mutilated chessboard", "<p>Remove two opposite corners (same color). Dominoes cover one of each color, but you're left with 30 vs 32. No tiling exists.</p>"],
 ["Coins", "<p>25 coins heads up; flip two at a time. The parity of heads never changes from odd, so all-tails (even) is impossible.</p>"],
 ["Try it", "<p>Numbers 1..2025 on a board; replace two with their difference. Show the last number is even.</p>"],
])
mod("parity", "Odd, even, and impossibility", "Invariants", [
 ["The simplest invariant", "<p>Sometimes whether a count is odd or even decides everything.</p>"],
 ["Handshake lemma", "<p>In any group, the number of people who shook an odd number of hands is even.</p>"],
 ["A tiling", "<p>Can you tile a $5\\times5$ board minus the center with dominoes? Color it: counts don't match, so no.</p>"],
 ["Try it", "<p>Can a knight start on a corner of a chessboard, visit every square once, and return? Consider colors.</p>"],
])
mod("coloring", "Coloring arguments", "Combinatorics", [
 ["Color to reveal structure", "<p>A clever coloring can prove something is impossible.</p>"],
 ["Tromino board", "<p>Color a board in stripes or blocks so each piece always covers a fixed color pattern, then compare totals.</p>"],
 ["Why it works", "<p>If the target needs a color balance the pieces can't produce, you're done.</p>"],
 ["Try it", "<p>Can you tile an $8\\times8$ board missing two same-colored squares with dominoes? Why not?</p>"],
])
mod("induction", "Dominoes and induction", "Proof", [
 ["A line of dominoes", "<p>Knock the first one, and make each knock the next: the whole line falls. That's induction.</p>"],
 ["A first proof", "<p>Sum of the first $n$ odd numbers:</p>$$1+3+\\cdots+(2n-1)=n^2.$$<p>Base $n=1$ works; adding $2n+1$ turns $n^2$ into $(n+1)^2$.</p>"],
 ["The catch", "<p>You need both parts: a first domino and the chain. Drop either and it fails.</p>"],
 ["Try it", "<p>Prove $n^3-n$ is divisible by 6, by induction and then without it.</p>"],
])
mod("nim_games", "Winning games: Nim", "Game theory", [
 ["Take-away games", "<p>Two players remove objects; the one who can't move loses. Is there a winning strategy?</p>"],
 ["Single pile", "<p>With one pile and a max take of $k$, leave a multiple of $k+1$ for your opponent and you win.</p>"],
 ["Nim values", "<p>For several piles, the key is the XOR of pile sizes. Leave XOR $=0$ to win.</p>"],
 ["Try it", "<p>Piles of 3, 4, 5: is the first player winning? Find the move.</p>"],
])
mod("logic", "Knights, knaves, and logic", "Logic", [
 ["Truth-tellers and liars", "<p>On an island, knights always tell the truth and knaves always lie. Statements become puzzles.</p>"],
 ["A classic", "<p>One says 'we are both knaves.' A knight couldn't say it; so the speaker is a knave and the other is a knight.</p>"],
 ["Tools", "<p>Casework and contradiction crack these. Assume a role, follow the consequences, check for conflict.</p>"],
 ["Try it", "<p>A says 'B is a knight.' B says 'we are different.' What are they?</p>"],
])

# --- Probability / expectation ---
mod("expected_value", "What to expect", "Probability", [
 ["The long-run average", "<p>Expected value is the balance point of all outcomes, even one you can't actually roll.</p>"],
 ["One die", "$$\\frac{1+2+3+4+5+6}{6}=3.5.$$<p>You never roll 3.5; it's the average.</p>"],
 ["Expectations add", "<p>Two dice average $3.5+3.5=7$, even though the dice aren't independent of the sum.</p>"],
 ["Try it", "<p>On average, how many rolls until your first six?</p>"],
])
mod("probability_intro", "Counting your chances", "Probability", [
 ["Probability basics", "<p>For equally likely outcomes, probability is favorable over total.</p>"],
 ["Two dice", "<p>$P(\\text{sum}=7)=\\frac{6}{36}=\\frac16$, the most likely sum.</p>"],
 ["Complementary counting", "<p>Sometimes it's easier to find $1-P(\\text{not it})$, like the birthday problem.</p>"],
 ["Try it", "<p>In a class of 23, what's the chance two share a birthday? (About 50%.)</p>"],
])

# --- Sequences / algebra ---
mod("fibonacci", "Rabbits and the golden ratio", "Sequences", [
 ["A sequence everywhere", "<p>1, 1, 2, 3, 5, 8, 13... each the sum of the two before.</p>"],
 ["Where it comes from", "<p>It counts stair-climbing routes and domino tilings of a $2\\times n$ strip:</p>$$f(n)=f(n-1)+f(n-2).$$"],
 ["The hidden number", "<p>Ratios of consecutive terms approach the golden ratio:</p>$$\\varphi=\\frac{1+\\sqrt5}{2}\\approx 1.618.$$"],
 ["Try it", "<p>How many ways to write $n$ as an ordered sum of 1s and 2s?</p>"],
])
mod("sequences", "Arithmetic and geometric series", "Sequences", [
 ["Two famous patterns", "<p>Arithmetic adds a fixed step; geometric multiplies by a fixed ratio.</p>"],
 ["Their sums", "$$\\text{arith: }\\tfrac{n}{2}(a_1+a_n),\\qquad \\text{geo: }a\\frac{1-r^n}{1-r}.$$"],
 ["Infinite geometric", "<p>If $|r|<1$, the sum converges:</p>$$a+ar+ar^2+\\cdots=\\frac{a}{1-r}.$$"],
 ["Try it", "<p>Evaluate $\\frac12+\\frac14+\\frac18+\\cdots$.</p>"],
])
mod("vieta", "Vieta's formulas", "Algebra", [
 ["Roots without solving", "<p>You can know the sum and product of a quadratic's roots without finding them.</p>"],
 ["The quadratic case", "<p>For $x^2-sx+p$ with roots $r_1,r_2$:</p>$$r_1+r_2=s,\\qquad r_1r_2=p.$$"],
 ["Check", "<p>$x^2-5x+6=(x-2)(x-3)$: roots sum to 5, multiply to 6.</p>"],
 ["Try it", "<p>If $r_1+r_2=5$ and $r_1r_2=6$, find $r_1^2+r_2^2$ without the roots.</p>"],
])
mod("polynomials", "Polynomials and their roots", "Algebra", [
 ["Building blocks", "<p>A degree-$n$ polynomial has $n$ roots (counting multiplicity and complex ones).</p>"],
 ["Factor theorem", "<p>$r$ is a root exactly when $(x-r)$ divides $p(x)$. Factoring and root-finding are the same job.</p>"],
 ["Rational root test", "<p>Any rational root $\\frac{p}{q}$ of an integer polynomial has $p\\mid a_0$ and $q\\mid a_n$.</p>"],
 ["Try it", "<p>Find all rational roots of $2x^3-3x^2-3x+2$.</p>"],
])
mod("amgm", "The inequality everywhere", "Inequalities", [
 ["Two averages", "<p>The arithmetic mean is at least the geometric mean.</p>"],
 ["The statement", "$$\\frac{a+b}{2}\\ge\\sqrt{ab},$$<p>equality only when $a=b$. It follows from $(\\sqrt a-\\sqrt b)^2\\ge 0$.</p>"],
 ["A clean payoff", "<p>For positive $x$: $x+\\frac1x\\ge 2$, hitting 2 at $x=1$.</p>"],
 ["Try it", "<p>Among rectangles with fixed perimeter, show the square has the largest area.</p>"],
])
mod("inequalities", "Bounding things", "Inequalities", [
 ["The art of bounds", "<p>Often you don't need the exact value, just a good inequality.</p>"],
 ["Squares are nonnegative", "<p>Nearly every olympiad inequality traces back to $x^2\\ge 0$.</p>"],
 ["Cauchy-Schwarz taste", "$$(a_1b_1+a_2b_2)^2\\le (a_1^2+a_2^2)(b_1^2+b_2^2).$$"],
 ["Try it", "<p>Show $a^2+b^2+c^2\\ge ab+bc+ca$ for all reals.</p>"],
])
mod("functional_eq", "Functional equations", "Algebra", [
 ["Equations about functions", "<p>Instead of solving for a number, you solve for a whole function.</p>"],
 ["A classic", "<p>If $f(x+y)=f(x)+f(y)$ for all reals and $f$ is reasonable, then $f(x)=cx$.</p>"],
 ["Strategy", "<p>Plug in clever values: $x=y=0$, then $y=x$, then $y=-x$, to pin the function down.</p>"],
 ["Try it", "<p>Find all $f$ with $f(x+y)=f(x)+f(y)$ and $f(xy)=f(x)f(y)$.</p>"],
])
mod("telescoping", "A sum that looks scary", "Algebra", [
 ["Ninety-nine fractions", "<p>Evaluate</p>$$\\sum_{n=1}^{99}\\frac{1}{n(n+1)}.$$<p>You only do one subtraction.</p>"],
 ["Split each term", "$$\\frac{1}{n(n+1)}=\\frac1n-\\frac{1}{n+1}.$$<p>Almost everything cancels.</p>"],
 ["The answer", "$$1-\\frac{1}{100}=\\frac{99}{100}.$$"],
 ["Try it", "<p>Telescope $\\sum \\frac{1}{n(n+1)(n+2)}$.</p>"],
])
mod("sum_squares", "Why the squares add up", "Algebra", [
 ["Back to the chessboard", "<p>The 204 squares on a board were $1^2+\\cdots+8^2$. Is there a formula?</p>"],
 ["The formula", "$$1^2+2^2+\\cdots+n^2=\\frac{n(n+1)(2n+1)}{6}.$$<p>At $n=8$: $\\frac{8\\cdot9\\cdot17}{6}=204$.</p>"],
 ["Proof idea", "<p>Induction closes it up; the base case and step both check.</p>"],
 ["Try it", "<p>Find a formula for $1^3+2^3+\\cdots+n^3$ and notice what it equals.</p>"],
])
mod("complex_intro", "Imagining new numbers", "Algebra", [
 ["Beyond the reals", "<p>Define $i$ with $i^2=-1$. Suddenly every polynomial has roots.</p>"],
 ["Arithmetic", "<p>Add and multiply like binomials, using $i^2=-1$: $(a+bi)(c+di)=(ac-bd)+(ad+bc)i$.</p>"],
 ["Geometry", "<p>Multiplying by $i$ rotates the plane $90^\\circ$. Complex numbers are points with built-in rotation.</p>"],
 ["Try it", "<p>Compute $(1+i)^2$ and $(1+i)^8$.</p>"],
])
mod("recursion", "Recursion and recurrences", "Combinatorics", [
 ["Solving by self-reference", "<p>Many counts satisfy a rule linking each value to earlier ones.</p>"],
 ["Tower of Hanoi", "<p>Moving $n$ disks needs $T_n=2T_{n-1}+1$, so $T_n=2^n-1$.</p>"],
 ["Reading recurrences", "<p>Compute small cases, guess the pattern, then prove it by induction.</p>"],
 ["Try it", "<p>How many regions do $n$ lines in general position cut the plane into?</p>"],
])

# --- Competitions / HiMCM ---
mod("contest_intro", "Our first contest season", "Competitions", [
 ["Why compete", "<p>Contests are optional, but a fun way to sharpen skills under a clock.</p>"],
 ["Good habits", "<p>Read carefully, try small cases, and skip-and-return without panic.</p>"],
 ["A drill problem", "<p>How many divisors does 2024 have? Factor first: $2024=2^3\\cdot11\\cdot23$, so $(3{+}1)(1{+}1)(1{+}1)=16$.</p>"],
 ["Try it", "<p>How many divisors does 360 have?</p>"],
])
mod("contest_season", "Competition season", "Competitions", [
 ["The events", "<p>AMC 10/12, then AIME, then ARML in spring. Each rewards different strengths.</p>"],
 ["A drilled problem", "<p>Ordered pairs with $\\frac1x+\\frac1y=\\frac1{12}$: rewrite as $(x-12)(y-12)=144$. With 15 divisors, there are 15 pairs.</p>"],
 ["The point", "<p>Turn the unfamiliar into the familiar. That habit outlasts any score.</p>"],
 ["Try it", "<p>Count ordered pairs with $\\frac1x+\\frac1y=\\frac1{6}$.</p>"],
])
mod("arml", "Getting ready for ARML", "Competitions", [
 ["A team sport", "<p>ARML is built for teams, so we practice it like one.</p>"],
 ["Relay rounds", "<p>Your answer feeds your teammate's problem. One slip poisons the chain, so accuracy matters most.</p>"],
 ["A relay taste", "<p>Given $T=36$: a rectangle has perimeter $T$, twice as long as wide. Width 6, area 72.</p>"],
 ["The habit", "<p>Pass answers clearly, double-check, and trust your teammates.</p>"],
])
mod("modeling", "Learning to model", "Modeling", [
 ["A different sport", "<p>Modeling turns a vague real-world question into something you can compute, honestly.</p>"],
 ["The loop", "<p>Assume, build, solve, then check by nudging the inputs.</p>"],
 ["A toy model", "<p>Coffee cooling: $\\frac{dT}{dt}=-k(T-A)$ gives $T(t)=A+(T_0-A)e^{-kt}$.</p>"],
 ["Sensitivity", "<p>How much does the answer move when $k$ is uncertain? That question is the heart of a good model.</p>"],
])
mod("himcm_prep", "Getting ready for HiMCM", "Modeling", [
 ["The contest", "<p>A long November weekend: pick an open problem, build a model, write a full paper.</p>"],
 ["Estimate first", "<p>A rough Fermi estimate catches order-of-magnitude mistakes before they cost you a day.</p>"],
 ["Write as you go", "<p>The one-page summary is read first, so we draft it early and defend it.</p>"],
 ["Plan", "<p>Assumptions, model, analysis, results, and an honest list of limitations.</p>"],
])
mod("himcm_recap", "Inside the HiMCM weekend", "Modeling", [
 ["How it went", "<p>Three days of building, testing, discarding, and rebuilding a model.</p>"],
 ["Day by day", "<p>Friday: assumptions. Saturday: first model and tests. Sunday: refine, sensitivity, write.</p>"],
 ["A saved hour", "<p>An early estimate flagged an assumption off by a factor of ten. Catching it Saturday was a relief.</p>"],
 ["Lesson", "<p>The hard part was deciding what to leave out so the model stayed honest.</p>"],
])
mod("himcm_results", "HiMCM results", "Competitions", [
 ["The news", "<p>Our team earned a Finalist designation on Problem B, competing as Team #17561.</p>"],
 ["What lifted it", "<p>The sensitivity analysis: showing the recommendation held up when inputs shifted by 10%.</p>"],
 ["Takeaways", "<p>Write as you solve, treat assumptions as a feature, and estimate before elaborating.</p>"],
 ["Thanks", "<p>Congratulations to the team and everyone at the fall modeling workshops.</p>"],
])

# --- Year wraps ---
mod("year_wrap1", "One year of problems", "Community", [
 ["Looking back", "<p>From five students and a borrowed table to a full room. Thanks for a great first year.</p>"],
 ["What we covered", "<p>Counting, divisibility, three proofs of Pythagoras, pigeonhole, induction, expected value, and our first contests.</p>"],
 ["See you in fall", "<p>Keep noticing the math around you over the summer.</p>"],
])
mod("year_wrap2", "Two years in", "Community", [
 ["A bigger circle", "<p>This year we ran our first HiMCM team and our first ARML practice block.</p>"],
 ["The best part", "<p>Not the results, but a new member explaining an idea to the whole room.</p>"],
 ["Onward", "<p>We move to the Teen Section in the fall. Bring a friend.</p>"],
])
mod("year_wrap3", "Year-end problem marathon", "Community", [
 ["A relay finale", "<p>We closed the year with a relay of everyone's favorite problems.</p>"],
 ["The closing problem", "<p>$S=\\frac12+\\frac14+\\frac18+\\cdots$. Two roads, one answer: $S=1$.</p>"],
 ["Thank you", "<p>Applications for next year's team are open over the summer. Have a problem-filled break.</p>"],
])

# ---------------------------------------------------------------------------
# EXTRA content beats appended to each module so every deck is substantial.
# Each is [heading, html]; math uses TeX.
# ---------------------------------------------------------------------------
import hashlib
EXTRA = {
 "welcome_gauss": [
  ["What we do here", "<p>We pick problems that look simple and chase them until they surprise us. You will be wrong sometimes. That is the job.</p>"],
  ["Warm-up", "<p>Add the first ten even numbers: $2+4+\\cdots+20$. Spot a shortcut before brute force.</p>"],
  ["A second pattern", "<p>The triangular numbers $1,3,6,10,15$ are partial sums $1+2+\\cdots+n$. Each is $\\frac{n(n+1)}{2}$.</p>"],
  ["Why pairing works", "<p>Reverse the sum and add it to itself. Every column totals $n+1$, and there are $n$ columns, so twice the sum is $n(n+1)$.</p>"],
  ["A picture", "<p>Two staircases of dots form a rectangle $n$ by $n+1$. Half of it is your sum.</p>"],
  ["Going further", "<p>What is $1+3+5+\\cdots+(2n-1)$? Try small cases and guess.</p>"],
 ],
 "welcome_squares": [
  ["Warm-up", "<p>Count the rectangles (not just squares) on a $2\\times 2$ grid of lines. Careful counting matters.</p>"],
  ["Build it up", "<p>An $n\\times n$ board has $\\sum_{k=1}^{n}k^2$ squares. We will see a closed form for that sum.</p>"],
  ["Where it shows up", "<p>Sums of squares appear in averages, variance, and the geometry of pyramids.</p>"],
  ["A guess", "<p>Compute the sum for $n=1,2,3,4$: you get $1,5,14,30$. Differences are the squares again.</p>"],
  ["Going further", "<p>Can you find the number of cubes in a stacked corner of side $n$?</p>"],
 ],
 "welcome_lockers": [
  ["Try a smaller case", "<p>Do the same with 10 lockers and 10 students by hand. Which stay open?</p>"],
  ["The key question", "<p>A locker ends open exactly when it is toggled an odd number of times. When does that happen?</p>"],
  ["Divisor pairing", "<p>Divisors pair up as $d$ and $n/d$, an even count, unless $d=n/d$, i.e. $n$ is a perfect square.</p>"],
  ["Name the survivors", "<p>The open lockers are exactly $1,4,9,16,\\dots,961$ for 1000 lockers.</p>"],
  ["Going further", "<p>With 2026 lockers, how many stay open?</p>"],
 ],
 "welcome_chocolate": [
  ["Try small bars", "<p>Snap a $1\\times3$ bar, then a $2\\times2$. Count the snaps each time.</p>"],
  ["Count the pieces", "<p>Track the number of pieces, not the snaps. Each snap raises the piece count by one.</p>"],
  ["An invariant in disguise", "<p>This is our first taste of invariants: the quantity \"snaps minus pieces\" never changes.</p>"],
  ["Why order is irrelevant", "<p>No matter the path, you go from 1 piece to $mn$ pieces, so always $mn-1$ snaps.</p>"],
  ["Going further", "<p>What if a snap could break along a curve? Why does the argument break too?</p>"],
 ],
 "counting": [
  ["Two rules", "<p>The addition rule (either/or) and the multiplication rule (this then that) are the backbone of counting.</p>"],
  ["A worked example", "<p>How many 3-letter codes use letters A to E with no repeats? $5\\cdot 4\\cdot 3=60$.</p>"],
  ["Order matters or not", "<p>Permutations count arrangements; combinations count selections. Dividing out the order links them.</p>"],
  ["Factorials", "<p>$n!$ counts the ways to arrange $n$ distinct items. It grows shockingly fast.</p>"],
  ["A pitfall", "<p>Double counting is the most common error. Always ask: did I count anything twice?</p>"],
  ["Going further", "<p>How many ways can 8 people sit around a round table? (Rotations are the same.)</p>"],
 ],
 "counting_grid": [
  ["Smaller grids", "<p>Count paths on a $2\\times 2$ grid by hand: there are 6. Check it against $\\binom{4}{2}$.</p>"],
  ["Why choosing works", "<p>A path is a word in R's and U's. Choosing the positions of the U's fixes the word.</p>"],
  ["A blocked corner", "<p>Forbid one intersection: count all paths, subtract those passing through it.</p>"],
  ["Pascal connection", "<p>The number of paths to each corner is a Pascal's triangle entry.</p>"],
  ["Going further", "<p>Count paths from $(0,0)$ to $(m,n)$ in general: $\\binom{m+n}{n}$.</p>"],
 ],
 "count_two_ways": [
  ["The principle", "<p>One set, two honest counts, one equation. This is double counting.</p>"],
  ["Handshake lemma", "<p>Summing everyone's handshakes counts each handshake twice: $\\sum \\deg = 2E$.</p>"],
  ["Another identity", "<p>$\\sum_{k=0}^n k\\binom{n}{k}=n2^{n-1}$ by counting (committee, then chair) two ways.</p>"],
  ["A pitfall", "<p>Both counts must describe the exact same set. Mismatched sets give false identities.</p>"],
  ["Going further", "<p>Prove $\\binom{n}{k}=\\binom{n}{n-k}$ by counting what you leave out.</p>"],
 ],
 "stars_bars": [
  ["Restate it", "<p>Putting $n$ balls in $k$ boxes equals counting nonnegative solutions of $x_1+\\cdots+x_k=n$.</p>"],
  ["The bijection", "<p>Each solution is a row of stars and bars; choosing bar positions is the count.</p>"],
  ["Worked example", "<p>Solutions of $a+b+c+d=7$: $\\binom{10}{3}=120$.</p>"],
  ["With a minimum", "<p>If each box needs at least one, hand out one first, then distribute the rest.</p>"],
  ["A pitfall", "<p>Stars and bars needs identical balls. Distinct balls is a different (bigger) count.</p>"],
  ["Going further", "<p>How many ways to write 12 as an ordered sum of 4 positive integers?</p>"],
 ],
 "binomial": [
  ["Small cases", "<p>Expand $(x+y)^2$ and $(x+y)^3$ by hand and read off the coefficients.</p>"],
  ["Why the coefficients count", "<p>Each term picks $y$ from some factors and $x$ from the rest; that is a choice.</p>"],
  ["Symmetry", "<p>The coefficients read the same forwards and backwards: $\\binom{n}{k}=\\binom{n}{n-k}$.</p>"],
  ["A useful trick", "<p>Differentiating the identity gives sums like $\\sum k\\binom{n}{k}$ for free.</p>"],
  ["Going further", "<p>Find the constant term in $\\left(x+\\frac1x\\right)^6$.</p>"],
 ],
 "pascal": [
  ["Build it", "<p>Write the first six rows. Every interior entry is the sum of the two above.</p>"],
  ["Symmetry and ends", "<p>Each row is symmetric and starts and ends with 1.</p>"],
  ["Powers of two", "<p>Row $n$ sums to $2^n$, the number of subsets of an $n$-set.</p>"],
  ["Diagonals", "<p>The third diagonal holds the triangular numbers; shallow diagonals hold Fibonacci numbers.</p>"],
  ["A pitfall", "<p>Rows are zero-indexed: row $n$ has $n+1$ entries.</p>"],
  ["Going further", "<p>Color the odd entries. What famous fractal appears?</p>"],
 ],
 "div9": [
  ["The rule for 3", "<p>The same digit-sum trick works for 3, because $10\\equiv 1\\pmod 3$ too.</p>"],
  ["Worked check", "<p>Is 8\\,127 divisible by 9? Digits sum to 18, which is, so yes.</p>"],
  ["The rule for 11", "<p>Alternate signs on digits, since $10\\equiv -1\\pmod{11}$.</p>"],
  ["Why remainders behave", "<p>Mod 9, a number equals its digit sum, so you can replace one with the other.</p>"],
  ["Going further", "<p>Build a divisibility rule for 99 using two-digit blocks.</p>"],
 ],
 "casting_nines": [
  ["Digit roots", "<p>Repeatedly summing digits gives the digit root, which is the value mod 9 (with 9 for multiples of 9).</p>"],
  ["Checking sums", "<p>The check works for addition too: digit roots add the way the numbers do.</p>"],
  ["A worked error", "<p>If a long multiplication's digit roots disagree, you definitely slipped somewhere.</p>"],
  ["The limitation", "<p>A matching check can still hide an error, since it only sees the remainder mod 9.</p>"],
  ["Going further", "<p>Why does swapping two digits never change the nines check?</p>"],
 ],
 "modular": [
  ["Build intuition", "<p>Days of the week are mod 7. Hours are mod 12 or 24. You already think modularly.</p>"],
  ["Arithmetic rules", "<p>You may add, subtract, and multiply congruences. Division needs care.</p>"],
  ["Worked example", "<p>What day is it 100 days from Monday? $100\\equiv 2\\pmod 7$, so Wednesday.</p>"],
  ["Powers cycle", "<p>Powers mod $m$ eventually repeat; finding the period cracks huge exponents.</p>"],
  ["A pitfall", "<p>You cannot always divide: $2x\\equiv 2\\pmod 4$ has two solutions, not one.</p>"],
  ["Going further", "<p>Find the remainder of $2^{1000}$ when divided by 7.</p>"],
 ],
 "euclid": [
  ["Run it again", "<p>Compute $\\gcd(1071,462)$ step by step until the remainder is zero.</p>"],
  ["Why it terminates", "<p>Remainders strictly shrink and stay nonnegative, so the process must stop.</p>"],
  ["Back-substitution", "<p>Unwinding the steps writes the gcd as $ax+by$, the heart of Bezout's identity.</p>"],
  ["An application", "<p>To reduce a fraction fully, divide top and bottom by their gcd.</p>"],
  ["Going further", "<p>Use the algorithm to solve $17x\\equiv 1\\pmod{43}$.</p>"],
 ],
 "primes": [
  ["A sieve", "<p>The Sieve of Eratosthenes crosses out multiples to leave the primes up to $n$.</p>"],
  ["Building blocks", "<p>Every integer factors uniquely into primes. That uniqueness does a lot of work.</p>"],
  ["Gaps and clusters", "<p>Primes thin out but never stop, and twin primes like 11 and 13 keep appearing.</p>"],
  ["A worked idea", "<p>$N=p_1\\cdots p_k+1$ is divisible by no listed prime, which forces a new one.</p>"],
  ["Going further", "<p>Show there are arbitrarily long runs of consecutive composite numbers.</p>"],
 ],
 "mod_inverse": [
  ["What an inverse is", "<p>The inverse of $a$ mod $m$ is the $x$ with $ax\\equiv 1$. It exists iff $\\gcd(a,m)=1$.</p>"],
  ["Finding one", "<p>Run the Euclidean algorithm backward, or use Fermat when $m$ is prime.</p>"],
  ["Worked example", "<p>Mod 11, the inverse of 4 is 3, since $4\\cdot 3=12\\equiv 1$.</p>"],
  ["Why primes are nice", "<p>Mod a prime, every nonzero element is invertible, so you can divide freely.</p>"],
  ["Going further", "<p>Solve $7x\\equiv 3\\pmod{26}$.</p>"],
 ],
 "number_bases": [
  ["Counting up", "<p>In base 2 you count 1, 10, 11, 100. Each carry happens at the base, not at ten.</p>"],
  ["Place value", "<p>Digit $d$ in position $k$ contributes $d\\cdot b^k$.</p>"],
  ["Converting back", "<p>Repeatedly divide by the base; the remainders are the digits, last first.</p>"],
  ["Hexadecimal", "<p>Base 16 packs four binary digits into one symbol, which is why computers love it.</p>"],
  ["Going further", "<p>What is $101101_2$ in base 10, and in base 16?</p>"],
 ],
 "diophantine": [
  ["When solutions exist", "<p>$ax+by=c$ has integer solutions exactly when $\\gcd(a,b)$ divides $c$.</p>"],
  ["Finding them all", "<p>One solution plus the gcd shifts gives the whole family.</p>"],
  ["A factoring tactic", "<p>Rearrange into a product equals constant, then test factor pairs.</p>"],
  ["A pitfall", "<p>Do not forget negative factors; they give extra solutions.</p>"],
  ["Going further", "<p>Find all integer solutions of $x^2-y^2=15$.</p>"],
 ],
 "pythagoras": [
  ["A second proof", "<p>Drop the altitude to the hypotenuse to make two similar triangles, then chase ratios.</p>"],
  ["Pythagorean triples", "<p>$(3,4,5)$, $(5,12,13)$, $(8,15,17)$ are right triangles with whole sides.</p>"],
  ["Generating triples", "<p>For $m>n$, the triple $(m^2-n^2,\\,2mn,\\,m^2+n^2)$ always works.</p>"],
  ["The converse", "<p>If $a^2+b^2=c^2$, the triangle must be right. The theorem runs both ways.</p>"],
  ["A pitfall", "<p>The relation only holds for right triangles. Check the angle first.</p>"],
  ["Going further", "<p>Is there a right triangle with all three sides odd? Why not?</p>"],
 ],
 "inscribed": [
  ["The statement again", "<p>An inscribed angle is half the central angle on the same arc.</p>"],
  ["Thales as a special case", "<p>An angle in a semicircle is a right angle.</p>"],
  ["Cyclic quadrilaterals", "<p>Opposite angles of a cyclic quadrilateral sum to $180^\\circ$.</p>"],
  ["A worked angle", "<p>If an arc measures $80^\\circ$, every inscribed angle on it is $40^\\circ$.</p>"],
  ["Going further", "<p>Prove the tangent-chord angle equals the inscribed angle on the cut-off arc.</p>"],
 ],
 "power_point": [
  ["Three configurations", "<p>The point can be inside, on, or outside the circle. The product rule adapts to each.</p>"],
  ["The tangent case", "<p>From outside, $PT^2=PA\\cdot PB$ links a tangent to any secant.</p>"],
  ["Worked example", "<p>Secant pieces 4 and 9 give a tangent length $\\sqrt{36}=6$.</p>"],
  ["The radical axis", "<p>Points with equal power to two circles form a line, the radical axis.</p>"],
  ["Going further", "<p>Three circles give three radical axes. Show they meet at one point.</p>"],
 ],
 "euler_poly": [
  ["Test more solids", "<p>Try a prism, a pyramid, and a soccer-ball shape. The alternating sum stays 2.</p>"],
  ["A proof sketch", "<p>Flatten to a planar graph and remove edges and vertices without changing $V-E+F$.</p>"],
  ["The five Platonic solids", "<p>Euler's relation limits the regular solids to exactly five.</p>"],
  ["Beyond the sphere", "<p>On a doughnut the formula changes to $V-E+F=0$. Topology is hiding here.</p>"],
  ["Going further", "<p>A soccer ball has 12 pentagons and 20 hexagons. Find $V$, $E$, and $F$.</p>"],
 ],
 "graphs": [
  ["Vocabulary", "<p>Vertices, edges, degree, path, cycle. A little language unlocks a lot.</p>"],
  ["Euler vs Hamilton", "<p>Euler trails use every edge once; Hamiltonian paths visit every vertex once. Very different difficulty.</p>"],
  ["The handshake lemma", "<p>The number of odd-degree vertices is always even.</p>"],
  ["Modeling with graphs", "<p>Friendships, road maps, and schedules all become graphs.</p>"],
  ["Going further", "<p>Can six people always include three mutual friends or three mutual strangers?</p>"],
 ],
 "picks": [
  ["Try it", "<p>Draw a few lattice polygons and check the area count against the formula.</p>"],
  ["Boundary points", "<p>Count lattice points on each edge using the gcd of its run and rise.</p>"],
  ["Why halves and minus one", "<p>Each boundary point is shared, and the lone $-1$ accounts for the polygon's outside.</p>"],
  ["A pitfall", "<p>Pick's theorem needs all corners on lattice points.</p>"],
  ["Going further", "<p>Use Pick to find the area of a pentagon you draw on the grid.</p>"],
 ],
 "triangle_centers": [
  ["Build each center", "<p>Medians meet at the centroid; bisectors at the incenter; perpendicular bisectors at the circumcenter.</p>"],
  ["The orthocenter", "<p>The three altitudes also meet at a single point.</p>"],
  ["The Euler line", "<p>Centroid, circumcenter, and orthocenter are collinear, with the centroid dividing $2:1$.</p>"],
  ["A worked location", "<p>In a right triangle the circumcenter is the midpoint of the hypotenuse.</p>"],
  ["Going further", "<p>Where do all four centers coincide? (Equilateral triangles.)</p>"],
 ],
 "geometry_transforms": [
  ["The toolbox", "<p>Translation, rotation, reflection, and glide reflection are the rigid motions of the plane.</p>"],
  ["Composition", "<p>Two reflections make a rotation or a translation, depending on the mirror lines.</p>"],
  ["A reflection trick", "<p>Reflect a target across a wall to turn a bounce path into a straight line.</p>"],
  ["Symmetry groups", "<p>The symmetries of a shape form a group; the square has eight.</p>"],
  ["Going further", "<p>Find the shortest path from $A$ to a river and then to $B$.</p>"],
 ],
 "pigeonhole_socks": [
  ["State it cleanly", "<p>More pigeons than holes forces a hole with at least two pigeons.</p>"],
  ["Worked example", "<p>Among 13 people, two share a birth month.</p>"],
  ["A harder one", "<p>In any group, two people have the same number of friends inside it.</p>"],
  ["Choosing the holes", "<p>The whole skill is deciding what the boxes should be.</p>"],
  ["Going further", "<p>Pick any 5 integers. Show two have a difference divisible by 4.</p>"],
 ],
 "pigeonhole": [
  ["Generalized form", "<p>With $n$ items in $k$ boxes, some box holds at least $\\lceil n/k\\rceil$.</p>"],
  ["A geometry use", "<p>Five points in a unit square force two within $\\frac{\\sqrt2}{2}$.</p>"],
  ["A number-theory use", "<p>Among $n+1$ numbers from $1$ to $2n$, two are consecutive.</p>"],
  ["A pitfall", "<p>Pigeonhole proves existence, not a method to find the pair.</p>"],
  ["Going further", "<p>Show some multiple of 2026 uses only digits 0 and 1.</p>"],
 ],
 "invariants": [
  ["The strategy", "<p>When moves change things, hunt for a quantity that never changes.</p>"],
  ["Color invariants", "<p>Coloring a board reveals which configurations are reachable.</p>"],
  ["Parity invariants", "<p>Often the parity of a count is the thing that stays fixed.</p>"],
  ["A worked impossibility", "<p>Two opposite corners off a chessboard cannot be domino-tiled; the colors do not balance.</p>"],
  ["Going further", "<p>Replace pairs on a board with their difference. What stays fixed?</p>"],
 ],
 "parity": [
  ["Odd and even", "<p>Sums and products of parities follow simple, unbreakable rules.</p>"],
  ["Handshake parity", "<p>The count of people who shook an odd number of hands is even.</p>"],
  ["A tiling argument", "<p>If a coloring gives unequal color counts, no domino tiling can exist.</p>"],
  ["A pitfall", "<p>Parity proves impossibility, but possibility needs an actual construction.</p>"],
  ["Going further", "<p>Can a knight return to its start after an odd number of moves?</p>"],
 ],
 "coloring": [
  ["The idea", "<p>A clever coloring exposes hidden structure and forces contradictions.</p>"],
  ["Checkerboard colorings", "<p>Two colors often reveal a piece always covers one of each.</p>"],
  ["Three or more colors", "<p>Some boards need a three-coloring to expose the obstruction.</p>"],
  ["A worked case", "<p>An L-tromino on a colored board always covers a fixed color pattern.</p>"],
  ["Going further", "<p>Can you tile a $10\\times10$ board with 1-by-4 tiles? Color it to decide.</p>"],
 ],
 "induction": [
  ["The two parts", "<p>A base case and an inductive step. Miss either and the chain fails.</p>"],
  ["A clean example", "<p>$1+3+\\cdots+(2n-1)=n^2$ falls out in one step.</p>"],
  ["Strong induction", "<p>Sometimes you assume all smaller cases, not just the previous one.</p>"],
  ["A famous trap", "<p>The \"all horses are the same color\" gag fails because its base case does not link to two.</p>"],
  ["Going further", "<p>Prove $2^n > n^2$ for all $n\\ge 5$.</p>"],
 ],
 "nim_games": [
  ["Play first", "<p>Try the game by hand and feel out which positions are losing.</p>"],
  ["Losing positions", "<p>A position you want to hand your opponent is a losing one for them.</p>"],
  ["The XOR rule", "<p>In Nim, a position is losing exactly when the XOR of pile sizes is zero.</p>"],
  ["Worked move", "<p>From piles 3,4,5 the XOR is 2; remove 2 from the 3-pile to win.</p>"],
  ["Going further", "<p>Analyze the subtraction game where you may remove 1, 2, or 3.</p>"],
 ],
 "logic": [
  ["Set the rules", "<p>Knights always tell the truth; knaves always lie. Every statement constrains roles.</p>"],
  ["Casework", "<p>Assume a role, follow the consequences, and look for a contradiction.</p>"],
  ["A self-reference", "<p>\"I am a knave\" can never be said truthfully or falsely, so nobody says it.</p>"],
  ["A worked puzzle", "<p>If A says B is a knight and B says they differ, then A is a knave and B a knight.</p>"],
  ["Going further", "<p>Three islanders make claims; sort out who is who.</p>"],
 ],
 "expected_value": [
  ["Definition", "<p>Expected value weights each outcome by its probability and sums.</p>"],
  ["Linearity", "<p>Expectations add, even when events are not independent. This is the secret weapon.</p>"],
  ["Worked example", "<p>The expected number of heads in 10 flips is $10\\cdot\\frac12=5$.</p>"],
  ["Indicator trick", "<p>Break a count into 0/1 indicators and add their expectations.</p>"],
  ["Going further", "<p>On average, how many fixed points does a random shuffle leave?</p>"],
 ],
 "probability_intro": [
  ["Sample spaces", "<p>List the equally likely outcomes, then count the favorable ones.</p>"],
  ["Complementary counting", "<p>Sometimes $1-P(\\text{not it})$ is far easier.</p>"],
  ["Independence", "<p>For independent events, probabilities multiply.</p>"],
  ["A pitfall", "<p>Outcomes are not always equally likely; check before you divide.</p>"],
  ["Going further", "<p>Two dice are rolled. What is the probability the product is even?</p>"],
 ],
 "fibonacci": [
  ["Three appearances", "<p>Rabbits, stairs, and domino tilings all give the same recurrence.</p>"],
  ["Why the recurrence", "<p>The last move splits the count into two earlier cases that add.</p>"],
  ["The golden ratio", "<p>Ratios of consecutive terms approach $\\varphi=\\frac{1+\\sqrt5}{2}$.</p>"],
  ["A surprising identity", "<p>$F_1+F_2+\\cdots+F_n=F_{n+2}-1$.</p>"],
  ["Going further", "<p>Show consecutive Fibonacci numbers are always coprime.</p>"],
 ],
 "sequences": [
  ["Two families", "<p>Arithmetic adds a step; geometric multiplies by a ratio.</p>"],
  ["Worked sums", "<p>An arithmetic series is (average term) times (count).</p>"],
  ["Convergence", "<p>A geometric series converges exactly when $|r|<1$.</p>"],
  ["A pitfall", "<p>Infinite sums need $|r|<1$; otherwise they diverge.</p>"],
  ["Going further", "<p>Write $0.\\overline{9}$ as a geometric series and find its value.</p>"],
 ],
 "vieta": [
  ["The quadratic", "<p>Roots of $x^2-sx+p$ sum to $s$ and multiply to $p$.</p>"],
  ["Cubics too", "<p>For a monic cubic, the roots sum to minus the next coefficient.</p>"],
  ["Symmetric sums", "<p>Power sums of roots follow from $s$ and $p$ without solving.</p>"],
  ["Worked example", "<p>If roots sum to 5 and multiply to 6, then $r_1^2+r_2^2=25-12=13$.</p>"],
  ["Going further", "<p>Find the sum of the squares of the roots of $x^3-2x^2+3x-4$.</p>"],
 ],
 "polynomials": [
  ["Roots and factors", "<p>$r$ is a root exactly when $(x-r)$ divides the polynomial.</p>"],
  ["Counting roots", "<p>A degree-$n$ polynomial has exactly $n$ roots over the complex numbers.</p>"],
  ["Rational root test", "<p>Rational roots $p/q$ satisfy $p\\mid a_0$ and $q\\mid a_n$.</p>"],
  ["A pitfall", "<p>Multiplicity counts: $(x-1)^2$ has a double root, not two roots.</p>"],
  ["Going further", "<p>Factor $x^3-6x^2+11x-6$ fully.</p>"],
 ],
 "amgm": [
  ["The two-term case", "<p>$\\frac{a+b}{2}\\ge\\sqrt{ab}$, with equality only when $a=b$.</p>"],
  ["Why it is true", "<p>It is just $(\\sqrt a-\\sqrt b)^2\\ge 0$ rearranged.</p>"],
  ["Many terms", "<p>The mean of $n$ nonnegatives is at least their $n$th-root product.</p>"],
  ["A worked use", "<p>$x+\\frac1x\\ge 2$ for positive $x$.</p>"],
  ["Going further", "<p>Maximize $xyz$ when $x+y+z=9$ with positive reals.</p>"],
 ],
 "inequalities": [
  ["Start from squares", "<p>Most inequalities reduce to a sum of squares being nonnegative.</p>"],
  ["Cauchy-Schwarz", "<p>A two-term version already proves striking bounds.</p>"],
  ["Rearrangement", "<p>Sorting both sequences the same way maximizes the paired sum.</p>"],
  ["A pitfall", "<p>Squaring can flip an inequality if a side is negative.</p>"],
  ["Going further", "<p>Show $a^2+b^2+c^2\\ge ab+bc+ca$.</p>"],
 ],
 "functional_eq": [
  ["Solve for a function", "<p>You hunt for every function satisfying a rule, not just a number.</p>"],
  ["Plug in values", "<p>Try $x=y=0$, then $y=x$, then $y=-x$ to extract structure.</p>"],
  ["Cauchy's equation", "<p>$f(x+y)=f(x)+f(y)$ forces $f(x)=cx$ under mild conditions.</p>"],
  ["A pitfall", "<p>Always check your candidate function actually satisfies the equation.</p>"],
  ["Going further", "<p>Find all $f$ with $f(x)f(y)=f(x+y)$.</p>"],
 ],
 "telescoping": [
  ["Spot the difference", "<p>Rewrite each term as $g(n)-g(n+1)$ so neighbors cancel.</p>"],
  ["Worked sum", "<p>$\\sum \\frac{1}{n(n+1)}$ collapses to $1-\\frac{1}{N+1}$.</p>"],
  ["Partial fractions", "<p>Splitting a fraction is how you find the telescoping form.</p>"],
  ["A pitfall", "<p>Track the leftover end terms carefully; that is the whole answer.</p>"],
  ["Going further", "<p>Telescope $\\sum \\frac{1}{n(n+2)}$.</p>"],
 ],
 "sum_squares": [
  ["The chessboard link", "<p>The 204 squares on a board are $1^2+\\cdots+8^2$.</p>"],
  ["The formula", "<p>$\\sum_{k=1}^n k^2=\\frac{n(n+1)(2n+1)}{6}$.</p>"],
  ["Proof by induction", "<p>Check $n=1$, then add $(n+1)^2$ and simplify.</p>"],
  ["A surprise", "<p>$\\sum k^3=\\left(\\sum k\\right)^2$. The cubes sum to a perfect square.</p>"],
  ["Going further", "<p>Find a formula for $1^2+3^2+5^2+\\cdots+(2n-1)^2$.</p>"],
 ],
 "complex_intro": [
  ["A new number", "<p>Define $i$ with $i^2=-1$ and every polynomial gains its roots.</p>"],
  ["Arithmetic", "<p>Add and multiply like binomials, replacing $i^2$ with $-1$.</p>"],
  ["The plane", "<p>$a+bi$ is the point $(a,b)$; multiplying by $i$ rotates by $90^\\circ$.</p>"],
  ["Modulus", "<p>The size $|a+bi|=\\sqrt{a^2+b^2}$ is the distance to the origin.</p>"],
  ["Going further", "<p>Compute $(1+i)^8$ using the rotation idea.</p>"],
 ],
 "recursion": [
  ["Self-reference", "<p>Define each value from earlier ones, then unwind.</p>"],
  ["Tower of Hanoi", "<p>$T_n=2T_{n-1}+1$ gives $T_n=2^n-1$.</p>"],
  ["Reading a recurrence", "<p>Compute small cases, guess the closed form, prove by induction.</p>"],
  ["A pitfall", "<p>Do not forget base cases; they anchor the whole recurrence.</p>"],
  ["Going further", "<p>How many regions do $n$ lines in general position make?</p>"],
 ],
 "contest_intro": [
  ["Why compete", "<p>Contests are optional fun that sharpen speed and nerve.</p>"],
  ["Test-taking habits", "<p>Read carefully, try small cases, and skip-and-return without panic.</p>"],
  ["A divisor count", "<p>$2024=2^3\\cdot 11\\cdot 23$ has $(3{+}1)(1{+}1)(1{+}1)=16$ divisors.</p>"],
  ["Estimation", "<p>A quick sanity estimate catches answers that are wildly off.</p>"],
  ["Going further", "<p>How many divisors does 360 have?</p>"],
 ],
 "contest_season": [
  ["The ladder", "<p>AMC leads to AIME leads to harder olympiads. Each step rewards new skills.</p>"],
  ["A drilled problem", "<p>$\\frac1x+\\frac1y=\\frac1{12}$ becomes $(x-12)(y-12)=144$, giving 15 pairs.</p>"],
  ["Pace and accuracy", "<p>On the AMC, careful beats fast. One silly error costs a hard problem.</p>"],
  ["Team energy", "<p>Studying together exposes blind spots quickly.</p>"],
  ["Going further", "<p>Count ordered pairs with $\\frac1x+\\frac1y=\\frac16$.</p>"],
 ],
 "arml": [
  ["A team sport", "<p>ARML rewards collaboration, especially in the relay rounds.</p>"],
  ["Relay discipline", "<p>Your answer feeds a teammate, so accuracy beats speed.</p>"],
  ["A relay taste", "<p>Given $T=36$, a rectangle twice as long as wide has area 72.</p>"],
  ["Communication", "<p>Pass answers clearly and double-check before handing them off.</p>"],
  ["Going further", "<p>Design your own three-step relay for the group.</p>"],
 ],
 "modeling": [
  ["A different sport", "<p>Modeling turns a vague question into something you can compute.</p>"],
  ["The loop", "<p>Assume, build, solve, then check by nudging inputs.</p>"],
  ["A cooling model", "<p>Newton's law gives $T(t)=A+(T_0-A)e^{-kt}$.</p>"],
  ["Sensitivity", "<p>How much does the answer move when an input is uncertain?</p>"],
  ["Going further", "<p>Model how long a phone battery lasts under steady use.</p>"],
 ],
 "himcm_prep": [
  ["The contest", "<p>A long weekend: choose a problem, build a model, write a full paper.</p>"],
  ["Estimate first", "<p>A Fermi estimate catches order-of-magnitude mistakes early.</p>"],
  ["Write as you go", "<p>The one-page summary is read first, so draft it early.</p>"],
  ["Roles", "<p>Split research, modeling, and writing, then reconvene often.</p>"],
  ["Going further", "<p>Practice stating three assumptions for a real-world prompt.</p>"],
 ],
 "himcm_recap": [
  ["How it felt", "<p>Three days of building, testing, discarding, and rebuilding.</p>"],
  ["Day by day", "<p>Assumptions, then a first model, then refining and writing.</p>"],
  ["A saved hour", "<p>An early estimate flagged an assumption off by tenfold.</p>"],
  ["The hard part", "<p>Deciding what to leave out so the model stays honest.</p>"],
  ["Going further", "<p>What would you change about our model next time?</p>"],
 ],
 "himcm_results": [
  ["The news", "<p>Our team earned a Finalist designation on Problem B.</p>"],
  ["What lifted it", "<p>A sensitivity analysis showing the recommendation held up.</p>"],
  ["Lessons", "<p>Write as you solve, and treat assumptions as a feature.</p>"],
  ["Credit", "<p>Thanks to everyone at the fall modeling workshops.</p>"],
  ["Going further", "<p>Read the full results writeup in the newsletter.</p>"],
 ],
 "year_wrap1": [
  ["What we built", "<p>From five students to a full room in one year.</p>"],
  ["Topics covered", "<p>Counting, number theory, geometry, pigeonhole, induction, and more.</p>"],
  ["A favorite moment", "<p>A quiet member explaining an idea better than the mentors.</p>"],
  ["Summer challenge", "<p>Keep a notebook of problems you notice in daily life.</p>"],
 ],
 "year_wrap2": [
  ["A bigger circle", "<p>Our first HiMCM team and first ARML practice block.</p>"],
  ["The best part", "<p>Watching members teach each other.</p>"],
  ["Moving up", "<p>We move to the Teen Section in the fall.</p>"],
  ["Summer challenge", "<p>Work through a strand of problems you find hard.</p>"],
 ],
 "year_wrap3": [
  ["A relay finale", "<p>We closed with everyone's favorite problems.</p>"],
  ["The closing sum", "<p>$S=\\frac12+\\frac14+\\cdots=1$, two ways.</p>"],
  ["Team applications", "<p>Tryouts for next year's team are open all summer.</p>"],
  ["Thank you", "<p>To students and parents alike: see you in September.</p>"],
 ],
}

# ---------------------------------------------------------------------------
# Topic -> candidate images (path, caption) for slide visuals.
# ---------------------------------------------------------------------------
IMG = {
 "Welcome":      [("images/usa/u03.jpg","Students at a United States mathematics program"),("images/usa/u02.jpg","An American college mathematics class"),("images/students.jpg","Working through a problem set"),("images/news2/m08.jpg","A tutoring session"),("images/usa/u15.jpg","A university study room")],
 "Combinatorics":[("images/news/abacus-1.jpg","An abacus"),("images/news2/m23.jpg","A bead abacus"),("images/news2/m22.jpg","An abacus and a laptop at Berkeley"),("images/chessboard.jpg","A board to count on"),("images/news2/m02.jpg","Working at the board")],
 "Algebra":      [("images/writing-math.jpg","Working through the algebra"),("images/hero-blackboard.jpg","A board of equations"),("images/news2/m18.jpg","A mathematician at the board"),("images/usa/u10.jpg","The UCLA mathematics building"),("images/usa/u01.jpg","A Cornell University blackboard")],
 "Number theory":[("images/usa/u06.jpg","A slide rule"),("images/news2/m20.jpg","A Keuffel and Esser slide rule"),("images/usa/u09.jpg","A slide rule"),("images/news/blackboard-1.jpg","A working blackboard"),("images/usa/u18.jpg","A calculator")],
 "Geometry":     [("images/usa/u16.jpg","Models of the Platonic solids"),("images/news/geometry-2.jpg","A geometric model"),("images/news/geometry-3.jpg","Basic geometric shapes"),("images/news/geometry-4.jpg","A cubic geometric model"),("images/usa/u17.jpg","A set of polyhedron models")],
 "Graph theory": [("images/usa/u17.jpg","A polyhedron, vertices and edges"),("images/news2/m17.jpg","A polyhedral model"),("images/news/geometry-4.jpg","Connected shapes"),("images/news2/m02.jpg","At the board"),("images/hero-blackboard.jpg","A board of ideas")],
 "Invariants":   [("images/chessboard.jpg","A chessboard"),("images/news/geometry-3.jpg","Shapes that stay fixed"),("images/news/blackboard-1.jpg","Working it out"),("images/news2/m02.jpg","At the board"),("images/hero-blackboard.jpg","A board of equations")],
 "Proof":        [("images/hero-blackboard.jpg","A board of equations"),("images/writing-math.jpg","Writing the argument"),("images/news2/m18.jpg","A mathematician at the board"),("images/news/patterns-3.jpg","A golden spiral"),("images/usa/u01.jpg","A university blackboard")],
 "Probability":  [("images/news2/m17.jpg","A polyhedral model"),("images/chessboard.jpg","A game of chance and skill"),("images/news2/m02.jpg","Working the odds"),("images/students.jpg","Reasoning it out"),("images/usa/u18.jpg","A calculator")],
 "Sequences":    [("images/news/patterns-2.jpg","A natural Fibonacci spiral"),("images/news/patterns-3.jpg","A golden spiral"),("images/news2/m02.jpg","Patterns on the board"),("images/hero-blackboard.jpg","A board of terms"),("images/news/abacus-1.jpg","Counting the terms")],
 "Inequalities": [("images/hero-blackboard.jpg","A board of bounds"),("images/writing-math.jpg","Working the inequality"),("images/news2/m18.jpg","At the board"),("images/usa/u11.jpg","The UCLA mathematics building"),("images/usa/u12.jpg","A university mathematics department")],
 "Game theory":  [("images/chessboard.jpg","A strategy game"),("images/news2/m17.jpg","A model to reason about"),("images/news2/m02.jpg","Analyzing positions"),("images/students.jpg","Thinking ahead"),("images/hero-blackboard.jpg","Working out a strategy")],
 "Logic":        [("images/news2/m02.jpg","At the board"),("images/hero-blackboard.jpg","Laying out the cases"),("images/news/blackboard-1.jpg","Reasoning on the board"),("images/news2/m18.jpg","A careful argument"),("images/students.jpg","Puzzling it through")],
 "Competitions": [("images/usa/u05.jpg","Students at the MATHCOUNTS competition"),("images/news2/m21.jpg","The Ross Mathematics Program"),("images/usa/u03.jpg","A United States mathematics program"),("images/usa/u02.jpg","An American college mathematics class"),("images/usa/u04.jpg","The National Museum of Mathematics"),("images/usa/u08.jpg","The National Museum of Mathematics, New York"),("images/news2/m18.jpg","A mathematician at the board"),("images/usa/u12.jpg","A university mathematics department")],
 "Modeling":     [("images/usa/u12.jpg","A university mathematics department"),("images/news2/m18.jpg","Working at the board"),("images/usa/u08.jpg","The National Museum of Mathematics"),("images/hero-blackboard.jpg","A board of equations"),("images/usa/u02.jpg","A college mathematics class")],
 "Community":    [("images/library.jpg","The Los Gatos Library"),("images/newsletter-feature.jpg","The Los Gatos Math Circle"),("images/hero.jpg","Our circle"),("images/students.jpg","Around the table"),("images/usa/u03.jpg","A mathematics program")],
}

def build_deck(mid):
    base = M[mid]
    beats = list(base["s"]) + EXTRA.get(mid, [])
    topic = base["topic"]
    heads = [b[0] for b in beats if b and b[0]]
    h = int(hashlib.md5(mid.encode()).hexdigest(), 16)
    imgs = IMG.get(topic, IMG["Community"])
    # rotate so different modules of one topic open with different photos
    rot = h % len(imgs)
    imgs = imgs[rot:] + imgs[:rot]

    target = 15 + (h % 6)          # 15..20 total slides (incl. JS title slide)
    content_target = target - 1     # slides we emit here

    deck = []
    deck.append(["Today's plan", "<ul>" + "".join("<li>" + x + "</li>" for x in heads[:6]) + "</ul>"])

    # how many photos to use
    fixed = 1 + 2  # agenda + recap + closing
    img_n = max(2, min(len(imgs), content_target - len(beats) - fixed))
    used = 0
    # interleave: drop a photo after roughly every third beat
    for k, b in enumerate(beats):
        deck.append(b)
        if used < img_n and (k + 1) % 3 == 0:
            p, c = imgs[used]; used += 1
            deck.append(["", "", p, c])
    # any remaining photos go before the recap
    while used < img_n:
        p, c = imgs[used]; used += 1
        deck.append(["", "", p, c])

    deck.append(["What we saw today", "<ul>" + "".join("<li>" + x + "</li>" for x in heads[:7]) + "</ul>"])
    deck.append(["Until next Saturday", "<p>Take the last problem home and sit with it. Bring a pencil, bring a question, and we will see you next week.</p>"])

    # trim extra photos (never the beats, agenda, recap, or closing) if too long
    while len(deck) > content_target:
        for i in range(len(deck) - 3, 0, -1):
            if len(deck[i]) >= 3:  # a photo slide
                deck.pop(i); break
        else:
            break
    return deck

for _mid in list(M.keys()):
    M[_mid]["s"] = build_deck(_mid)

# ---------------------------------------------------------------------------
# Anchor dates from the newsletter timeline -> module id.
# ---------------------------------------------------------------------------
ANCHOR = {
 "2023-09-09":"welcome_gauss","2023-10-07":"counting","2023-11-04":"div9","2023-12-02":"pythagoras",
 "2024-01-13":"pigeonhole_socks","2024-02-10":"contest_intro","2024-03-09":"induction","2024-04-06":"expected_value","2024-06-01":"year_wrap1",
 "2024-09-07":"welcome_squares","2024-10-05":"fibonacci","2024-10-19":"euler_poly","2024-11-02":"modeling","2024-11-23":"himcm_recap","2024-12-07":"casting_nines",
 "2025-01-11":"vieta","2025-01-25":"inscribed","2025-02-08":"contest_season","2025-02-22":"sum_squares","2025-03-08":"count_two_ways","2025-03-22":"euclid","2025-04-12":"arml","2025-05-24":"year_wrap2",
 "2025-09-06":"welcome_lockers","2025-09-20":"counting_grid","2025-10-04":"invariants","2025-10-18":"pigeonhole","2025-11-01":"himcm_prep","2025-11-22":"himcm_recap","2025-12-06":"modular",
 "2026-01-10":"welcome_chocolate","2026-01-24":"pascal","2026-02-14":"himcm_results","2026-03-07":"contest_season","2026-03-21":"graphs","2026-04-11":"telescoping","2026-05-09":"power_point","2026-06-06":"year_wrap3",
}

# Filler curriculum per year (used for non-anchor Saturdays, in order).
FILL = {
 "2023\u201324":["stars_bars","probability_intro","number_bases","parity","binomial","amgm","sequences","primes","logic","coloring","polynomials","recursion","mod_inverse","triangle_centers","geometry_transforms","inequalities","diophantine","functional_eq","picks","complex_intro","nim_games"],
 "2024\u201325":["binomial","parity","number_bases","amgm","stars_bars","primes","sequences","coloring","logic","polynomials","mod_inverse","recursion","triangle_centers","inequalities","picks","geometry_transforms","diophantine","complex_intro","functional_eq","probability_intro","nim_games"],
 "2025\u201326":["parity","stars_bars","amgm","binomial","sequences","primes","number_bases","polynomials","coloring","logic","recursion","mod_inverse","inequalities","triangle_centers","picks","diophantine","geometry_transforms","functional_eq","complex_intro","nim_games","probability_intro"],
}

# ---------------------------------------------------------------------------
# Build the schedule.
# ---------------------------------------------------------------------------
SEASONS = [
 ("2023\u201324", date(2023,9,9),  date(2024,6,1)),
 ("2024\u201325", date(2024,9,7),  date(2025,5,24)),
 ("2025\u201326", date(2025,9,6),  date(2026,6,6)),
]

# Cancelled Saturdays (no meeting). date -> reason.
CANCELLED = {
 "2023-10-21": "Cancelled",
 "2024-04-13": "Cancelled",
 "2025-02-08": "Cancelled",
 "2025-11-08": "Cancelled",
}
MONTHS=["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
WD=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def last_monday_may(y):
    d=date(y,5,31)
    while d.weekday()!=0: d-=timedelta(days=1)
    return d
def thanksgiving_sat(y):
    d=date(y,11,1)
    while d.weekday()!=3: d+=timedelta(days=1)
    d+=timedelta(days=21)        # 4th Thursday
    return d+timedelta(days=2)   # Saturday after
def last_sat_march(y):
    d=date(y,3,31)
    while d.weekday()!=5: d-=timedelta(days=1)
    return d

def break_label(d, end):
    if d==end: return None
    y=d.year
    if d==thanksgiving_sat(y): return "Thanksgiving break"
    if (d.month==12 and d.day>=15) or (d.month==1 and d.day<=7): return "Winter break"
    if d==last_sat_march(y): return "Spring break"
    mem=last_monday_may(y)
    if d==mem-timedelta(days=2): return "Memorial Day weekend"
    return None

schedule=[]
for label, start, end in SEASONS:
    # first Saturday on/after start
    d=start
    while d.weekday()!=5: d+=timedelta(days=1)
    meetings=[]; n=0; fi=0
    fill=FILL[label]
    while d<=end:
        iso=d.isoformat()
        dl=f"{WD[d.weekday()]}, {MONTHS[d.month]} {d.day}, {d.year}"
        bl=break_label(d, end)
        if bl:
            meetings.append({"date":iso,"label":dl,"type":"break","brk":bl})
        elif iso in CANCELLED:
            meetings.append({"date":iso,"label":dl,"type":"cancelled","brk":CANCELLED[iso]})
        else:
            n+=1
            if iso in ANCHOR:
                mid=ANCHOR[iso]
            else:
                mid=fill[fi % len(fill)]; fi+=1
            meetings.append({"date":iso,"label":dl,"type":"meeting","n":n,"module":mid,
                             "title":M[mid]["t"],"topic":M[mid]["topic"]})
        d+=timedelta(days=7)
    schedule.append({"year":label,"meetings":meetings})

# Sanity: every anchor placed, every module exists.
placed={m["date"] for s in schedule for m in s["meetings"]}
for a in ANCHOR:
    assert a in placed, f"anchor {a} not in schedule"
for c in CANCELLED:
    assert c in placed, f"cancelled {c} not on a scheduled Saturday"
for s in schedule:
    for m in s["meetings"]:
        if m["type"]=="meeting":
            assert m["module"] in M, m["module"]

out = ("/* AUTO-GENERATED by generate_meetings.py. Edit modules there and re-run. */\n"
       "const MODULES = " + json.dumps(M, ensure_ascii=False) + ";\n"
       "const SCHEDULE = " + json.dumps(schedule, ensure_ascii=False) + ";\n"
       "if (typeof window !== 'undefined') { window.MODULES = MODULES; window.SCHEDULE = SCHEDULE; }\n")
open("js/meetings.js","w").write(out)

tot_meet=sum(1 for s in schedule for m in s["meetings"] if m["type"]=="meeting")
tot_break=sum(1 for s in schedule for m in s["meetings"] if m["type"]=="break")
tot_cancel=sum(1 for s in schedule for m in s["meetings"] if m["type"]=="cancelled")
print(f"modules: {len(M)}   meetings: {tot_meet}   breaks: {tot_break}   cancelled: {tot_cancel}")
# Slide-count stats (each shown deck = these + 1 title slide added by the viewer).
lens=sorted(len(M[m]["s"])+1 for m in M)
imgslides=sum(1 for m in M for sl in M[m]["s"] if len(sl)>=3)
print(f"  deck sizes (incl. title): min {lens[0]}, max {lens[-1]}, "
      f"distinct sizes {sorted(set(lens))}")
print(f"  total image-slides across modules: {imgslides}")
for s in schedule:
    mm=[m for m in s['meetings'] if m['type']=='meeting']
    bb=[m for m in s['meetings'] if m['type']=='break']
    print(f"  {s['year']}: {len(mm)} meetings, {len(bb)} breaks ({mm[0]['date']} -> {mm[-1]['date']})")
    for b in bb: print(f"      break {b['date']}: {b['brk']}")
