# Duolingo codex

A standalone, installable Junior Cycle Business Studies revision app for third-year students in Ireland. Original design and teaching material; independent of Duolingo and NCCA.

## Run in Chrome

Run `./start.sh` from this folder, then visit **http://127.0.0.1:4173/** in Chrome. The launcher starts a background server and saves its process ID in `server.pid` and output in `server.log`. You can close the launcher terminal. Run `./start.sh` again after restarting the computer.

On another device on the same Wi-Fi, use this computer’s local network IP address with port `4173`. The computer must stay awake. Progress is saved separately in each browser; use backup/restore to transfer it.

The local-network HTTP version works in the browser but cannot use a service worker for offline installation. Install/offline features are available on localhost or HTTPS. If port 4173 is already serving this app, use the existing server.

Chrome’s menu → Cast, save and share → Install page as app opens it in its own window (menu wording varies). The service worker caches the app for offline use after an initial successful visit. Offline availability depends on the browser keeping its site data.

## Learning features

- 24 lessons, eight per NCCA strand: Personal Finance, Enterprise, Our Economy.
- 96 original multiple-choice questions, concise teaching notes and worked examples.
- Explanations after every answer; shuffled answer positions; targeted mistake revision.
- Animated Finn coaching, three-heart missions with free refills, optional sound, combo bonuses, stars and confetti.
- Typed calculation challenges, Match Dash vocabulary game, and a 60-second Business Blitz that pauses for explanations.
- Daily five-question challenge guaranteed to cover all three strands; 12-question revision sprint.
- 75% completion threshold, personal bests, XP, daily goals, streaks and six achievement badges.
- Searchable study notes, keyboard-accessible controls and responsive layout.
- Device-local progress with JSON backup and validated restore. No account or analytics.

This is a revision companion, not full course certification or a replacement for extended accounting exercises, teacher instruction or classroom-based assessments. Monetary examples and rates are illustrative. Consumer guidance checked against CCPC and payslip terminology against Revenue on 26 October 2026.

## References

- https://www.curriculumonline.ie/junior-cycle/junior-cycle-subjects/business-studies/expectations-for-students/
- https://www.ccpc.ie/consumer-advice/faulty-products-and-goods/repairs-and-replacements/
- https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx

## Structure

`dist/` is the complete static application. There is no install or build step. Serve over HTTPS for hosting, or localhost for development; service workers and installability require a secure context.

`node verify.cjs` checks curriculum structure, question integrity, balanced daily challenges, answer randomisation, scoring, replay XP, persistence, combo bonuses, hearts, numeric answers, matching rewards and timer expiry. Node is only needed for verification, not to serve the app.

## GitHub Pages

The `.github/workflows/pages.yml` workflow validates the course and games, then publishes only `dist/` to GitHub Pages when changes are pushed to the `pages` branch. Local server logs, process IDs and preview images are excluded from source control.
