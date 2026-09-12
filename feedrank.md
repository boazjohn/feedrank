# feedrank — 2026-09-12

_80 items, 5d window._

### 1. [Artifactory Under Attack: In-the-Wild Exploitation of CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329](https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201)
_Wiz Research · Sep 12 · score 2.091 · **CRITICAL 9.5** · ×4 reports · CVE-2026-42016, CVE-2026-42018, CVE-2026-82329_

Wiz Research has identified active, in-the-wild exploitation of three critical and high-severity vulnerabilities impacting JFrog Artifactory (CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329). Attackers are chaining these vulnerabilities to bypass authentication and gain administrative control.

`cve-`

_also: [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-42016), [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-42018), [The Hacker News](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html)_

### 2. [OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)
_The Hacker News · Sep 12 · score 1.094 · **CRITICAL 9.0**_

The "major malicious attack" that targeted RubyGems in May 2026 was the work of a swarm of OpenAI agents, according to a new report published by researchers Spencer Kitts, Thomas Larsen, and Sydney Von Arx. On May 12, Maciej Mensfeld, senior product manager for software supply chain security at Mend…

`rubygems` `supply chain` `rce`

### 3. [Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/)
_BleepingComputer · Sep 12 · score 0.293 · **CRITICAL 9.5** · CVE-2026-85102, CVE-2026-85103_

The Dutch Nationaal Cyber Security Centrum (NCSC) is warning of imminent exploitation of two critical flaws in Check Point VPN tracked as CVE-2026-85102 and CVE-2026-85103. [...]

`vpn` `cve-`

### 4. [Cisco Secure Firewall Management Center (FMC) and Security Cloud Control (SCC) Firewall Management: Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-20079)
_CISA KEV · Sep 11 · score 3.745 · **CRITICAL 9.0** · ×3 reports · CVE-2026-20079_

Cisco Secure Firewall Management Center (FMC) Software and Cisco Security Cloud Control (SCC) Firewall Management contain an authentication Bypass using an alternate path or channel vulnerability that could allow an unauthenticated, remote attacker to bypass authentication and execute script files o…

`cisco` `firewall` `authentication bypass`

_also: [The Hacker News](https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html), [The Hacker News](https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html)_

### 5. [PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html)
_The Hacker News · Sep 11 · score 0.966 · **CRITICAL 9.5**_

PaperCut on Thursday released a new security maintenance release that replaces all previously published emergency patches that were pushed to address two security flaws that have come under active exploitation. The software development company said PaperCut NG/MF versions 26.0.5, 25.0.13 and 24.1.10…

`actively exploited`

### 6. [GitLab Community Edition and Enterprise Edition: GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-85706)
_CISA KEV · Sep 11 · score 0.922 · **CRITICAL 9.0** · ×3 reports · CVE-2026-85706_

GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API. Required action: Apply mitigations in accordan…

`gitlab`

_also: [The Hacker News](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html), [BleepingComputer](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)_

### 7. [Prowler: SAML Domain Claiming Enables Cross-Tenant Account Takeover](https://github.com/advisories/GHSA-h8m9-jgf8-vwvp)
_GHSA — pip · Sep 11 · score 0.844 · **CRITICAL 9.6** · CVE-2026-59151_

Affected: prowler-cloud. ## SAML Tenant Binding Enables Cross-Tenant Account Takeover ### Summary Prowler's SAML authentication flow trusted the email domain asserted in a SAMLResponse when deciding which tenant should receive the final token. A malicious tenant with its own SAML configuration and a…

`saml` `token`

### 8. [MySQL MCP Server: Missing Origin/Host Validation in SSE Transport Enables Unauthenticated SQL Execution (DNS Rebinding / Direct Exposure)](https://github.com/advisories/GHSA-rqfv-2mw9-78g2)
_GHSA — pip · Sep 11 · score 0.590 · **CRITICAL 10.0** · CVE-2026-59971_

Affected: mysql-mcp-server. ## Summary In SSE/HTTP transport mode, `mysql_mcp_server` constructs `SseServerTransport` without passing `security_settings`. As a result, the MCP Python SDK's DNS-rebinding protection (Origin/Host header validation) is disabled; the Starlette application has no CORS or …

`python` `mysql` `dns`

### 9. [Artifactory flaws chained in attacks deploying backdoor malware](https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/)
_BleepingComputer · Sep 11 · score 0.294 · **CRITICAL 9.5**_

Threat actors are exploiting critical and high-severity vulnerabilities in JFrog Artifactory to bypass authentication, gain administrative privileges, and deploy a Rust backdoor on vulnerable self-hosted servers. [...]

`rust` `backdoor`

### 10. [yayson: Prototype pollution in Store/LegacyStore deserialization](https://github.com/advisories/GHSA-325j-mg25-8q58)
_GHSA — npm · Sep 11 · score 0.277 · **CRITICAL 9.1** · CVE-2026-61534_

Affected: yayson. # Summary `Store`/`LegacyStore` key internal lookup tables by the `type`, `id`, and relationship names from a JSON:API document. Because these were plain objects, a document with `type: "__proto__"` writes onto `Object.prototype`, polluting every object in the process. # Severity S…

`rce` `deserialization` `cvss`

### 11. [Your Critical Vulnerabilities Might Not Be Your Biggest Risk](https://thehackernews.com/2026/09/your-critical-vulnerabilities-might-not.html)
_The Hacker News · Sep 11 · score 0.148 · **CRITICAL 9.5**_

Security teams have become exceptionally talented at finding vulnerabilities. Now, it’s time to turn our attention to optimizing the process for determining which of those vulnerabilities actually create a path to compromise. A critical vulnerability may look alarming on a scanner report, but if it …

