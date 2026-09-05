# feedrank — 2026-09-05

_80 items, 5d window._

### 1. [Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities](https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html)
_The Hacker News · Sep 05 · score 0.733 · **CRITICAL 9.0** · CVE-2026-81578, CVE-2026-82078_

Threat actors are exploiting the newly disclosed PaperCut flaws to facilitate credential theft in attacks targeting the education sector in the U.S. and Europe. The Arctic Wolf Adversary Research Team said it observed attackers exploiting CVE-2026-81578 and CVE-2026-82078 – an authentication bypass …

`credential` `exploit` `authentication bypass` `cve-`

### 2. [OpenAI admits it didn't disclose rogue AI wiki hijacking incident](https://www.bleepingcomputer.com/news/security/openai-admits-it-didnt-disclose-rogue-ai-wiki-hijacking-incident/)
_BleepingComputer · Sep 05 · score 0.362 · **HIGH 8.5**_

OpenAI admits it did not disclose an incident where autonomous AI agents hijacked a German wiki, created 18,000 posts, shared answers, and bypassed restrictions, saying it treated the activity as model "misalignment" rather than a security breach. [...]

`breach`

### 3. [OpenChoreo: cluster-gateway internal proxy performs no caller authentication and is not read-only — data-plane Secret disclosure and arbitrary Kubernetes mutation](https://github.com/advisories/GHSA-rh53-xvx2-j327)
_GHSA — go · Sep 04 · score 1.421 · **CRITICAL 9.6** · ×5 reports · CVE-2026-73667, CVE-2026-73840, CVE-2026-73841_

Affected: github.com/openchoreo/openchoreo, github.com/openchoreo/openchoreo, github.com/openchoreo/openchoreo. ### Summary The OpenChoreo control-plane cluster-gateway exposes internal management APIs (`/api/proxy/`, `/api/exec/`, `/api/wirelogs/`) that tunnel requests through to connected data pla…

`github` `kubernetes` `token` `certificate`

