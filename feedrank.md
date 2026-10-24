# feedrank — 2026-10-24

_80 items, 5d window._

### 1. [CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud](https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html)
_The Hacker News · Oct 24 · score 0.712 · **CRITICAL 9.5** · CVE-2026-110447_

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday added two vulnerabilities impacting Collabora Online Built-in CODE Server and Arista VeloCloud Orchestrator (VCO) to its Known Exploited Vulnerabilities (KEV), citing reports of active exploitation in the wild. The critical-s…

`arista` `actively exploited` `in the wild` `kev` `cve-`

### 2. [Node.js Brotli Decoder Out-of-Bounds Write (RCE) – CVE-2026-111497](https://www.ox.security/blog/node-js-brotli-decoder-out-of-bounds-write-rce-cve-2026-111497/)
_OX Security · Oct 24 · score 0.454 · **CRITICAL 9.0** · ×3 reports · CVE-2026-111497_

On October 21, 2026, Node.js shipped security releases across all supported lines fixing a high-severity out-of-bounds write in the bundled Brotli decoder. A Node.js process that decompresses attacker-controlled Brotli data &#8212; including Brotli-encoded HTTP responses it fetches &#8212; can be dr…

`node` `rce` `cve-`

_also: [The Hacker News](https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html), [The Hacker News](https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html)_

### 3. [Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)
_The Hacker News · Oct 24 · score 0.300 · **HIGH 8.5**_

LiteLLM on Friday revealed that an Agent Platform master key accidentally published to a public GitHub repository in late May 2026 ultimately allowed the threat actor to push a malicious version of the popular Python package. "On May 27, 2026, a configuration file was committed to the public LiteLLM…

`python` `github`

### 4. [PHP2Shell (CVE-2026-109618 and CVE-2026-109619): Detecting unauthenticated remote code execution in PHP core](https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core)
_Sysdig · Oct 23 · score 1.486 · **CRITICAL 9.5** · ×7 reports · CVE-2026-109618, CVE-2026-109619_

PHP2Shell (CVE-2026-109618 and CVE-2026-109619) lets an unauthenticated attacker run code on a PHP server with HTTP requests alone. The Sysdig Threat Research Team analyzed the exploitation and outlines affected versions, mitigations, and how to detect post-exploitation activity at runtime with Sysd…

`php` `cve-`

