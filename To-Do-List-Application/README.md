
# To-Do List Application by Samuel Nicolas W R

A minimal, futuristic task manager built with vanilla HTML, CSS and JavaScript.
No frameworks, no dependencies, no build step.
</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Data Storage](#data-storage)
- [Customization](#customization)
- [Browser Support](#browser-support)
- [Contributing](#contributing)
- [License](#license)

## Overview

This is a lightweight, client-side to-do list. Tasks are stored in the browser's `localStorage`, so they persist between visits without any server or account. The interface uses a dark glass-panel design with neon accents and a live progress indicator, and adapts to desktop, tablet and mobile screens.

## Features

| Feature | Description |
|---|---|
| **Add tasks** | Create tasks with a simple input field, or press `Enter` |
| **Mark complete** | Check off tasks with visual feedback and a strike-through |
| **Delete tasks** | Remove individual tasks with an inline confirmation step |
| **Clear completed** | Remove all completed tasks in one click |
| **Persistent storage** | Tasks are saved to the browser's local storage |
| **Task statistics** | Live total and completed counts, plus a progress bar |
| **Input validation** | Empty tasks are rejected and length is capped at 100 characters |
| **Responsive design** | Works on desktop, tablet and mobile |
| **Modern UI** | Minimal, futuristic look with smooth animations |
| **Accessibility** | Labelled controls, keyboard support and reduced-motion respect |

## Tech Stack

- **HTML5** for semantic structure
- **CSS3** with custom properties, flexbox, gradients and keyframe animations
- **JavaScript (ES5-compatible)** for all application logic
- **Web Storage API** (`localStorage`) for persistence

## Project Structure

```
To-Do-List-Application/
├── index.html          # HTML structure
├── style.css           # Styling and animations
├── script.js           # JavaScript functionality
├── README.md           # Project documentation
└── screenshots/        # Output screenshots
    ├── empty-state.png
    ├── with-tasks.png
    ├── completed-task.png
    └── mobile-view.png
```

## Getting Started

No installation or build tools are required.

### Prerequisites

A modern web browser (Chrome, Firefox, Safari or Edge).

### Run locally

```bash
# 1. Clone the repository
git clone https://github.com/CSE-Cyber-security/SAMUEL-NICOLAS-W-R-111924CB01040.git

# 2. Move into the project folder
cd To-Do-List-Application

# 3. Open index.html in your browser
```

You can also serve it with any static server, for example:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

### Deploy with GitHub Pages

1. Push the project to a GitHub repository.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch** and select your main branch and the `/ (root)` folder.
4. Save. Your app will be available at `https://<your-username>.github.io/To-Do-List-Application/`.

## Usage

| Action | How |
|---|---|
| Add a task | Type in the input and click **+** or press `Enter` |
| Complete a task | Click its checkbox |
| Delete a task | Click **×**, then confirm with **Yes** |
| Clear completed | Click **Clear completed** (disabled when nothing is completed) |

Validation rules: a task cannot be empty (whitespace only is rejected) and cannot exceed **100 characters**.

## Data Storage

Tasks are saved under the `todo.tasks` key in `localStorage` as JSON:

```json
[
  { "id": 1730000000000.123, "text": "Write documentation", "done": false }
]
```

Data stays on the user's device and is never sent anywhere. Clearing site data in the browser will remove saved tasks.

## Customization

- **Colors:** edit the CSS variables at the top of `style.css` (`--accent`, `--accent2`, `--bg`, and so on).
- **Task length limit:** change `MAX` in `script.js` and the `maxlength` attribute in `index.html`.
- **Storage key:** change `KEY` in `script.js`.

## Browser Support

| Browser | Support |
|---|---|
| Chrome / Edge | Latest 2 versions |
| Firefox | Latest 2 versions |
| Safari | Latest 2 versions |

The glass-panel blur effect uses `backdrop-filter`; browsers without it fall back to a solid translucent panel.

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please keep changes dependency-free and consistent with the existing code style.

This project is open source and available under the MIT License.

Copyright (c) 2026 SAEC [CSE - Cyber security]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<div align="center">

Built with HTML, CSS and JavaScript.

</div>
