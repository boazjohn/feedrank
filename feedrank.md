# feedrank — 2026-11-14

_80 items, 5d window._

### 1. [NLTK: Quadratic-time CPU denial of service in CCG lexicon parser (fromstring) on wide bracket bodies and operator chains](https://github.com/advisories/GHSA-89p3-fcch-88ph)
_GHSA — pip · Nov 14 · score 1.110 · **HIGH 7.5** · ×6 reports · CVE-2026-126298, CVE-2026-126299, CVE-2026-126300_

Affected: nltk. ## Summary The public CCG lexicon parser `nltk.ccg.lexicon.fromstring` parses caller-influenced lexicon text with two pure-Python loops whose cost is quadratic in the input width. A service that parses an untrusted CCG lexicon string can be driven into tens of seconds of single-threa…

`python`

_also: [GHSA — pip](https://github.com/advisories/GHSA-r53h-rw34-8h97), [GHSA — pip](https://github.com/advisories/GHSA-gpwc-27cw-rh9r), [GHSA — pip](https://github.com/advisories/GHSA-ffr9-mgrr-wcvr), [GHSA — pip](https://github.com/advisories/GHSA-4hvg-fv5c-9936), [GHSA — pip](https://github.com/advisories/GHSA-g5wx-957h-f4wj)_

### 2. [Check Point Multiple Products: Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)
_CISA KEV · Nov 13 · score 1.379 · **CRITICAL 9.5** · ×2 reports · CVE-2026-114713, CVE-2026-123039_

Check Point Firewall, Multi-Domain Security Management Server, Scalable Platforms, Security Gateway, and Security Management Server contain an incorrect permissions assignment for critical resources vulnerability when the Gaia OS DynamicCLI daemon runs as root and listens on a world-writable local s…

`firewall`

_also: [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/13/cisa-adds-two-known-exploited-vulnerabilities-catalog)_

### 3. [Check Point warns of zero-day flaw exploited for root access](https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/)
_BleepingComputer · Nov 13 · score 1.097 · **CRITICAL 9.0**_

Check Point Software has released emergency hotfixes to address a high-severity flaw that hackers have been exploiting to gain root privileges and establish persistence on vulnerable devices since late October. [...]

`zero-day`

### 4. [Critical RCE Vulnerability in Apache HTTP Server: Everything You Need To Know](https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability)
_Wiz Research · Nov 13 · score 0.684 · **CRITICAL 9.5** · ×4 reports · CVE-2026-119618_

Detect and mitigate CVE-2026-119618, a critical RCE vulnerability in Apache HTTP Server. According to Wiz data, 64% of cloud environments have resources vulnerable to CVE-2026-119618. Immediate patching is advised.

`rce` `cve-`

_also: [Sysdig](https://webflow.sysdig.com/blog/httpd-cve-2026-119618-detecting-heap-corruption-and-rce-in-apache-http-server-mod-http2), [OX Security](https://www.ox.security/blog/cve-2026-119618-critical-apache-http-server-flaw-exposes-web-servers-to-remote-code-execution/), [The Hacker News](https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html)_

### 5. [Rucio: Unauthenticated administrator impersonation through SSH challenge tokens](https://github.com/advisories/GHSA-x585-4vv8-2mh2)
_GHSA — pip · Nov 13 · score 0.610 · **CRITICAL 9.8** · CVE-2026-100397_

Affected: rucio, rucio, rucio, rucio. ## Summary SSH challenge tokens are mistakenly accepted as valid credentials during the authentication token validation process. While an SSH challenge token is intended as a short-lived nonce for use in a subsequent SSH key exchange, the function to validate au…

`token` `ssh`

### 6. [How one AI agent exposed five critical enterprise security gaps](https://www.bleepingcomputer.com/news/security/how-one-ai-agent-exposed-five-critical-enterprise-security-gaps/)
_BleepingComputer · Nov 13 · score 0.289 · **CRITICAL 9.5**_

An AI agent built to automate invoice processing could be manipulated into changing vendor bank details through a malicious email, without triggering traditional security alerts. Token Security examines five critical AI agent security gaps and shares practical guidance from industry security leaders…

`token`

### 7. [PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html)
_The Hacker News · Nov 13 · score 0.211 · **CRITICAL 9.0** · CVE-2026-6460_

A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked …

`postgresql` `rce` `cve-` `cvss`

### 8. [Hijacked GitHub Accounts Push “wfx” CI Secret Stealer to Thousands of Repositories | Endor Labs](https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale)
_Endor Labs · Nov 13 · score 0.799 · **HIGH 8.5**_

Stolen GitHub credentials let attackers push a CI secret stealer into thousands of repositories. Learn how the attack works, what it steals, and what to rotate.

`github` `stealer`

### 9. [Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files](https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html)
_The Hacker News · Nov 13 · score 0.693 · **HIGH 8.5**_

An unknown threat actor has been observed targeting unpatched Check Point Security Gateways to obtain initial access via the PHP2Shell vulnerabilities and then a previously unreported local privilege escalation flaw in Gaia OS&nbsp; to deploy a backdoor called TSGA. The activity, detailed by Check P…

`esxi` `exploit` `backdoor` `privilege escalation`

### 10. [ag-psd can exhaust memory when parsing crafted PSD dimensions](https://github.com/advisories/GHSA-qfx6-q44v-9qqw)
_GHSA — npm · Nov 13 · score 0.318 · **HIGH 7.5** · CVE-2026-62297_

Affected: ag-psd. ### Summary readPsd() commits the image/layer buffers from the declared header geometry (width x height x channels x depth, and per-layer rectangles) before validating those values against the actual data. A tiny crafted PSD declaring huge geometry forces a multi-gigabyte allocatio…

`node`

### 11. [Siemens RUGGEDCOM APE1808](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-05)
_CISA Advisories · Nov 12 · score 1.950 · **CRITICAL 9.5** · ×2 reports · CVE-2026-109618, CVE-2026-109619_

View CSAF Summary Palo Alto Networks has published information on vulnerabilities in PAN-OS related to PHP2Shell vulnerabilities. This advisory lists the related Siemens Industrial products affected by these vulnerabilities. Customers are advised to consult and implement the workarounds provided in …

`palo alto` `cve-` `cvss`

_also: [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-01)_

### 12. [New N-able "4EverAble2Shell" zero-day exploited hours after PoC released](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/)
_BleepingComputer · Nov 12 · score 0.965 · **CRITICAL 9.0**_

Hackers are actively exploiting a newly disclosed N-able N-central zero-day vulnerability dubbed "4EverAble2Shell" to compromise servers and deploy cryptocurrency miners, with researchers reporting at least 21 affected systems, including 19 running the company's latest security update. [...]

`zero-day`

### 13. [Apache HTTP Server patches critical HTTP/2 remote code execution flaw](https://www.bleepingcomputer.com/news/security/apache-http-server-patches-critical-http-2-remote-code-execution-flaw/)
_BleepingComputer · Nov 12 · score 0.942 · **CRITICAL 9.5**_

A critical vulnerability in the HTTP/2 module of Apache HTTP Server could be exploited by an unauthenticated attacker to obtain remote code execution (RCE). [...]

`rce`

### 14. [Siemens Desigo, Gridscale](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-02)
_CISA Advisories · Nov 12 · score 0.930 · **CRITICAL 9.5** · ×2 reports · CVE-2026-111497_

View CSAF Summary On October 21, 2026, the Node.js project released security updates addressing a critical vulnerability in the Brotli decoder bundled with Node.js, commonly referred to as "Node2Shell" (tracked as CVE-2026-111497). The vulnerability is an out-of-bounds write that could allow a remot…

`node` `cve-`

_also: [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-03)_

### 15. [Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass](https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html)
_The Hacker News · Nov 12 · score 0.894 · **CRITICAL 9.5** · CVE-2026-120868_

Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass. The critical vulnerabilities that impact NetScaler ADC and NetScaler Gateway are listed be…

`authentication bypass` `cve-` `cvss`

### 16. [PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution](https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html)
_The Hacker News · Nov 12 · score 0.760 · **CRITICAL 9.5** · CVE-2026-126325_

PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325, carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as …

`deserialization` `cve-` `cvss`

### 17. [[tl;dr sec] #354 - ARTEX & Agentic Hacking in the Wild, The Patchless Window, Backporting Security Fixes](https://tldrsec.com/p/tldr-sec-354)
_tl;dr sec · Nov 12 · score 0.718 · **CRITICAL 9.5**_

ARTEX be hacking errybody up in here, the critical gap between when a patch is public and defenders respond, and how stable releases may be missing many patches

`in the wild`

### 18. [CVE-2026-126187: React Server Components Flaw Lets Attackers Execute Code Through Smuggled Flight Rows](https://www.stepsecurity.io/blog/cve-2026-126187-react-flight-rce)
_StepSecurity · Nov 12 · score 0.581 · **CRITICAL 9.0** · CVE-2026-126187_

React shipped fixes on November 10, 2026 for a CVSS 9.5 unauthenticated RCE in React Server Components' Flight protocol. Read how a silent serialization bug turns typed arrays into code execution, who is exposed, and how to find affected installs in CI and on developer machines.

`rce` `cve-` `cvss`

### 19. [New Windows SignDrop zero-day gives hackers SYSTEM privileges](https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/)
_BleepingComputer · Nov 12 · score 0.415 · **CRITICAL 9.0**_

Security researcher Abdelhamid Naceri (also known as Nightmare Eclipse) has released a new Windows zero-day exploit that can let attackers gain SYSTEM privileges. [...]

`windows` `zero-day` `exploit`

### 20. [New SignDrop Zero-Day Exploit Turns Windows CLFS Security Feature Into SYSTEM Access](https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html)
_The Hacker News · Nov 12 · score 0.391 · **CRITICAL 9.0**_

Public exploit code released earlier this week claims that a local Windows user can gain SYSTEM privileges through the Common Log File System driver. The proof of concept, called SignDrop, targets a log-authentication feature added to the driver last year. It abuses how clfs.sys creates companion fi…

`windows` `zero-day` `exploit`

### 21. [CVE-2026-118383: Use-after-free vulnerability in MongoDB](https://securitylabs.datadoghq.com/articles/cve-2026-118383-mongodb-server-use-after-free/)
_Datadog Security Labs · Nov 12 · score 0.310 · **CRITICAL 9.5** · ×2 reports · CVE-2026-118383_

We reproduced CVE-2026-118383, a critical use-after-free in MongoDB Server's primary catch-up process that unauthenticated clients can set up, and explain how to detect and remediate it.

`mongodb` `cve-`

_also: [The Hacker News](https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html)_

### 22. [New N-central Exploits Work Against Patched Servers, Enable Root RCE and Windows SYSTEM Access](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html)
_The Hacker News · Nov 12 · score 0.300 · **CRITICAL 9.0**_

N-able on Thursday said it's investigating a new public disclosure containing claims of additional vulnerabilities in on-premise versions of N-central running version 2026.4.1 HF2. "Based on our initial review, the server issue described depends on a non-default configuration in which the Legacy API…

`windows` `rce`

### 23. [Critical Red Hat Quay Flaw Lets Attackers Read and Overwrite All Private Container Images in a Registry](https://thehackernews.com/2026/11/critical-red-hat-quay-flaw-lets.html)
_The Hacker News · Nov 12 · score 0.281 · **CRITICAL 9.5**_

A critical flaw in Red Hat Quay allows an attacker who can access a Quay registry to read and overwrite private container images in every repository. Quay enables anonymous access by default, and while it is enabled, the attacker needs no account. When it is off, anyone with a valid account can stil…

`container` `exploit`

### 24. [SCKit Malware Turns ScreenConnect Support Sessions Into Potential MSP Attack Paths](https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html)
_The Hacker News · Nov 12 · score 0.269 · **CRITICAL 9.5** · CVE-2026-84869_

The ongoing campaign targeting ConnectWise ScreenConnect deployments involves the exploitation of a now-patched critical security flaw in the remote access software, and not a new vulnerability, it has emerged. Blackpoint Cyber's Adversary Pursuit Group (APG), which shared the details with The Hacke…

`cve-` `cvss`

### 25. [Thousands Of GitHub Accounts Hijacked With wfx-loot CI Secret Stealing Malware Via GitHub Actions & npm](https://www.ox.security/blog/thousands-of-github-accounts-hijacked-with-wfx-loot-ci-secret-stealing-malware-via-github-actions-npm/)
_OX Security · Nov 12 · score 1.129 · **HIGH 8.5**_

Threat actors used thousands of hijacked GitHub accounts to inject a self-erasing CI secret stealer into tens of thousands of repositories, stealing cloud, package registry and AI credentials Overview OX Security researchers are tracking a large-scale supply chain campaign, dubbed wfx-loot, in which…

`npm` `github` `github actions` `supply chain` `stealer`

### 26. [pgEdge Control Plane generates pg_hba.conf with trust authentication for local and loopback connections](https://github.com/advisories/GHSA-vq9p-w6wv-cr25)
_GHSA — go · Nov 12 · score 0.703 · **HIGH 7.8** · CVE-2026-125323_

Affected: github.com/pgEdge/control-plane. ### Summary Every `pg_hba.conf` generated by the pgEdge Control Plane begins with a hard-coded block of `trust` entries covering Unix-socket and loopback connections. Any operating-system account that can reach the Postgres socket or the loopback interface …

`github` `postgres` `credential`

### 27. [Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data](https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html)
_The Hacker News · Nov 12 · score 0.519 · **HIGH 8.0**_

A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections. Fixed ver…

`node`

### 28. [Attacker Used 4,837 Hijacked GitHub Accounts to Run a CI Secret Stealer in 1,806+ Repositories](https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html)
_The Hacker News · Nov 12 · score 0.519 · **HIGH 8.5**_

Starting Tuesday, an attacker used stolen credentials for 4,837 GitHub accounts to plant a secret stealer in repositories those accounts could write to, according to Aikido Security, a security software company. The stealer is built to take the secrets and cloud credentials that a repository's CI wo…

`github` `stealer`

### 29. [pgEdge RAG Server unbounded corpus read allows resource exhaustion from unauthenticated requests](https://github.com/advisories/GHSA-5qg5-rgp6-j5m5)
_GHSA — go · Nov 12 · score 0.418 · **HIGH 7.5** · ×3 reports · CVE-2026-125325, CVE-2026-125326, CVE-2026-125327_

Affected: github.com/pgEdge/pgedge-rag-server. ### Impact An unauthenticated caller able to reach the query endpoint could exhaust database and server resources with ordinary, inexpensive requests. The keyword-search arm read the entire corpus on every request and rebuilt an in-memory BM25 index fro…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-68g8-gh8f-7rhg), [GHSA — go](https://github.com/advisories/GHSA-w437-9mwm-j6vq)_

### 30. [Cisco BroadWorks: Cisco BroadWorks Improper Restriction of XML External Entity Reference Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-20320)
_CISA KEV · Nov 11 · score 1.398 · **CRITICAL 9.5** · ×5 reports · CVE-2026-111560, CVE-2026-111793, CVE-2026-116606_

Cisco BroadWorks contains an improper restriction of XML external entity reference vulnerability that could allow an unauthenticated, remote attacker to read sensitive configuration information on an affected system. Required action: Apply mitigations in accordance with vendor instructions, ensuring…

`cisco`

_also: [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-111560), [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-116606), [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog), [The Hacker News](https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html)_

### 31. [Critical Zoom Workplace Flaw Could Allow Unauthenticated Remote Privilege Escalation](https://thehackernews.com/2026/11/critical-zoom-workplace-flaw-could.html)
_The Hacker News · Nov 11 · score 0.573 · **CRITICAL 9.5** · CVE-2026-108186_

Zoom has released software updates to address two security flaws impacting Zoom Workplace for Windows, including a critical bug that could result in privilege escalation on affected systems. The vulnerabilities are listed below - CVE-2026-108186 (CVSS score: 9.6) - An improper input validation vulne…

`windows` `zoom` `privilege escalation` `cve-` `cvss`

### 32. [Endor Labs’ AI SAST Finds Zero Day Memory-Amplification DoS in Anthropic’s buffa library | Endor Labs](https://www.endorlabs.com/learn/endor-labs-ai-sast-finds-zero-day-cve-2026-55407-buffa)
_Endor Labs · Nov 11 · score 0.390 · **CRITICAL 9.0** · CVE-2026-55407_

We identified an unbounded-allocation data flow in buffa's protobuf decoder that I developed into a ~22x memory-amplification denial of service for CVE-2026-55407

`cve-`

### 33. [Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons](https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html)
_The Hacker News · Nov 11 · score 0.132 · **CRITICAL 9.0**_

An AI model can be given a hidden backdoor by editing fewer than 10 of its rarely used neurons, without retraining the model, Microsoft researchers have shown. When a chosen trigger appears, the model outputs an attacker's command, which an agent using that model would run with the agent's own permi…

`backdoor`

### 34. [eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise](https://thehackernews.com/2026/11/emudhra-revokes-8-more-cas-it.html)
_The Hacker News · Nov 11 · score 0.547 · **HIGH 8.5**_

The in-house Python script behind eMudhra's October key compromise has now cost the company 8 more of its intermediate certificate authorities (CAs), even though it did not weaken their keys. Each intermediate CA has its own private key, which the company uses to sign the certificates it issues. The…

`python` `certificate` `ca`

### 35. [Microsoft Security Advisory CVE-2026-120792 - Aspire Information Disclosure Vulnerability](https://github.com/advisories/GHSA-q6jf-24jf-m3cg)
_GHSA — npm · Nov 11 · score 0.402 · **HIGH 7.3** · ×2 reports · CVE-2026-120778, CVE-2026-120792_

Affected: Aspire.Cli, Aspire.Cli.linux-x64, Aspire.Cli.linux-arm64, Aspire.Cli.linux-musl-x64, Aspire.Cli.osx-x64. ## Executive summary Microsoft is releasing this security advisory to provide information about a vulnerability in the Aspire CLI. This advisory provides guidance on updating affected a…

`dotnet` `github` `linux` `musl` `cve-`

_also: [GHSA — npm](https://github.com/advisories/GHSA-m63f-xhvm-6mv5)_

### 36. [Hackers Exploit Critical Xen Orchestra Auth Bypass Flaw to Gain Admin Access](https://thehackernews.com/2026/11/hackers-exploit-critical-xen-orchestra.html)
_The Hacker News · Nov 10 · score 0.516 · **CRITICAL 9.5**_

French software company Vates VMS has warned of a critical security vulnerability in Xen Orchestra that it said is being actively exploited in the wild. The authentication bypass flaw, which does not yet have a CVE identifier, is tracked as VSA-2026-062. "REST cookie parsing turns authenticationToke…

`xen` `exploit` `actively exploited` `in the wild` `authentication bypass`

### 37. [SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution](https://thehackernews.com/2026/11/sap-patches-four-cvss-100-flaws.html)
_The Hacker News · Nov 10 · score 0.417 · **CRITICAL 9.0**_

Four flaws that attackers could exploit without logging in were fixed today as part of SAP's monthly Security Patch Day—the vendor rates all four 10.0, the maximum CVSS score. Three are in the SAP NetWeaver application server, the software SAP systems run on, and one is in the Web Dispatcher, which …

`exploit` `cvss`

### 38. [node-opcua: Namespace-Level RBAC Fail-Open - Anonymous Write/Call Bypass via Unbound `DefaultRolePermissions](https://github.com/advisories/GHSA-xggf-m53x-jc3f)
_GHSA — npm · Nov 10 · score 0.394 · **CRITICAL 9.1** · CVE-2026-95860_

Affected: node-opcua, node-opcua-address-space, node-opcua-server. ## Summary An unauthenticated (**Anonymous**) client can **Write** protected Variables and **Call** privileged Methods on any Node that lacks explicit per-node permissions. This follows the inheritance model defined by OPC UA Part 3,…

`node` `unbound`

### 39. [SGLang RCE Exploit Breaches NEAR AI, Steals Data From 18 Agents and About 100 Users](https://thehackernews.com/2026/11/sglang-rce-exploit-breaches-near-ai.html)
_The Hacker News · Nov 10 · score 0.388 · **CRITICAL 9.0**_

An attacker exploited a remote code execution flaw in SGLang, an open-source inference engine, and ran code on one of NEAR AI's inference servers last Sunday. The attacker could also have seen requests being processed on that server that day, including requests sent in confidential mode, the company…

`rce` `exploit`

### 40. [GPUStack: Missing authorization on several cluster and resource endpoints allows cross-user access and cluster takeover](https://github.com/advisories/GHSA-3hch-x692-6qj3)
_GHSA — pip · Nov 10 · score 0.334 · **CRITICAL 9.8** · ×4 reports · CVE-2026-102894, CVE-2026-102895, CVE-2026-103002_

Affected: gpustack. ### Impact An authenticated non-administrative user could access a Kubernetes cluster they are not authorized to access through GPUStack's Kubernetes API proxy. The `cluster_apiserver_proxy` handler did not perform a resource-level authorization check before forwarding requests t…

`kubernetes`

_also: [GHSA — pip](https://github.com/advisories/GHSA-62m9-f875-rqw6), [GHSA — pip](https://github.com/advisories/GHSA-gj9m-f8ph-pmhr), [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/09/cisa-adds-four-known-exploited-vulnerabilities-catalog)_

### 41. [Google Chromium: Google Chromium Use-After-Free Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-125350)
_CISA KEV · Nov 10 · score 0.258 · **CRITICAL 9.5** · ×2 reports · CVE-2026-125350_

Google Chromium contains a use-after-free vulnerability in the XML component that could allow a remote attacker to execute arbitrary code inside the sandbox via a specially crafted webpage. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Go…

`chrome` `chromium` `edge`

_also: [The Hacker News](https://thehackernews.com/2026/11/google-issues-chrome-security-update.html)_

### 42. [Mongoose: Prototype pollution via Schema.prototype.virtual()](https://github.com/advisories/GHSA-6972-9mcm-vhwj)
_GHSA — npm · Nov 10 · score 0.252 · **CRITICAL 9.8** · ×2 reports · CVE-2026-125118, CVE-2026-125120_

Affected: mongoose, mongoose, mongoose, mongoose. ### Summary Prototype pollution via Schema.prototype.virtual() — the 2022 fix for CVE-2022-2564 / CVE-2022-24304 protected Schema.path()/add() but never virtual(), so the same class of bug is still exploitable in all maintained release lines. ### Det…

`javascript` `cve-`

_also: [GHSA — npm](https://github.com/advisories/GHSA-pcrw-h46h-c93h)_

### 43. [bitcoinjs-lib: Undetected merkle node duplication in block root computation validates a forged transaction list](https://github.com/advisories/GHSA-8vv3-6qpc-gpw6)
_GHSA — npm · Nov 10 · score 0.163 · **CRITICAL** · CVE-2026-107846_

Affected: bitcoinjs-lib, bitcoinjs-lib, bitcoinjs-lib. ### Summary `fastMerkleRoot` pads an odd level by hashing the last node with itself. It does not report that it did so, and `checkTxRoots` never looks for repeated transactions. A peer can therefore duplicate transactions to fill the pad and pro…

`node`

### 44. [Forge: Ed25519 signature verification accepts small-order public keys](https://github.com/advisories/GHSA-6889-vf6x-f3g5)
_GHSA — npm · Nov 10 · score 1.143 · **HIGH 7.5** · ×9 reports · CVE-2026-118774, CVE-2026-118776, CVE-2026-119189_

Affected: node-forge. ### Summary `ed25519.verify()` does not reject public keys of small order, such as the identity point. Under such a key, a signature with `S = 0` and a small-order `R` verifies for many messages, or for every message with the identity key, without any private key. Fixed in node…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-w4xr-hqv8-ch44), [GHSA — npm](https://github.com/advisories/GHSA-6cv4-p8m7-4r25), [GHSA — npm](https://github.com/advisories/GHSA-j8rw-jp99-435v), [GHSA — npm](https://github.com/advisories/GHSA-9wg5-mj3p-v49q), [GHSA — npm](https://github.com/advisories/GHSA-2vgq-wchc-25w7)_

### 45. [Attackers Exploit AhsayCBS Flaws to Deploy Sandbox-Evading Python Backdoor](https://thehackernews.com/2026/11/attackers-exploit-ahsaycbs-flaws-to.html)
_The Hacker News · Nov 10 · score 0.345 · **HIGH 8.5** · CVE-2026-105133, CVE-2026-105134_

Cybersecurity researchers have disclosed details of an attack that exploited two now-patched vulnerabilities in AhsayCBS to deliver a Python-based implant. The activity, observed by Huntress in early October 2026, involves the exploitation of a chain comprising CVE-2026-105133 and CVE-2026-105134 to…

`python` `exploit` `backdoor` `cve-`

### 46. [Cocos AI Intra-handshake attested TLS implementation is vulnerable to TOCTOU Attacks](https://github.com/advisories/GHSA-ghwv-vrp2-2975)
_GHSA — go · Nov 10 · score 0.325 · **HIGH 6.3** · CVE-2026-119345_

Affected: github.com/ultravioletrs/cocos. ### Summary An attacker who can modify the attested workload’s code, memory-backed state, or configuration after the initial attestation — but without necessarily terminating the existing TLS connection — can cause the peer to continue trusting the connectio…

`github` `tls`

### 47. [Nuxt Content: Unauthenticated SQLite Function DoS via Content Query API](https://github.com/advisories/GHSA-xxrh-5hgg-gj4h)
_GHSA — npm · Nov 10 · score 0.236 · **HIGH 7.5** · CVE-2026-102650_

Affected: @nuxt/content. ### Summary The `POST /__nuxt_content/:collection/query` endpoint in `@nuxt/content` accepts an attacker-controlled `sql` field from the HTTP request body and executes it against a local SQLite database after passing it through an insufficient validator (`assertSafeQuery`). …

`sqlite`

### 48. [OHIF Viewers: DOM-Based Cross Site Scripting (XSS) through MIME type of document](https://github.com/advisories/GHSA-xwgp-w3pj-q5h3)
_GHSA — npm · Nov 10 · score 0.222 · **HIGH 8.8** · CVE-2026-118670_

Affected: @ohif/extension-dicom-pdf, @ohif/extension-dicom-pdf, @ohif/extension-dicom-pdf. ### Summary An XSS (Cross-Site Scripting) vulnerability occurs when an attacker is able to inject their own JavaScript code into a web page's source, which is subsequently processed by the victim's browser. A …

`javascript` `exploit` `xss`

### 49. [Pocket ID: Email verification token remains valid after address change, enabling arbitrary verified-email spoofing](https://github.com/advisories/GHSA-rm8c-2cv8-jwf6)
_GHSA — go · Nov 09 · score 0.384 · **CRITICAL 9.6** · ×2 reports · CVE-2026-115770, CVE-2026-62662_

Affected: github.com/pocket-id/pocket-id/backend. ## Summary An authenticated Pocket ID user can request an email-verification token while their account uses an address they control, change the account email address, and then redeem the previously issued token. The token is bound only to the user ID…

`github` `oidc` `token`

_also: [GHSA — go](https://github.com/advisories/GHSA-q4xm-p75h-h9p3)_

### 50. [Kubeflow Pipelines: Reflected XSS in the frontend pod information and events error responses](https://github.com/advisories/GHSA-g3qx-frcg-j979)
_GHSA — go · Nov 09 · score 0.246 · **CRITICAL 9.6** · ×6 reports · CVE-2026-77596, CVE-2026-88982, CVE-2026-88983_

Affected: github.com/kubeflow/pipelines. ## Summary The Kubeflow Pipelines frontend reflected untrusted pod names and namespaces into HTML error responses from the pod-information and pod-events routes. An attacker could craft a link that causes JavaScript to execute in the frontend's origin when a …

`javascript` `github` `k8s` `xss`

_also: [GHSA — go](https://github.com/advisories/GHSA-r4mx-2gr2-8277), [GHSA — go](https://github.com/advisories/GHSA-ghgh-57qv-h687), [GHSA — go](https://github.com/advisories/GHSA-f7vj-6669-qvv4), [GHSA — go](https://github.com/advisories/GHSA-2xwh-426q-42c5), [GHSA — go](https://github.com/advisories/GHSA-rjr3-43j3-4q8g)_

### 51. [fastapi-code-generator: Import-time RCE via route path -> unescaped @app.get('...') decorator](https://github.com/advisories/GHSA-p2mm-64f6-gmpp)
_GHSA — pip · Nov 09 · score 0.218 · **CRITICAL** · ×2 reports · CVE-2026-63469, CVE-2026-63471_

Affected: fastapi-code-generator. ### Summary fastapi-code-generator (koxudaxi) emits the OpenAPI path into the generated main.py route decorator as a single-quoted string literal (`@app.get('/u/<path>/x')`) without escaping the `'`. A `'` in the path closes the decorator string and, via concatenati…

`python` `rce`

_also: [GHSA — pip](https://github.com/advisories/GHSA-6xmv-cjr5-w3q8)_

### 52. [Malicious bee-js npm Release and Swarm Desktop Releases Deliver SleepyDuck Ethereum C2 Backdoor](https://socket.dev/blog/bee-js-compromise?utm_medium=feed)
_Socket Blog · Nov 09 · score 0.951 · **HIGH 8.5**_

Compromised maintainer accounts pushed malicious @ethersphere/bee-js 13.3.0 and Swarm Desktop 0.56.2, reusing SleepyDuck’s Ethereum-addressed C2 infrastructure.

`npm` `backdoor`

### 53. [Ethersphere Hijacked With Crypto Stealing Malware Via Github & npm](https://www.ox.security/blog/ethersphere-hijacked-with-crypto-stealing-malware-via-github-npm/)
_OX Security · Nov 09 · score 0.677 · **HIGH 8.5**_

Threat actors compromised Ethersphere&#8217;s npm and GitHub packages to steal crypto wallet keys and deploy cross-platform backdoors Overview OX Security researchers identified a coordinated supply chain compromise affecting the Ethersphere ecosystem, a decentralized storage and communication proto…

`npm` `github` `supply chain`

### 54. [Telepresence: Tunnel endpoint accepts caller-supplied session ID with no ownership proof — active client sessions hijackable](https://github.com/advisories/GHSA-6j3h-rp73-6rvf)
_GHSA — go · Nov 09 · score 0.656 · **HIGH 8.2** · CVE-2026-102339_

Affected: github.com/telepresenceio/telepresence/v2. ## Summary The Traffic Manager `Tunnel` gRPC streaming endpoint accepts a session ID from the first bytes of the client-controlled message payload. No verification confirms the caller owns the session. An attacker supplying a valid active session …

`go ` `github` `session` `credential`

### 55. [traQ: Privilege escalation by OAuth prompt=none request](https://github.com/advisories/GHSA-8cfq-jgf7-8m27)
_GHSA — go · Nov 09 · score 0.521 · **HIGH 7.3** · ×2 reports · CVE-2026-63197, CVE-2026-63198_

Affected: github.com/traPtitech/traQ. In OAuth2 silent authorization (`prompt=none`), when the `scope` parameter was empty or omitted, all scopes registered for the OAuth client became eligible for issuance. However, the prior consent check was performed against the empty requested scope set. As a r…

`github` `oauth` `token` `privilege escalation`

_also: [GHSA — go](https://github.com/advisories/GHSA-p74g-f95m-7fx7)_

### 56. [DDEV incomplete tar symlink traversal fix allows host file overwrite - Incomplete fix of CVE-2026-32885](https://github.com/advisories/GHSA-9hq4-hm3j-jmph)
_GHSA — go · Nov 09 · score 0.374 · **HIGH 8.8** · CVE-2026-108262_

Affected: github.com/ddev/ddev. ## Summary The CVE-2026-32885 ZipSlip fix added a symlink-target escape check to Untar, but the check rebases an ABSOLUTE symlink target into dest before validating (filepath.Join(dest, "/etc") stays lexically inside dest and passes), while the symlink is then created…

`github` `rce` `cve-`

### 57. [Telepresence: Traffic Manager gRPC has no auth — any pod claims arbitrary namespace and intercepts services, receiving victim environment secrets](https://github.com/advisories/GHSA-j8j4-rw65-56r6)
_GHSA — go · Nov 09 · score 0.335 · **HIGH 8.5** · CVE-2026-102340_

Affected: github.com/telepresenceio/telepresence. ## Summary Telepresence's Traffic Manager gRPC API (port 8081) requires no authentication. Any pod with cluster-network access to the Traffic Manager can register as a client in an arbitrary managed namespace and create intercepts against services in…

`github` `kubernetes` `container`

### 58. [zizmor: Debug logging prints available GitHub credentials in cleartext](https://github.com/advisories/GHSA-f42p-wjw5-97qh)
_GHSA — pip · Nov 09 · score 0.173 · **HIGH** · CVE-2026-102289_

Affected: zizmor. ### Summary zizmor 1.27.0 exposes GitHub access tokens in cleartext when debug-level logging is enabled. Tokens supplied via environment variables (`GH_TOKEN`, `GITHUB_TOKEN`, `ZIZMOR_GITHUB_TOKEN`), or the corresponding command-line options (`--gh-token`, `--github-token`, `--zizm…

`github` `token`

### 59. [Claude Code: TOCTOU Race in Edit Tool Allows File Writes Outside the Workspace](https://github.com/advisories/GHSA-5xjx-9qx6-jcrv)
_GHSA — npm · Nov 09 · score 0.158 · **HIGH** · CVE-2026-88968_

Affected: @anthropic-ai/claude-code. Claude Code validated Edit tool targets using point-in-time pathname and symlink resolution that was not bound to the underlying directory inodes or file descriptors. On macOS, a process running inside Claude Code's Bash sandbox could exploit the resulting time-o…

`macos` `exploit`

### 60. [esm.sh: web.NewHandler allows arbitrary file read via encoded dot-segment path traversal](https://github.com/advisories/GHSA-g3c2-rjq2-c763)
_GHSA — go · Nov 09 · score 0.113 · **HIGH 7.5** · CVE-2026-102657_

Affected: github.com/esm-dev/esm.sh/web. ### Summary The documented `web.NewHandler` static file server can read files outside `Config.AppDir` when the request path contains URL-encoded dot-segments such as `%2e%2e`. Go's `ServeMux` redirects plain `/../` paths, but it passes encoded dot-segments to…

`go ` `github`

### 61. [Code Graph RAG: MCP paginated read_file path traversal / arbitrary file read](https://github.com/advisories/GHSA-vvr2-h2jp-838m)
_GHSA — pip · Nov 09 · score 0.079 · **HIGH 7.5** · CVE-2026-77604_

Affected: code-graph-rag. ### Summary The `read_file` MCP tool in `codebase_rag/mcp/tools.py` contains a path traversal vulnerability in its paginated branch (when `offset` or `limit` is supplied). The handler constructs a file path using `Path(self.project_root) / file_path` without subsequently va…

`python`

### 62. [File Browser: Trailing-slash directory deletion leaves public shares active for recreated paths](https://github.com/advisories/GHSA-pp88-jhwj-5qh5)
_GHSA — go · Nov 13 · score 0.832 · **LOW 3.1** · CVE-2026-62683_

Affected: github.com/filebrowser/filebrowser/v2. ## Summary File Browser v2.63.15 can leave a public directory share behind when the shared directory is deleted through a path with a trailing slash. The share cleanup path calls `DeleteWithPathPrefix(file.Path, userID)`, but the Bolt backend performs…

`github`

### 63. [OpenTelemetry-Go: Eager W3C baggage-property materialization causes bounded memory-allocation amplification](https://github.com/advisories/GHSA-rrfc-gjm9-cgrj)
_GHSA — go · Nov 13 · score 0.586 · **MEDIUM 5.3** · CVE-2026-128086_

Affected: go.opentelemetry.io/otel/baggage, go.opentelemetry.io/otel/propagation. ## Summary OpenTelemetry Go eagerly materializes W3C baggage metadata into property objects during parsing. Slice growth, serialization, and copying into the internal representation cause **bounded but disproportionate…

`go ` `opentelemetry`

### 64. [OpenTelemetry JavaScript: Insertion of Sensitive Information into Log File and Exposure of Sensitive Information to an Unauthorized Actor in @opentelemetry/instrumentation-http](https://github.com/advisories/GHSA-3v2p-hm54-8qcq)
_GHSA — npm · Nov 13 · score 0.558 · **MEDIUM 5.8** · CVE-2026-128080_

Affected: @opentelemetry/instrumentation-http. ### Summary `@opentelemetry/instrumentation-http` redacts sensitive URL query parameters on **outgoing (client) spans** but not on **incoming (server) spans**. The server-span path writes the raw query string verbatim into the `url.query` attribute, so …

`javascript` `aws` `azure` `opentelemetry`

### 65. [ARTEX: Attackers Adopted This AI Pentesting Tool in Three Months. Leaked Secrets Are Its Fastest Way In.](https://www.stepsecurity.io/blog/artex-ai-pentesting-tool-attackers-leaked-secrets)
_StepSecurity · Nov 13 · score 0.490_

ARTEX is an open-source tool where AI agents run a penetration test on their own. Since August 2026, state-aligned groups, criminal crews and one runaway research agent have pointed ARTEX at hundreds of organizations. In one case, an agent went from a GitHub search for leaked secrets to stolen cloud…

`github`

### 66. [Astro: Image endpoint in @astrojs/node can read files from a case-variant sibling of the output directory on case-sensitive filesystems](https://github.com/advisories/GHSA-r3h5-4585-7x3w)
_GHSA — npm · Nov 13 · score 0.483 · **MEDIUM** · CVE-2026-126364_

Affected: @astrojs/node, astro. ## Summary The `/_image` endpoint used by the `@astrojs/node` adapter checks that a requested local image is inside the build output directory before reading it from disk. That check compared paths case-insensitively. On case-sensitive filesystems (such as Linux), a d…

`node` `linux`

### 67. [Check Point gateways hacked via PHP2Shell to deploy VMware ESXi wiper](https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/)
_BleepingComputer · Nov 13 · score 0.476_

Vulnerable Check Point Security Gateway instances have been targeted in PHP2Shell attacks that deployed data-wiping malware on VMware ESXi hosts. [...]

`vmware` `esxi`

### 68. [The Green Agent POV: Formulating the Fix for an Exposed Container with Sensitive Data Access](https://www.wiz.io/blog/inside-green-agent-investigation)
_Wiz Research · Nov 13 · score 0.401_

See how the Green Agent balanced security urgency with business continuity to turn a toxic combination into an executable remediation plan and ready-to-merge pull requests.

`container`

### 69. [russh kex_done: Shared-secret callback runs before server host-key verification](https://github.com/advisories/GHSA-9264-jvgf-6w2f)
_GHSA — rust · Nov 13 · score 0.381 · **LOW 3.7** · ×2 reports · CVE-2026-128087, CVE-2026-128088_

Affected: russh. ### Summary A malicious SSH server whose host key is rejected can still cause russh's `client::Handler::kex_done()` callback to execute with the raw key-exchange shared secret. Applications using the callback for its documented protocol-bridging purpose may derive keys, initialize a…

`ssh`

_also: [GHSA — rust](https://github.com/advisories/GHSA-736f-c93q-9fwx)_

### 70. [OpenTelemetry Python API: Denial of service through quadratic-time traceparent parsing](https://github.com/advisories/GHSA-mf5v-w3w3-f6cg)
_GHSA — pip · Nov 13 · score 0.323 · **MEDIUM 5.3** · CVE-2026-126360_

Affected: opentelemetry-api. ## Summary `TraceContextTextMapPropagator.extract()` in `opentelemetry-api` is vulnerable to regular expression denial of service (ReDoS) when processing a specially crafted `traceparent` value. A malformed value containing a trace-context prefix followed by a long white…

`python` `opentelemetry`

### 71. [The Take-Home Test That Runs on Your Work Laptop: Inside the AccuraSoftHire Fake Interview Campaign](https://www.stepsecurity.io/blog/accurasofthire-fake-interview-developer-machines)
_StepSecurity · Nov 13 · score 0.310_

Binance says its $6.34 billion theft began when an engineer ran a fake interview assignment on his work computer. JFrog has now exposed a fake company, AccuraSoftHire, built to run the same trick. We decoded the attacker's server history from a public Ethereum wallet and found npm packages from the …

`npm`

### 72. [Nuxt: Incomplete fix for GHSA-9v7c-q64q-vv33: a leading `//` in the request path bypasses `server/middleware` path checks and server route rules on page routes](https://github.com/advisories/GHSA-r99w-jh2x-3mg9)
_GHSA — npm · Nov 13 · score 0.304 · **MEDIUM 6.5** · CVE-2026-128077_

Affected: @nuxt/nitro-server. ### Summary Since `4.6.0`, Nuxt parses a request path that starts with `//` as a URL with a host before rendering a page, so `//x/admin` renders the page at `/admin`. Nitro's routing, Nitro's route rules and `server/middleware` see the path as `//x/admin`, so server-sid…

`github`

### 73. [Soup Sieve: Uncontrolled recursion in CSS parser lets nested pseudo-class selectors exhaust the Python call stack](https://github.com/advisories/GHSA-7g44-g9rc-x53w)
_GHSA — pip · Nov 13 · score 0.290 · **MEDIUM 5.3** · CVE-2026-126193_

Affected: soupsieve. ## Summary The Soup Sieve CSS selector parser recurses once per level of nested pseudo-class selector (`:is()`, `:not()`, `:where()`, `:has()`) without any limit on nesting depth. An unauthenticated attacker who can supply a CSS selector string to `soupsieve.compile()`, `soupsie…

`python`

### 74. [RUSTSEC-2026-0524: Vulnerability in quinn-proto](https://rustsec.org/advisories/RUSTSEC-2026-0524.html)
_RustSec · Nov 13 · score 0.281_

Long Retry token can panic or exhaust memory in a QUIC client

`token`

### 75. [opentelemetry-go: AttributeValueLengthLimit is fully bypassed by attribute values composed of valid U+FFFD runes](https://github.com/advisories/GHSA-q7gw-24fr-5p69)
_GHSA — go · Nov 13 · score 0.246 · **MEDIUM 5.3** · CVE-2026-128085_

Affected: go.opentelemetry.io/otel/sdk, go.opentelemetry.io/otel/sdk/log, go.opentelemetry.io/otel/trace. ## Summary The `AttributeValueLengthLimit` span/log-record limit can be bypassed entirely with attribute values that consist of valid U+FFFD (REPLACEMENT CHARACTER) runes. The counting-based tru…

`opentelemetry`

### 76. [Microsoft confirms Windows activation failures after November updates](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-activation-failures-after-november-updates/)
_BleepingComputer · Nov 13 · score 0.244_

Microsoft has confirmed that this month's Patch Tuesday security updates are causing Windows activation and licensing failures with 0x80041008 error codes. [...]

`windows`

### 77. [SvelteKit: `@sveltejs/adapter-node` crashes when proxying certain requests via `fetch`](https://github.com/advisories/GHSA-rqw3-x7hx-mm3p)
_GHSA — npm · Nov 13 · score 0.218 · **MEDIUM 5.9** · CVE-2026-128123_

Affected: @sveltejs/adapter-node, @sveltejs/adapter-node. In affected versions, `@sveltejs/adapter-node` can attempt to add a header to an immutable request in a context that causes the server to crash, denying service to any other requests routed to that server.

`node`

### 78. [Tornado: Open redirect via triple-slash redirect paths](https://github.com/advisories/GHSA-5cjw-f85j-cv6r)
_GHSA — pip · Nov 13 · score 0.161 · **LOW 3.1** · CVE-2026-126347_

Affected: tornado. ### Summary Due to differences in the way browsers and Python's `urllib` parse urls, browsers treat a string starting with three or more slashes as a protocol-level redirect, while `urllib` does not. This means that the 6.6.0 fix for the RedirectHandler open redirect (CVE-2026-116…

`python` `cve-`

### 79. [RUSTSEC-2026-0529: Vulnerability in bsv-rs](https://rustsec.org/advisories/RUSTSEC-2026-0529.html)
_RustSec · Nov 13 · score 0.159_

KVStoreInterpreter::verify_signature_legacy answers true for every token and every key

`token`

### 80. [Operation Endgame Takes Down Gootloader, CastleRAT and StealC Servers, Seizes 6.4M Stolen Logins](https://thehackernews.com/2026/11/operation-endgame-takes-down-gootloader.html)
_The Hacker News · Nov 13 · score 0.155_

An international police operation took down servers behind Gootloader, CastleRAT and StealC this week. Criminals used the three malware tools to gain access to computers, steal passwords, and launch ransomware attacks. Police also seized about 6.4 million stolen logins belonging to more than 40,000 …

`ransomware`
