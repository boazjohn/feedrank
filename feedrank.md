# feedrank — 2026-10-03

_80 items, 5d window._

### 1. [Warlock Exploits SharePoint Flaws to Disable Security Tools and Deploy Ransomware](https://thehackernews.com/2026/10/warlock-exploits-sharepoint-flaws-to.html)
_The Hacker News · Oct 03 · score 0.602 · **CRITICAL 9.5**_

The suspected China-linked threat actor known as Warlock is still continuing to weaponize Microsoft SharePoint vulnerabilities, likely both old and new, in attacks targeting organizations in Portuguese- and Spanish-speaking countries. The activity, observed by the Symantec and Carbon Black Threat Hu…

`ransomware`

### 2. [SiYuan Agent Tools SSRF via DNS-Rebinding TOCTOU (Bypass of CheckHostSSRF)](https://github.com/advisories/GHSA-x8gv-g2g3-65fj)
_GHSA — go · Oct 02 · score 1.813 · **CRITICAL 10.0** · ×11 reports · CVE-2026-69085, CVE-2026-72788, CVE-2026-73605_

Affected: github.com/siyuan-note/siyuan/kernel. # Security Advisory — SiYuan Agent Tools SSRF via DNS-Rebinding TOCTOU (Bypass of `CheckHostSSRF`) | Field | Value | |---|---| | **Disclosed by** | joysinleung (`joysinleung@gmail.com`) | | **Report date** | 2026-08-13 | | **Product** | SiYuan (思源笔记) —…

`go ` `github` `kernel` `dns` `ssrf`

