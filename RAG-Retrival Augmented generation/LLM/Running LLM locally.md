# 1) Install Ollama (macOS)

**With Homebrew (recommended):**

```bash
brew install ollama
ollama --version
```

*(No Homebrew? You can also grab the .dmg from the GitHub releases page you linked and drag the app to Applications.)*

Start the local server (one-time per terminal session):

```bash
ollama serve
```

(You can leave this running in one tab and use another tab for the next commands.)

---

# 2) Pull & run Llama 3.1

Most Macs should use the 8B variant:

```bash
# Pull the model (first time only)
ollama pull llama3.1:8b

# Run it interactively
ollama run llama3.1:8b
```

Quick API sanity check (optional):

```bash
curl http://localhost:11434/api/generate \
  -d '{"model":"llama3.1:8b","prompt":"Say hello in one short sentence."}'
```

List installed models:

```bash
ollama list
```

---

# 3) Open the models/blobs folder in Finder

*(Note the correct macOS path uses forward slashes and a dot folder):*

```bash
open ~/.ollama/models/blobs
```

---

# 4) Move the blobs to the **Trash** (NOT permanent delete)

### Option A — via Finder (safest)

After running the `open` command above, **Cmd+A → Cmd+Backspace** to send them to Trash.

### Option B — from the terminal, send to Trash using AppleScript

```bash
osascript -e 'tell application "Finder" to delete every item of folder (POSIX file "'"$HOME"'/.ollama/models/blobs")'
```

### Option C — from the terminal, using the `trash` CLI

```bash
brew install trash
trash ~/.ollama/models/blobs/*
```

> ⚠️ If you truly want to nuke them (permanent delete), you could do:
>
> ```bash
> rm -rf ~/.ollama/models/blobs/*
> ```
>
> but that bypasses the Trash. Use with care.

---

# 5) (Optional) Uninstall Ollama itself

**If installed via Homebrew:**

```bash
brew uninstall ollama
```

**Clean up Ollama data (permanent delete, not Trash):**

```bash
rm -rf ~/.ollama
```

If you’d rather move the whole `~/.ollama` folder to the **Trash** instead:

```bash
osascript -e 'tell application "Finder" to delete (POSIX file "'"$HOME"'/.ollama")'
```
 