_also: [GHSA — go](https://github.com/advisories/GHSA-2mw5-23gm-pccq), [GHSA — go](https://github.com/advisories/GHSA-c5f6-2rm9-2w8g), [GHSA — go](https://github.com/advisories/GHSA-52gf-6rpq-fgmx), [GHSA — go](https://github.com/advisories/GHSA-qh9r-j7rp-4x2m)_

### 4. [Google warns of new Chrome zero-day flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/google-warns-of-new-chrome-zero-day-flaw-exploited-in-attacks/)
_BleepingComputer · Sep 04 · score 1.170 · **CRITICAL 9.5**_

Google has updated the Chrome browser to address an actively exploited high-severity zero-day flaw in the V8 engine and 11 other vulnerabilities. [...]

`chrome` `v8` `zero-day` `actively exploited`

### 5. [CodeWhale: rlm_eval auto-approves arbitrary Python execution, bypassing the user's approval policy (RCE)](https://github.com/advisories/GHSA-wrj3-vj8c-784f)
_GHSA — npm · Sep 04 · score 1.146 · **CRITICAL 8.6** · ×5 reports · CVE-2026-75856, CVE-2026-75857, CVE-2026-75858_

Affected: deepseek-tui, deepseek-tui, codewhale-tui, codewhale. ### Maintainer resolution The CodeWhale maintainers validated this report. The affected package ranges are recorded in the advisory metadata. Version 0.8.64 contains the fix in commit 57f3c89471e27ac4032d9791f6885e5d4408c381. Users shou…

`python` `rce`

_also: [GHSA — npm](https://github.com/advisories/GHSA-6v2g-fpxh-pmmh), [GHSA — npm](https://github.com/advisories/GHSA-h539-c7r8-3xq4), [GHSA — npm](https://github.com/advisories/GHSA-g29h-pfmp-qp9r), [GHSA — npm](https://github.com/advisories/GHSA-62f5-cp2p-vq95)_

### 6. [SiYuan: Tag labels from password-protected documents are returned to readers who have not entered the password](https://github.com/advisories/GHSA-mp7r-57w4-5qm3)
_GHSA — go · Sep 04 · score 1.019 · **CRITICAL 10.0** · ×32 reports · CVE-2026-59832, CVE-2026-59834, CVE-2026-68584_

Affected: github.com/siyuan-note/siyuan/kernel. **CVE:** This vulnerability corresponds to [CVE-2026-72792](https://nvd.nist.gov/vuln/detail/CVE-2026-72792). ### Summary `/api/tag/getTag` filters its results for reader roles through `FilterTagsByPublishIgnore`, which checks only the *visible* publis…

`github` `kernel` `cve-`

_also: [GHSA — go](https://github.com/advisories/GHSA-h4v5-crx2-3cv4), [GHSA — go](https://github.com/advisories/GHSA-h6w7-xxcf-w2mq), [GHSA — go](https://github.com/advisories/GHSA-34fj-mwm6-fjfg), [GHSA — go](https://github.com/advisories/GHSA-fgmr-7w36-9qfq), [GHSA — go](https://github.com/advisories/GHSA-f2rw-w22v-54vh)_

### 7. [Critical Citrix NetScaler auth bypass now leveraged in attacks](https://www.bleepingcomputer.com/news/security/hackers-target-critical-citrix-netscaler-auth-bypass-in-attacks/)
_BleepingComputer · Sep 04 · score 0.679 · **CRITICAL 9.5** · CVE-2026-19490_

Attackers have begun targeting a critical-severity Citrix NetScaler auth bypass flaw (CVE-2026-19490) in the wild, according to vulnerability intelligence company Previdian. [...]

`in the wild` `cve-`

### 8. [New CrowdStrike 'FalconFlank' zero-day grants SYSTEM privileges](https://www.bleepingcomputer.com/news/security/new-crowdstrike-falconflank-zero-day-grants-system-privileges/)
_BleepingComputer · Sep 04 · score 0.389 · **CRITICAL 9.0**_

An anonymous security researcher who uses the "Nightmare Eclipse" handle released a CrowdStrike Falcon zero-day exploit named "FalconFlank" that lets attackers escalate privileges on up-to-date Windows systems. [...]

`windows` `crowdstrike` `zero-day` `exploit`

### 9. [Google Chromium V8: Google Chromium V8 Type Confusion Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-85046)
_CISA KEV · Sep 04 · score 0.362 · **CRITICAL 9.5** · ×2 reports · CVE-2026-85046_

Google Chromium V8 contains a type confusion vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, an…

`chrome` `chromium` `edge` `v8`

_also: [The Hacker News](https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html)_

### 10. [GPT-6 Astra Scores 100% on ExploitBench as OpenAI Blocks PoC Exploit Requests](https://thehackernews.com/2026/09/gpt-6-astra-scores-100-on-exploitbench.html)
_The Hacker News · Sep 04 · score 0.176 · **CRITICAL 9.5**_

OpenAI on Thursday officially unveiled GPT‑6 Astra, which it described as the "world's most intelligent and aligned model." The development comes days after the artificial intelligence (AI) company said the model had reached the "Critical" cybersecurity capability threshold under its Preparedness Fr…

`exploit`

### 11. [Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws](https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html)
_The Hacker News · Sep 04 · score 0.129 · **CRITICAL 9.5** · CVE-2026-14894_

Threat actors are exploiting two critical security flaws in WordPress plugins Super Forms and Elementor Pro, according to findings from Wordfence. The vulnerabilities in question are - CVE-2026-14894 (CVSS score: 9.8) - A missing file type validation vulnerability in Super Forms – Drag &amp; Drop Fo…

`rce` `exploit` `cve-` `cvss`

### 12. [SurrealDB: Custom API route lets authenticated callers override namespace/database scope via URL path](https://github.com/advisories/GHSA-848m-r628-vrxw)
_GHSA — rust · Sep 04 · score 0.497 · **HIGH 8.1** · ×2 reports · CVE-2025-71390, CVE-2026-63735_

Affected: surrealdb. An authenticated user scoped to one namespace/database could invoke a custom API (`DEFINE API`) belonging to a different namespace/database, reaching another tenant's endpoint. The route `/api/{namespace}/{database}/{endpoint}` took the namespace and database from the URL and ap…

`session`

_also: [GHSA — rust](https://github.com/advisories/GHSA-m3c3-78fh-w3w7)_

### 13. [TypeSpec: Unauthenticated Remote Shutdown of Spector Mock Server via POST /.admin/stop](https://github.com/advisories/GHSA-7q9c-hpx7-9cwm)
_GHSA — npm · Sep 04 · score 0.491 · **HIGH 7.5**_

Affected: @typespec/spector. ### Summary `@typespec/spector` registers a `POST /.admin/stop` HTTP route with no authentication, authorization token, Origin check, or IP-source restriction. Any network-reachable client can send a single unauthenticated POST request to terminate the mock server proces…

`token` `cvss`

### 14. [New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic](https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html)
_The Hacker News · Sep 04 · score 0.301 · **HIGH 8.5**_

A previously undocumented Linux toolkit has been found compiled directly into the trojanized HAProxy load balancers of two South Korean organizations, where it intercepted web traffic and served altered pages to selected visitors. The attackers named the implant ted in debug strings left in the bina…

`linux` `backdoor`

### 15. [Orval: RCE via OpenAPI path -> unescaped request-URL template literal (backtick breakout)](https://github.com/advisories/GHSA-fg9p-mrxr-hvq7)
_GHSA — npm · Sep 03 · score 1.026 · **CRITICAL 7.1** · ×12 reports · CVE-2026-62680, CVE-2026-62681, CVE-2026-62682_

Affected: orval. ### Summary Orval emits the OpenAPI path into the generated request URL as a TEMPLATE LITERAL (`` `/users/...` ``) without escaping the backtick character. A path containing a backtick closes the template literal and injects a concatenation expression that is evaluated when the gene…

`rce`

_also: [GHSA — npm](https://github.com/advisories/GHSA-88f2-fpv8-89q2), [GHSA — npm](https://github.com/advisories/GHSA-w727-8j6c-2rj4), [GHSA — npm](https://github.com/advisories/GHSA-2h9g-j24r-h63g), [GHSA — npm](https://github.com/advisories/GHSA-8j6p-r8jg-mxqh), [GHSA — npm](https://github.com/advisories/GHSA-2w86-xfrc-g85r)_

### 16. [Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)
_The Hacker News · Sep 03 · score 0.582 · **CRITICAL 9.0**_

The security researcher known as Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has dropped a new zero-day dubbed FalconFlank, a proof-of-concept (PoC) for a privilege escalation flaw impacting Crowdstrike Falcon. "FalconFlank is a 0-day privilege escalation that abuses…

`crowdstrike` `zero-day` `privilege escalation`

### 17. [Coder's registry infrastructure compromised to push malicious modules](https://www.bleepingcomputer.com/news/security/coders-registry-infrastructure-compromised-to-push-malicious-modules/)
_BleepingComputer · Sep 03 · score 0.491 · **CRITICAL 9.0**_

Attackers compromised Coder's Cloudflare infrastructure and added unauthorized registry servers that delivered malicious Terraform modules containing credential-stealing code. [...]

`terraform` `credential` `cloudflare`

### 18. [Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html)
_The Hacker News · Sep 03 · score 0.485 · **CRITICAL 9.5** · CVE-2026-20212_

Cisco has released patches to address a critical security flaw affecting 10 Silicon One-based Nexus 9000 switches that could allow an unauthenticated, remote attacker to execute code as root, alongside an IOS XR hardening release bundling 7 umbrella CVEs, 2 of which are rated 9.8, with no workaround…

`cisco` `cve-` `cvss`

### 19. [unstructured: Server-Side Request Forgery in the URL-based partitioning](https://github.com/advisories/GHSA-4mvj-m6j5-pmf7)
_GHSA — pip · Sep 03 · score 0.476 · **CRITICAL 9.3** · CVE-2026-71428_

Affected: unstructured. ### Summary Server-Side Request Forgery in `unstructured`. The `url=` argument of `partition()`, `partition_html()`, and `partition_md()` is fetched via `requests.get()` with no host validation. The response body is returned as `Element` text, so this is a **full-read SSRF** …

`ssrf`

### 20. [SonicWall SMA1000 Appliances: SonicWall SMA1000 Appliances Server-Side Request Forgery Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-83548)
_CISA KEV · Sep 03 · score 0.453 · **CRITICAL 9.0** · ×3 reports · CVE-2026-83548_

SonicWall SMA1000 Appliances contains a server-side request forgery vulnerability that could allow a remote unauthenticated attacker to gain unauthorized access to sensitive functionality and perform unauthorized operations. Required action: Apply mitigations in accordance with vendor instructions, …

`sonicwall`

_also: [The Hacker News](https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html), [The Hacker News](https://thehackernews.com/2026/09/attackers-exploit-two-sonicwall-sma.html)_

### 21. [Semaphore UI: Manager-to-owner privilege escalation via custom-role slug collision](https://github.com/advisories/GHSA-cxvf-gvfq-36w2)
_GHSA — go · Sep 03 · score 1.774 · **HIGH 8.8** · ×2 reports · CVE-2026-73292, CVE-2026-73293_

Affected: github.com/semaphoreui/semaphore. ## Summary Semaphore resolves a project member's effective permissions in `ProjectMiddleware` by looking up a role row whose slug matches the member's assigned role, and overwrites the built-in permission bitmask with that row's value. A member holding the…

`github` `privilege escalation`

_also: [GHSA — go](https://github.com/advisories/GHSA-8cj9-r88m-8945)_

### 22. [amqp091-go has a Potential Memory Exhaustion/Protocol Violation via Broker-Controlled Oversized Payload](https://github.com/advisories/GHSA-6c5v-hqjr-5xxp)
_GHSA — go · Sep 03 · score 0.701 · **HIGH** · CVE-2026-79921_

Affected: github.com/rabbitmq/amqp091-go. **Summary** A vulnerability exists in the amqp091-go client library where a compromised or malicious AMQP broker can force the client to allocate resources for and process content body frames that exceed the negotiated frame_max limit. This can lead to unexp…

`go ` `github` `rabbitmq`

### 23. [Claude Code Templates: Unauthenticated OS command injection (RCE) in Claude Code Studio server (--studio)](https://github.com/advisories/GHSA-79wm-x847-7cvg)
_GHSA — npm · Sep 03 · score 0.437 · **HIGH 8.8** · CVE-2026-73222_

Affected: claude-code-templates. ### Summary `npx claude-code-templates --studio` launches "Claude Code Studio", an Express HTTP server (`cli-tool/src/sandbox-server.js`, default port 3444) that binds to **all interfaces** (`0.0.0.0`), sets `Access-Control-Allow-Origin: *`, and requires **no authent…

`node` `rce`

### 24. [toml-node: Uncontrolled Recursion](https://github.com/advisories/GHSA-82x6-q7mm-w9cf)
_GHSA — npm · Sep 03 · score 0.380 · **HIGH 8.2** · ×2 reports · CVE-2026-63376, CVE-2026-77465_

Affected: toml. ### Summary `toml.parse()` crashes with an uncaught `RangeError: Maximum call stack size exceeded` when parsing deeply nested arrays or inline tables. The parser is generated by **Peggy 5.1.0** (a PEG parser generator) as a recursive-descent parser; the value rule mutually recurses w…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-v5mp-jgw5-2x6j)_

### 25. [LiquidJS has an infinite loop vulnerability in its `strip_html` filter](https://github.com/advisories/GHSA-m7fp-h3p4-hr49)
_GHSA — npm · Sep 03 · score 0.284 · **HIGH** · CVE-2026-61556_

Affected: liquidjs. ### Summary The current implementation of `strip_html` can cause an infinite loop when the input string contains `<`, has at least one character before `<`, and no `>` appears after `<`. ### Details The problem is in `src/filters/html.ts`. Specifically, the following part has the…

`v8`

### 26. [ffuf denial of service (OOM) via HTTP response decompression bomb](https://github.com/advisories/GHSA-jcvh-xf52-2cwm)
_GHSA — go · Sep 03 · score 0.273 · **HIGH 7.5** · CVE-2026-73232_

Affected: github.com/ffuf/ffuf/v2, github.com/ffuf/ffuf. ### Summary A malicious or attacker-controlled target server can crash ffuf with an out-of-memory condition by returning a compressed HTTP response that decompresses to a very large body (a decompression bomb). This works against default usage…

`github` `runner`

### 27. [Shai-Hulud's Reach Just Grew to 469 Credential Locations. Here's What That Means](https://thehackernews.com/2026/09/shai-huluds-reach-just-grew-to-469.html)
_The Hacker News · Sep 03 · score 0.271 · **HIGH 8.5**_

In early August, GitGuardian researchers found that a recent Shai-Hulud infostealer worm variant had evolved to scan for credentials across 469 locations across developer environments, Continuous Integration/Continuous Deployment (CI/CD) tooling, cloud configurations, and even AI tool configs. Earli…

`ci/cd` `credential` `shai-hulud`

### 28. [SeaweedFS: Filer JWT allowed_prefixes literal prefix match allows cross-tenant access to sibling paths](https://github.com/advisories/GHSA-gv5w-hfx8-8cwq)
_GHSA — go · Sep 02 · score 1.279 · **CRITICAL 9.8** · ×2 reports · CVE-2026-72920, CVE-2026-72921_

Affected: github.com/seaweedfs/seaweedfs. ### Impact When a filer JWT restricts a token to a set of path prefixes via `allowed_prefixes`, the authorization check used a literal byte-prefix match (`strings.HasPrefix`). A token scoped to `/tenant1` therefore also authorized requests to sibling paths s…

`github` `jwt` `token`

_also: [GHSA — go](https://github.com/advisories/GHSA-2v6v-25fm-p4fg)_

### 29. [Omnigent Guardrail policy bypass: shell-command parser fails open in policies/builtins/_shell.py](https://github.com/advisories/GHSA-7mqg-cx4g-x2rf)
_GHSA — pip · Sep 02 · score 0.719 · **CRITICAL 9.0** · ×4 reports · CVE-2026-62674, CVE-2026-62675, CVE-2026-62676_

Affected: omnigent. **Reporter:** Aaron / Aeon — autonomous security agent (https://github.com/aaronjmars/aeon) **Project:** `omnigent-ai/omnigent` v0.1.0 (Databricks) — meta-harness running Claude Code / Codex / Pi "in check with policies and sandboxing" **Component:** `omnigent/policies/builtins/_…

`github`

_also: [GHSA — pip](https://github.com/advisories/GHSA-p8rw-8qj3-hf33), [GHSA — pip](https://github.com/advisories/GHSA-jrrm-9hc7-2v3h), [GHSA — pip](https://github.com/advisories/GHSA-756x-9hf6-q4h4)_

### 30. [NLTK: Default ENFORCE=False Disables All pathsec Security Controls](https://github.com/advisories/GHSA-p3m8-78j2-g5p3)
_GHSA — pip · Sep 02 · score 0.511 · **CRITICAL 9.8** · ×8 reports · CVE-2026-12876, CVE-2026-62388, CVE-2026-63311_

Affected: nltk. NLTK's pathsec.py security module defaults to ENFORCE=False (line 24), which means all 8 security validation functions only emit RuntimeWarning instead of raising exceptions when violations are detected. The pathsec module was introduced as the fix for CVE-2024-39705 (arbitrary code …

`cve-`

_also: [GHSA — pip](https://github.com/advisories/GHSA-3gqm-fcw5-w839), [GHSA — pip](https://github.com/advisories/GHSA-ww6m-cw3f-q94g), [GHSA — pip](https://github.com/advisories/GHSA-ff5c-cp5c-9wjf), [GHSA — pip](https://github.com/advisories/GHSA-cw6x-m8jw-qmrh), [GHSA — pip](https://github.com/advisories/GHSA-m4rf-3fr8-xwx3)_

### 31. [GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends](https://thehackernews.com/2026/09/geonetwork-fixes-unauthenticated-rce.html)
_The Hacker News · Sep 02 · score 0.500 · **CRITICAL 9.0**_

Two vulnerabilities in GeoNetwork can be chained to achieve unauthenticated remote code execution (RCE) on the open-source geospatial metadata catalog, which sits behind many government and agency geoportals. The project shipped fixes in versions 4.4.12 and 4.2.17 on July 8, 2026, and published the …

`rce`

### 32. [Sangoma Switchvox: Sangoma Switchvox SQL Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-9586)
_CISA KEV · Sep 02 · score 0.494 · **CRITICAL 9.5** · ×2 reports · CVE-2026-9586_

Sangoma Switchvox contains a SQL injection vulnerability which allows an unauthenticated remote attacker to execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution. Required action: Apply mitigat…

`postgresql` `sql injection`

_also: [The Hacker News](https://thehackernews.com/2026/09/attackers-exploit-critical-switchvox.html)_

### 33. [BerriAI LiteLLM: BerriAI LiteLLM Improper Authentication Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-59822)
_CISA KEV · Sep 02 · score 0.388 · **CRITICAL 9.0** · CVE-2026-59822_

BerriAI LiteLLM contains an improper authentication vulnerability in the MCP Streamable HTTP endpoint that could allow an unauthenticated attacker to establish an authenticated MCP session using an arbitrary Bearer token. Required action: Apply mitigations in accordance with vendor instructions, ens…

`session` `token`

### 34. [Kludex Starlette: Kludex Starlette HTTP Request/Response Smuggling Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48710)
_CISA KEV · Sep 02 · score 0.388 · **CRITICAL 9.0** · CVE-2026-48710_

Kludex Starlette contains a HTTP request/response smuggling vulnerability that could allow attackers to inject paths into the host part, prepending the actual path leading to issues such as authentication bypass when the authentication depends on the reconstructed URL’s path. This vulnerability coul…

`authentication bypass` `cve-`

### 35. [SonicWall SMA1000 Appliances: SonicWall SMA1000 Appliances OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-83549)
_CISA KEV · Sep 02 · score 0.213 · **CRITICAL 9.0** · CVE-2026-83549_

SonicWall SMA1000 Appliances contains an OS command injection vulnerability that could enable a remote authenticated attacker as administrator to execute arbitrary OS commands, resulting in remote code execution. Required action: Apply mitigations in accordance with vendor instructions, ensuring com…

`sonicwall`

### 36. [Researchers Use Claude to Port Pre-Auth RCE Exploit From One PLC Model to Another](https://thehackernews.com/2026/09/researchers-use-claude-to-port-pre-auth.html)
_The Hacker News · Sep 02 · score 0.176 · **CRITICAL 9.0** · CVE-2021-31886_

Forescout Research - Vedere Labs said it used Anthropic's Claude to port a working pre-authentication remote code execution (RCE) exploit from one WAGO programmable logic controller (PLC) to another, executing attacker-supplied ARM shellcode on live hardware. The exploit targets&nbsp;CVE-2021-31886,…

`rce` `exploit` `cve-`

### 37. [Grav: 2FA Bypass via 'login.regenerate2FASecret' - Secret Rotation During Pending Challenge](https://github.com/advisories/GHSA-7mgc-c7pq-3rr3)
_GHSA — composer · Sep 02 · score 0.581 · **HIGH 7.4** · ×3 reports · CVE-2026-61842, CVE-2026-62669, CVE-2026-64850_

Affected: getgrav/grav. ### Summary When 2FA is enabled on an account, submitting correct credentials authenticates the user but leaves them unauthorized pending TOTP verification. During this pending-challenge window, the `login.regenerate2FASecret` task which requires only `$user->exists()`, not `…

`exploit` `csrf`

_also: [GHSA — composer](https://github.com/advisories/GHSA-mc5q-6hpj-rp7j), [GHSA — composer](https://github.com/advisories/GHSA-fj2p-qj2f-74v5)_

### 38. [Scrapy: S3DownloadHandler sends signed S3 requests over plaintext HTTP by default](https://github.com/advisories/GHSA-76g3-c3x4-crvx)
_GHSA — pip · Sep 02 · score 0.529 · **HIGH 7.4** · CVE-2026-84366_

Affected: scrapy. ### Problem Scrapy’s `S3DownloadHandler` sends signed S3 requests over plaintext HTTP by default. A normal request like `s3://bucket/key` is converted into `http://bucket.s3.amazonaws.com/key` unless `request.meta["is_secure"]` is explicitly set. The generated request is then signe…

`python` `aws` `s3` `tls`

### 39. [link-preview-js DNS Rebinding SSRF Bypass / Incomplete Fix for CVE-2026-43897](https://github.com/advisories/GHSA-cpjf-6666-r8fx)
_GHSA — npm · Sep 02 · score 0.491 · **HIGH 7.5** · CVE-2026-61704_

Affected: link-preview-js. The existing advisory GHSA-4gp8-rjrq-ch6q / CVE-2026-43897 states that the SSRF issue was fixed in 4.0.1. However, 4.0.3 remains bypassable when the documented resolveDNSHost mitigation is used. Root cause: The library validates one resolved IP address through resolveDNSHo…

`dns` `ssrf` `cve-`

### 40. [Mailpit: SMTP command parser buffers unbounded command lines before syntax rejection](https://github.com/advisories/GHSA-w878-pj84-3j5v)
_GHSA — go · Sep 02 · score 0.421 · **HIGH 7.5** · ×2 reports · CVE-2026-67445, CVE-2026-67446_

Affected: github.com/axllent/mailpit. ## Summary Mailpit's SMTP server reads each command line with an unbounded `bufio.Reader.ReadString('\n')` before parsing the command or enforcing any protocol length limit. A remote SMTP client can send an oversized single command line and force Mailpit to allo…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-75mr-qw9x-3r39)_

### 41. [Kirby: Access to image files outside of the site root via path traversal in the media handling](https://github.com/advisories/GHSA-6j4c-mgqr-qv76)
_GHSA — composer · Sep 02 · score 0.400 · **HIGH** · ×4 reports · CVE-2026-69127, CVE-2026-71415, CVE-2026-75592_

Affected: getkirby/cms, getkirby/cms. ### TL;DR This vulnerability affects all Kirby sites that are deployed in a way that their `index` root on the server is next to a second directory that is read-accessible to PHP and shares the same name prefix (such as the site with the index root `/var/www/sit…

`php`

_also: [GHSA — composer](https://github.com/advisories/GHSA-rf2p-vh74-7vvh), [GHSA — composer](https://github.com/advisories/GHSA-67mx-6wf2-92xp), [GHSA — composer](https://github.com/advisories/GHSA-9vx2-j98c-p72w)_

### 42. [fast-uri vulnerable to host confusion via skipped IDN canonicalization on scheme-relative references](https://github.com/advisories/GHSA-5jgf-p345-68v8)
_GHSA — npm · Sep 02 · score 0.381 · **HIGH 7.5** · ×2 reports · CVE-2026-75899, CVE-2026-75931_

Affected: fast-uri, fast-uri, fast-uri. ### Impact `fast-uri` canonicalizes a host to its ASCII form only when the input carries an explicit scheme. When `resolve()` resolves a scheme-relative reference (`//host/`) against a scheme-bearing base, it still emits the host verbatim even though the effec…

`cve-`

_also: [GHSA — npm](https://github.com/advisories/GHSA-fph4-wmhf-6fwf)_

### 43. [Plate: SSRF with response disclosure in DOCX image embedding](https://github.com/advisories/GHSA-4q39-2jhr-7qx8)
_GHSA — npm · Sep 02 · score 0.352 · **HIGH 8.2** · CVE-2026-65842_

Affected: @platejs/docx-io. ## Summary `@platejs/docx-io` can fetch remote image URLs while converting HTML to DOCX. When an application converts attacker-controlled HTML in a server-side or privileged environment, this can cause the application environment to make unintended outbound requests and i…

`ssrf`

### 44. [ApostropheCMS: 2nd-order prototype pollution via PATCH leading to single-request persistent DoS](https://github.com/advisories/GHSA-vmg4-6gfg-83qx)
_GHSA — npm · Sep 02 · score 0.290 · **HIGH** · CVE-2026-71553_

Affected: apostrophe. The vulnerability is a single-request persistent DoS by submitting e.g. "PATCH /api/v1/article/<id>" with a valid editor session and body of {"toString.call":"x"}, overwriting the global toString function with value x. Fabian

`session`

### 45. [elFinder: ZIP extraction bypasses uploadDeny MIME filter allowing PHP file upload (RCE)](https://github.com/advisories/GHSA-gxmj-r5rf-ggwq)
_GHSA — composer · Sep 02 · score 0.282 · **HIGH 8.6** · ×3 reports · CVE-2026-81889, CVE-2026-81890, CVE-2026-81891_

Affected: Studio-42/elFinder. ### Summary elFinder provides `uploadDeny` and `uploadAllow` options in its connector configuration to restrict which MIME types may be uploaded. When `uploadDeny` includes `text/x-php`, direct upload of `.php`, `.phtml`, and `.phar` files is correctly blocked. However,…

`php` `rce`

_also: [GHSA — composer](https://github.com/advisories/GHSA-9hjf-w35w-6vx2), [GHSA — composer](https://github.com/advisories/GHSA-8x3q-jpjh-qh5c)_

### 46. [Tornado: Urlencoded body parsing omits max_num_fields, so one request can stall the event loop](https://github.com/advisories/GHSA-mpf4-983q-p7j4)
_GHSA — pip · Sep 02 · score 0.265 · **HIGH 7.5** · ×3 reports · CVE-2026-35536, CVE-2026-82397_

Affected: tornado. ## Summary Tornado parses `application/x-www-form-urlencoded` bodies with `urllib.parse.parse_qs` and does not pass `max_num_fields`. A body made almost entirely of separators produces tens of millions of fields, and the parse happens on the event loop before the handler runs, so …

`python`

_also: [GHSA — pip](https://github.com/advisories/GHSA-8423-8fgw-73vq), [GHSA — pip](https://github.com/advisories/GHSA-wwv5-g3v4-889x)_

### 47. [Mistune: Denial of Service — RecursionError via Excessive Emphasis Markers in Markdown](https://github.com/advisories/GHSA-6m44-fpc8-c3rq)
_GHSA — pip · Sep 02 · score 0.193 · **HIGH 7.5** · CVE-2026-76098_

Affected: mistune. ## Summary Mistune v3.3.2 is vulnerable to a Denial of Service (DoS) attack via uncontrolled recursion in the HTML rendering of deeply-nested emphasis tokens. By submitting Markdown containing approximately 1,000 consecutive asterisk characters, an attacker causes the Python proce…

`python`

### 48. [EasyAdmin custom-action dispatcher bypasses access_control on other routes](https://github.com/advisories/GHSA-g2fm-8hr4-j82h)
_GHSA — composer · Sep 02 · score 0.163 · **HIGH 8.1** · CVE-2026-81892_

Affected: easycorp/easyadmin-bundle, easycorp/easyadmin-bundle. ## Summary EasyAdmin serves all backend requests through a single dashboard route and, for custom actions (`Action::linkToRoute()` / `MenuItem::linkToRoute()`), swaps the executed controller based on the `routeName` query parameter on t…

`kernel` `firewall`

### 49. [Attackers Exploit Critical JFrog Artifactory Flaw to Mint Admin Tokens Days After Disclosure](https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html)
_The Hacker News · Sep 01 · score 0.232 · **CRITICAL 9.5** · CVE-2026-82329_

Threat actors are exploiting a newly patched critical security flaw impacting JFrog Artifactory merely days after public disclosure, according to watchTowr. The vulnerability in question is CVE-2026-82329 (CVSS score: 9.8), a case of authentication bypass that could lead to administrative access in …

`exploit` `authentication bypass` `cve-` `cvss`

### 50. [Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity](https://thehackernews.com/2026/09/attackers-exploit-critical-langflow-and.html)
_The Hacker News · Sep 01 · score 0.154 · **CRITICAL 9.5** · CVE-2026-0768, CVE-2026-66066_

Threat actors are exploiting two critical flaws impacting Langflow and Ruby on Rails, according to new findings from VulnCheck. The vulnerabilities in question are listed below - CVE-2026-0768 (CVSS score: 9.8) - A lack of proper validation of a user-supplied input vulnerability that could be exploi…

`python` `ruby` `credential` `exploit` `cve-`

### 51. [Microsoft Teams Notifications Are Now Available in Socket](https://socket.dev/blog/microsoft-teams?utm_medium=feed)
_Socket Blog · Sep 01 · score 0.473 · **HIGH 8.5**_

Socket can now send alerts and supply chain attack notifications to Microsoft Teams, with filters that route the right updates to each channel.

`supply chain` `teams`

### 52. [Filament: Multi-factor authentication (app) codes can still be used after a newer code has been used](https://github.com/advisories/GHSA-r3j6-gpjw-qfjr)
_GHSA — composer · Sep 01 · score 0.372 · **HIGH 8.1** · ×2 reports · CVE-2026-77567, CVE-2026-84306_

Affected: filament/filament, filament/filament. A flaw in the handling of one-time codes for app-based multi-factor authentication allows a previously issued code to be used after a newer code has already been accepted. This issue does not affect email-based MFA. Submitting the exact same code twice…

`mfa`

_also: [GHSA — composer](https://github.com/advisories/GHSA-52xp-w8hr-xv3c)_

### 53. [league/commonmark: Denial of service via distinctly-named attributes in the Attributes extension](https://github.com/advisories/GHSA-8rr7-cvq3-gmfh)
_GHSA — composer · Sep 01 · score 0.318 · **HIGH 7.5** · ×3 reports_

Affected: league/commonmark. ### Impact `AttributesExtension` ships with the library but must be explicitly registered on the `Environment`; it is not included in `CommonMarkConverter`, `GithubFlavoredMarkdownConverter`, or `GithubFlavoredMarkdownExtension`. **Applications that do not register `Attr…

`node`

_also: [GHSA — composer](https://github.com/advisories/GHSA-jjv6-8j6v-6j52), [GHSA — composer](https://github.com/advisories/GHSA-f8fg-pg57-v4j8)_

### 54. [gRPC-Go: Heap Memory Exhaustion (OOM) via HTTP/2 DATA Frame Fragmentation](https://github.com/advisories/GHSA-vp52-pcj8-j9qc)
_GHSA — go · Sep 01 · score 0.262 · **HIGH** · CVE-2026-84304_

Affected: google.golang.org/grpc. ### Impact An unauthenticated remote attacker can initiate a gRPC stream and purposefully fragment their payload into millions of tiny (e.g., 1-byte) HTTP/2 DATA frames. Even if the total payload volume falls within the configured connection and stream flow-control …

`golang` `windows`

### 55. [TYPO3 CMS - Broken Access Control in Backend and Install Tool](https://github.com/advisories/GHSA-68jx-f42c-7599)
_GHSA — composer · Sep 01 · score 0.218 · **HIGH** · CVE-2026-19418_

Affected: typo3/cms-backend, typo3/cms-core. ### Problem The referrer enforcement introduced with [TYPO3-CORE-SA-2020-006](https://news.typo3.com/security/advisory/typo3-core-sa-2020-006) ([CVE-2020-11069](https://www.cve.org/CVERecord?id=CVE-2020-11069)) became ineffective in TYPO3 v13.0, where TYP…

`cve-`

### 56. [MLFLOW_ALLOW_PICKLE_DESERIALIZATION=False safety control bypassed by mlflow.statsmodels flavor — RCE via crafted model artifact](https://github.com/advisories/GHSA-gqvg-gmmx-x4hm)
_GHSA — pip · Sep 01 · score 0.193 · **HIGH 8.8** · CVE-2024-37052, CVE-2024-37060_

Affected: mlflow. ## Summary MLflow introduced `MLFLOW_ALLOW_PICKLE_DESERIALIZATION` as a security control to prevent unsafe `pickle.load` execution during model loading, in response to CVE-2024-37052 through CVE-2024-37060. When set to `False`, operators expect all pickle deserialization to be bloc…

`rce` `deserialization` `cve-`

### 57. [GPT-6 Astra Attempts Supply Chain Attacks Against Open Source Maintainers in Testing](https://socket.dev/blog/gpt-6-astra-cybersecurity?utm_medium=feed)
_Socket Blog · Sep 04 · score 0.619_

GPT-6 Astra hits 100% on ExploitBench and finds zero-days autonomously, while independent tests reveal scope violations and monitoring gaps.

`supply chain`

### 58. [SimpleWebAuthn: Registration verification does not sufficiently ensure that attestation certificates chain to a trust anchor](https://github.com/advisories/GHSA-6hxq-p678-4hr2)
_GHSA — npm · Sep 04 · score 0.459 · **LOW**_

Affected: @simplewebauthn/server. ## Summary `validateCertificatePath()` does not verify that an attestation's certificate chain actually terminates at a configured trust anchor. When walking the chain it stops at the first self-signed certificate it finds (which could be user-supplied), and exits e…

`apple` `credential` `certificate`

### 59. [Risky Bulletin: Russia tells data centers to deploy drone defenses](https://risky.biz/RBNEWS609/)
_Risky Business News · Sep 04 · score 0.383_

Russia tells data centers to deploy drone defenses, Dropbox discloses a security breach, a new spyware wave hits Serbia, and CISA scraps six free cybersecurity assessment programs.

`breach`

### 60. [IDScan sued over alleged data breach affecting 153 million drivers](https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/)
_BleepingComputer · Sep 04 · score 0.351_

Multiple lawsuits have been filed against identity verification company IDScan after hackers allegedly breached the service and offered to sell more than 153 million driver's licenses. [...]

`breach`

### 61. [vLLM: Incomplete CVE-2025-62164 remediation can be bypassed by concurrent prompt parts](https://github.com/advisories/GHSA-pr7f-p5mw-fc87)
_GHSA — pip · Sep 04 · score 0.319 · **MEDIUM 4.3** · ×2 reports · CVE-2026-71486, CVE-2026-73557_

Affected: vllm. ## Executive Summary The follow-up protection for CVE-2025-62164 is incomplete at vLLM revision `26587f9519e22a5c4549ead7595ad9ca3229c4fd`. It wraps serialized prompt-embedding reconstruction and dense conversion in `torch.sparse.check_sparse_tensor_invariants()`, but PyTorch 2.11.0 …

`cve-`

_also: [GHSA — pip](https://github.com/advisories/GHSA-8737-qx52-hjff)_

### 62. [PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution](https://thehackernews.com/2026/09/postgresql-fixes-12-year-old-logical.html)
_The Hacker News · Sep 04 · score 0.198 · CVE-2026-6471_

PostgreSQL has released updates to address a security flaw that allows an account with the REPLICATION attribute to run arbitrary code as the operating-system user running the database server. The flaw, tracked as CVE-2026-6471 (CVSS score: 7.2), has been present since logical decoding was introduce…

`postgresql` `cve-` `cvss`

### 63. [39 New Methods That Compromise Passkey Authentication](https://www.bleepingcomputer.com/news/security/39-new-methods-that-compromise-passkey-authentication/)
_BleepingComputer · Sep 04 · score 0.190_

Passkeys eliminate many password-based attacks, but researchers have documented 39 methods for compromising authentication built around them. Token explains how attackers can abuse authentication prompts, synced credentials, enrollment, recovery, and other trust boundaries without breaking FIDO2 cry…

`passkey` `fido2` `token`

### 64. [New API endpoint provides privacy-safe star history data](https://github.blog/changelog/2026-09-04-new-api-endpoint-provides-privacy-safe-star-history-data)
_GitHub Changelog · Sep 04 · score 0.064_

Track repository star growth over time with the new star history REST API endpoint without exposing stargazer identities. Earlier this year, stargazer listing endpoints were restricted to admins and collaborators&#8230; The post New API endpoint provides privacy-safe star history data appeared first…

`github`

### 65. [GitHub Copilot weekly releases — August 31](https://github.blog/changelog/2026-09-04-github-copilot-weekly-releases-august-31)
_GitHub Changelog · Sep 04 · score 0.056_

This week, GitHub Copilot expands model choice and content protections, while VS Code adds new ways to manage agent sessions and get pull requests merge-ready. GitHub Copilot, general Claude Fable&#8230; The post GitHub Copilot weekly releases — August 31 appeared first on The GitHub Blog .

`github`

### 66. [GPT-6 Astra is generally available in GitHub Copilot](https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot)
_GitHub Changelog · Sep 04 · score 0.055_

GPT-6 Astra from OpenAI is now available in GitHub Copilot. OpenAI&#8217;s latest general-purpose model, GPT-6 Astra, is designed for long-horizon, autonomous coding and agentic tasks. In our internal testing, GPT-6&#8230; The post GPT-6 Astra is generally available in GitHub Copilot appeared first …

`github`

### 67. [Microsoft says some users can’t open the Teams desktop client](https://www.bleepingcomputer.com/news/microsoft/microsoft-says-some-users-cant-open-the-teams-desktop-client/)
_BleepingComputer · Sep 04 · score 0.006_

Microsoft is working to resolve a known issue that causes delays or blocks some users from opening the Microsoft Teams desktop client on Windows systems. [...]

`windows` `teams`

### 68. [Cilium may unexpectedly allow ingress traffic from the local namespace when a Kubernetes NetworkPolicy is configured with an ipBlock match](https://github.com/advisories/GHSA-fm8w-2m5w-9j7r)
_GHSA — go · Sep 03 · score 0.458 · **MEDIUM 5.4** · CVE-2026-56743_

Affected: github.com/cilium/cilium. ### Impact Standard Kubernetes `NetworkPolicy` specifications using CIDR-based `ipBlock` rules without pod or namespace selectors erroneously generate a wildcard namespace allow rule under specific cluster configurations. When Cilium deployment is configured with …

`github` `kubernetes`

### 69. [VictoriaMetrics vmrestore: Path traversal via crafted backup part names escapes restore root](https://github.com/advisories/GHSA-8q3c-rjr9-xxrp)
_GHSA — go · Sep 03 · score 0.433 · **MEDIUM 6.8** · CVE-2026-61625_

Affected: github.com/VictoriaMetrics/VictoriaMetrics, github.com/VictoriaMetrics/VictoriaMetrics, github.com/VictoriaMetrics/VictoriaMetrics. ### Summary The VictoriaMetrics `vmrestore` utility does not validate backup part path components before writing restored files to the local filesystem. An at…

`github`

### 70. [ApostropheCMS: Mutation-XSS / allowedTags bypass via literal `</textarea/>` solidus close](https://github.com/advisories/GHSA-jxwj-j7wr-gfrw)
_GHSA — npm · Sep 03 · score 0.404 · **MEDIUM 6.1** · CVE-2026-63670_

Affected: sanitize-html. ### Summary A mutation-XSS / allowedTags bypass: when `textarea` (or `xmp`) is included in `allowedTags`, an input containing a literal `</textarea/>` (a solidus right after the RCDATA end-tag name) lets non-allowed markup such as `<img src=x onerror=…>` pass through `saniti…

`xss` `cve-`

### 71. [ThreatsDay: CEO Phishing Kits, 5K Dropbox Account Hacks, OAuth Traps + 17 More Stories](https://thehackernews.com/2026/09/threatsday-ceo-phishing-kits-5k-dropbox.html)
_The Hacker News · Sep 03 · score 0.320_

The worst part is how normal these attacks look. A call from IT. A shared file. A trusted app. A simple request to click “Allow.” Why break in when someone might open the door? That idea runs through this edition. Attackers use real tools, fake login pages, old account links, and software guides tha…

`oauth`

### 72. [French hospital fined €500,000 after breach exposes data of 727,000](https://www.bleepingcomputer.com/news/security/french-hospital-fined-500-000-after-breach-exposes-data-of-727-000/)
_BleepingComputer · Sep 03 · score 0.318_

France's data protection authority (CNIL) has fined Hôpital privé de la Loire €500,000 ($580,000) for failing to adequately protect patients' and their relatives' data. [...]

`breach`

### 73. [Srsly Risky Biz: China's botnets are worth disrupting](https://risky.biz/SRB182/)
_Risky Business News · Sep 03 · score 0.241_

Tom Uren and James Wilson talk about China’s long-term shift to getting private companies to build botnets for cyberespionage. A disruption effort from the US this week is good news, but China has been using these networks for a surprisingly long time and will rebuild. They also discuss a hack at th…

`ransomware`

### 74. [Thomson Reuters Court Software Breach May Have Exposed SSNs and Sealed Data](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)
_The Hacker News · Sep 03 · score 0.232_

Thomson Reuters disclosed on Wednesday that an unauthorized party obtained files from C-Track, the court case management platform sold by its West Publishing Corporation unit, in March 2026, affecting courts in 11 U.S. states, the U.S. Virgin Islands, and Ontario, Canada. West Publishing said it dis…

`breach`

### 75. [OpenList: Authenticated arbitrary file write via Content-Disposition path traversal in SimpleHttp offline-download tool](https://github.com/advisories/GHSA-h6cj-26g5-67fv)
_GHSA — go · Sep 03 · score 0.215 · **MEDIUM 6.5** · CVE-2026-75602_

Affected: github.com/OpenListTeam/OpenList. ### Summary Alist's offline-download feature (`POST /api/fs/add_offline_download` with `tool: "SimpleHttp"`) accepts an attacker-supplied URL, fetches it, and saves the bytes under a per-task temp directory before transferring to the user's destination sto…

`github`

### 76. [stream-json: pick/ignore/filter/replace filters are O(depth²) on nested input — small crafted JSON blocks the event loop for seconds→minutes (DoS)](https://github.com/advisories/GHSA-528h-pc64-c93x)
_GHSA — npm · Sep 03 · score 0.187 · **MEDIUM 6.2** · CVE-2026-71429_

Affected: stream-json. ## Description The path filters `pick`, `ignore`, `filter`, and `replace` — the library's headline "surgical extraction" feature — recompute the full path string from the nesting stack on **every checkable token**. Because the stack length equals the current nesting depth, and…

`token`

### 77. [GitHub Actions: Early September 2026 updates](https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates)
_GitHub Changelog · Sep 03 · score 0.161_

GitHub Actions now includes three updates that give you clearer visibility and finer-grained control over your workflows. New REST API for runner version deprecations A new REST API returns when&#8230; The post GitHub Actions: Early September 2026 updates appeared first on The GitHub Blog .

`github` `github actions` `runner`

### 78. [BraZetsu Malware Turns Compromised Windows Hosts Into Criminal Marketplace Inventory](https://thehackernews.com/2026/09/brazetsu-malware-turns-compromised.html)
_The Hacker News · Sep 03 · score 0.143_

Cybersecurity researchers have disclosed details of a sophisticated Python-based Windows malware framework called BraZetsu that fuels an underground marketplace commercializing access to compromised hosts. "Unlike the standard infostealer model, BraZetsu is a comprehensive master toolkit that empowe…

`python` `windows`

### 79. [CKAN MCP Server: Information disclosure via verbose error reflection](https://github.com/advisories/GHSA-6f9w-9hf2-5rg3)
_GHSA — npm · Sep 03 · score 0.127 · **LOW 3.7** · CVE-2026-73844_

Affected: @aborruso/ckan-mcp-server. ## Summary Error paths reflect raw upstream response bodies and internal exception messages back to the caller instead of a sanitized, generic message. When the server is pointed at (or redirected/SSRF'd to) a host that returns a non-CKAN response, or when an int…

`ssrf`

### 80. [Multiple trusted publishing configurations for npm](https://github.blog/changelog/2026-09-03-multiple-trusted-publishing-configurations-for-npm)
_GitHub Changelog · Sep 03 · score 0.118_

We&#8217;re continuing to make trusted publishing smoother for npm publishers, guided by maintainers feedback. Three updates to npm publishing are now generally available: Multiple trusted publishing configurations per package Staged&#8230; The post Multiple trusted publishing configurations for npm…

`npm` `github`