_also: [GHSA — go](https://github.com/advisories/GHSA-p23f-cm6q-2qp8), [GHSA — go](https://github.com/advisories/GHSA-4vpg-gwqq-w44c), [GHSA — go](https://github.com/advisories/GHSA-3cc2-h3v6-rqpq), [GHSA — go](https://github.com/advisories/GHSA-vg99-7gj7-2fr5), [GHSA — go](https://github.com/advisories/GHSA-9cqf-hhrq-7v45)_

### 3. [Fortinet FortiMail: Fortinet FortiMail Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-104286)
_CISA KEV · Oct 02 · score 1.252 · **CRITICAL 9.5** · ×3 reports · CVE-2026-104286_

Fortinet FortiMail contains a path traversal and an improper neutralization of NULL byte or NULL character vulnerability that may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests. Required action: Apply mitigations in accordance w…

`fortinet`

_also: [The Hacker News](https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html), [BleepingComputer](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/)_

### 4. [gitea-runner: workflow container.options passes host namespaces and capability flags to job container when privileged mode is disabled](https://github.com/advisories/GHSA-x4q3-gcj3-m6cf)
_GHSA — go · Oct 02 · score 0.868 · **CRITICAL 9.9** · CVE-2026-73802_

Affected: gitea.com/gitea/runner. ### Summary act_runner appends workflow-controlled `jobs.<job>.container.options` directly to the Docker HostConfig for the job container. When runner privileged mode is disabled, only `Privileged` is forced false. Host namespace flags, capability expansion, and sec…

`runner` `container` `docker`

### 5. [Vibe-Trading FastAPI endpoints permit unauthenticated access, file upload, and an RCE chain](https://github.com/advisories/GHSA-v2f8-6655-7grj)
_GHSA — pip · Oct 02 · score 0.609 · **CRITICAL 10.0** · ×3 reports_

Affected: vibe-trading-ai. ### Summary: 5 findings — unauthenticated full-API exposure (F1, lead Critical), read-side authorization gap that persists even with `API_AUTH_KEY` set (F2), unauthenticated file write of `.py`/`.sh`/`.yaml` to a server-returned path (F3), default-permissive CORS that comb…

`rce`

_also: [GHSA — pip](https://github.com/advisories/GHSA-5rmq-chc7-m22f), [GHSA — pip](https://github.com/advisories/GHSA-jqmf-mx4f-hfr6)_

### 6. [Zammad GmbH Zammad: Zammad GmbH Zammad Improper Privilege Management Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-102490)
_CISA KEV · Oct 02 · score 0.595 · **CRITICAL 9.0** · CVE-2026-102490_

Zammad GmbH Zammad contains an improper privilege management vulnerability that can allow the local zammad user to escalate privileges to root. This vulnerability can be chained with CVE-2026-102489. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with …

`cve-`

### 7. [GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers](https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html)
_The Hacker News · Oct 02 · score 0.589 · **CRITICAL 9.5**_

A critical flaw in GitLab's AI Gateway could let a logged-in user with Duo Agent Platform access run commands on the gateway under certain conditions, GitLab&nbsp;said in an advisory. The gateway is the service that connects a GitLab instance to AI models, and only organizations that host their own …

`gitlab` `duo`

### 8. [Trigger.dev: Cross-tenant SQL injection in the TSQL query compiler (POST /api/v1/query) via unsanitized window-function name](https://github.com/advisories/GHSA-9q4r-4842-93vw)
_GHSA — npm · Oct 02 · score 0.565 · **CRITICAL 7.7** · ×5 reports_

Affected: trigger.dev. ### Summary A cross-tenant SQL injection in the TSQL query compiler lets **any authenticated trigger.dev customer read every other tenant's analytics data**. The customer-facing query endpoint `POST /api/v1/query` accepts a TSQL/TRQL query that is compiled to ClickHouse SQL by…

`clickhouse` `sql injection`

_also: [GHSA — npm](https://github.com/advisories/GHSA-pqxw-g93w-hj9x), [GHSA — npm](https://github.com/advisories/GHSA-gg6r-gp4c-89hp), [GHSA — npm](https://github.com/advisories/GHSA-q567-cr4x-96w4), [GHSA — npm](https://github.com/advisories/GHSA-xxv7-2vv3-h682)_

### 9. [@a2ui/web_core: `openUrl` permits `javascript:` URI execution via agent-supplied button actions](https://github.com/advisories/GHSA-72qq-p3r5-f7wq)
_GHSA — npm · Oct 02 · score 0.492 · **CRITICAL 9.3** · CVE-2026-10032_

Affected: @a2ui/web_core. ### Summary The `openUrl` function in `@a2ui/web_core` passes an agent-controlled URL directly to `window.open()` without validating the URI scheme. A malicious agent can supply a `javascript:` URI as the `url` argument of a `Button` component's `functionCall` action. When …

`javascript` `xss`

### 10. [Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes](https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html)
_The Hacker News · Oct 02 · score 0.432 · **CRITICAL 9.5** · CVE-2026-63688_

Dell has released security updates to address multiple critical security flaws in Dell Container Storage Modules (CSM) that could be exploited by bad actors to take over susceptible systems. The vulnerabilities are listed below - CVE-2026-63688 (CVSS score: 10.0) - A missing authentication for criti…

`kubernetes` `container` `cve-` `cvss`

### 11. [Zammad GmbH Zammad: Zammad GmbH Zammad Session Fixation Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-102489)
_CISA KEV · Oct 02 · score 0.404 · **CRITICAL 9.0** · CVE-2026-102489_

Zammad GmbH Zammad contains a session fixation vulnerability that can lead to remote code execution as the zammad user. This vulnerability can be chained with CVE-2026-102490. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Priorit…

`session` `cve-`

### 12. [GitLab warns of critical RCE vulnerability in AI Gateway service](https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-rce-vulnerability-in-ai-gateway-service/)
_BleepingComputer · Oct 02 · score 0.304 · **CRITICAL 9.5**_

GitLab warned customers today to immediately patch a critical AI Gateway vulnerability that could let attackers run arbitrary commands on vulnerable instances. [...]

`gitlab` `rce`

### 13. [aws-smithy-json: Uncontrolled recursion in the aws-smithy-json unknown-key skip path allows unauthenticated remote denial of service in smithy-rs generated servers](https://github.com/advisories/GHSA-8ffr-xgwf-xj56)
_GHSA — rust · Oct 02 · score 0.547 · **HIGH 7.5** · CVE-2026-18140_

Affected: aws-smithy-json. ### Summary Smithy-RS is a Rust code generation and runtime framework that generates HTTP clients and servers from Smithy interface definitions, powering the AWS SDK for Rust and custom service implementations. An issue exists which allows uncontrolled recursion in the unk…

`rust` `aws`

### 14. [Dulwich: Arbitrary File Write (RCE) on Windows via Unvalidated Drive Letters in Tree Paths](https://github.com/advisories/GHSA-8mcx-5rqc-vhmf)
_GHSA — pip · Oct 02 · score 0.419 · **HIGH 8.8** · ×2 reports_

Affected: dulwich. ### Affected files * `dulwich/index.py` (Methods: `validate_path_element_ntfs`, `_tree_to_fs_path`) * `dulwich/porcelain/__init__.py` (Method: `_checked_worktree_path`) ### Description / Summary A High-severity Path Traversal vulnerability exists in Dulwich's checkout logic when r…

`windows` `rce`

_also: [GHSA — pip](https://github.com/advisories/GHSA-8w8g-wq8h-fq33)_

### 15. [@fastify/busboy vulnerable to Denial of Service via prototype-named multipart part header](https://github.com/advisories/GHSA-x8mw-p69m-v3mx)
_GHSA — npm · Oct 02 · score 0.296 · **HIGH 7.5** · ×2 reports · CVE-2026-19481, CVE-2026-19484_

Affected: @fastify/busboy. ### Impact Versions of `@fastify/busboy` from 1.0.0 and prior to 3.2.1 are vulnerable to a Denial of Service. The multipart header parser stores part-header names on a plain JavaScript object, so a part header named `__proto__` or `constructor` resolves to an inherited val…

`node` `javascript`

_also: [GHSA — npm](https://github.com/advisories/GHSA-xjh9-v7x6-24jw)_

### 16. [Antino Backdoor Uses Outlook and OneDrive for C2 in China-Nexus Espionage Campaign](https://thehackernews.com/2026/10/antino-backdoor-uses-outlook-and.html)
_The Hacker News · Oct 02 · score 0.244 · **HIGH 8.5**_

Government and policy organizations across Asia have become the target of a new campaign orchestrated by a China-nexus threat actor. The activity, which has targeted government and policy organizations in Taiwan, India, the Philippines, Cambodia, Pakistan, Thailand, and Myanmar, involves the deploym…

`cisco` `backdoor`

### 17. [Xray-core: Pinning a CA certificate via pinnedPeerCertSha256 can lead to the success of MITM attacks](https://github.com/advisories/GHSA-5wf9-h793-w73c)
_GHSA — go · Oct 02 · score 0.240 · **HIGH**_

Affected: github.com/xtls/xray-core. ### Summary Pinning a CA certificate via `pinnedPeerCertSha256` can lead to the success of MITM attacks in some cases. ### Details https://github.com/XTLS/Xray-core/blob/45cf2898ab12e97a55dd8f1f3d78d903340bdc9e/transport/internet/tls/config.go#L333-L347 If `r.Con…

`go ` `github` `tls` `certificate` `ca`

### 18. [Microsoft’s X account hacked in crypto pump-and-dump scheme](https://www.bleepingcomputer.com/news/security/microsofts-x-account-hacked-in-crypto-token-pump-and-dump-scheme/)
_BleepingComputer · Oct 02 · score 0.212 · **HIGH 8.5**_

On Thursday, unknown attackers hijacked the official Microsoft account on X, which has over 13 million followers, in what appeared to be a pump-and-dump scheme promoting a crypto token. [...]

`token`

### 19. [figlet is vulnerable to denial of service via unbounded loop when whitespaceBreak is used with a small width](https://github.com/advisories/GHSA-62ch-8vmq-8xm7)
_GHSA — npm · Oct 02 · score 0.176 · **HIGH** · CVE-2026-96780_

Affected: figlet. ### Impact A denial-of-service (infinite loop) can occur in `text()` / `textSync()` when **both**: - `whitespaceBreak: true` is set, **and** - `width` is set smaller than the rendered width of a single FIGlet character. Under these conditions `breakWord()` could never find a valid …

`node`

### 20. [Cisco Catalyst SD-WAN Manager: Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76504)
_CISA KEV · Oct 01 · score 0.917 · **CRITICAL 9.5** · ×3 reports · CVE-2026-76504_

Cisco Catalyst SD-WAN Manager contains a hex encoding vulnerability that could allow an unauthenticated, remote attacker to access an affected system with privileges of the admin user due to improper handling of URI encoding in an HTTP request. Required action: Apply mitigations in accordance with v…

`cisco`

_also: [The Hacker News](https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html), [The Hacker News](https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html)_

### 21. [vm2: Incomplete nodejs.* symbol filtering lets sandbox override host WebStream state checks](https://github.com/advisories/GHSA-jf8q-945g-9q4c)
_GHSA — npm · Oct 01 · score 0.697 · **CRITICAL 10.0** · ×14 reports · CVE-2026-92935, CVE-2026-92937, CVE-2026-92938_

Affected: vm2. ## Summary vm2 current head (`v3.11.5`, commit `7a1f5100b96f48d34e0fe104ab37c0acc5944f92`) still exposes registered Node.js internal symbols from host WebStream prototypes to sandbox code. The prior `nodejs.*` symbol hardening blocks `Symbol.for('nodejs.<name>')` at the source, but th…

`node` `nodejs`

_also: [GHSA — npm](https://github.com/advisories/GHSA-qhwx-74w5-xhxq), [GHSA — npm](https://github.com/advisories/GHSA-jxxv-8r27-vm4p), [GHSA — npm](https://github.com/advisories/GHSA-h85j-hv3c-qfgq), [GHSA — npm](https://github.com/advisories/GHSA-c48m-32m9-vx93), [GHSA — npm](https://github.com/advisories/GHSA-6rh5-qq4q-97xh)_

### 22. [Apple Multiple Products: Apple Multiple Products Out-of-Bounds Write Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-86950)
_CISA KEV · Oct 01 · score 0.468 · **CRITICAL 9.0** · ×3 reports · CVE-2026-86950_

Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see U…

`macos` `apple`

_also: [The Hacker News](https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html), [The Hacker News](https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html)_

### 23. [Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html)
_The Hacker News · Oct 01 · score 0.435 · **CRITICAL 9.0**_

Cryptocurrency exchange Bitget on Wednesday confirmed that attackers who stole $387.5 million last week exploited a zero-day flaw in third-party security products, citing ongoing investigation findings from SlowMist. "Their investigation identified malicious activity involving third-party security p…

`zero-day`

### 24. [ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories](https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html)
_The Hacker News · Oct 01 · score 0.285 · **CRITICAL 9.0**_

This week, the useful words are boring ones: inspect, cache, compile, store, trust. Each sounds harmless. Each can become an attack path when a system does a little more than people expect. A model check can run code. A cache can mix up requests. A public secret can stay useful for years. That is th…

`rce` `zero-day`

### 25. [piscina: Prototype-pollution gadget in ThreadPool.options allows RCE via execArgv / loadBalancer / env](https://github.com/advisories/GHSA-67c8-pqhq-4rmx)
_GHSA — npm · Oct 01 · score 0.204 · **CRITICAL** · CVE-2026-102992_

Affected: piscina, piscina, piscina. ### Summary A prototype-pollution gadget in `ThreadPool.options` allows an attacker who can pollute `Object.prototype` to execute arbitrary code in Piscina worker threads, invoke arbitrary functions during task scheduling, or inject environment variables into wor…

`rce`

### 26. [pypdf: Possible long runtimes with large amount of embedded files](https://github.com/advisories/GHSA-v247-6f48-mgcj)
_GHSA — pip · Oct 01 · score 0.421 · **HIGH** · ×8 reports · CVE-2026-102993, CVE-2026-102994, CVE-2026-102995_

Affected: pypdf. ### Impact An attacker who uses this vulnerability can craft a PDF which leads to long runtimes. This requires accessing the embedded files through the dictionary-based API. ### Patches This has been fixed in [pypdf==6.19.0](https://github.com/py-pdf/pypdf/releases/tag/6.19.0). ### …

`github`

_also: [GHSA — pip](https://github.com/advisories/GHSA-php9-fj8v-98fj), [GHSA — pip](https://github.com/advisories/GHSA-w23x-9jrw-r45c), [GHSA — pip](https://github.com/advisories/GHSA-jw7q-gvrg-4vj3), [GHSA — pip](https://github.com/advisories/GHSA-g9cg-prrw-2r8q), [GHSA — pip](https://github.com/advisories/GHSA-fp3h-c4fm-7vvf)_

### 27. [WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory](https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html)
_The Hacker News · Oct 01 · score 0.379 · **HIGH 8.5**_

Cybersecurity researchers have shed light on a WordPress compromise in which threat actors deployed multiple persistence mechanisms to ensure that the final payload kept returning without having to infect the site again. The backdoor has been codenamed SC after the "SC_" markers present in the injec…

`backdoor`

### 28. [devalue: `stringify`/`uneval` serialize shared memory](https://github.com/advisories/GHSA-j22f-vq7h-c4qm)
_GHSA — npm · Oct 01 · score 0.317 · **HIGH 7.5** · ×4 reports · CVE-2026-92708_

Affected: devalue. ### Impact `stringify` and `uneval` serialize a typed array by emitting its backing `ArrayBuffer`, not just the view. In the case of a Node `Buffer` object, the backing buffer is a process-wide shared pool, meaning unrelated memory can be serialized into a response that is then se…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-hx4r-w6wj-j8fg), [GHSA — npm](https://github.com/advisories/GHSA-x5rw-q4pp-hg5g), [GHSA — npm](https://github.com/advisories/GHSA-4q55-j62x-fr9h)_

### 29. [JupyterLab: Cross-site scripting (XSS) in JupyterLab via crafted language package (jupyterlab.json)](https://github.com/advisories/GHSA-3jqq-pw4j-pqcj)
_GHSA — pip · Oct 01 · score 0.291 · **HIGH 8.1** · ×3 reports · CVE-2026-102830, CVE-2026-102831, CVE-2026-102904_

Affected: jupyterlab, jupyterlab, jupyterlite-core. ## Description A language pack ships a `Plural-Forms` header saying how the language counts, for example `nplurals=2; plural=(n != 1);`. JupyterLab turns that string into a function with `new Function`, so the header gets executed. The check that m…

`xss`

_also: [GHSA — pip](https://github.com/advisories/GHSA-3325-v43h-43rv), [GHSA — pip](https://github.com/advisories/GHSA-6966-vjj6-99xv)_

### 30. [virtualenv: Command injection via --prompt in activate.bat (batch activator)](https://github.com/advisories/GHSA-x78j-v8h9-3j2q)
_GHSA — pip · Oct 01 · score 0.195 · **HIGH** · ×2 reports · CVE-2026-102930, CVE-2026-102937_

Affected: virtualenv. `BatchActivator.quote()` returned its input unchanged, the only activator with no escaping at all. `--prompt`, the `VIRTUALENV_PROMPT` environment variable, and the config file all set the prompt, and `activate.bat` writes it straight into `@set "VAR=value"`. A prompt containin…

`runner` `windows`

_also: [GHSA — pip](https://github.com/advisories/GHSA-94p9-xgh2-xp45)_

### 31. [PyJWT: Unauthenticated RecursionError DoS in pre-verification payload parse (PyJWKClient.get_signing_key_from_jwt / verify_signature=False)](https://github.com/advisories/GHSA-42vr-xj54-vc7v)
_GHSA — pip · Sep 30 · score 0.636 · **CRITICAL 9.1** · ×11 reports · CVE-2026-101917, CVE-2026-101918, CVE-2026-102265_

Affected: PyJWT. ## Summary `PyJWKClient.get_signing_key_from_jwt(token)` — the first step of the JWKS verification flow documented in `docs/usage.rst` — must decode a token's payload before its signature can be checked, via `jwt.api_jwt.decode_complete(token, options={"verify_signature": False})`. …

`jwt` `token`

_also: [GHSA — pip](https://github.com/advisories/GHSA-jwrc-g2q2-pq5p), [GHSA — pip](https://github.com/advisories/GHSA-8wjv-2p76-3863), [GHSA — pip](https://github.com/advisories/GHSA-hxm8-2xgr-2p9m), [GHSA — pip](https://github.com/advisories/GHSA-ffc3-869f-jxw9), [GHSA — pip](https://github.com/advisories/GHSA-w2cx-738m-mc7w)_

### 32. [ShinyHunters suspect arrested in the Netherlands](https://risky.biz/RBNEWS617/)
_Risky Business News · Sep 30 · score 0.377 · **CRITICAL 9.0**_

A ShinyHunters suspect has been arrested in the Netherlands, Apple fixes an iOS zero-day found by Meta, recent Citrix zero-days see mass exploitation within hours and NVIDIA launches an AI sandboxing platform.

`apple` `zero-day`

### 33. [Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets](https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html)
_The Hacker News · Sep 30 · score 0.288 · **CRITICAL 9.0** · CVE-2026-73570_

Threat actors have weaponized a now-patched security flaw in Zimbra Collaboration Suite (ZCS) to deploy web shells and access mailbox data, according to findings from the Microsoft Security Research team. The attack exploits CVE-2026-73570 (CVSS score: 8.9), an unauthenticated operating system comma…

`exploit` `cve-` `cvss`

### 34. [Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution](https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html)
_The Hacker News · Sep 30 · score 0.270 · **CRITICAL 9.5** · CVE-2026-88772_

Cybersecurity researchers have disclosed technical details of a recently patched critical security flaw in Citrix NetScaler ADC and Gateway that has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-88772 (CVSS score: 9.5), has been described as a memory overflow bug…

`exploit` `in the wild` `cve-` `cvss`

### 35. [Sckit Supply Chain Worm Hits MemTensor npm & PyPi scopes](https://www.stepsecurity.io/blog/sckit-supply-chain-worm-hits-memtensor-npm-pypi-scopes)
_StepSecurity · Sep 30 · score 1.520 · **HIGH 8.5**_

Compromised MemTensor npm releases turn an AI memory plugin into a credential-harvesting entry point, exposing prompts and creating a path to further package compromise.

`npm` `pypi` `supply chain` `credential`

### 36. [OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted](https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html)
_The Hacker News · Sep 30 · score 0.477 · **HIGH 7.5**_

A High-severity OpenSSL flaw can leak heap memory to the other side of a DTLS connection or crash the program,&nbsp;OpenSSL said&nbsp;on September 29 as it released fixes. DTLS, the TLS variant used for UDP traffic, resends a handshake message if no reply arrives before the timer expires. The leak o…

`tls` `openssl`

### 37. [tornado: CurlAsyncHTTPClient enforces no response-size limit — decompression bomb drives unbounded memory accumulation to OOM](https://github.com/advisories/GHSA-chx6-46f5-w4vp)
_GHSA — pip · Sep 30 · score 0.469 · **HIGH 7.5** · ×2 reports · CVE-2026-49855_

Affected: tornado. An unbounded memory accumulation (decompression bomb) in `tornado.curl_httpclient.CurlAsyncHTTPClient` — the client-side sibling gap of CVE-2026-49855 — verified end-to-end on the 2026-08-15 master snapshot (`6.6.dev1`) and present unchanged in the latest release tag `v6.5.8` and …

`tls` `cve-`

_also: [GHSA — pip](https://github.com/advisories/GHSA-c2m8-h5v5-343r)_

### 38. [fastify vulnerable to Denial of Service via unhandled exception on HTTP/2 trailer responses](https://github.com/advisories/GHSA-4mh8-r7rc-xpvc)
_GHSA — npm · Sep 30 · score 0.363 · **HIGH 7.5** · ×4 reports · CVE-2026-76169, CVE-2026-84428, CVE-2026-84469_

Affected: fastify. ### Impact `fastify` crashes with an uncaught `ERR_HTTP2_INVALID_CONNECTION_HEADERS` exception when a route that registers a response trailer via `reply.trailer()` is served over HTTP/2. Fastify unconditionally adds the `Transfer-Encoding: chunked` header when a trailer is set, wh…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-p68q-wchp-6fh7), [GHSA — npm](https://github.com/advisories/GHSA-hwr6-493r-vm6h), [GHSA — npm](https://github.com/advisories/GHSA-9q9j-q6p8-xq58)_

### 39. [league/commonmark: DisallowedRawHtml bypassed when a disallowed tag name ends the raw-HTML literal](https://github.com/advisories/GHSA-97jj-33gv-5xf9)
_GHSA — composer · Sep 30 · score 0.355 · **HIGH 7.5** · ×2 reports_

Affected: league/commonmark. ﻿## Summary The `DisallowedRawHtml` extension does not escape a disallowed tag when the tag name is the last thing in the raw HTML. A Markdown line containing just `<script` is emitted unchanged, and the next block can supply its attributes. With the shipped GFM defaults…

`xss`

_also: [GHSA — composer](https://github.com/advisories/GHSA-3q6v-r5mr-hxv8)_

### 40. [Russh: Unbounded memory exhaustion via CHANNEL_OPEN flood during a client-stalled rekey](https://github.com/advisories/GHSA-35g8-35p8-c8fw)
_GHSA — rust · Sep 30 · score 0.304 · **HIGH 7.5** · ×3 reports · CVE-2026-102821, CVE-2026-102823, CVE-2026-102824_

Affected: russh. ## Summary A russh **server** can be driven to unbounded heap growth (process OOM / kill) by a peer that speaks only standard SSH messages, in the **default configuration**. The peer starts a key re-exchange (sends `SSH_MSG_KEXINIT`) but never sends the follow-up `SSH_MSG_KEX_ECDH_I…

`ssh`

_also: [GHSA — rust](https://github.com/advisories/GHSA-47hw-gvq5-r2gm), [GHSA — rust](https://github.com/advisories/GHSA-w3jg-pjxf-73p4)_

### 41. [GitPython submodule update path traversal can write outside the repository](https://github.com/advisories/GHSA-59cr-6r3x-644w)
_GHSA — pip · Sep 30 · score 0.278 · **HIGH 7.5** · ×2 reports · CVE-2026-87819_

Affected: GitPython. **Affected:** `GitPython` **3.1.61** (latest release) and `main` — `git/objects/submodule/base.py`. `git diff 3.1.61 origin/main -- git/objects/submodule/` is empty, so both are identical here. --- ## The gap The fix for `GHSA-hmq2-w58f-27jc` added `Submodule._validated_name()` …

`python`

_also: [GHSA — pip](https://github.com/advisories/GHSA-g5vv-9gxw-82hx)_

### 42. [Astro: Malformed port in the Host header can crash the Node adapter](https://github.com/advisories/GHSA-qh8j-hqjv-7m4x)
_GHSA — npm · Sep 30 · score 0.201 · **HIGH** · CVE-2026-102984_

Affected: @astrojs/node. ## Summary In the Astro Node adapter, a request whose `Host` header contains a malformed port (for example `example.com:65536` or `example.com:8080:8080`) produced an invalid request URL. The fallback intended to recover from an unparseable URL reused the same malformed host…

`node`

### 43. [urllib3: HTTPS proxy TLS configuration may be ignored or overridden](https://github.com/advisories/GHSA-8988-9cw3-xx77)
_GHSA — pip · Sep 30 · score 0.191 · **HIGH** · CVE-2026-97687_

Affected: urllib3. ## Impact urllib3 supports configuring TLS independently for an HTTPS proxy and the target server. `proxy_ssl_context`, `proxy_assert_hostname`, and `proxy_assert_fingerprint` configure the TLS connection to the proxy. `ssl_context` and the other target-specific TLS parameters con…

`tls` `ssl`

### 44. [Angular Server-Side Rendering (SSR): Denial of Service via Numeric URL Matrix Parameters](https://github.com/advisories/GHSA-ff3f-86qr-9cv3)
_GHSA — npm · Sep 30 · score 0.110 · **HIGH** · CVE-2026-101896_

Affected: @angular/router, @angular/router, @angular/router, @angular/router. A denial of service (DoS) vulnerability was identified in `@angular/router` when Server-Side Rendering (SSR) is enabled on Node.js (V8). When `@angular/router` parses incoming request URLs, it extracts path segments, matri…

`node` `javascript` `v8`

### 45. [PHPCSUtils: Remote code execution via eval() in AbstractArrayDeclarationSniff::getActualArrayKey()](https://github.com/advisories/GHSA-r6hr-vr92-vv28)
_GHSA — composer · Sep 29 · score 0.405 · **HIGH 8.6** · CVE-2026-65954_

Affected: phpcsstandards/phpcsutils. ### Impact PHPCSUtils versions 1.0.0-alpha1 through 1.2.2 contain an arbitrary code execution vulnerability in `PHPCSUtils\AbstractSniffs\AbstractArrayDeclarationSniff::getActualArrayKey()`. The vulnerable method is reached by any sniff that extends `AbstractArra…

`php`

### 46. [Russia's Star Blizzard Targets 100+ Organizations With Fake Event Invites to Deliver Backdoor](https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html)
_The Hacker News · Sep 29 · score 0.137 · **HIGH 8.5**_

Russian state hackers known as Star Blizzard have been using fake event invitations to trick people into installing a backdoor on their Windows computers,&nbsp;according to Microsoft. The campaigns, aimed at people and organizations tied to Ukraine, have affected more than 100 organizations since Ja…

`windows` `backdoor`

### 47. [How we found 24 Android vulnerabilities using our open source AI security agent](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/)
_GitHub Security Blog · Sep 28 · score 0.113 · **CRITICAL 9.5**_

A look at the targeted AI taskflows behind these findings, the critical Android bugs they uncovered, and how to run the same open-source agent on your own app. The post How we found 24 Android vulnerabilities using our open source AI security agent appeared first on The GitHub Blog .

`github`

### 48. [Danish university DTU breach exposes data of up to 200,000 people](https://www.bleepingcomputer.com/news/security/danish-university-dtu-breach-exposes-data-of-up-to-200-000-people/)
_BleepingComputer · Oct 03 · score 0.272_

The Technical University of Denmark (DTU) says information belonging to up to 200,000 users may have been exposed after hackers accessed its identity and access management system and downloaded a large amount of data. [...]

`breach`

### 49. [Composer: GHSA-gjfg-22fp-rrxx fix bypass via symlinked package bin path](https://github.com/advisories/GHSA-96h3-5x6v-m776)
_GHSA — composer · Oct 02 · score 0.970 · **MEDIUM 6.1** · CVE-2026-59944_

Affected: composer/composer, composer/composer. ## Summary A malicious or compromised Composer package could, when installed as a dependency, cause Composer to change the permissions of a file outside that package's own directory and to register a runnable `vendor/bin` command that points at that ou…

`composer`

### 50. [Anubis: Policy bypass via client controlled X-Original-URI header](https://github.com/advisories/GHSA-6wcg-mqvh-fcvg)
_GHSA — go · Oct 02 · score 0.661 · **MEDIUM 5.8** · CVE-2026-62314_

Affected: github.com/TecharoHQ/anubis. Any HTTP client can bypass Anubis bot protection on the default configuration by adding a single request header. No challenge needs to be solved. Affected versions: v1.22.0 through v1.25.0 (introduced in commit d1d631a, PR #1015) The root cause is in `lib/polic…

`go ` `github`

### 51. [Warlock ransomware breach SharePoint in water, telecom operator attacks](https://www.bleepingcomputer.com/news/security/warlock-ransomware-breach-sharepoint-in-water-telecom-operator-attacks/)
_BleepingComputer · Oct 02 · score 0.317_

The China-linked ransomware group Warlock targeted a water utility, a telecom provider, a regional government body, and a university by exploiting SharePoint vulnerabilities to gain initial access. [...]

`ransomware` `breach`

### 52. [Frontline Education breach exposes school district employee data](https://www.bleepingcomputer.com/news/security/frontline-education-data-breach-impacts-school-district-employees/)
_BleepingComputer · Oct 02 · score 0.314_

Frontline Education is notifying school districts of a data breach after attackers exploited a vulnerability in third-party software to gain unauthorized access to its systems and steal employee information, including Social Security numbers. [...]

`breach`

### 53. [rmcp OAuth client fetches server-controlled resource_metadata URLs](https://github.com/advisories/GHSA-c9xm-49cp-xcr9)
_GHSA — rust · Oct 02 · score 0.225 · **MEDIUM**_

Affected: rmcp. ## Summary The `rmcp` OAuth client accepts a server-controlled `resource_metadata=` URL from the `WWW-Authenticate` header and fetches it without same-origin or private-network validation. An attacker-controlled MCP server can return a `401 WWW-Authenticate: Bearer resource_metadata=…

`rust` `oauth`

### 54. [AI agent exploits Zammad zero-days in DIVD breach: What we know and how to detect it](https://webflow.sysdig.com/blog/ai-agent-exploits-zammad-zero-days-in-divd-breach-what-we-know-and-how-to-detect-it)
_Sysdig · Oct 02 · score 0.202_

`breach`

### 55. [Dell asks admins to patch max severity CSM flaws as soon as possible](https://www.bleepingcomputer.com/news/security/new-max-severity-dell-csm-flaws-give-hackers-admin-privileges/)
_BleepingComputer · Oct 02 · score 0.144_

Dell has patched two maximum severity vulnerabilities in the Container Storage Modules (CSM) that connect Dell enterprise storage arrays to Kubernetes environments. [...]

`kubernetes` `container`

### 56. [Authorities dismantle KillSec group](https://risky.biz/RBNEWS618/)
_Risky Business News · Oct 02 · score 0.137_

Authorities dismantle the KillSec hacking group, South Africa thwarts a ransomware attack against air traffic control systems, the US sanctions Venezuelan ATM hackers and a Chinese APT targets AI experts.

`ransomware`

### 57. [Why CISOs Struggle to Answer the Board's Three Hardest Questions, and How to Fix the Report](https://thehackernews.com/2026/10/why-cisos-struggle-to-answer-boards.html)
_The Hacker News · Oct 02 · score 0.106_

The quarterly board meeting is two weeks out. The security team is pulling exports from the identity provider, the cloud posture tool, the vulnerability scanner, the SIEM and the EDR console. Someone is building a spreadsheet to reconcile them. Someone else is turning that spreadsheet into slides. T…

`siem` `edr`

### 58. [Stateless GitHub App installation tokens rolled out](https://github.blog/changelog/2026-10-02-stateless-github-app-installation-tokens-rolled-out)
_GitHub Changelog · Oct 02 · score 0.070_

The staged rollout of the stateless GitHub App installation token format, which began on April 27, 2026, is complete. By default, all newly minted GitHub App installation tokens will be&#8230; The post Stateless GitHub App installation tokens rolled out appeared first on The GitHub Blog .

`github` `token`

### 59. [Repository security advisory comments API in public preview](https://github.blog/changelog/2026-10-02-repository-security-advisory-comments-api-in-public-preview)
_GitHub Changelog · Oct 02 · score 0.053_

You can now read, add, and edit comments on repository security advisories using the REST API, including advisories created from private vulnerability reports. Until now, the discussion on an advisory&#8230; The post Repository security advisory comments API in public preview appeared first on The G…

`github`

### 60. [Selected models in GitHub Copilot deprecated](https://github.blog/changelog/2026-10-02-selected-models-in-github-copilot-deprecated)
_GitHub Changelog · Oct 02 · score 0.037_

As of today, October 2, 2026, we have deprecated the following models across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions). Model&#8230; The post Selected models in GitHub Copilot deprecated appeared first on The GitHub Blog .

`github`

### 61. [Copilot code review: API support and new default effort level](https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level)
_GitHub Changelog · Oct 02 · score 0.034_

You can now request a GitHub Copilot code review through the REST and GraphQL APIs and set the review effort level for each request. Balanced is also now the default&#8230; The post Copilot code review: API support and new default effort level appeared first on The GitHub Blog .

`github`

### 62. [New fields for SecurityAdvisory GraphQL API](https://github.blog/changelog/2026-10-02-new-fields-for-securityadvisory-graphql-api)
_GitHub Changelog · Oct 02 · score 0.031_

You can now read more of the GitHub Advisory Database directly from the GraphQL API without falling back to the REST API. The SecurityAdvisory object gained five new fields: cveId:&#8230; The post New fields for SecurityAdvisory GraphQL API appeared first on The GitHub Blog .

`github`

### 63. [xxhash-rust: Safe xxh3 custom-secret API accepts too-short secret in release](https://github.com/advisories/GHSA-6g2r-675j-hx59)
_GHSA — rust · Oct 02 · score 0.012 · **LOW 2.3**_

Affected: xxhash-rust. I have a minimized safe Rust witness for xxhash-rust 0.8.15. Safe public route: xxhash_rust::xxh3::xxh3_64_with_secret(&[0x41], &[]) The caller-side harness contains no unsafe code. Under release execution, the internal minimum custom-secret length predicate is enforced only b…

`rust`

### 64. [The EDR blind spot: 3 ways browser attacks evade endpoint telemetry](https://www.bleepingcomputer.com/news/security/the-edr-blind-spot-3-ways-browser-attacks-evade-endpoint-telemetry/)
_BleepingComputer · Oct 02 · score 0.006_

Browser-based attacks can steal sessions, abuse extensions, or manipulate users without creating the endpoint artifacts EDR is designed to detect. NordLayer explains three ways attacks can evade endpoint telemetry and why browser-level controls can help close the gap. [...]

`edr`

### 65. [Confidential comments on repository security advisories](https://github.blog/changelog/2026-10-02-confidential-comments-on-repository-security-advisories)
_GitHub Changelog · Oct 02 · score 0.003_

You can now post confidential comments on repository security advisories. Confidential comments are visible only to people with write access to the repository, so you can discuss a report with&#8230; The post Confidential comments on repository security advisories appeared first on The GitHub Blog .

`github`

### 66. [Police Arrest 16-Year-Old Suspected of Running KillSec, Seize Ransomware Leak Site and Servers](https://thehackernews.com/2026/10/police-arrest-16-year-old-suspected-of.html)
_The Hacker News · Oct 01 · score 0.289_

Police in Spain have arrested a 16-year-old whom investigators suspect of running the KillSec ransomware group. KillSec is accused of stealing data from organizations and threatening to publish it on its leak site unless they paid. The 16-year-old was one of 3 people arrested on September 30, when p…

`ransomware`

### 67. [Insecure Agents Podcast: How to Keep AI Agents From Bypassing Security Controls](https://socket.dev/blog/insecure-agents-security-controls?utm_medium=feed)
_Socket Blog · Oct 01 · score 0.230_

Socket CTO Ahmad Nassri discusses how to keep AI agents from bypassing package blocks, limit credential access, and monitor their actions.

`credential`

### 68. [Police dismantle KillSec ransomware gang allegedly led by 16-year-old](https://www.bleepingcomputer.com/news/security/police-dismantle-killsec-ransomware-gang-allegedly-led-by-16-year-old/)
_BleepingComputer · Oct 01 · score 0.224_

An international law enforcement operation dubbed "Operation KillSwitch" seized the KillSec ransomware gang's data leak site and servers, led to three arrests, and identified a 16-year-old as the group's alleged administrator. [...]

`ransomware` `data leak`

### 69. [The Day-One Hole in Zero Trust Architecture](https://www.bleepingcomputer.com/news/security/the-day-one-hole-in-zero-trust-architecture/)
_BleepingComputer · Oct 01 · score 0.197_

Zero Trust can verify users once they are established, but onboarding creates a gap where organizations must decide who to trust before strong authentication exists. Specops explains why identity verification should begin before credentials, MFA methods, and access are issued. [...]

`mfa`

### 70. [How Financial Services Companies Can Modernize Their Software Supply Chain](https://thehackernews.com/2026/10/how-financial-services-companies-can.html)
_The Hacker News · Oct 01 · score 0.164_

Every security leader at a bank, insurer, or asset manager has had a version of this conversation: Security wants to eliminate a class of vulnerabilities. Engineering explains what it would take to upgrade the platform where they live. Somebody prices out the regression testing. Somebody else raises…

`supply chain`

### 71. [GitHub Actions: macOS 14 runner image retirement](https://github.blog/changelog/2026-10-01-github-actions-macos-14-runner-image-retirement)
_GitHub Changelog · Oct 01 · score 0.147_

The macOS 14 runner image will be retired on November 2, 2026. To raise awareness of the upcoming removal, jobs using macOS 14 will temporarily fail during the following scheduled&#8230; The post GitHub Actions: macOS 14 runner image retirement appeared first on The GitHub Blog .

`github` `github actions` `runner` `macos`

### 72. [Securing the Financial Frontier: How Capital One Uses Socket for Open Source Security](https://socket.dev/blog/capital-one-open-source-security?utm_medium=feed)
_Socket Blog · Oct 01 · score 0.097_

Capital One is partnering with Socket to proactively secure its open source supply chain.

`supply chain`

### 73. [Microsoft says threat actors are ahead in the early AI race](https://www.bleepingcomputer.com/news/security/microsoft-says-threat-actors-are-ahead-in-the-early-ai-race/)
_BleepingComputer · Oct 01 · score 0.087_

Microsoft says cyberattackers are currently benefiting from artificial intelligence faster than defenders, allowing threat actors to speed up vulnerability discovery, malware development, and post-compromise activity while security teams struggle to keep pace. [...]

`teams`

### 74. [Microsoft enables Windows settings backup by default for orgs](https://www.bleepingcomputer.com/news/microsoft/microsoft-enables-windows-settings-backup-by-default-for-orgs/)
_BleepingComputer · Oct 01 · score 0.078_

Microsoft announced that Windows settings backup and restore is now enabled by default on all Microsoft Entra-joined or Microsoft Entra hybrid-joined enterprise systems upgraded to Windows 11 26H2. [...]

`entra` `windows`

### 75. [Rate limits for private vulnerability reports](https://github.blog/changelog/2026-10-01-rate-limits-for-private-vulnerability-reports)
_GitHub Changelog · Oct 01 · score 0.067_

Open source maintainers are receiving more low-quality and automated vulnerability reports, which can bury the reports that matter. Rate limits cap how many new reports a single account can submit&#8230; The post Rate limits for private vulnerability reports appeared first on The GitHub Blog .

`github`

### 76. [GitHub Copilot can now interact with desktop apps with computer use](https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps)
_GitHub Changelog · Oct 01 · score 0.032_

Computer use is now available in public preview in GitHub Copilot CLI and the GitHub Copilot app on macOS and Windows. Copilot can interact with desktop applications on your behalf&#8230; The post GitHub Copilot can now interact with desktop apps with computer use appeared first on The GitHub Blog .

`github` `windows` `macos`

### 77. [Structured forms for private vulnerability reports](https://github.blog/changelog/2026-10-01-structured-forms-for-private-vulnerability-reports)
_GitHub Changelog · Oct 01 · score 0.027_

Private vulnerability reports can now use a structured form that asks reporters for the details you need to assess a vulnerability, including a reproducible proof of concept. A single free-text&#8230; The post Structured forms for private vulnerability reports appeared first on The GitHub Blog .

`github`

### 78. [Securing the Kubernetes Supply Chain: Introducing WizOS Helm Charts](https://www.wiz.io/blog/wizos-helm-charts)
_Wiz Research · Sep 30 · score 0.327_

Secure your Kubernetes supply chain with WizOS Helm Charts. Eliminate hidden CI/CD risks and unmaintained dependencies with hardened, signed, and CVE-scanned charts for seamless Kubernetes deployment.

`ci/cd` `supply chain` `kubernetes` `helm` `cve-`

### 79. [Astro: Netlify Image CDN allowlist bypass enables SSRF](https://github.com/advisories/GHSA-4233-jc72-56c5)
_GHSA — npm · Sep 30 · score 0.286 · **MEDIUM** · CVE-2026-102983_

Affected: @astrojs/netlify. ## Summary The `@astrojs/netlify` adapter generated regular expressions for Netlify Image CDN remote-image allowlists without anchoring them to the beginning of the URL. Netlify evaluates these expressions with `RegExp.test()`, so an allowed image origin appearing anywher…

`cdn` `ssrf`

### 80. [New AISI Report Details How GPT-6 Astra Turned CTF Challenges Into Supply Chain Attacks](https://socket.dev/blog/astra-supply-chain-attacks?utm_medium=feed)
_Socket Blog · Sep 30 · score 0.273_

GPT-6 Astra tried to plant malicious code in simulated open source projects using fake GitHub accounts and deceptive PRs during an assigned CTF challenge.

`github` `supply chain`