`teams`

### 12. [Shopper: Missing authorization on product removal actions in CollectionProducts component](https://github.com/advisories/GHSA-2cg9-97gq-9mqp)
_GHSA — composer · Sep 11 · score 0.892 · **HIGH 8.8** · ×6 reports · CVE-2026-56825, CVE-2026-56826, CVE-2026-56827_

Affected: shopper/framework. ## Title Missing authorization on product removal actions in CollectionProducts component ## Description A lack of authorization control was discovered on both the per-record delete action and the bulk delete action inside `packages/admin/src/Livewire/Components/Collecti…

`php`

_also: [GHSA — composer](https://github.com/advisories/GHSA-99h5-jhh7-v3r3), [GHSA — composer](https://github.com/advisories/GHSA-g3f9-g5vj-p62f), [GHSA — composer](https://github.com/advisories/GHSA-j328-xmgp-j4q3), [GHSA — composer](https://github.com/advisories/GHSA-f7h9-qv4x-9x57), [GHSA — composer](https://github.com/advisories/GHSA-243p-f3cv-c5wh)_

### 13. [@Mockoon/commons-server: Unauthenticated admin API + wildcard CORS allows mock-state hijack and secret theft](https://github.com/advisories/GHSA-rqx4-3f6q-3x2v)
_GHSA — npm · Sep 11 · score 0.614 · **HIGH 8.8** · CVE-2026-59148_

Affected: @mockoon/commons-server, @mockoon/cli. ## Summary Mockoon's admin API ([`commons-server/src/libs/server/admin-api.ts`](https://github.com/mockoon/mockoon/blob/4375a8f/packages/commons-server/src/libs/server/admin-api.ts)) is mounted on the same Express listener as the user-defined mock rou…

`github` `token`

### 14. [FrontMCP and mcp-from-openapi have bypass of OpenAPI external $ref SSRF fix](https://github.com/advisories/GHSA-65h7-9wrw-629c)
_GHSA — npm · Sep 11 · score 0.396 · **HIGH 8.5** · CVE-2026-59973_

Affected: mcp-from-openapi, @frontmcp/adapters, frontmcp. ## Summary The published fix for GHSA-v6ph-xcq9-qxxj / CVE-2026-39885 added a direct hostname denylist for OpenAPI external `$ref` dereferencing, but the latest patched dependency `mcp-from-openapi` 2.3.0 still makes backend-origin requests t…

`ssrf` `cve-`

### 15. [China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor](https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html)
_The Hacker News · Sep 11 · score 0.298 · **HIGH 8.5**_

A China-linked hacking group exploited a flaw in Sogou Input Method, one of the most widely used tools for typing Chinese characters on Windows, to install a backdoor on victims' computers, security company Gen Digital said in&nbsp;research published Thursday. The attack started with a crafted link …

`windows` `backdoor`

### 16. [rclone archive/zip: Zip Slip via unsanitized zip entry names lets a malicious archive escape its own namespace](https://github.com/advisories/GHSA-66hp-wgxq-6f5q)
_GHSA — go · Sep 10 · score 2.434 · **CRITICAL 9.8** · ×9 reports · CVE-2026-88013, CVE-2026-88014, CVE-2026-88015_

Affected: github.com/rclone/rclone. ### Summary `backend/archive` mounts a zip file as a browsable, syncable rclone `Fs` (e.g. `rclone lsf :zip:downloaded.zip` or `rclone copy :zip:downloaded.zip dest:`). Go's `archive/zip` package does not sanitize `file.Name` - it is taken verbatim from the untrus…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-486v-q2wf-fp2r), [GHSA — go](https://github.com/advisories/GHSA-f8g7-2xjc-7mfh), [GHSA — go](https://github.com/advisories/GHSA-p6m2-r3w9-mpxw), [GHSA — go](https://github.com/advisories/GHSA-xwwr-4h3p-r22c), [GHSA — go](https://github.com/advisories/GHSA-p569-5gjg-9cmj)_

### 17. [Traefik: Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling') and Incorrect Authorization](https://github.com/advisories/GHSA-w4v4-9rw7-5326)
_GHSA — go · Sep 10 · score 0.530 · **CRITICAL** · ×4 reports · CVE-2026-88004, CVE-2026-88007, CVE-2026-88008_

Affected: github.com/traefik/traefik/v3, github.com/traefik/traefik/v2. ## Summary There is a high-severity request-smuggling vulnerability in Traefik's handling of the HTTP/1.1 `Upgrade` mechanism. Since Traefik moved to unencrypted HTTP/2 with prior knowledge (Go 1.24), a client-initiated `Upgrade…

`go ` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-v67p-phpq-fc8x), [GHSA — go](https://github.com/advisories/GHSA-qqjf-53cj-pwvv), [GHSA — go](https://github.com/advisories/GHSA-f52w-8j3h-j724)_

### 18. [MikroTik RouterOS: MikroTik RouterOS Missing Authentication for Critical Function Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-67277)
_CISA KEV · Sep 10 · score 0.530 · **CRITICAL 9.0** · CVE-2026-67277_

MikroTik RouterOS contains a missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing S…

`kernel`

### 19. [MikroTik RouterOS: MikroTik RouterOS Improper Neutralization of Argument Delimiters in a Command Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-86060)
_CISA KEV · Sep 10 · score 0.509 · **CRITICAL 9.0** · CVE-2026-86060_

MikroTik RouterOS contains an improper neutralization of argument delimiters in a command vulnerability which allows an attacked to change the trusted RouterOS policy mask, leading to privilege escalation. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance…

`privilege escalation`

### 20. [OmniRoute ACP Custom-Agent Remote Code Execution (RCE)](https://github.com/advisories/GHSA-hf57-cqmx-p4gr)
_GHSA — npm · Sep 10 · score 0.508 · **CRITICAL** · CVE-2026-88062_

Affected: omniroute. ## 2. Summary `POST /api/acp/agents` registers a custom ACP agent. The endpoint accepts user-controlled `binary` and `versionCommand` values. After saving the custom agent, the same request calls `refreshAgentCache()`, which triggers agent version detection. The version probe ev…

`token` `rce`

### 21. [Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html)
_The Hacker News · Sep 10 · score 0.472 · **CRITICAL 9.5**_

Check Point has patched two critical vulnerabilities in the way its firewall and management products handle VPN certificates. The company says both could allow an unauthenticated remote attacker to run code, but only "under specific conditions" that it has not described. One flaw affects Check Point…

`certificate` `vpn` `firewall` `rce`

### 22. [Open WebUI: Users denied by the OAuth role policy can still sign in via token exchange](https://github.com/advisories/GHSA-wvm9-9g5j-623f)
_GHSA — pip · Sep 10 · score 3.014 · **HIGH 8.7** · ×9 reports · CVE-2026-87011, CVE-2026-87014, CVE-2026-87015_

Affected: open-webui. ## Summary Open WebUI's OAuth token exchange endpoint issues a session for a provider access token without running the OAuth role management that the normal OAuth login callback runs. A user whose provider roles the login callback would refuse, or would demote, could still obta…

`oauth` `session` `token`

_also: [GHSA — pip](https://github.com/advisories/GHSA-3g9q-v48f-hh9w), [GHSA — pip](https://github.com/advisories/GHSA-wjwr-xfp9-r66p), [GHSA — pip](https://github.com/advisories/GHSA-p78m-89r6-pgf7), [GHSA — pip](https://github.com/advisories/GHSA-wpmr-8h3q-fwj7), [GHSA — pip](https://github.com/advisories/GHSA-jmc6-2wr8-h3wj)_

### 23. [n8n: Per-Resource OAuth Consent Bypass via Unbound Refresh Token Resource Substitution](https://github.com/advisories/GHSA-cw9w-vv67-hf73)
_GHSA — npm · Sep 10 · score 2.295 · **HIGH** · ×14 reports · CVE-2026-86073, CVE-2026-86074, CVE-2026-86075_

Affected: n8n, n8n. ## Impact The OAuth token endpoint bound an authorization code's first access token to the consented resource, but not its refresh token. Refreshing only checked that the requested resource was registered, not that it matched the original grant. An OAuth client approved for one w…

`oauth` `token` `unbound`

_also: [GHSA — npm](https://github.com/advisories/GHSA-q5wm-mgqx-fv2f), [GHSA — npm](https://github.com/advisories/GHSA-qgpw-8g46-w95v), [GHSA — npm](https://github.com/advisories/GHSA-pq6c-vh67-xpm3), [GHSA — npm](https://github.com/advisories/GHSA-pf83-w3f9-8m37), [GHSA — npm](https://github.com/advisories/GHSA-5m98-cgcr-xx3q)_

### 24. [Excelize: Streaming GetRows row-bound bypass causes attacker-controlled allocation](https://github.com/advisories/GHSA-q5j5-6p94-4gwc)
_GHSA — go · Sep 10 · score 0.390 · **HIGH** · ×2 reports · CVE-2026-59161, CVE-2026-59162_

Affected: github.com/xuri/excelize/v2, github.com/xuri/excelize. # Streaming GetRows row-bound bypass causes attacker-controlled allocation ## Summary Excelize's prior row-bound fix for GHSA-h69g / CVE-2026-54063 protects the checked worksheet parser, but the streaming worksheet reader used by `Rows…

`github` `cve-`

_also: [GHSA — go](https://github.com/advisories/GHSA-fx5j-qcqg-grpf)_

### 25. [mistral.rs Media Loader: Unauthenticated SSRF and arbitrary local file read via image_url](https://github.com/advisories/GHSA-wfgq-w7cq-qj7j)
_GHSA — rust · Sep 10 · score 0.273 · **HIGH 7.2**_

Affected: mistralrs-server-core. ### Summary mistral.rs fetches any request-supplied image/audio URL with no host or IP validation, and opens arbitrary local files (a `file://` URL, or any existing relative/absolute path). A remote, unauthenticated client of any vision/audio deployment can cause the…

`ssrf`

### 26. [Angular: SSR XSS via Unescaped <template> Content Across DocumentFragment Boundaries in Fallback Raw-Content Elements](https://github.com/advisories/GHSA-v3p8-whq6-r5jg)
_GHSA — npm · Sep 10 · score 0.255 · **HIGH** · ×2 reports · CVE-2026-88056, CVE-2026-88060_

Affected: @angular/platform-server, @angular/platform-server, @angular/platform-server, @angular/platform-server. ### Summary An XSS vulnerability exists in `@angular/platform-server` during server-side rendering (SSR) HTML serialization when traversing ancestor tags across `<template>` element boun…

`xss`

_also: [GHSA — npm](https://github.com/advisories/GHSA-f6mr-pjwc-34m4)_

### 27. [Pimcore: SQL Injection in Custom Reports via Malicious Report Configuration](https://github.com/advisories/GHSA-23rh-xw42-fq82)
_GHSA — composer · Sep 10 · score 0.190 · **HIGH 8.8** · CVE-2026-55416_

Affected: pimcore/pimcore, pimcore/pimcore, pimcore/pimcore. # Security Advisory: SQL Injection in Custom Reports via Malicious Report Configuration ## Summary ### Impact A SQL injection vulnerability exists in the Custom Reports bundle (`bundles/CustomReportsBundle/src/Tool/Adapter/Sql.php:84-135`)…

`php` `sql injection`

### 28. [@eigenpal/docx-editor-react: CSS injection and print-time XSS via unescaped embedded font-family name](https://github.com/advisories/GHSA-x7m8-jrm8-hpvx)
_GHSA — npm · Sep 10 · score 0.151 · **HIGH 8.1**_

Affected: @eigenpal/docx-editor-core, @eigenpal/docx-editor-react. ## Summary Embedded font-family names (`word/fontTable.xml`) were interpolated unescaped into an injected `@font-face` `<style>` and into the print window's `document.write()`. A crafted name injects page-wide CSS on open, and breaks…

`exfiltration` `xss`

### 29. [Citrix NetScaler: Citrix NetScaler Authentication Bypass Using an Alternate Path or Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-19490)
_CISA KEV · Sep 09 · score 1.063 · **CRITICAL 9.0** · CVE-2026-19490_

Citrix NetScaler ADC and NetScaler Gateway contain an authentication-bypass vulnerability involving an alternate path or channel. When the NetScaler appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy), an unauthenticated remote threat actor may b…

`rdp` `ssl` `vpn` `authentication bypass`

### 30. [N-able N-central Pre-Auth RCE Flaw Exploited in the Wild](https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html)
_The Hacker News · Sep 09 · score 0.743 · **CRITICAL 9.0** · CVE-2026-86218_

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. Th…

`rce` `in the wild` `kev` `cve-` `cvss`

### 31. [Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html)
_The Hacker News · Sep 09 · score 0.584 · **CRITICAL 9.5**_

Microsoft on Tuesday broke Patch Tuesday records by addressing an earth-shattering 974 vulnerabilities spanning its software portfolio, including two flaws that it said have been actively exploited in the wild. These include 723 flaws in Windows, 111 in Office and Office 2016, 62 in SQL, and 22 in D…

`windows` `actively exploited` `in the wild` `critical severity`

### 32. [Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise](https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise)
_Wiz Research · Sep 09 · score 0.523 · **CRITICAL 9.0**_

How default keys, unauthenticated MCP sessions, and custom code guardrails expose cloud AI infrastructure to root-level remote code execution and IAM theft.

`iam` `authentication bypass`

### 33. [Fortinet Multiple Products: Fortinet Multiple Products Heap-based Buffer Overflow Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-25249)
_CISA KEV · Sep 09 · score 0.507 · **CRITICAL 9.0** · CVE-2025-25249_

Fortinet FortiOS, FortiSwitchManager, and FortiSASE contain a heap-based buffer overflow vulnerability that allows an attacker to execute unauthorized code or commands via specially crafted packets. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with C…

`fortinet`

### 34. [SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution](https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html)
_The Hacker News · Sep 09 · score 0.417 · **CRITICAL 9.0** · CVE-2026-44756_

SAP has released security updates to address multiple vulnerabilities, including a maximum-severity flaw in SAP Extended Passport (EPP) Processing that could have a severe impact on the confidentiality, integrity, and availability of the application The vulnerability, tracked as CVE-2026-44756 (CVSS…

`kernel` `cve-` `cvss`

### 35. [Google Chromium V8: Google Chromium V8 Out of Bounds Write Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-87491)
_CISA KEV · Sep 09 · score 0.314 · **CRITICAL 9.0** · ×2 reports · CVE-2026-87491_

Google Chromium V8 contains an out of bounds write vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Ed…

`chrome` `chromium` `edge` `v8`

_also: [The Hacker News](https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html)_

### 36. [Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed](https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html)
_The Hacker News · Sep 09 · score 0.294 · **CRITICAL 9.0** · CVE-2026-69414_

The security researcher known as Chaotic Eclipse has dropped a proof-of-concept (PoC) for yet another zero-day in Microsoft Defender. The vulnerability, codenamed ShieldCrash, is assessed to be a patch bypass for CVE-2026-69414 (CVSS score: 7.8), also called ShieldBreak, which the researcher reporte…

`defender` `zero-day` `cve-` `cvss`

### 37. [Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets](https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html)
_The Hacker News · Sep 09 · score 0.120 · **CRITICAL 9.5**_

Bitcoin wallet company Alby has&nbsp;warned of a critical flaw&nbsp;in Alby Hub that could have let an attacker take over a wallet and send its funds, but only where the owner had made the Hub reachable from the internet. Alby Hub is a self-hosted Lightning wallet, meaning the owner runs it on their…

`lightning`

### 38. [functype-mcp-server: MCP `set_functype_version` Package Alias RCE via Unsanitized pnpm install + Dynamic Import](https://github.com/advisories/GHSA-wcjj-9m6g-2fr2)
_GHSA — npm · Sep 09 · score 0.465 · **HIGH 7.8** · CVE-2026-59176_

Affected: functype-mcp-server. ## MCP `set_functype_version` Package Alias RCE via Unsanitized pnpm install + Dynamic Import ### Summary The `set_functype_version` MCP tool in `functype-mcp-server` accepts an unconstrained `version` string, interpolates it directly into an npm package specifier (`fu…

`npm` `rce`

### 39. [@yeger/turbo-graph: Unauthenticated Network-Exposed Task Execution via /api/run](https://github.com/advisories/GHSA-2r5q-h53f-9rp3)
_GHSA — npm · Sep 09 · score 0.357 · **HIGH 8.8** · CVE-2026-59160_

Affected: @yeger/turbo-graph. ## Unauthenticated Network-Exposed Turborepo Task Execution via /api/run ### Summary `@yeger/turbo-graph` starts its embedded Next.js server without binding to the loopback interface, causing it to listen on all network interfaces (`0.0.0.0:29312` by default). The `/api…

`csrf`

### 40. [Komari: Management Interface CSRF](https://github.com/advisories/GHSA-hxjg-93wc-h8p8)
_GHSA — go · Sep 09 · score 0.353 · **HIGH 8.8**_

Affected: github.com/komari-monitor/komari. # Vulnerability Overview The `session_token` cookie is set **without** the `SameSite` or `Secure` attributes (`login.go:68`). All `/api/admin/` management endpoints rely solely on this cookie for authentication, with **no CSRF token or Origin validation**.…

`go ` `github` `session` `token` `csrf`

### 41. [Identrail Cross-tenant IDOR: Client-supplied GitHub App installation_id is bound to the caller's workspace without ownership verification](https://github.com/advisories/GHSA-cp3j-m783-3ph5)
_GHSA — go · Sep 09 · score 0.284 · **HIGH 8.5** · CVE-2026-59185_

Affected: github.com/identrail/identrail. ## Summary identrail's GitHub App connection-completion endpoint binds a fully client-supplied `installation_id` to the caller's workspace without verifying that the installation belongs to, or was installed by, the workspace that initiated the connect flow.…

`github` `jwt` `token`

### 42. [Joker linter executed project-local .jokerd/linter.* files during linting](https://github.com/advisories/GHSA-m835-3cm9-rggg)
_GHSA — go · Sep 09 · score 0.216 · **HIGH 7.8** · CVE-2026-59172_

Affected: github.com/candid82/joker. ## Impact In Joker versions before 1.8.2, `joker --lint <file>` located a `.jokerd/` directory by walking up from the linted file and executed matching `linter.*` files from that directory before linting. Because these files are executable Joker/Clojure code, lin…

`github`

### 43. [@openhop/server: Path Traversal in Flow ID File Operations](https://github.com/advisories/GHSA-g72f-jw3w-mgh7)
_GHSA — npm · Sep 09 · score 0.153 · **HIGH 8.3** · CVE-2026-59179_

Affected: @openhop/server. ## Path Traversal in Flow ID File Operations ### Summary `@openhop/server` passes unsanitized HTTP route parameters directly to `path.join()` when constructing filesystem paths for flow YAML files. An unauthenticated attacker who can reach the server can read arbitrary `.y…

`docker` `exploit`

### 44. [Severity Is Not a Strategy: What CISA BOD 26-04 Means for the Future of Federal Software Security](https://checkmarx.com/blog/severity-is-not-a-strategy-what-cisa-bod-26-04-means-for-the-future-of-federal-software-security/)
_Checkmarx Zero · Sep 09 · score 0.135 · **HIGH 7.5**_

CISA’s latest directive shifts the focus from severity or number of findings to the actual risk context when deciding how to remediate. For federal cybersecurity teams, that shift is becoming increasingly important as vulnerabilities are discovered faster than teams can fix them. When every high-sev…

`teams`

### 45. [Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html)
_The Hacker News · Sep 08 · score 0.419 · **CRITICAL 9.5** · CVE-2026-75650_

Adobe on Monday released security patches to address a maximum-severity flaw impacting Adobe Commerce and Magento Open Source that has come under active exploitation in the wild. The vulnerability, now tracked as CVE-2026-75650 (CVSS score: 10.0), has been codenamed StyleSmuggler by Sansec, which di…

`rust` `php` `zero-day` `in the wild` `backdoor`

### 46. [Gitea: Remote Code Execution via diffpatch Git Hook Installation](https://github.com/advisories/GHSA-rcr6-4jqh-j84m)
_GHSA — go · Sep 08 · score 0.317 · **CRITICAL 9.8** · CVE-2026-60004_

Affected: gitea.dev. ### Summary Gitea's `diffpatch` endpoint can be abused to install and execute a Git hook from repository-controlled content. An attacker with ordinary write access to a repository can execute arbitrary shell commands as the Gitea OS user. With default open registration, an unaut…

`go `

### 47. [CVE-2026-82533: DeepSeek Harness Vulnerability Lets AI Agents Escape Their Own Sandbox](https://www.ox.security/blog/cve-2026-82533-deepseek-harness-ai-agent-sandbox-escape/)
_OX Security · Sep 08 · score 0.312 · **CRITICAL 9.5** · CVE-2026-82533_

OX Research found and disclosed a critical vulnerability in DeepSeek Harness, DeepSeek&#8217;s open-source AI coding-agent harness, that allowed a sandboxed AI agent to disable its own confinement with a single shell command &#8211; on shipped defaults, with no network exposure and no credentials. V…

`cve-`

### 48. [Predis: Redis command injection and denial of service via CRLF smuggling in pipelined commands on aggregate connections](https://github.com/advisories/GHSA-w6f5-v2h6-g786)
_GHSA — composer · Sep 08 · score 0.289 · **CRITICAL 9.8** · CVE-2026-84372_

Affected: predis/predis. ### Summary An improper CRLF neutralization flaw in Predis' pipeline handling on aggregate connections lets an unauthenticated attacker who can influence any pipelined argument — a value **or** a key, e.g. a URL slug used as a cache key — smuggle arbitrary Redis commands int…

`node` `redis`

### 49. [NLTK: ReDoS in nltk.tgrep via unvalidated user-supplied regular expressions](https://github.com/advisories/GHSA-w3v8-gmh9-3wv7)
_GHSA — pip · Sep 08 · score 0.266 · **CRITICAL 7.5** · ×7 reports · CVE-2026-62384, CVE-2026-78682, CVE-2026-78683_

Affected: nltk. ### Summary The NLTK `tgrep` module accepts user-supplied regular expressions and passes them to the Python `re` engine without a timeout or validation, enabling catastrophic backtracking (ReDoS). Applications that expose the `tgrep` API to external input are vulnerable to a single-r…

`python` `node`

_also: [GHSA — pip](https://github.com/advisories/GHSA-rrv8-h7p8-rx55), [GHSA — pip](https://github.com/advisories/GHSA-3gq4-3j92-5w49), [GHSA — pip](https://github.com/advisories/GHSA-x99w-6fgc-pmfw), [GHSA — pip](https://github.com/advisories/GHSA-6ww7-3frv-cqxh), [GHSA — pip](https://github.com/advisories/GHSA-rhp5-r9x4-f5g2)_

### 50. [CakePHP: FunctionsBuilder::jsonValue() vulerable to SQL injection with PostgresDriver](https://github.com/advisories/GHSA-fxf7-vhh8-7vpq)
_GHSA — composer · Sep 08 · score 0.196 · **CRITICAL** · CVE-2026-77635_

Affected: cakephp/cakephp, cakephp/cakephp, cakephp/cakephp, cakephp/database, cakephp/database. ### Impact The `FunctionsBuilder::jsonValue($field, $jsonPath)` methods with the Postgres driver is vulnerable to SQL injection if user controlled data is supplied to the `$jsonPath` parameter. ### Patch…

`postgres` `sql injection`

### 51. [Semaphore U: OS Command Injection](https://github.com/advisories/GHSA-xp7j-h7jc-4w8p)
_GHSA — go · Sep 08 · score 0.177 · **CRITICAL 9.9** · CVE-2026-73294_

Affected: github.com/semaphoreui/semaphore. # Summary An OS command injection in repository git_url handling lets any user holding the Manager or Owner role on any project (the normal project-collaborator roles) achieve remote code execution on the Semaphore server host. Using git's --upload-pack=<c…

`github` `runner`

### 52. [Microsoft Windows: Microsoft Windows Link Following Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-81963)
_CISA KEV · Sep 08 · score 0.159 · **CRITICAL 9.0** · CVE-2026-81963_

Microsoft Windows Update Stack contains a link following vulnerability that allows a local attacker to escalate privileges locally up to SYSTEM. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on…

`windows`

### 53. [Microsoft Windows: Microsoft Windows Heap-Based Buffer Overflow Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-85880)
_CISA KEV · Sep 08 · score 0.159 · **CRITICAL 9.0** · CVE-2026-85880_

Microsoft Windows Advanced Local Procedure Call contains a heap-based buffer overflow vulnerability that allows an attacker to elevate privileges locally. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Update…

`windows`

### 54. [GitPython: Dormant multi-line git-config values are corrupted into live injected directives (e.g. core.hooksPath) on any unrelated GitConfigParser write, enabling RCE](https://github.com/advisories/GHSA-284h-m62q-gf8w)
_GHSA — pip · Sep 08 · score 0.127 · **CRITICAL 9.8** · CVE-2026-78676_

Affected: GitPython. - **CWE:** CWE-88 (Argument Injection) / CWE-94 (Code Injection) — via a read-then-corrupt-on-rewrite config round trip, not a direct setter argument - **Affected component:** `git/config.py` — `GitConfigParser._read()` (multi-line value decoding, lines 444-541, esp. `string_dec…

`rce`

### 55. [Composer arbitrary command execution via a malicious package's Perforce source URL](https://github.com/advisories/GHSA-rvx4-ffvw-m9q3)
_GHSA — composer · Sep 08 · score 0.559 · **HIGH** · CVE-2026-84361_

Affected: composer/composer, composer/composer. ## Summary If the `p4` Perforce CLI client is installed, a malicious dependency package from a package repository allowing arbitrary perforce source URLs (packagist.org is safe) could execute arbitrary commands when running `composer install` or `compo…

`composer` `packagist`

### 56. [HTTPX2: Secure WebSocket traffic sent without TLS through SOCKS proxies](https://github.com/advisories/GHSA-7mj9-2mp8-4m2p)
_GHSA — pip · Sep 08 · score 0.355 · **HIGH 8.1** · CVE-2026-84381_

Affected: httpcore2, httpx2. ### Summary httpcore2 does not start TLS for `wss://` connections routed through a SOCKS5 proxy. The WebSocket opening handshake and all subsequent frames are sent in plaintext through the proxy path, despite the caller selecting the secure `wss` scheme. The transport fl…

`tls`

### 57. [Nodemailer: IDN/Punycode domain allow-list bypass leads to email delivery to an attacker-controlled domain](https://github.com/advisories/GHSA-wmmp-3585-3rmp)
_GHSA — npm · Sep 08 · score 0.311 · **HIGH 7.5** · ×2 reports_

Affected: nodemailer. ### Summary Nodemailer resolves an international (IDN / non-ASCII) recipient **domain** to a different Punycode `xn--` label than every UTS‑46‑conformant parser (web browsers, the WHATWG URL Standard, Node's `url.domainToASCII`, Python's `idna`). Its address normalizer (`_norma…

`python` `node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-2x7j-588g-ccc2)_

### 58. [gRPC-Go xDS servers: Denial of Service (DoS) via crash due to missing `:authority` and `Host` headers](https://github.com/advisories/GHSA-2v4p-qf9q-27wj)
_GHSA — go · Sep 08 · score 0.234 · **HIGH** · ×2 reports · CVE-2026-84303, CVE-2026-84445_

Affected: google.golang.org/grpc, google.golang.org/grpc, google.golang.org/grpc. A vulnerability exists in gRPC-Go servers configured with `xds.NewGRPCServer()` where a crafted request missing both `:authority` and `Host` headers can cause a server panic, resulting in a Denial of Service (DoS). Ser…

`go ` `golang`

_also: [GHSA — go](https://github.com/advisories/GHSA-qc2q-p7wx-3px3)_

### 59. [js-yaml: maxTotalMergeKeys does not limit CPU use for empty merge sources](https://github.com/advisories/GHSA-2883-xcg3-v3hh)
_GHSA — npm · Sep 08 · score 0.233 · **HIGH 7.5** · CVE-2026-84375_

Affected: js-yaml, js-yaml. ## Summary `maxTotalMergeKeys` does not count empty mappings. An attacker can repeatedly merge a large sequence of them and consume significant CPU without reaching the configured limit. ## Example ```yaml arr: &arr [{}, {}, {}, ...] # N empty mappings targets: - <<: *arr…

`node`

### 60. [multer vulnerable to Denial of Service via crafted multipart field names](https://github.com/advisories/GHSA-wc9g-mqfw-jrwm)
_GHSA — npm · Sep 08 · score 0.205 · **HIGH 7.5** · ×2 reports · CVE-2026-77078, CVE-2026-82333_

Affected: multer. ### Impact A vulnerability in multer allows a remote, unauthenticated attacker to crash the Node.js process with a single `multipart/form-data` request. Two specially crafted text field names cause an uncaught `RangeError: Invalid array length` inside multer's field parsing, which …

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-535w-7cp7-47q4)_

### 61. [mongodb: Reject "." and NUL bytes in database and collection names](https://github.com/advisories/GHSA-65fr-j4p9-vc33)
_GHSA — composer · Sep 08 · score 0.175 · **HIGH 8.1** · CVE-2026-81525_

Affected: mongodb/mongodb, mongodb/mongodb. ### Impact Passing untrusted input as part of a database or collection name may result in targeting a different database or collection than specified. ### Patches Fixed in PHP library 1.21.4 and 2.4.1. ### Workarounds Validate database and collection names…

`php` `mongodb`

### 62. [sharp: Vulnerabilities in libheif: GHSA-g89c-p67h-r497 and GHSA-2jg2-4ch7-h545](https://github.com/advisories/GHSA-rgj7-g3m4-5g8c)
_GHSA — npm · Sep 08 · score 0.175 · **HIGH**_

Affected: sharp. ### Impact A number of vulnerabilities, two rated as "Critical" severity using CVSSv3, have been discovered and fixed in the upstream libheif dependency. These can lead to possible remote code execution (RCE) on glibc-based Linux when run under certain conditions. The attack vector …

`linux` `glibc` `rce`

### 63. [Windows ML CLI: CORS misconfig enables localhost RCE](https://github.com/advisories/GHSA-96p9-rh4f-92cf)
_GHSA — pip · Sep 08 · score 0.164 · **HIGH** · CVE-2026-84452_

Affected: winml-cli. Case Description: MSRC Notes: Attachments: 1 file(s) attached (1 mp4) Summary: The vulnerability lies in the 'serve/cli_api.py' component of the 'winml-cli' project, which exposes all winml CLI commands over HTTP without authentication. Although it binds to localhost by default,…

`windows` `rce`

### 64. [SiYuan: The publish-access gate treats encrypted notebooks as publicly accessible by default, allowing anonymous readers to retrieve fully decrypted document content while a notebook is unlocked](https://github.com/advisories/GHSA-v684-q882-jgmq)
_GHSA — go · Sep 08 · score 0.144 · **HIGH 8.6** · ×3 reports · CVE-2026-72789, CVE-2026-72790_

Affected: github.com/siyuan-note/siyuan/kernel. **CVE:** This vulnerability corresponds to [CVE-2026-72789](https://nvd.nist.gov/vuln/detail/CVE-2026-72789). ### Summary `publishAccess.json` is an opt-out list. The publish gate returns *accessible* for anything not explicitly listed in it. Encrypted…

`github` `kernel` `cve-`

_also: [GHSA — go](https://github.com/advisories/GHSA-74pj-6g7r-j55c), [GHSA — go](https://github.com/advisories/GHSA-57v5-wqx3-cgj4)_

### 65. [Laravel Excel writes exports outside the configured filesystem disk when given a caller-controlled path](https://github.com/advisories/GHSA-c7r6-vx3h-w5g2)
_GHSA — composer · Sep 08 · score 0.112 · **HIGH 7.5** · CVE-2026-84374_

Affected: maatwebsite/excel. ### Summary `Excel::store()` resolved the destination path against the process working directory rather than the configured filesystem disk. When that path resolved to an existing file, the export was written straight to it with `fopen()`, bypassing the disk entirely. An…

`php`

### 66. [ZITADEL: Auto-linking by email: IdP-side email verification is not checked](https://github.com/advisories/GHSA-992q-9gwp-7r79)
_GHSA — go · Sep 11 · score 0.651 · **MEDIUM 4.8** · ×2 reports · CVE-2026-56665, CVE-2026-56666_

Affected: github.com/zitadel/zitadel. ### Summary A flaw in the external identity provider handler allows unauthorized account linking to occur under specific administrative configurations. When auto-linking by email is enabled, ZITADEL checks that the local user's email is verified, but does not ex…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-v77h-2w3m-94hx)_

### 67. [Passkey-themed phishing attacks lead to Microsoft 365 data theft](https://www.bleepingcomputer.com/news/security/passkey-themed-phishing-attacks-lead-to-microsoft-365-data-theft/)
_BleepingComputer · Sep 11 · score 0.447_

Microsoft says threat actors linked to ShinyHunters, Helix, and other extortion gangs are using passkey and single sign-on-themed social engineering attacks to compromise corporate Microsoft accounts and steal data from Microsoft 365 services. [...]

`passkey`

### 68. [Malicious Twitch Browser Extension Exposes 30,000 Users’ OAuth Tokens to Russian Bot Service](https://socket.dev/blog/malicious-twitch-browser-extension?utm_medium=feed)
_Socket Blog · Sep 11 · score 0.358_

A Twitch browser extension on Chrome and Firefox forwards users’ live OAuth session tokens through proxies controlled by a Russian bot service.

`oauth` `session` `chrome` `firefox`

### 69. [Risky Bulletin: Anthropic agents went hacking again](https://risky.biz/RBNEWS612/)
_Risky Business News · Sep 11 · score 0.285_

Anthropic agents went hacking again, South Korea increases its data breach fines, Apple notifies three Turkish ministers of mercenary spyware attacks, and CISA is ready to hire 250 staff.

`apple` `breach`

### 70. [Florida confirms DMV database breached via stolen police account](https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/)
_BleepingComputer · Sep 11 · score 0.221_

The Florida Department of Highway Safety and Motor Vehicles (FLHSMV) has confirmed that its DAVID driver database suffered a data breach, saying the attackers gained access using credentials belonging to a police department employee. [...]

`breach`

### 71. [Trezor: 347,000 users targeted in phishing attacks after Brevo breach](https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/)
_BleepingComputer · Sep 11 · score 0.188_

Trezor has revealed that phishing attacks against its customers earlier this week targeted 347,000 email addresses and affected 2,500 users who clicked an embedded malicious link. [...]

`breach`

### 72. [Conti ransomware gang member sentenced to 4 years in prison](https://www.bleepingcomputer.com/news/security/conti-ransomware-gang-member-sentenced-to-four-years-in-prison/)
_BleepingComputer · Sep 11 · score 0.187_

A Ukrainian national has been sentenced to four years in prison for his role in Conti ransomware attacks between 2021 and 2022. [...]

`ransomware`

### 73. [Machine speed, hold the AI: Hand-rolled marimo CVE-2026-39987 exploit](https://webflow.sysdig.com/blog/machine-speed-hold-the-ai-hand-rolled-marimo-cve-2026-39987-exploit)
_Sysdig · Sep 11 · score 0.142 · CVE-2026-39987_

Sysdig TRT details a hand-rolled attack against marimo's CVE-2026-39987 without AI, building custom Python tools to breach a cloud bastion host.

`python` `exploit` `breach` `cve-`

### 74. [Microsoft fixes Teams, Outlook launch failures on ARM Windows PCs](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-teams-outlook-launch-failures-on-arm-windows-pcs/)
_BleepingComputer · Sep 11 · score 0.079_

Microsoft has fixed a bug that prevented Teams and Outlook from launching on ARM-based Windows devices after installing updates released since the August 2026 Patch Tuesday. [...]

`windows` `teams`

### 75. [Auto-resolution and analysis updates in Copilot code review](https://github.blog/changelog/2026-09-11-auto-resolution-and-analysis-updates-in-copilot-code-review)
_GitHub Changelog · Sep 11 · score 0.061_

Copilot code review now resolves its own comments once you address them and writes smart commit messages for you when you apply its code suggestions. Behind the scenes, Copilot now&#8230; The post Auto-resolution and analysis updates in Copilot code review appeared first on The GitHub Blog .

`github`

### 76. [Add VS Code Agents to Copilot usage metrics](https://github.blog/changelog/2026-09-11-add-vs-code-agents-to-copilot-usage-metrics)
_GitHub Changelog · Sep 11 · score 0.035_

GitHub Copilot usage metrics reports now include generally available metrics for activity in the dedicated VS Code Agents window, helping you measure adoption and engagement across enterprises and organizations. What&#8217;s&#8230; The post Add VS Code Agents to Copilot usage metrics appeared first …

`github`

### 77. [Anthropic Identifies Biased Reasoning and Recklessness as Drivers of Claude’s PyPI Attack](https://socket.dev/blog/claude-pypi-attack?utm_medium=feed)
_Socket Blog · Sep 10 · score 0.438_

Anthropic found biased reasoning and recklessness drove Claude Mythos 5 to publish malware on PyPI and compromise a security vendor.

`pypi`

### 78. [Rubrik + RL: Bring Threat Intelligence and Detection to Backups](https://www.reversinglabs.com/blog/rubrik-rl-threat-intelligence-ransomware-backups)
_ReversingLabs · Sep 10 · score 0.289_

With this integration, Rubrik users can now tap ReversingLabs' ransomware feed to decide whether each file in their backup is safe.

`ransomware`

### 79. [Traefik: ForwardAuth identity spoofing via dot-form header alias](https://github.com/advisories/GHSA-rf44-j88r-hh8c)
_GHSA — go · Sep 10 · score 0.279 · **MEDIUM 5.3** · ×2 reports · CVE-2026-88011, CVE-2026-88012_

Affected: github.com/traefik/traefik/v2, github.com/traefik/traefik/v3. ## Summary There is a medium severity vulnerability in Traefik's handling of request headers whose name aliases another header name. Go canonicalizes header names on dashes only, so `X-Auth-User`, `X_Auth_User` and `X.Auth.User`…

`go ` `php` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-7ghq-v6jf-g56c)_

### 80. [New Android malware encrypts files, steals data, and harasses victims](https://www.bleepingcomputer.com/news/security/new-android-malware-encrypts-files-steals-data-and-harasses-victims/)
_BleepingComputer · Sep 10 · score 0.245_

A new Android malware strain called Mantax Otax combines ransomware and spyware capabilities to encrypt files, steal sensitive data, and spam and harass victims. [...]

`ransomware`
