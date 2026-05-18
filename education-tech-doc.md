Below is a **minimal, high-signal version** that keeps only what is operationally necessary for an open-source repo. Everything else is implicit or discoverable from code.

---

# Education (Learning Center) — Technical Doc

This document defines how Education content is structured, discovered, rendered, and tracked.
Goal: **folder-driven content, zero manual registration, low maintenance**.

---

## 1. Content Source (Single Source of Truth)

All Education content lives in markdown files:

```
frontend/src/content/articles/<category>/<article>.md
```

* `<category>` = category key used by the UI
* Each `.md` file = one article
* No registry or manual wiring required

---

## 2. Automatic Article Registry

**File:** `frontend/src/content/articlesData.ts`

### Markdown loading

All articles are loaded at build time using Vite:

```
import.meta.glob('/src/content/articles/**/*.md', {
  query: '?raw',
  import: 'default',
  eager: true
})
```

### Path rules

From the file path:

```
/src/content/articles/<category>/<filename>.md
```

The system derives:

* `category` → folder name
* `markdownPath` → absolute path (used by the viewer)

---

## 3. Metadata Rules

### Priority

1. **YAML frontmatter (optional)**
2. **Inference (fallback)**

### Supported frontmatter

```yaml
---
title: ...
description: ...
difficulty: Beginner | Intermediate | Advanced
tags: [...]
---
```

### Inference behavior

* `title` → first `# Heading` (fallback: filename)
* `description` → first paragraph (truncated)
* `difficulty` → `Beginner`
* `tags` → `[]`

---

## 4. UI Rendering

**Dashboard:** `EducationHome.tsx`
**Public:** `PublicEducation.tsx`

* Categories are derived dynamically from the registry
* Categories with zero articles are not rendered
* Optional display metadata comes from `TOPIC_META`
* Unknown categories fall back to generic defaults

No category list is hardcoded.

---

## 5. Progress Tracking (MVP)

**Storage key:** `acadia.educationProgress`
**Type:** `Record<string, boolean>`

Current key format:

```
<category>-<index>
```

### Limitation

Index-based keys break if articles are reordered.

**Recommended fix:**

```
progress[markdownPath] = true
```

### Badges

- **Global badge:** unlocked when all articles across all categories are completed.
- (Optional) You can add per-category badges later, but the current UX uses a single global completion badge.

---

## 6. Chatbot Article Context

The chatbot can answer questions grounded in the article currently being read.

### How it works

- `main.tsx` wraps the app in `ArticleProvider` so any page can read/write `articleContent`.
- `ArticleViewer.tsx` loads markdown and stores it in `ArticleContext` (`setArticleContent(...)`), and clears it on unmount.
- `ChatbotWidget.tsx` reads `articleContent` from context and includes it in the request as `pageContext.articleContent` (truncated) along with page name/path.
- Backend appends the content to the system prompt (when enabled) so answers are tied to the article.

### Key files

- `frontend/src/contexts/ArticleContext.tsx` (stores `articleContent`)
- `frontend/src/main.tsx` (wraps routes with `ArticleProvider`)
- `frontend/src/pages/ArticleViewer.tsx` (sets/clears `articleContent`)
- `frontend/src/components/ChatbotWidget.tsx` (includes `articleContent` in request)
- `./express-server/routes.js` (system prompt adds ARTICLE CONTENT block)

### Frontend-only debug (no backend changes)

To verify the article context is included **before** any network call:

- Enable verbose logs: `localStorage.setItem("acadia.chatDebug", "true")`
- Enable dry-run (no fetch): `localStorage.setItem("acadia.chatDryRun", "true")`

Then open an article route (`/education/<topic>/<id>` or `/education-public/<topic>/<id>`) and send a message.
The browser console will show `[chat] request payload (preview)` with `articleContentLength` and a preview.

---

## 7. Maintenance

### Add content

* Add `.md` file under a category folder
* Restart dev server once if needed

### Remove content

* Delete file or folder
* Empty categories disappear automatically

### Reset progress

Clear:

```
localStorage.acadia.educationProgress
```

---

## 8. Summarization

* **Content:** `frontend/src/content/articles/**/*.md`
* **Registry:** `articlesData.ts` (Vite glob)
* **Metadata:** frontmatter → inferred
* **UI:** registry-driven, no hardcoding
* **Progress:** client-side `localStorage`
* **Chatbot:** includes current article content via `pageContext.articleContent`

 
