# Education Experience Hierarchy

Documenting the simplified structure for both the authenticated Education dashboard (`frontend/src/pages/dashboards/EducationHome.tsx`) and the public education page.

## High-Level Layout
1. **Hero Section**
   - Lightweight intro copy + supporting stats (`.heroSimple`, `.statSimple`).
   - Communicates purpose, total available lessons, track count, and the currently highlighted topic.
2. **Topic Tabs**
   - Button grid rendered from `topics` config.
   - Each button shows icon, title, and short description to help users switch domains quickly.
3. **Topic Summary**
   - Reinforces which track is active, its description, featured tags, lesson count, and suggested learning style.
   - Keeps context visible before the lesson grid.
4. **Lesson Grid**
   - `EducationCard` instances rendered for each article in the selected track.
   - Cards surface difficulty, lesson number, tag chips, and a “Read Article” CTA.

## Component Responsibilities
- `EducationHome` orchestrates state (`selected` topic) and supplies metadata to visual elements.
- `EducationCard` focuses on lightweight lesson summaries and navigation logic.
- `Education.module.css` stores shared styling so the dashboard and public page stay consistent.

## Simplification Notes
- Removed heavy gradients and overlapping layers from the hero + cards to keep visual hierarchy calm.
- Stats use monochrome cards with subtle borders; buttons rely on border changes instead of large shadows.
- Topic summary uses a single bordered container so screen readers and smaller screens can parse the layout more easily.

## Progress Tracking
- A lightweight checkbox on each `EducationCard` lets users log completion locally.  
- Progress is stored in `localStorage` under `acadia.educationProgress`, which keeps state between sessions without hitting the backend.  
- When every article inside a topic is checked off we surface an inline “Track badge unlocked” callout.  
- This flow keeps the UX responsive now and can be swapped for a real profile-backed API later by replacing the `persistProgress` helper.  