_also: [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/), [Snyk](https://snyk.io/blog/php-patches-critical-unauthenticated-rces/), [Endor Labs](https://www.endorlabs.com/learn/php2shell-critical-vulnerabilities-in-php-cve-2026-109618-cve-2026-109619), [OX Security](https://www.ox.security/blog/cve-2026-109618-cve-2026-109619-two-vulnerabilities-allow-unauthenticated-rce-in-php/), [OX Security](https://www.ox.security/blog/php-cve-2026-109618-cve-2026-109619-what-to-do-before-the-details-drop/)_

### 5. [Laravel TokenGuard authentication bypass through non-string API credentials](https://github.com/advisories/GHSA-f9x3-7vq9-cph6)
_GHSA — composer · Oct 23 · score 0.683 · **CRITICAL** · CVE-2026-114509_

Affected: laravel/framework, laravel/framework. Laravel's built-in TokenGuard, **when configured with a standard token-based API guard**, may be bypassed to authenticate as an arbitrary existing user without knowledge of their valid API token. **Under certain database configurations (MySQL/MariaDB)*…

`mysql` `mariadb` `token` `credential` `authentication bypass`

### 6. [Three Critical Pillow CVEs: RCE and Heap Overflows in Python’s Imaging Library – CVE-2026-112900 CVE-2026-112393 CVE-2026-112403](https://www.ox.security/blog/three-critical-pillow-cves-rce-and-heap-overflows-in-pythons-imaging-library-cve-2026-112900-cve-2026-112393-cve-2026-112403/)
_OX Security · Oct 23 · score 0.582 · **CRITICAL 9.5** · ×2 reports · CVE-2026-112393, CVE-2026-112403, CVE-2026-112900_

Three CVSS 9.2 vulnerabilities in the Python imaging library, allow remote code execution and heap corruption via a single malicious image upload Overview Three critical Pillow vulnerabilities (CVSS 9.2, disclosed 2026-10-19) let a crafted EPS, TIFF or JPEG file trigger command execution or heap cor…

`python` `rce` `cve-` `cvss`

_also: [The Hacker News](https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html)_

### 7. [Echo: WebSocket proxy can retain connections and handlers after client disconnect](https://github.com/advisories/GHSA-9969-6676-49h5)
_GHSA — go · Oct 23 · score 0.562 · **CRITICAL** · ×4 reports_

Affected: github.com/labstack/echo/v4, github.com/labstack/echo/v5. ## Impact Echo's Proxy middleware could retain a handler, copy goroutines and network connections after a WebSocket client disconnected if the upstream kept its connection open. The raw proxy waited for both copy directions to finis…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-h7wr-284f-5qvc), [GHSA — go](https://github.com/advisories/GHSA-cxf3-9h37-7rr8), [GHSA — go](https://github.com/advisories/GHSA-f48p-c9v4-h7xv)_

### 8. [obsidian-tc: Memory-lifecycle tools overwrite unowned notes or partially commit lifecycle changes](https://github.com/advisories/GHSA-r3g7-r4hr-m258)
_GHSA — npm · Oct 23 · score 0.406 · **CRITICAL 9.9** · ×3 reports · CVE-2026-115478, CVE-2026-77363, CVE-2026-77366_

Affected: obsidian-tc. ### Summary `create_entity`, `link_entities`, `rename_entity`, `unlink_entities` and `delete_entity` regenerate a memory note's body from SQLite at the computed `memory/<type>/<name>.md` path. When a note already existed at that path and was not owned by the entity being writt…

`sqlite`

_also: [GHSA — npm](https://github.com/advisories/GHSA-pqh8-4pj7-32xx), [GHSA — npm](https://github.com/advisories/GHSA-84c9-qqpq-2pq5)_

### 9. [HPE patches eight max severity RCE and auth bypass AOS flaws](https://www.bleepingcomputer.com/news/security/hpe-patches-eight-max-severity-rce-and-auth-bypass-aos-flaws/)
_BleepingComputer · Oct 23 · score 0.334 · **CRITICAL 9.0**_

Hewlett Packard Enterprise (HPE) released security updates to patch 72 vulnerabilities in the Aruba Operating System (ArubaOS), including eight maximum-severity authentication bypass and code execution issues. [...]

`rce` `authentication bypass`

### 10. [Arista VeloCloud Orchestrator: Arista VeloCloud Orchestrator SQL Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-114625)
_CISA KEV · Oct 23 · score 0.318 · **CRITICAL 9.0** · CVE-2026-114625_

Arista VeloCloud Orchestrator on-prem contains a SQL injection vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data mana…

`arista` `sql injection`

### 11. [PHP shares mitigation for new RCE vulnerability with no patch](https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/)
_BleepingComputer · Oct 23 · score 0.306 · **CRITICAL 9.0**_

The PHP security team has shared mitigation measures for a new remote code execution vulnerability that affects systems with non-default configurations and has no patch. [...]

`php` `rce`

### 12. [Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents’ Token Balances](https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html)
_The Hacker News · Oct 23 · score 0.218 · **CRITICAL 9.5**_

AI agents paying for API calls with the&nbsp;x402 SDKs&nbsp;could sign a payment for their full balance of a supported token if a malicious API asked for it,&nbsp;security firm V12 said&nbsp;on October 22. The cause was the SDKs' default client, which set no spending limit until releases on August 1…

`token`

### 13. [Abandoned Popcorn Time app exposed millions of devices to RCE attacks](https://www.bleepingcomputer.com/news/security/abandoned-popcorn-time-app-exposed-millions-of-device-to-rce-attacks/)
_BleepingComputer · Oct 23 · score 0.199 · **CRITICAL 9.0**_

Researchers remotely disabled a vulnerable updater in the abandoned Time4Popcorn app, a fork of the Popcorn Time BitTorrent client, closing a security flaw that could have allowed attackers to execute malicious code with elevated privileges on millions of computers. [...]

`rce`

### 14. [Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws](https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html)
_The Hacker News · Oct 23 · score 0.191 · **CRITICAL 9.5**_

Ruby has released versions 4.0.9, 3.4.12, and 3.3.13 to fix three bugs in Onigmo, the regular expression engine built into the language. The bugs lie behind four critical security flaws that GitLab patched over the past month. GitLab found that a specially crafted pattern could corrupt memory while …

`ruby` `gitlab` `rce`

### 15. [PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches](https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html)
_The Hacker News · Oct 23 · score 0.166 · **CRITICAL 9.5** · CVE-2026-115560_

PHP has warned of another way an attacker could run code on a web server, two days after it shipped emergency fixes for the critical PHP2Shell flaws. The new issue, assigned CVE-2026-115560, affects only web applications configured in an unusual way, and PHP considers it an unlikely risk.The project…

`php` `rce` `cve-`

### 16. [Electron: Mitigation for compromised eMudhra intermediate certificates](https://github.com/advisories/GHSA-jr5w-w6x2-84p9)
_GHSA — npm · Oct 23 · score 0.999 · **HIGH 7.4** · ×7 reports · CVE-2026-113796, CVE-2026-113797, CVE-2026-113798_

Affected: electron, electron, electron, electron. ### Impact A set of eMudhra intermediate certificates were compromised and are being blocked by browsers and other TLS clients. This Electron update adds the same block to both Chromium networking and Node.js `tls`, `https` and `fetch`. On earlier ve…

`node` `tls` `certificate` `chromium` `electron`

_also: [GHSA — npm](https://github.com/advisories/GHSA-2p8c-gr87-2676), [GHSA — npm](https://github.com/advisories/GHSA-x562-297c-g43g), [GHSA — npm](https://github.com/advisories/GHSA-98mx-cjp9-gchm), [GHSA — npm](https://github.com/advisories/GHSA-3qxv-5xgr-q7w9), [GHSA — npm](https://github.com/advisories/GHSA-h3v5-h239-pg29)_

### 17. [New Evidence Shows LiteLLM Secret-Stealing Workflows Ran 11 Days Before Supply Chain Attack](https://socket.dev/blog/litellm-attack-timeline?utm_medium=feed)
_Socket Blog · Oct 23 · score 0.757 · **HIGH 8.5**_

Socket uncovered secret-stealing workflows that ran in LiteLLM’s GitHub repository 11 days before the supply chain attack on PyPI and Docker.

`pypi` `github` `supply chain` `docker`

### 18. [filelock: ReadWriteLock on the hard-link route deletes any directory another user renames onto its .filelock-* link directory name](https://github.com/advisories/GHSA-jqc4-5cvw-7w85)
_GHSA — pip · Oct 23 · score 0.671 · **HIGH 7.1** · ×6 reports · CVE-2026-112906, CVE-2026-112907, CVE-2026-112913_

Affected: filelock. `ReadWriteLock` and `AsyncReadWriteLock` (the SQLite-backed reader/writer lock) remove their private `.filelock-*` link directories with `shutil.rmtree` (a recursive delete) on a remembered path. They do not check that the path still names the directory they created. This happens…

`container` `linux` `macos` `sqlite`

_also: [GHSA — pip](https://github.com/advisories/GHSA-9vhv-jxww-xfm5), [GHSA — pip](https://github.com/advisories/GHSA-567q-5qvw-pf92), [GHSA — pip](https://github.com/advisories/GHSA-2g95-wg33-c5x2), [GHSA — pip](https://github.com/advisories/GHSA-crv4-6mhj-j5jh), [GHSA — pip](https://github.com/advisories/GHSA-v4x8-3wr5-3wq8)_

### 19. [Risky Bulletin: Supply chain attack lets ransomware group inside 40 shipping companies](https://risky.biz/RBNEWS624/)
_Risky Business News · Oct 23 · score 0.659 · **HIGH 8.5**_

A ransomware group used a supply chain compromise to hack around 40 shipping companies, the Pentagon assembles a technology sabotage unit, PHP2Shell exploitation gets underway and GoDaddy revokes 400,000 certs.

`supply chain` `ransomware`

### 20. [SiYuan: Missing consistency check between packageName and repoURL/repoHash in bazaar package install allows overwriting an existing, trusted plugin](https://github.com/advisories/GHSA-rpx2-p6hp-x5gj)
_GHSA — go · Oct 23 · score 0.558 · **HIGH 7.5** · ×5 reports · CVE-2026-62204, CVE-2026-73049, CVE-2026-73054_

Affected: github.com/siyuan-note/siyuan/kernel. ## Summary `installBazaarPlugin` (and the equivalent endpoints for widgets/icons/templates/themes) accept `packageName`, `repoURL`, and `repoHash` as independent request fields with no validation that they refer to the same package. `packageName` alone…

`github` `kernel`

_also: [GHSA — go](https://github.com/advisories/GHSA-c8w8-3pqp-wr83), [GHSA — go](https://github.com/advisories/GHSA-4pjg-x8qj-33j5), [GHSA — go](https://github.com/advisories/GHSA-p4qw-vx5p-g984), [GHSA — go](https://github.com/advisories/GHSA-xp3q-r38w-vgqm)_

### 21. [pypdf: Possible long runtimes for repeated references to the same missing object](https://github.com/advisories/GHSA-6c7f-9265-g8fw)
_GHSA — pip · Oct 23 · score 0.541 · **HIGH** · ×6 reports · CVE-2026-113789, CVE-2026-113790, CVE-2026-113791_

Affected: pypdf. ### Impact An attacker who uses this vulnerability can craft a PDF which leads to long runtimes. This requires loading relevant parts of a file (like their pages) where the same, but non-existent indirect object is referenced multiple times. ### Patches This has been fixed in [pypdf…

`github`

_also: [GHSA — pip](https://github.com/advisories/GHSA-jr96-gvgh-j3r4), [GHSA — pip](https://github.com/advisories/GHSA-gmh7-3g9r-mjh5), [GHSA — pip](https://github.com/advisories/GHSA-6vvc-x485-93v7), [GHSA — pip](https://github.com/advisories/GHSA-f54x-cmq8-qg57), [GHSA — pip](https://github.com/advisories/GHSA-cgf9-327m-v77c)_

### 22. [Mistune: Path Traversal and XSS in Include directive](https://github.com/advisories/GHSA-h7ww-273w-6cm8)
_GHSA — pip · Oct 23 · score 0.463 · **HIGH 7.5** · ×2 reports · CVE-2026-115355_

Affected: mistune. The Include directive in `src/mistune/directives/include.py` does not validate that the resolved file path stays within the source directory, allowing path traversal via `../` sequences to read arbitrary files. Additionally, error messages and included file contents are rendered w…

`xss`

_also: [GHSA — pip](https://github.com/advisories/GHSA-8cqv-vvq2-6p8c)_

### 23. [Twisted: Denial of Service in the Twisted IMAP4 Server via a Negative Literal Size in SEARCH](https://github.com/advisories/GHSA-2qrf-pqgx-qh9v)
_GHSA — pip · Oct 23 · score 0.332 · **HIGH 4.9** · ×2 reports · CVE-2026-115774, CVE-2026-115775_

Affected: Twisted. ## Summary An infinite-loop vulnerability (CWE-835) in the Twisted IMAP4 server lets an authenticated client freeze the whole process with one small command. `twisted.mail.imap4.parseNestedParens` reads an IMAP literal size with `int()` and never rejects a negative value. A negati…

`python`

_also: [GHSA — pip](https://github.com/advisories/GHSA-3476-c5c2-fr73)_

### 24. [undici vulnerable to Denial of Service via unhandled error on excessive content-encodings](https://github.com/advisories/GHSA-xjj6-f33q-929c)
_GHSA — npm · Oct 23 · score 0.277 · **HIGH 7.5** · ×2 reports · CVE-2026-109841, CVE-2026-109869_

Affected: undici, undici, undici. ### Impact undici's `fetch()` crashes the Node.js process when a malicious server returns a response with more than five content codings and closes the connection before sending the body. undici rejects such responses (a content-encoding limit), but it created the i…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-f72v-6w45-q472)_

### 25. [MSAL Node authorization code flow may disclose parameters to an attacker-controlled endpoint](https://github.com/advisories/GHSA-xcx6-jx8p-x3h5)
_GHSA — npm · Oct 23 · score 0.263 · **HIGH 7.5** · CVE-2026-109461_

Affected: @azure/msal-node. ### Impact Origin validation error in Microsoft Authentication Library (MSAL) for Node.js allows an unauthorized attacker to disclose information over a network. This affects the auth_code flow. ### Patches Version 7.1.0 and higher are patched. ### Workarounds Ensure you …

`node` `azure`

### 26. [multer vulnerable to Denial of Service via a pending asynchronous fileFilter after request teardown](https://github.com/advisories/GHSA-q7qp-rjg7-q26m)
_GHSA — npm · Oct 23 · score 0.263 · **HIGH 7.5** · CVE-2026-113872_

Affected: multer. ### Impact When `multer` is configured with an asynchronous `fileFilter`, a single request can crash the Node.js process. If a request is aborted (for example when one file is rejected) while another file's async `fileFilter` is still pending, the pending callback later resumes a p…

`node`

### 27. [Happy DOM: Incomplete fix for CVE-2026-33943: unsanitized import alias leads to host code execution](https://github.com/advisories/GHSA-834v-8h66-3h79)
_GHSA — npm · Oct 23 · score 0.252 · **HIGH 8.8** · CVE-2026-115895_

Affected: happy-dom. ## Summary The ESM compiler in `happy-dom@20.14.5` does not validate imported local binding aliases before interpolating them into generated JavaScript. As a result, an invalid ESM import alias can be transformed into a valid JavaScript destructuring default initializer and exec…

`javascript` `cve-`

### 28. [Strands Agents SDK: Exposure of data element to wrong session in the A2A Server](https://github.com/advisories/GHSA-4v6f-7vjh-6x4m)
_GHSA — npm · Oct 23 · score 0.247 · **HIGH 8.1** · CVE-2026-115419_

Affected: strands-agents, @strands-agents/sdk. **Summary** Strands Agents SDK is an open-source SDK, available for Python (strands-agents) and TypeScript (@strands-agents/sdk), for building and running AI agents. An issue exists where, under certain circumstances, the Agent2Agent (A2A) server shares…

`python` `typescript` `session`

### 29. [Russia-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack](https://thehackernews.com/2026/10/russian-linked-hackers-used-new-mesh.html)
_The Hacker News · Oct 23 · score 0.127 · **HIGH 8.5**_

The Russian state-sponsored hacking group Sandworm teamed up with another threat actor to carry out a destructive wiping attack targeting a Ukrainian logistics company last year. According to ESET, the attack involved UAC-0099 (aka Earth Sirrush) obtaining initial access to the target on July 16, 20…

`backdoor`

### 30. [litellm 1.107.0 Compromised on PyPI: Backdoored Wheels Drop a Credential Stealer and an Hourly Remote Code Loader](https://www.stepsecurity.io/blog/litellm-1-107-0-compromised-pypi-backdoored-wheels-credential-stealer)
_StepSecurity · Oct 22 · score 0.748 · **CRITICAL 9.0**_

litellm 1.107.0 PyPI wheels and Docker images shipped a .pth credential stealer and an hourly remote code loader that exfiltrate to litellm.dev. Analysis, IOCs, and how to respond.

`pypi` `docker` `credential` `stealer`

### 31. [Arista patches new VeloCloud Orchestrator zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/)
_BleepingComputer · Oct 22 · score 0.683 · **CRITICAL 9.5**_

Arista Networks released security updates to patch an actively exploited zero-day vulnerability affecting VeloCloud Orchestrator (VCO) On-Prem deployments. [...]

`arista` `zero-day` `actively exploited`

### 32. [Arista Warns of Critical VeloCloud SQL Injection Zero-Day Exploited in Attacks](https://thehackernews.com/2026/10/arista-warns-of-critical-velocloud-sql.html)
_The Hacker News · Oct 22 · score 0.499 · **CRITICAL 9.5**_

Attackers are exploiting a zero-day SQL injection flaw in Arista's VeloCloud Orchestrator (VCO), the&nbsp;central management system&nbsp;for VeloCloud SD-WAN networks, the company said in an&nbsp;advisory&nbsp;on October 22. The flaw lets anyone who can log in to the orchestrator, even with a read-o…

`arista` `zero-day` `sql injection`

### 33. [LiteLLM Suspects GitHub Token Leak in AI Gateway Logs Behind Malicious Package Release](https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html)
_The Hacker News · Oct 22 · score 0.421 · **CRITICAL 9.0**_

LiteLLM on Wednesday disclosed that threat actors compromised "multiple independent security controls" to push a malicious version of the Python package containing a credential stealer and a backdoor. On October 21, 2026, LiteLLM's release pipeline was compromised to push 1.107.0 to the Docker Hub r…

`pypi` `python` `github` `docker` `token`

### 34. [ThreatsDay: AI Secrets Leak, PingCAP Source Theft, Signal Hang-Up Flaw, Laravel Auth Bypass + 21 More](https://thehackernews.com/2026/10/threatsday-ai-secrets-leak-pingcap.html)
_The Hacker News · Oct 22 · score 0.304 · **CRITICAL 9.5**_

This week has already been rough for cybersecurity. Critical PHP and GitLab RCE flaws, serious Linux security bugs, compromised eMudhra certificates, a Node.js RCE flaw, a hacked LiteLLM release, and hundreds of hijacked Tor relays. That's a lot to deal with in just a few days. And the week isn't ev…

`node` `php` `gitlab` `linux` `rce`

### 35. [Node.js Brotli Decoder Bug Could Allow Remote Code Execution in All Supported Versions](https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html)
_The Hacker News · Oct 22 · score 0.225 · **CRITICAL 9.0**_

Node.js released&nbsp;security updates&nbsp;on October 21 for its three supported release lines, 22.x, 24.x and 26.x, fixing 10 flaws. The most serious is a bug in the Brotli decompression code that Node.js bundles, which the project says can allow remote code execution, meaning an attacker could ru…

`node`

### 36. [Machine speed attacks require machine speed detection and response](https://www.bleepingcomputer.com/news/security/machine-speed-attacks-require-machine-speed-detection-and-response/)
_BleepingComputer · Oct 22 · score 0.206 · **CRITICAL 9.5**_

Attackers can steal credentials and begin exfiltrating data within minutes, often before security teams can respond. Exaforce examines real-world attacks involving stolen GitHub tokens, malicious AI installers, and MFA phishing, explaining why faster detection and automated containment are critical.…

`github` `mfa` `teams`

### 37. [PHP2Shell: 24 hours in, 99.3% of Measurable PHP Instances Are Still Unpatched](https://www.ox.security/blog/php2shell-24-hours-in-99-3-of-measurable-php-instances-are-still-unpatched/)
_OX Security · Oct 22 · score 0.188 · **CRITICAL 9.5**_

OX Security tracked over 2.2 million publicly exposed PHP instances following disclosure. Within 24 hours, only 14,151 affected systems visible on Shodan had been patched. The rate at which critical vulnerabilities are discovered continues to outpace our ability to remediate them at scale Overview O…

`php`

### 38. [Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes](https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html)
_The Hacker News · Oct 22 · score 0.182 · **CRITICAL 9.0**_

Linux servers running KSMBD, the kernel's built-in SMB server, are exposed to two publicly reported remote code execution flaws rated 9.0 by&nbsp;Trend Micro's Zero Day Initiative, with no fix yet in the mainline kernel. One of them, ZDI-CAN-33774, can be triggered before any network authentication.…

`linux` `kernel` `smb` `rce` `cvss`

### 39. [toml-node: Quadratic-complexity DoS via many array-of-tables headers in toml.parse()](https://github.com/advisories/GHSA-4qx8-w7c3-pj3p)
_GHSA — npm · Oct 22 · score 0.398 · **HIGH 7.5** · ×3 reports · CVE-2026-114141, CVE-2026-114143, CVE-2026-114144_

Affected: toml. ## Summary `toml.parse()` is vulnerable to a quadratic-complexity (O(n²)) denial-of-service via many array-of-tables (`[[name]]`) headers. `addTableArray()` in `lib/compiler.js` rescans two entire bookkeeping Sets on every `[[name]]` header without pruning unrelated or distinct entri…

`node` `edge`

_also: [GHSA — npm](https://github.com/advisories/GHSA-9j65-hcg3-gc64), [GHSA — npm](https://github.com/advisories/GHSA-9qmh-m7c6-f92p)_

### 40. [Django REST framework: TokenProxy.delete() reports success and revokes nothing](https://github.com/advisories/GHSA-xw6w-gcfp-cf8m)
_GHSA — pip · Oct 22 · score 0.345 · **HIGH 7.5** · ×2 reports · CVE-2026-114137, CVE-2026-114138_

Affected: djangorestframework. ### Summary Deleting an authentication token through `TokenProxy` silently deletes nothing. The call raises no exception and reports success, the database row survives, and the token keeps authenticating. Any application, admin integration or operational script that re…

`python` `token`

_also: [GHSA — pip](https://github.com/advisories/GHSA-33wh-fxxf-88vv)_

### 41. [China-Linked Hackers Use ARTEX AI Agents in ConnectWise Supply Chain Attack](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html)
_The Hacker News · Oct 22 · score 0.296 · **HIGH 8.5**_

Microsoft on Wednesday disclosed that a China state-aligned actor dubbed Storm-0940 was behind the recent supply chain compromise of the ConnectWise Cloud Backup application. During the incident, Storm-0940 used ARTEX, a Go-based agentic AI penetration testing framework that was made closed-source i…

`supply chain`

### 42. [GraphQL Tools: Prototype pollution in mergeIncrementalResult via non-primitive path segments](https://github.com/advisories/GHSA-c4qx-w738-7hr3)
_GHSA — npm · Oct 22 · score 0.256 · **HIGH** · CVE-2026-114604_

Affected: @graphql-tools/utils. ## Report metadata | Field | Value | | --- | --- | | Package | `@graphql-tools/utils` (npm, `pkg:github/ardatan/graphql-tools`) | | Repository | https://github.com/ardatan/graphql-tools | | Component | `mergeIncrementalResult` / `setObjectKeyPath` (`packages/utils/src…

`npm` `github`

### 43. [toml-node: Prototype pollution: parsing a TOML document can write to Object.prototype](https://github.com/advisories/GHSA-h895-cgqg-jf52)
_GHSA — npm · Oct 22 · score 0.206 · **HIGH** · CVE-2026-114142_

Affected: tome. ### Summary CVE-2026-63376 described prototype pollution through __proto__ key-path desynchronization and was fixed in 4.1.2 by rewriting the path bookkeeping and adding an ownedContainers WeakSet. The desynchronization is still reachable, spelled with a quote character instead of a …

`node` `container` `cve-`

### 44. [nbconvert: Arbitrary file write through path traversal in cell output filenames when exporting to md, latex, rst and asciidoc](https://github.com/advisories/GHSA-pjvx-prjx-h659)
_GHSA — pip · Oct 22 · score 0.206 · **HIGH** · CVE-2026-114140_

Affected: nbconvert. ### Summary nbconvert <= v7.17.1 has an arbitrary file write vulnerability due to a path traversal in ipynb cell output metadata, more specifically on the filename attribute. Vulnerable converters : `--to markdown`, `--to latex`, `--to rst`, `--to asciidoc`. In `ExtractOutputPre…

`github`

### 45. [Black: GitHub Action installs unvalidated required-version from pyproject.toml](https://github.com/advisories/GHSA-cg8m-r9f2-5wm2)
_GHSA — pip · Oct 22 · score 0.206 · **HIGH** · CVE-2026-114134_

Affected: black. ### Summary The GitHub Action bundled with Black can read the version from `tool.black.required-version` if `use_pyproject` is set to True. This version is not validated and therefore can be used to execute untrusted code in the context of a victim's repository. ### Details This is …

`github` `cve-`

### 46. [GitPython validates a submodule's ".git" path only after cloning into it (RCE)](https://github.com/advisories/GHSA-83vg-56qc-22m7)
_GHSA — pip · Oct 22 · score 0.175 · **HIGH 7.5** · CVE-2026-114145_

Affected: Gitpython. ### Summary `create_submodule(name, path, url)` clones a submodule into the repo's own `.git` directory before it rejects the path. A `path` of ".git/hooks" is accepted by the pre-clone check, so the submodule is cloned straight into the live hooks directory, and a file named `p…

`rce`

### 47. [GraphQL-core: Denial of service via comment tokens bypassing the parser's max_tokens limit](https://github.com/advisories/GHSA-r77w-qph3-7vf8)
_GHSA — pip · Oct 22 · score 0.175 · **HIGH 7.5** · CVE-2026-75508_

Affected: graphql-core, graphql-core. ### Summary The parser's `max_tokens` limit — the documented defence against oversized GraphQL documents — did not count comment tokens. A document padded with comments could therefore pass a `max_tokens` check of any size while still allocating one `Token` obje…

`token`

### 48. [OpenCode Flaw Lets Malicious MCP Servers Execute Code During Sign-In on Windows and WSL](https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html)
_The Hacker News · Oct 22 · score 0.162 · **HIGH 8.5**_

A flaw in the OpenCode AI coding agent allowed a malicious or hijacked MCP server to run code on a developer's Windows or WSL machine when the developer signed in. OpenCode connects to MCP (Model Context Protocol) servers to add outside tools, and such code would run with the developer's own access.…

`windows`

### 49. [Storybook dev server vulnerable to code injection from the local network](https://github.com/advisories/GHSA-px85-f4q5-jh77)
_GHSA — npm · Oct 22 · score 0.137 · **HIGH** · CVE-2026-114126_

Affected: storybook, storybook, storybook, storybook, @storybook/core. **Summary:** The Storybook dev server exposes its WebSocket authentication token to any client that can load its HTML pages. Any host on a LAN can open a Storybook app by IP address, and therefore obtain the token. The WebSocket …

`token`

### 50. [LiteLLM Compromised in Supply Chain Attack Delivering Credential Stealer and Backdoor](https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html)
_The Hacker News · Oct 21 · score 0.950 · **CRITICAL 9.0**_

The popular LiteLLM Python package has been compromised as part of a software supply chain attack that delivered a credential stealer and a backdoor, according to reports from SafeDep, Socket, StepSecurity, and Upwind. The compromise affects LiteLLM 1.107.0, distributed through PyPI wheels and Docke…

`pypi` `python` `supply chain` `docker` `credential`

### 51. [LiteLLM Compromised, Steals Credentials](https://www.wiz.io/blog/litellm-compromised-steals-credentials)
_Wiz Research · Oct 21 · score 0.695 · **CRITICAL 9.0**_

In a new incident, a malicious version (1.107.0) of the LiteLLM package was uploaded to PyPI and Docker on October 21. The malicious version includes a credential stealer targeting browser, cloud and AI secrets as well as a dormant C2 capability.

`pypi` `docker` `credential` `stealer`

### 52. [LiteLLM 1.107.0 Compromised With A RAT InfoStealer](https://www.ox.security/blog/litellm-1-107-0-compromised-with-a-rat-infostealer/)
_OX Security · Oct 21 · score 0.293 · **CRITICAL 9.0**_

LiteLLM got hijacked again: the AI gateway used to route traffic to dozens of LLM providers shipped a credential stealer with remote access built in Overview On October 21, 2026, a malicious version of LiteLLM (version 1.107.0) was published to PyPI. LiteLLM is one of the most popular open source ga…

`pypi` `credential` `stealer` `rat`

### 53. [PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet](https://www.wiz.io/blog/php2shell-php-rce)
_Wiz Research · Oct 21 · score 0.237 · **CRITICAL 9.5**_

Core PHP engine flaws enable remote code execution and Heartbleed-style memory disclosure across the web.

`php` `rce`

### 54. [PHP Patches Critical RCE Vulnerabilities, Organizations Urged to Take Unpatched Sites Offline](https://socket.dev/blog/php-critical-rce-patches?utm_medium=feed)
_Socket Blog · Oct 21 · score 0.201 · **CRITICAL 9.5**_

PHP releases emergency patches for two critical RCE vulnerabilities as agencies urge organizations to take unpatched sites offline.

`php` `rce`

### 55. [PHP Foundation Says Chainguard Broke Security Embargo Ahead of Emergency Patches](https://socket.dev/blog/php-embargo-dispute?utm_medium=feed)
_Socket Blog · Oct 21 · score 0.181 · **CRITICAL 9.5**_

The PHP Foundation says Chainguard broke a security embargo ahead of critical RCE patches, as leaks disrupted the coordinated release.

`php` `rce`

### 56. [Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html)
_The Hacker News · Oct 21 · score 0.171 · **CRITICAL 9.5**_

GitLab released fixes on October 21 for a flaw that lets an attacker run code on a self-managed server without logging in, and it affects every version of the software going back to 7.0, released in 2014. The fix matters even for administrators who patched nine days earlier: the October 12 update co…

`gitlab` `rce` `cvss`

### 57. [PHP2Shell: What Actually Protects You Before the 14:00 UTC PHP RCE Patch, and What Doesn't](https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html)
_The Hacker News · Oct 21 · score 0.117 · **CRITICAL 9.5**_

You cannot fully block the two critical PHP flaws called PHP2Shell before today's fix, and the one setting being passed around as a workaround is not enough on its own, the security firm that suggested it now says. PHP will release the fix at&nbsp;14:00 UTC on October 21&nbsp;for two flaws it rates …

`php` `rce`

### 58. [PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html)
_The Hacker News · Oct 21 · score 0.117 · **CRITICAL 9.5**_

This story is developing and was written before PHP's scheduled 14:00 UTC release on October 21. Once the release is out, the affected and fixed versions below are confirmed by the official advisory. PHP will ship an out-of-cycle security release at 14:00 UTC today, October 21, for two critical vuln…

`php` `rce` `cvss`

### 59. [PHP Issues Emergency Patches for Two Critical PHP2Shell RCE Flaws as Exploit Attempts Emerge](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html)
_The Hacker News · Oct 21 · score 0.106 · **CRITICAL 9.5**_

PHP has released emergency updates that fix two critical flaws in the language itself, letting an attacker without an account run code on a web server. The fixes are in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, and the PHP team says only updating fully protects a server. The flaws, together called PHP2…

`php` `rce` `exploit`

### 60. [LiteLLM PyPI Package and Docker Images Compromised to Steal Cloud and AI Credentials](https://socket.dev/blog/litellm-compromise?utm_medium=feed)
_Socket Blog · Oct 21 · score 0.587 · **HIGH 8.5**_

A supply chain attack compromised LiteLLM 1.107.0 on PyPI and Docker, spreading malware that steals cloud credentials, developer secrets, and AI provider keys.

`pypi` `supply chain` `docker`

### 61. [OpenChoreo: Authorization bypass on WorkflowRun update allows cross-project takeover of workflow runs](https://github.com/advisories/GHSA-46r4-q7wv-32fc)
_GHSA — go · Oct 21 · score 0.225 · **HIGH 7.4** · CVE-2026-113727_

Affected: github.com/openchoreo/openchoreo, github.com/openchoreo/openchoreo, github.com/openchoreo/openchoreo. ## Summary The OpenChoreo API server authorized `PUT .../workflowruns/{runName}` against ownership metadata taken from the request body, while the object it actually mutated was selected b…

`github`

### 62. [Moov signedxml: Unauthenticated denial of service in exclusive XML canonicalization](https://github.com/advisories/GHSA-5588-rp99-5fjh)
_GHSA — go · Oct 21 · score 0.155 · **HIGH 7.5** · CVE-2026-113729_

Affected: github.com/moov-io/signedxml. Exclusive XML canonicalization (`http://www.w3.org/2001/10/xml-exc-c14n#`) in `github.com/moov-io/signedxml` copied the entire accumulated namespace map at every node during `ValidateReferences()`, before any reference digest or signature check. For a chain of…

`node` `github`

### 63. [Hackers Hid Vasilek Backdoor in VMware Tools During 2-Year Russian Healthcare Intrusion](https://thehackernews.com/2026/10/hackers-hid-vasilek-backdoor-in-vmware.html)
_The Hacker News · Oct 21 · score 0.128 · **HIGH 8.5**_

A Belarus-aligned hacktivist group spent nearly two years within the network of a Russian healthcare organization. According to a report published by Russian cybersecurity firm Solar, the activity has been attributed to a threat cluster dubbed Partisan Zmiy, which is also known as the Cyber Partisan…

`vmware` `backdoor`

### 64. [Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections](https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html)
_The Hacker News · Oct 21 · score 0.111 · **HIGH 8.5**_

Attackers took control of more than 300 Tor exit relays in early October and used them to redirect SSH connections to servers that stole login passwords, a researcher found. Exit relays are the last hop in a Tor circuit, where traffic leaves the network for its destination. Only a password login to …

`ssh`

### 65. [Attackers Abuse UpdraftCentral Keys to Plant Backdoors on WordPress Sites](https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html)
_The Hacker News · Oct 21 · score 0.075 · **HIGH 8.5**_

Unknown threat actors breached TeamUpdraft's website and potentially gained unauthorized access to customers' connection keys for UpdraftCentral, UpdraftVault, and UpdraftClone, using them to backdoor WordPress sites. TeamUpdraft is the developer behind UpdraftPlus, a popular WordPress backup plugin…

`backdoor`

### 66. [Critical FortiSIEM Flaw Gets Public Exploit PoC for Unauthenticated Remote Code Execution](https://thehackernews.com/2026/10/critical-fortisiem-flaw-gets-public.html)
_The Hacker News · Oct 20 · score 0.185 · **CRITICAL 9.5** · CVE-2026-106173_

Cybersecurity researchers have released a proof-of-concept (PoC) exploit for a recently patched critical security flaw impacting Fortinet FortiSIEM that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-106173 (CVSS score: 9.4), is a critical path traversal flaw that c…

`fortinet` `exploit` `cve-` `cvss`

### 67. [Plex Media Server: Plex Media Server External Control of File Name or Path Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96656)
_CISA KEV · Oct 20 · score 0.159 · **CRITICAL 9.0** · CVE-2026-96656_

Plex Media Server contains an external control of file name or path vulnerability which can allow an admin user to write arbitrary files that may be executed on load. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96654, and CVE-2026-96655. Required action: Apply mitigations in acco…

`cve-`

### 68. [Plex Media Server: Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96655)
_CISA KEV · Oct 20 · score 0.159 · **CRITICAL 9.0** · CVE-2026-96655_

Plex Media Server contains a server-side request forgery (SSRF) vulnerability that could allow an authenticated user to request arbitrary internal or external addresses via the '/video/:/transcode/universal' path parameter. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96654, and C…

`ssrf` `cve-`

### 69. [Plex Media Server: Plex Media Server Improper Neutralization of Encoded URI Schemes in a Web Page Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96654)
_CISA KEV · Oct 20 · score 0.159 · **CRITICAL 9.0** · CVE-2026-96654_

Plex Media Server contains an improper neutralization of encoded URI schemes in a web page vulnerability that could allow an attacker to call other plugins' functions and supply their own parameters. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96655, and CVE-2026-96656. Required …

`cve-`

### 70. [From Phishing to LLMjacking: Threat Actors Targeting Cloud Billing Accounts for LLM Usage](https://www.wiz.io/blog/from-phishing-to-llmjacking)
_Wiz Research · Oct 20 · score 0.426 · **HIGH 8.5**_

How a single Google Search ad click leads to credential theft, hijacking of cloud billing account, and hundreds of thousands of dollars incurred in unauthorized AI API usage

`credential`

### 71. [Compress/s2: Integer Overflow or Wraparound and Out-of-bounds Write in compress](https://github.com/advisories/GHSA-259r-337f-4rfw)
_GHSA — go · Oct 20 · score 0.084 · **HIGH 7.5** · CVE-2026-63209_

Affected: github.com/klauspost/compress. # Signed Integer Overflow in s2.NewDict ## Summary A signed integer overflow vulnerability in `s2.NewDict()` allows an attacker to bypass repeat index validation by supplying a dictionary with a uvarint-encoded repeat value exceeding `MaxInt64`. When `Dict.En…

`go ` `github`

### 72. [OVHcloud CLI Compromised via GitHub Release Swap: Detonating the Real GlassWorm Loader and What We Found](https://www.stepsecurity.io/blog/ovhcloud-cli-github-release-swap-glassworm)
_StepSecurity · Oct 24 · score 0.384_

An attacker swapped the binaries on five OVHcloud CLI releases, stayed live for 94 minutes, and deleted the evidence. We rebuilt the exact attacker build, recovered the GlassWorm loader from an orphaned commit, and detonated the full chain in an isolated chamber. The replay shows that install.sh nev…

`github` `linux`

### 73. [Everything, everywhere, all at once… the week software broke | Endor Labs](https://www.endorlabs.com/learn/everything-everywhere-all-at-once-the-week-software-broke)
_Endor Labs · Oct 24 · score 0.009_

Three incidents hit at least nine languages and six Linux distributions in 48 hours. If you’re wondering whether you need to update or pin something, the answer is almost certainly yes.

`linux`

### 74. [fast-uri vulnerable to URI scheme spoofing via percent-encoded scheme decoding](https://github.com/advisories/GHSA-w74x-v6f9-j3xg)
_GHSA — npm · Oct 23 · score 0.359 · **MEDIUM 6.1** · ×2 reports · CVE-2026-110306, CVE-2026-110725_

Affected: fast-uri, fast-uri, fast-uri. ### Impact `fast-uri` percent-decodes the scheme component with the legacy global `unescape()` before validating it, so an input whose decoded scheme is a valid but dangerous token is emitted as a live scheme. RFC 3986 section 3.1 does not allow percent-encodi…

`javascript` `token`

_also: [GHSA — npm](https://github.com/advisories/GHSA-333x-w4r6-6crp)_

### 75. [Echo: X-Real-IP extractor trusts the header value instead of the sending peer](https://github.com/advisories/GHSA-h53f-rm2w-w7rg)
_GHSA — go · Oct 23 · score 0.341 · **MEDIUM 5.3** · ×2 reports_

Affected: github.com/labstack/echo/v5. ## Impact In Echo v5, `ExtractIPFromRealIPHeader` checked whether the address supplied in `X-Real-IP` belonged to a trusted range instead of checking the address of the direct network peer. An untrusted client could therefore supply a loopback or private addres…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-x9ff-22gv-65f4)_

### 76. [chi: Client IP spoofing in ClientIPFromXFF via X-Forwarded-For](https://github.com/advisories/GHSA-j6qf-3m9c-vwj3)
_GHSA — go · Oct 23 · score 0.330 · **MEDIUM 4.8** · ×2 reports · CVE-2026-114437_

Affected: github.com/go-chi/chi/v5. ### Summary `ClientIPFromXFF` skips any `X-Forwarded-For` entry in a configured trusted CIDR but never verifies that the direct TCP peer in `http.Request.RemoteAddr` belongs to that CIDR. A client that can reach the Go server directly can therefore append a truste…

`go ` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-7cgw-qmxx-7fc2)_

### 77. [Fallow: A `.*` glob segment let an analyzed repository make Fallow test paths in the parent of the project root](https://github.com/advisories/GHSA-h4fr-cmh5-qr62)
_GHSA — npm · Oct 23 · score 0.296 · **LOW 3.3** · ×2 reports · CVE-2026-115569_

Affected: fallow, @fallow-cli/fallow-node, fallow-cli, fallow-config, fallow-core. ### Impact Fallow expands some globs from the analyzed repository on disk. Before 3.34.0, a segment such as `.*`, `.?` or `..*` in such a glob also matched the special `..` entry. The `glob` crate tests `..` against a…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-jfwm-3p3c-6hx5)_

### 78. [Quest Diagnostics confirms data breach exposed patient records](https://www.bleepingcomputer.com/news/security/quest-diagnostics-confirms-data-breach-exposed-patient-records/)
_BleepingComputer · Oct 23 · score 0.286_

American clinical laboratory company Quest Diagnostics disclosed that patient records have been exposed after a threat actor gained unauthorized access to its Quanum LSM system. [...]

`breach`

### 79. [setuptools: Windows path escape via namespace_packages.txt during legacy wheel installation  Description](https://github.com/advisories/GHSA-xmj3-9gf7-h52w)
_GHSA — pip · Oct 23 · score 0.275 · **LOW**_

Affected: setuptools. ### Summary On Windows, attacker-controlled content in a wheel's `.dist-info/namespace_packages.txt` can cause setuptools' legacy wheel installation path to create an `__init__.py` outside the requested `destination_eggdir`. The attacker can influence the destination path, but …

`windows`

### 80. [vLLM: Forged multimodal UUID + P0/P1 processor-cache eviction drift: unauthenticated remote crash of the whole vLLM engine](https://github.com/advisories/GHSA-p92p-rxj5-7p2x)
_GHSA — pip · Oct 23 · score 0.267 · **MEDIUM 6.5** · CVE-2026-114050_

Affected: vllm. ## Summary Multimodal content parts (`image_url`, `video_url`, `input_audio`, ...) accept a user-supplied `uuid` field that vLLM uses **verbatim as the item's cache identity** (`mm_hash`). The two frontend/engine processor caches (P0 "sender" cache in the API process, P1 "receiver" c…

`exploit`
