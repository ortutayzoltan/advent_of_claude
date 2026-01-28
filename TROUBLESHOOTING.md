# Troubleshooting Guide

Common issues and solutions when working through the Advent of Claude Code curriculum.

---

## Installation & Setup

### Claude Code Not Found

**Symptom:**
```
command not found: claude
```

**Solutions:**
1. Ensure Claude Code is installed:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. Check your PATH includes npm global bin:
   ```bash
   echo $PATH
   npm bin -g
   ```

3. On macOS/Linux, add to your shell profile:
   ```bash
   export PATH="$PATH:$(npm bin -g)"
   ```

---

### Authentication Errors

**Symptom:**
```
Error: Invalid API key
Error: Authentication failed
```

**Solutions:**

1. **Check API key is set:**
   ```bash
   echo $ANTHROPIC_API_KEY
   ```

2. **Set API key:**
   ```bash
   # Temporary (current session)
   export ANTHROPIC_API_KEY="your-key-here"

   # Permanent (add to ~/.bashrc or ~/.zshrc)
   echo 'export ANTHROPIC_API_KEY="your-key-here"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. **Verify key is valid:**
   - Go to https://console.anthropic.com
   - Check your API keys section
   - Ensure the key hasn't expired or been revoked

4. **Check for typos:**
   - API keys start with `sk-ant-`
   - No trailing spaces or newlines

---

### Model Not Available

**Symptom:**
```
Error: Model 'claude-opus-4' not available
Error: Insufficient permissions for this model
```

**Solutions:**

1. **Check your account tier:**
   - Some models require higher API tiers
   - Visit console.anthropic.com to check your access

2. **Use an available model:**
   ```
   /model
   ```
   Select from the list of models you have access to.

3. **Default to Sonnet:**
   - Claude Sonnet is available on most tiers
   - Excellent for most development tasks

---

## Session Issues

### Context Window Full

**Symptom:**
```
Error: Context window exceeded
Claude responses become truncated or confused
```

**Solutions:**

1. **Clear context:**
   ```
   /clear
   ```

2. **Start fresh session:**
   - Exit with `Ctrl+D`
   - Start new session with `claude`

3. **Be more concise:**
   - Reference specific files instead of entire directories
   - Use `@file.py:10-50` for specific line ranges

4. **Break into smaller tasks:**
   - Complete one feature at a time
   - Commit frequently

---

### CLAUDE.md Not Loading

**Symptom:**
- Claude doesn't follow your project conventions
- Need to repeat preferences each session

**Solutions:**

1. **Check file location:**
   ```bash
   ls -la CLAUDE.md
   ```
   Must be in project root.

2. **Check file permissions:**
   ```bash
   chmod 644 CLAUDE.md
   ```

3. **Verify syntax:**
   - CLAUDE.md should be valid Markdown
   - No special characters that might cause parsing issues

4. **Recreate with /init:**
   ```
   /init
   ```

---

### Slow Responses

**Symptom:**
- Long wait times for Claude responses
- Timeouts

**Solutions:**

1. **Check internet connection:**
   ```bash
   ping api.anthropic.com
   ```

2. **Try a different model:**
   - Haiku is fastest
   - Sonnet is balanced
   - Opus is slowest but most capable

3. **Reduce context:**
   - Reference fewer files
   - Use `/clear` to reset

4. **Check API status:**
   - Visit https://status.anthropic.com

---

## File & Git Issues

### File References Not Working

**Symptom:**
```
@filename.py doesn't load file content
Claude says "I don't see that file"
```

**Solutions:**

1. **Check file exists:**
   ```bash
   ls -la filename.py
   ```

2. **Use correct path:**
   ```
   @./src/filename.py      # Relative path
   @/home/user/project/file.py  # Absolute path
   ```

3. **Check for typos in filename**

4. **Verify file permissions:**
   ```bash
   chmod 644 filename.py
   ```

---

### Git Commands Failing

**Symptom:**
```
fatal: not a git repository
```

**Solutions:**

1. **Initialize git:**
   ```bash
   git init
   ```

2. **Check you're in the right directory:**
   ```bash
   pwd
   git status
   ```

3. **Configure git (if first time):**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

---

### Commit/PR Commands Not Working

**Symptom:**
```
Error: No changes to commit
Error: gh: command not found
```

**Solutions:**

1. **For "no changes":**
   ```bash
   git status
   git add .
   ```
   Ensure files are staged.

2. **Install GitHub CLI (for /pr):**
   ```bash
   # macOS
   brew install gh

   # Ubuntu/Debian
   sudo apt install gh

   # Then authenticate
   gh auth login
   ```

---

## Platform-Specific Issues

### Windows

**PowerShell path issues:**
```powershell
# Add npm global to PATH
$env:PATH += ";$(npm bin -g)"
```

**Line ending issues:**
```bash
git config --global core.autocrlf true
```

**WSL recommended:**
- Install WSL2 for best experience
- Run Claude Code inside WSL

---

### macOS

**zsh completion issues:**
```bash
# Add to ~/.zshrc
autoload -Uz compinit && compinit
```

**Permissions on /usr/local:**
```bash
sudo chown -R $(whoami) /usr/local
```

---

### Linux

**Node.js version:**
```bash
# Ensure Node.js 18+
node --version

# Use nvm to upgrade
nvm install 18
nvm use 18
```

**Permission issues:**
```bash
# Don't use sudo with npm install -g
# Instead, configure npm prefix
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
```

---

## Common Error Messages

### "Rate limit exceeded"

**Cause:** Too many API requests in short time.

**Solutions:**
- Wait a few minutes
- Reduce request frequency
- Check your API tier limits

---

### "Request too large"

**Cause:** Sending too much context.

**Solutions:**
- Reference fewer files
- Use specific line ranges: `@file.py:1-100`
- Split into multiple requests

---

### "Connection refused"

**Cause:** Network or firewall issues.

**Solutions:**
- Check internet connection
- Verify no VPN/proxy blocking
- Check firewall rules

---

### "Invalid JSON in response"

**Cause:** Usually a temporary API issue.

**Solutions:**
- Retry the request
- If persistent, check API status page
- Try with simpler prompt

---

## Getting More Help

1. **Official Documentation:**
   https://docs.claude.com/en/docs/claude-code/overview

2. **GitHub Issues:**
   https://github.com/anthropics/claude-code/issues

3. **Community Discord:**
   Search for "Claude Developers Discord"

4. **Ask Claude:**
   ```
   I'm getting this error: [paste error]
   What might be causing it?
   ```

---

## Quick Diagnostic Commands

Run these to gather info when reporting issues:

```bash
# Version info
claude --version
node --version
npm --version

# Environment
echo $ANTHROPIC_API_KEY | head -c 10  # Just first 10 chars
echo $SHELL
which claude

# Git status
git status
git remote -v

# System
uname -a
```

---

*If your issue isn't covered here, check the GitHub issues or ask in the community Discord!*
