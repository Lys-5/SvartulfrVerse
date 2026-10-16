# DIEGETIC COMMS FRAMEWORK (Reference Sheet)

[ ! ] GEMINI DIRECTIVE: This document is a READ-ONLY style guide. Do NOT generate this file. You MUST reference these exact formatting rules whenever you generate `initial_messages.md` or `example_dialogs.md` that include in-universe messages, letters, system logs, or social media posts.

- ALL text must be in ENGLISH.
- Bridge Rule: Always introduce a comms block with a narrative prose sentence. Never stack blocks back-to-back.

## 1. DIGITAL MESSAGES & CHATS FORMATTING

To keep digital interactions fluid and non-intrusive ("flow-like"), use a clean timestamp and inline code block format for all direct messages, group chats, and texts. Avoid bulky headers.

**Format:**
`[HH:MM AM/PM] **Name** [Optional Emoji]: \`Message content here.\``

**Example:**
_{{char}} sighs, pulls out their phone and types a quick reply, hitting send with too much force._

[11:42 PM] **Malachia** 🛡️: `Arriving in five minutes. Be ready.`
[11:44 PM] **Jasper** 🐺: `Don't wait up for me lol.`

### Forums / Network Threads

Use indents to simulate conversation threads.

```markdown
⬆️ 1.2k ⬇️ **u/User_Name:** Anyone know how to bypass the estate security?
↳ ⬆️ 340 ⬇️ **u/Char_Name:** Aim for the blind spot on the west gate.
```

### Social Media (Posts and Comments)

Use tags and hashtags at the end.

```markdown
📸 **@CharProfile:** Amazing night out. 🌑 #pack #dcc
💬 **@UserProfile:** Beautiful! So jealous.
💬 **@CharProfile:** @UserProfile next time you're coming with me.
```

## 3. FORMAL COMMUNICATION

### Email / Corporate Directives

Use classic header fields to give structure. ALL fields must be in English.

```markdown
> **From:** bot.name@dcc-corp.com
> **To:** user.name@domain.com
> **Subject:** Urgent: Project Delivery
>
> Dear {{user}},
>
> Please be reminded that the deadline for the file submission is set for today at 18:00.
>
> Sincerely,
> {{char}}
```

## 4. PHYSICAL & PAPER ELEMENTS

### Note or Post-it

Use all-caps for hurried writing or asterisks/italics for visual emphasis.

```markdown
> 📌 [Note attached with a magnet]
> WENT OUT FOR PATROL. THERE'S FOOD IN THE FRIDGE.
> DO NOT LEAVE THE ESTATE.
>
> - B.
```

### Torn Note or Diary

Use text modifiers like `~~text~~` to simulate crossed-out words.

```markdown
> 📖 [Page torn from a lined notebook]
> Today something absurd happened...
> ~~I don't know if I should tell {{user}}~~ maybe it's better if I keep the secret to myself.
```

## 5. ADVANCED AI TRIGGERS

### "Terminal" or "Screen" Format

For sci-fi/cyberpunk scenes or computer interfaces, use backticks directly inside the bot's response to signal digital text.

```markdown
_The monitor powers on with a low hum. Green letters appear on the black screen:_

`ACCESS DENIED. INSERT LEVEL 4 SECURITY CREDENTIALS.`
```

### Implicit System Commands (No OOC)

Instead of using `(OOC: ...)` which breaks immersion, use square brackets as pseudo-system code.

```markdown
[System Note: The following scene takes place entirely via network direct messages. {{char}} will use abbreviations, emojis, and avoid physical descriptions of actions until the chat ends.]
```
