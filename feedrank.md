# feedrank — 2026-10-17

_80 items, 5d window._

### 1. [Drupal patches critical RCE flaws, warns exploits may emerge soon](https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaws-warns-exploits-may-emerge-soon/)
_BleepingComputer · Oct 17 · score 0.203 · **CRITICAL 9.5**_

Drupal has patched two critical vulnerabilities that could allow attackers to execute code remotely on websites running any supported version of the content management system. [...]

`rce`

### 2. [MALFEX npm Package 'imgdecode' Hides Shellcode Loader in Windows Native Addon](https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html)
_The Hacker News · Oct 17 · score 1.229 · **HIGH 8.5**_

Cybersecurity researchers have discovered a malicious npm package that's part of a recently disclosed software supply chain attack campaign dubbed MALFEX. The package, named "imgdecode," was uploaded to the package registry on September 30, 2026, by a user named "malfexteste8." It has been downloade…

`npm` `supply chain` `windows`

### 3. [Hackers breach Microsoft 365 tenants via ConnectWise supply-chain attack](https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/)
_BleepingComputer · Oct 17 · score 0.419 · **HIGH 8.5**_

ConnectWise has shut down customer access to its Cloud Backup service (formerly SkyKick Cloud Backup) after hackers accessed application identities and compromised Microsoft 365 tenants. [...]

`breach`

### 4. [BeyondTrust Remote Support: BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-102764)
_CISA KEV · Oct 16 · score 1.672 · **CRITICAL 9.0** · ×2 reports · CVE-2026-102764_

BeyondTrust Remote Support contains an authentication bypass by spoofing vulnerability that could allow a remote attacker to perform file operations on the appliance. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Sec…

`authentication bypass`

_also: [The Hacker News](https://thehackernews.com/2026/10/china-linked-hackers-exploited.html)_

### 5. [Fortinet Multiple Products: Fortinet Multiple Products Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-61624)
_CISA KEV · Oct 16 · score 1.236 · **CRITICAL 9.0** · ×2 reports · CVE-2025-61624_

FortiOS, FortiPAM, FortiProxy, and FortiSwitchManager contain a path traversal vulnerability that may allow an authenticated attacker with admin profile and at least read-write permissions to write or delete arbitrary files via specific CLI commands. Required action: Apply mitigations in accordance …

`fortinet`

_also: [The Hacker News](https://thehackernews.com/2026/10/attackers-exploit-fortios-flaw-to.html)_

### 6. [BeyondTrust patches zero-day exploited in attacks since August](https://www.bleepingcomputer.com/news/security/beyondtrust-patches-zero-day-exploited-in-attacks-since-august/)
_BleepingComputer · Oct 16 · score 1.170 · **CRITICAL 9.5**_

BeyondTrust warned customers on Thursday to patch a critical flaw in its Remote Support (RS) that has been exploited in zero-day attacks since late August. [...]

`zero-day`

### 7. [LMCache: Remote code execution via unsafe deserialization in multiprocess mode transport](https://github.com/advisories/GHSA-w5f2-9q9c-ff4h)
_GHSA — pip · Oct 16 · score 0.904 · **CRITICAL 9.8** · CVE-2026-105192_

Affected: lmcache. ### Summary LMCache is vulnerable to Unauthenticated Remote Code Execution via Pickle Deserialization on the Multiprocess ZMQ Transport ### Details LMCache multiprocess mode, also called distributed mode, opens an unauthenticated ZeroMQ ROUTER so worker processes can register and …

`deserialization`

### 8. [Claude Agent SDK: Argument Injection via resume Option Allows Arbitrary Command Execution](https://github.com/advisories/GHSA-h4mw-j7qp-8mwm)
_GHSA — pip · Oct 16 · score 0.507 · **CRITICAL** · CVE-2026-96620_

Affected: claude-agent-sdk. The Claude Agent SDK for Python passed the `resume` option to the Claude CLI without validation, allowing a value beginning with `-` to be interpreted as a separate CLI flag. An attacker who controlled the `resume` value could inject an `--mcp-config` flag defining a stdi…

`python` `session`

### 9. [Critical BlockStrap flaw lets hackers run code on Magento servers](https://www.bleepingcomputer.com/news/security/critical-blockstrap-flaw-lets-hackers-run-code-on-magento-servers/)
_BleepingComputer · Oct 16 · score 0.245 · **CRITICAL 9.5** · CVE-2026-103849_

Researchers warn that hackers could soon exploit a maximum-severity vulnerability (CVE-2026-103849) affecting Magento and Adobe Commerce, potentially allowing them to execute arbitrary PHP code on store servers. [...]

`php` `exploit` `cve-`

### 10. [Arcane: Delegated users:update permission allows admin account takeover via password reset (no privilege-hierarchy check)](https://github.com/advisories/GHSA-pw5q-rjx4-7f7p)
_GHSA — go · Oct 16 · score 1.048 · **HIGH 8.8** · ×2 reports · CVE-2026-96627, CVE-2026-96628_

Affected: github.com/getarcaneapp/arcane/backend/v2. ## Summary A user holding the delegated `users:update` permission can reset the global administrator's password and take over the admin account. `UpdateUser` sets the target user's `PasswordHash` from the request body for ANY target with no compar…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-mp22-58ff-6fhr)_

### 11. [GitHub Action tj-actions/changed-files supply chain attack: what you need to know | Endor Labs](https://www.endorlabs.com/learn/github-action-tj-actions-changed-files-supply-chain-attack-what-you-need-to-know)
_Endor Labs · Oct 16 · score 0.942 · **HIGH 8.5**_

GitHub Action tj-actions/changed-files was compromised, exposing CI/CD secrets. Learn how this attack impacts repositories and what steps to take now.

`github` `ci/cd` `supply chain` `tj-actions`

### 12. [What We Can Learn About GitHub Actions Security from the Trivy Breach | Endor Labs](https://www.endorlabs.com/learn/github-actions-security-lessons-from-trivy)
_Endor Labs · Oct 16 · score 0.925 · **HIGH 8.5**_

The recent supply chain attack on one of the most trusted open-source security scanners started with a single workflow misconfiguration in GitHub Actions. Here’s what happened, why it matters, and what you can do about it.

`github` `github actions` `supply chain` `breach`

### 13. [kin-openapi openapi3filter: nil-pointer panic in ValidateResponse on a response header declared with content](https://github.com/advisories/GHSA-74vm-87hj-r66f)
_GHSA — go · Oct 16 · score 0.796 · **HIGH 7.5** · ×9 reports · CVE-2026-100347, CVE-2026-100348, CVE-2026-100349_

Affected: github.com/getkin/kin-openapi. ## Summary `ValidateResponse` panics on a nil pointer when a spec declares a response header with `content` instead of `schema`. `doc.Validate()` accepts that document, so the crash comes from a spec the library just called valid. Same class as GHSA-jpcw-4wr7…

`go ` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-vrcc-3ch7-hppw), [GHSA — go](https://github.com/advisories/GHSA-g8cf-rcjf-c8cf), [GHSA — go](https://github.com/advisories/GHSA-rj39-cv6w-8wv7), [GHSA — go](https://github.com/advisories/GHSA-23vg-4cjm-66q5), [GHSA — go](https://github.com/advisories/GHSA-h4r5-mxv5-8mjc)_

### 14. [Attackers Tampered with AOMEI Backupper's Update Servers for Minutes to Deliver a Backdoor](https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html)
_The Hacker News · Oct 16 · score 0.235 · **HIGH 8.5**_

Attackers repeatedly changed the files that AOMEI Backupper fetches from the vendor's own update servers, in windows of five to ten minutes at a time between May and July 2026, so that any copy of the Windows backup program that checked for an update during one of those windows would download and ru…

`windows` `backdoor`

### 15. [gomarkdown/markdown IsSafeURL panics on short URLs](https://github.com/advisories/GHSA-cv23-7vc5-jfh7)
_GHSA — go · Oct 16 · score 0.225 · **HIGH 7.5** · CVE-2026-102941_

Affected: github.com/gomarkdown/markdown. ## Summary IsSafeURL slices url[:nPath] before checking that len(url) >= nPath, so a URL shorter than a path prefix (0, 1 or 2 bytes) triggers a slice-bounds panic, and this is reached end to end when the html.Safelink hardening flag is enabled and the input…

`go ` `github`

### 16. [Palo Alto Networks PAN-OS: Palo Alto Networks PAN-OS Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-0322)
_CISA KEV · Oct 15 · score 1.909 · **CRITICAL 9.0** · ×2 reports · CVE-2026-0322_

Palo Alto Networks PAN-OS contains a code injection vulnerability that could allow an authenticated attacker with network access to execute arbitrary code with root privileges on the firewall. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s …

`palo alto` `firewall`

_also: [The Hacker News](https://thehackernews.com/2026/10/palo-alto-networks-patches-pan-os.html)_

### 17. [KEDA: Privilege escalation from namespace admin to cluster admin via KEDA TriggerAuthentication](https://github.com/advisories/GHSA-637c-6jxx-4rwm)
_GHSA — go · Oct 15 · score 1.092 · **CRITICAL 9.9** · CVE-2026-77524_

Affected: github.com/kedacore/keda, github.com/kedacore/keda/v2. ## Summary A namespace admin who creates a `TriggerAuthentication` and a `ScaledObject` in their own namespace can make the KEDA operator send its own ServiceAccount token to a tenant-controlled URL. That token holds `["*"]/["*"] get` …

`github` `token` `privilege escalation`

### 18. [Critical PwnEscape Linux Kernel Vulnerability Lets Guest VMs Read Host Memory](https://thehackernews.com/2026/10/critical-pwnescape-linux-kernel.html)
_The Hacker News · Oct 15 · score 0.783 · **CRITICAL 9.5** · CVE-2026-99999_

A newly disclosed critical flaw in the Linux kernel allows code inside a virtual machine to read memory on the host computer it runs on. A researcher demonstrated the leak against Vercel's live cloud sandboxes, and Vercel confirmed it. The flaw, now tracked as CVE-2026-99999 and nicknamed PwnEscape,…

`linux` `kernel` `cve-`

### 19. [ThreatsDay: Adobe RCE, DNS Wallet Theft, NVIDIA Container Escape, Self-Healing Backdoor + 23 More](https://thehackernews.com/2026/10/threatsday-adobe-rce-dns-wallet-theft.html)
_The Hacker News · Oct 15 · score 0.717 · **CRITICAL 9.0**_

Someone built a tool to steal data, then decided it should scare the victim for fun. Yes, that’s an actual feature. And somehow, it fits right in with this week's security stories. The rest gets interesting in different ways. A small permission can lead to a big theft. A trusted login can hide the w…

`container` `dns` `rce` `backdoor`

### 20. [Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing](https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html)
_The Hacker News · Oct 15 · score 0.528 · **CRITICAL 9.5**_

Next.js released an&nbsp;out-of-band security update&nbsp;on October 14 that fixes two critical flaws allowing unauthenticated remote code execution, along with a high-severity denial-of-service flaw. One code-execution flaw is in React Server Components, and the other in librsvg, the open-source li…

`rce`

### 21. [TanStack Router: Unauthenticated reflected XSS in TanStack Start server-function responses](https://github.com/advisories/GHSA-qx66-fv34-fjm8)
_GHSA — npm · Oct 15 · score 0.507 · **CRITICAL 9.3** · CVE-2026-102989_

Affected: @tanstack/start-server-core, @tanstack/react-start, @tanstack/solid-start, @tanstack/vue-start. ## Impact An unauthenticated attacker can craft a URL to a server function in an affected TanStack Start app. If someone opens the link, the app can return attacker-controlled HTML from its own …

`javascript` `ca` `xss`

### 22. [Atlassian Multiple Products: Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-21589)
_CISA KEV · Oct 15 · score 0.457 · **CRITICAL 9.0** · CVE-2026-21589_

Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an un…

`atlassian` `jira` `confluence`

### 23. [Argo CD: AppProject destination-namespace and resource restrictions bypassed by PreDelete/PostDelete resource hooks](https://github.com/advisories/GHSA-fmxq-cgp8-87wp)
_GHSA — go · Oct 15 · score 0.422 · **CRITICAL 9.9** · CVE-2026-77459_

Affected: github.com/argoproj/argo-cd/v2, github.com/argoproj/argo-cd/v3, github.com/argoproj/argo-cd/v3, github.com/argoproj/argo-cd/v3, github.com/argoproj/argo-cd/v3. ### Impact Argo CD checks an Application's AppProject before it creates resources during a sync. That check covers destination nam…

`github`

### 24. [Dgraph: Zero Unauthenticated HTTP Admin removeNode Denial of Service](https://github.com/advisories/GHSA-qj98-gp63-54xj)
_GHSA — go · Oct 15 · score 0.376 · **CRITICAL** · CVE-2026-102748_

Affected: github.com/dgraph-io/dgraph/v25. ### Summary Dgraph `v25.3.8` exposes a Zero HTTP administrative surface that is unauthenticated when port `6080` is reachable. The exposed routes include: - `/state` - `/assign` - `/removeNode` - `/moveTablet` An unauthenticated request to `/removeNode?id=1…

`node` `github`

### 25. [NGINX Fixes 5 Flaws, Including Possible RCE and a TLS Bug That May Skip Client-Cert Checks](https://thehackernews.com/2026/10/nginx-fixes-5-flaws-including-possible.html)
_The Hacker News · Oct 15 · score 0.347 · **CRITICAL 9.0**_

NGINX released&nbsp;versions 1.30.6 and 1.31.7&nbsp;on October 14 to fix five vulnerabilities, one of them present in every release since May 2005. There are three memory bugs that F5, the company behind NGINX, says could crash a worker process or possibly let an attacker run code, and each requires…

`session` `tls` `f5` `rce` `exploit`

### 26. [Ahsay AhsayCBS: Ahsay AhsayCBS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-105134)
_CISA KEV · Oct 15 · score 0.341 · **CRITICAL 9.0** · ×3 reports · CVE-2026-105133, CVE-2026-105134_

Ahsay AhsayCBS contains a command injection vulnerability that could allow a remote attacker to execute operating system commands via manipulation of the random parameter in the Replication Receiver component’s /rps/api/json/UpdateReceivers.do endpoint. This vulnerability can be chained with CVE-202…

`cve-`

_also: [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-105133), [The Hacker News](https://thehackernews.com/2026/10/ahsaycbs-flaws-exploited-to-deploy-web.html)_

### 27. [Podman: The `podman run` command can be instructed to disable almost all sandboxing by image annotation](https://github.com/advisories/GHSA-2cvf-wqm6-wr9g)
_GHSA — go · Oct 15 · score 0.286 · **CRITICAL 10.0** · CVE-2026-94603_

Affected: github.com/containers/podman, go.podman.io/podman/v6. ### Impact Podman v4.4.0 added a feature where container checkpoints (from the `podman container checkpoint` command) could be distributed via OCI registry, and pulled from that registry and run via the `podman run` command. This allowe…

`github` `container` `podman` `checkpoint`

### 28. [Hackers exploit Collabora RCE flaw to backdoor Nextcloud servers](https://www.bleepingcomputer.com/news/security/hackers-exploit-collabora-rce-flaw-to-backdoor-nextcloud-servers/)
_BleepingComputer · Oct 15 · score 0.228 · **CRITICAL 9.5** · CVE-2026-110447_

Threat actors are exploiting a critical command execution flaw, now tracked as CVE-2026-110447, in the Collabora Online - Built-in CODE Server app (richdocumentscode) for Nextcloud. [...]

`rce` `exploit` `backdoor` `cve-`

### 29. [Vitess vttablet /twopcz reflected XSS](https://github.com/advisories/GHSA-v75v-6fpf-gvw8)
_GHSA — go · Oct 15 · score 0.216 · **CRITICAL 9.8** · CVE-2026-104252_

Affected: vitess.io/vitess, vitess.io/vitess. From: xylove21 To: security@vitess.io Subject: [Security Report] Vitess vttablet /twopcz reflected XSS Date: Tue, 24 Jun 2026 14:30:00 +0800 ## Summary The `twopczHandler` in `go/vt/vttablet/tabletserver/twopcz.go` (line 185) reflects the `Action` and `d…

`mysql` `xss`

### 30. [Langflow's Critical Authenticated RCE Flaw Targeted in 1,423 Honeypot Exploit Attempts](https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html)
_The Hacker News · Oct 15 · score 0.201 · **CRITICAL 9.5** · CVE-2026-105740_

Threat actors are exploiting a critical security flaw in Langflow, according to an alert from Previdian. Langflow is an open-source platform that allows developers to build artificial intelligence (AI) applications and agentic workflows. In February 2025, DataStax, the parent company of Langflow, wa…

`rce` `exploit` `cve-` `cvss`

### 31. [Drupal Patches Critical Field UI Flaw With Unauthenticated RCE Path via Contributed Modules](https://thehackernews.com/2026/10/drupal-patches-critical-core-rce-flaw.html)
_The Hacker News · Oct 15 · score 0.176 · **CRITICAL 9.5**_

Drupal core has a critical flaw in its Field UI module that could let an attacker run code on the site's server, and fixes were shipped on October 14 in Drupal 11.4.10, 11.3.19, and 10.6.19. An attacker cannot reach the flaw through core alone, the Drupal Security Team said in&nbsp;its advisory. Sev…

`rce` `exploit`

### 32. [containerd: Unpack DoS via repeated opaque whiteouts](https://github.com/advisories/GHSA-rp3h-jf77-q9p4)
_GHSA — go · Oct 15 · score 0.951 · **HIGH 7.8** · ×2 reports · CVE-2026-95837, CVE-2026-95838_

Affected: github.com/containerd/containerd/v2, github.com/containerd/containerd, github.com/containerd/containerd/v2, github.com/containerd/containerd/v2. ### Impact A vulnerability exists in containerd's layer unpack handler where the processing of certain image layers causes superlinear time compl…

`github` `kubernetes` `container` `containerd`

_also: [GHSA — go](https://github.com/advisories/GHSA-p7v4-vr35-mj6f)_

### 33. [OpenNext Cloudflare: Cache interception can bypass middleware protection for encoded paths](https://github.com/advisories/GHSA-2vc4-c4r6-p6v6)
_GHSA — npm · Oct 15 · score 0.424 · **HIGH 7.5** · CVE-2026-100409_

Affected: @opennextjs/cloudflare. ## Summary When cache interception is enabled, `@opennextjs/cloudflare` can interpret percent-encoded paths differently during middleware matching and cache lookup. An encoded request may fail to match authorization middleware, then be decoded into the cache key of …

`cloudflare`

### 34. [Nginx UI: OTP secure-session step-up can be bypassed via MCP configuration tools](https://github.com/advisories/GHSA-vc32-4gwf-77xp)
_GHSA — go · Oct 15 · score 0.403 · **HIGH 8.8** · ×9 reports · CVE-2026-84314, CVE-2026-84315, CVE-2026-84316_

Affected: github.com/0xJacky/Nginx-UI. ### Summary An OTP-enabled authenticated user who cannot use the HTTP configuration mutation endpoints without a valid secure session can still mutate Nginx configuration through `/mcp` and `/mcp_message` using only ordinary authentication. ### Details The HTTP…

`github` `session`

_also: [GHSA — go](https://github.com/advisories/GHSA-wq4w-vwvq-q3x9), [GHSA — go](https://github.com/advisories/GHSA-cf23-7qxj-xmhr), [GHSA — go](https://github.com/advisories/GHSA-5v7c-xpfp-p65m), [GHSA — go](https://github.com/advisories/GHSA-2gc7-j998-5xx6), [GHSA — go](https://github.com/advisories/GHSA-9jww-cxg5-rj9m)_

### 35. [Sliver: Unauthenticated Memory Exhaustion Denial of Service in Sliver HTTP(S) Listener PNG Decoder](https://github.com/advisories/GHSA-663m-7x7m-g4fw)
_GHSA — go · Oct 15 · score 0.291 · **HIGH** · CVE-2026-77622_

Affected: github.com/BishopFox/sliver. ### Summary Sliver is vulnerable to a Denial of Service (DOS) attack because there is no cap in the size of a PNG file that can be sent to an open http listener and there is a small amount of possible nonces. This vulnerability lets the attacker completely max …

`go ` `github`

### 36. [FrankenPHP: Cross-request PHP session ID leak in worker mode when the session extension is a shared module](https://github.com/advisories/GHSA-v3ph-cgqh-r8p5)
_GHSA — go · Oct 15 · score 0.286 · **HIGH 7.7** · CVE-2026-82416_

Affected: github.com/dunglas/frankenphp. ## Summary In worker mode under concurrency, FrankenPHP can hand a PHP session id from one request to another when PHP's `session` extension is loaded as a shared module instead of being statically linked into the FrankenPHP binary. A request presenting `Cook…

`php` `github` `session` `cve-`

### 37. [Nginx UI: Casdoor SSO callback uses a constant `state` parameter (login CSRF)](https://github.com/advisories/GHSA-44xr-mrhh-qm78)
_GHSA — go · Oct 15 · score 0.267 · **HIGH 8.8** · ×2 reports · CVE-2026-84312, CVE-2026-84313_

Affected: Nginx-UI. ## Summary In the Casdoor SSO flow, the OAuth `state` parameter is hard-coded to `settings.CasdoorSettings.Application` — a value identical for every user and every login. The callback handler accepts whatever `state` the client sends without comparing it to anything stored in th…

`go ` `oauth` `csrf`

_also: [GHSA — go](https://github.com/advisories/GHSA-gfrc-g87h-7h5w)_

### 38. [mise permits untrusted local configuration to override default shell arguments](https://github.com/advisories/GHSA-g74g-rg72-j2p3)
_GHSA — rust · Oct 15 · score 0.258 · **HIGH 7.8** · CVE-2026-103929_

Affected: mise. ## Summary Untrusted local .mise.toml [settings] can set the shell interpreter args (unix/windows default_inline / default_file shell_args), yielding arbitrary command execution, because those command-interpreter settings were not added to the global_only denylist the CVE-2026-55448 …

`windows` `cve-`

### 39. [react/http: Unbounded HTTP Client Response Header Buffering Leads to Memory Exhaustion DoS](https://github.com/advisories/GHSA-g4f2-2pf3-2pwj)
_GHSA — composer · Oct 15 · score 0.239 · **HIGH 7.5** · CVE-2026-104827_

Affected: react/http. ### Summary `React\Http\Browser` and its lower-level HTTP stack impose no limit on the size of a response's header section while it is being received. `ClientRequestStream::handleData()` appends every incoming byte to an internal buffer and only scans that buffer for the `\r\n\…

`php`

### 40. [Qwik: Crashing any Qwik Server via Resource thenable](https://github.com/advisories/GHSA-x586-xvc8-g7q6)
_GHSA — npm · Oct 15 · score 0.122 · **HIGH** · CVE-2026-84994_

Affected: @builder.io/qwik, @qwik.dev/core. ### Summary A Qwik server in the default configuration can be crashed with one unauthenticated HTTP request. During qwik-json body parsing, `ResourceSerializer.$fill$` does `Promise.resolve(resource._resolved)`. If `_resolved` is a plain object whose `.the…

`node`

### 41. [Ivanti Connect Secure: Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-104935)
_CISA KEV · Oct 14 · score 1.561 · **CRITICAL 9.5** · ×2 reports · CVE-2026-104935_

Ivanti Connect Secure contains an authentication bypass by spoofing vulnerability that allows a remote unauthenticated attacker to execute arbitrary commands. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Up…

`ivanti` `authentication bypass`

_also: [The Hacker News](https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html)_

### 42. [Cisco Warns of Active Attacks Exploiting New Critical Secure Email Gateway Vulnerability](https://thehackernews.com/2026/10/cisco-warns-of-active-attacks.html)
_The Hacker News · Oct 14 · score 0.508 · **CRITICAL 9.5**_

Attackers are exploiting a critical flaw in Cisco Secure Email Gateway that lets a sender with no login write files to the appliance's operating system, Cisco&nbsp;said in an advisory&nbsp;on Wednesday. The attacker sends an email with a crafted attachment through the gateway and, if it succeeds, co…

`cisco`

### 43. [Cisco Secure Email Gateway: Cisco Secure Email Gateway Relative Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76519)
_CISA KEV · Oct 14 · score 0.479 · **CRITICAL 9.0** · CVE-2026-76519_

Cisco Secure Email Gateway contains a relative path traversal vulnerability that could allow an unauthenticated, remote attacker to write arbitrary files on the underlying operating system. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD…

`cisco`

### 44. [An AI Agent Found a Critical OTP Bypass in Production. The Attack Was the Easy Part.](https://thehackernews.com/2026/10/an-ai-agent-found-critical-otp-bypass.html)
_The Hacker News · Oct 14 · score 0.373 · **CRITICAL 9.5**_

The bug was simple: the login let you choose where your sign-in code went. Proving it on a live website was the hard part. TL;DR During an authorized assessment, an AI pentesting agent found a critical authentication bypass on a major insurer's production website, on its own. One login request let t…

`authentication bypass`

### 45. [Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App](https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html)
_The Hacker News · Oct 14 · score 0.200 · **CRITICAL 9.5**_

Attackers exploited a flaw in an optional Nextcloud app,&nbsp;Collabora Online - Built-in CODE Server, to plant web shells on Nextcloud servers. Three administrators&nbsp;reported the issue on GitHub, with the first logged attack on September 10. A web shell is a small file that executes any command…

`github` `backdoor`

### 46. [RUSTSEC-2026-0349: Vulnerability in rustls](https://rustsec.org/advisories/RUSTSEC-2026-0349.html)
_RustSec · Oct 14 · score 0.129 · **HIGH 8.0**_

Unauthenticated ServerHello can downgrade later connections to classical key exchange

`rustls`

### 47. [Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access, Only Two Patched So Far](https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html)
_The Hacker News · Oct 13 · score 0.350 · **CRITICAL 9.0**_

An attacker chained three zero-day flaws in Ivanti Connect Secure, a VPN appliance, to run commands as root without logging in, security firm&nbsp;Volexity said&nbsp;on October 13. Ivanti has released fixes for two of the flaws and told customers on affected versions to "act immediately." A fix for …

`vpn` `ivanti` `vpn appliance` `zero-day`

### 48. [SAP Discloses Critical CVSS 10 Flaw in Cloud SDK for Python Allowing OAuth2 Credential Theft](https://thehackernews.com/2026/10/sap-discloses-critical-cvss-10-flaw-in.html)
_The Hacker News · Oct 13 · score 0.235 · **CRITICAL 9.5**_

A flaw in SAP's&nbsp;Cloud SDK for Python&nbsp;can send an application's OAuth2 client credentials to a server an attacker controls, SAP said in a&nbsp;security advisory&nbsp;on October 13. The flaw affects multi-tenant applications on SAP Business Technology Platform (BTP) that use the SDK, SAP's o…

`python` `credential` `cvss`

### 49. [Microsoft Windows: Microsoft Windows Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96951)
_CISA KEV · Oct 13 · score 0.201 · **CRITICAL 9.0** · CVE-2026-96951_

Microsoft Windows Shell contains a command injection vulnerability that allows an unauthorized attacker to bypass a security feature over a network. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Base…

`windows`

### 50. [Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images as Another](https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html)
_The Hacker News · Oct 13 · score 0.160 · **CRITICAL 9.5**_

A flaw in Docker Hub, the registry where container images are published and downloaded, let one user push, pull, or delete images as another user. Docker fixed the flaw on September 30 and says it found no evidence that anyone exploited it. The flaw was in the feature that&nbsp;converts a personal a…

`container` `docker`

### 51. [Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft 365 Tenants](https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html)
_The Hacker News · Oct 17 · score 0.552_

Cybersecurity researchers are sounding the alarm related to an active campaign in which unknown threat actors are abusing a compromised Microsoft 365 (M365) credential belonging to ConnectWise Cloud Backup (formerly SkyKick) to gain unauthorized access to customers' M365 environments. ConnectWise Cl…

`credential`

### 52. [RUSTSEC-2026-0367: Vulnerability in zip](https://rustsec.org/advisories/RUSTSEC-2026-0367.html)
_RustSec · Oct 17 · score 0.371_

Insecure Preservation of SUID/SGID Bits during ZIP Extraction Leading to Potential Privilege Escalation

`privilege escalation`

### 53. [What Is Software Supply Chain Security? The Complete Guide | Endor Labs](https://www.endorlabs.com/learn/what-is-software-supply-chain-security-the-complete-guide)
_Endor Labs · Oct 16 · score 0.459_

What Is Software Supply Chain Security? The Complete Guide

`supply chain`

### 54. [Burger King Japan data breach exposes 11 million customer records](https://www.bleepingcomputer.com/news/security/burger-king-japan-data-breach-exposes-11-million-customer-records/)
_BleepingComputer · Oct 16 · score 0.359_

Burger King Japan, the Japanese subsidiary of global fast-food giant Burger King, disclosed a major data breach after attackers accessed a server containing 11.18 million customer records. [...]

`breach`

### 55. [ClickMigrate has Path Traversal in "revision -m" argument](https://github.com/advisories/GHSA-vgf9-9mxx-hq54)
_GHSA — pip · Oct 16 · score 0.328 · **LOW 3.3** · CVE-2026-68549_

Affected: ClickMigrate. ### Impact A path traversal vulnerability in the `revision` command allowed a crafted migration name supplied via the `-m` argument to escape the intended migrations directory. Under specific conditions, an attacker could cause the tool to create a `.sql` file in an arbitrary…

`ci/cd`

### 56. [UAT-11985 Uses Fake Event Invites to Target Taiwan Research Affiliates With Google AitM Phishing](https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html)
_The Hacker News · Oct 16 · score 0.322_

Cybersecurity researchers have disclosed details of an advanced persistent threat (APT) spear-phishing campaign that has targeted individuals affiliated with Taiwan research organizations to direct victims to an adversary-in-the-middle (AitM) phishing framework designed to harvest their Google accou…

`mfa`

### 57. [Surprise Your Github Actions Are Dependencies Too |… | Endor Labs](https://www.endorlabs.com/learn/surprise-your-github-actions-are-dependencies-too)
_Endor Labs · Oct 16 · score 0.306_

Read Surprise Your Github Actions Are Dependencies Too and learn practical strategies for application security, risk prioritization, and faster…

`github` `github actions`

### 58. [Container Scanning + SCA = Better Together | Endor Labs](https://www.endorlabs.com/learn/container-scanning-sca-better-together)
_Endor Labs · Oct 16 · score 0.288_

We’re excited to announce that Endor Labs now extends our software supply chain platform to include container scanning.

`supply chain` `container`

### 59. [PWN Request Threat: A Hidden Danger in GitHub Actions | Endor Labs](https://www.endorlabs.com/learn/pwn-request-threat-a-hidden-danger-in-github-actions)
_Endor Labs · Oct 16 · score 0.286_

Endor Labs provides comprehensive CI/CD security for GitHub action workflows that detect patterns that may indicate PWN request threats.

`github` `github actions` `ci/cd`

### 60. [Introducing CI/CD Security with Endor Labs | Endor Labs](https://www.endorlabs.com/learn/introducing-ci-cd-security-with-endor-labs)
_Endor Labs · Oct 16 · score 0.240_

Endor Labs CI/CD helps organizations secure their pipelines through pipeline discovery, repository security posture management, and build integrity verification (artifact signing).

`ci/cd`

### 61. [Researchers Demonstrate OpenBSD Root Exploit Chaining 37-Year-Old Shared-Memory Bug](https://thehackernews.com/2026/10/researchers-demonstrate-openbsd-root.html)
_The Hacker News · Oct 16 · score 0.232_

A local privilege escalation exploit published today gains root on OpenBSD 7.9 by chaining a roughly 37-year-old integer overflow with a separate kernel flaw, bypassing OpenBSD's KARL kernel-address randomization and its SMAP and SMEP hardware protections.Security firm Calif, which found and reporte…

`kernel` `exploit` `privilege escalation`

### 62. [CoreDNS `k8s_external` headless AXFR can emit an empty transfer batch that panics the `transfer` plugin](https://github.com/advisories/GHSA-74w3-63xv-x9mv)
_GHSA — go · Oct 16 · score 0.191 · **LOW 3.7** · CVE-2026-62994_

Affected: github.com/coredns/coredns. ### Summary A network DNS client allowed to request AXFR for a CoreDNS zone can trigger a panic when CoreDNS is configured with `k8s_external` headless-service zone transfers and Kubernetes contains a headless service endpoint with no declared ports. The built-i…

`github` `kubernetes` `dns`

### 63. [Xcode 27 runner image generally available](https://github.blog/changelog/2026-10-15-xcode-27-runner-image-generally-available)
_GitHub Changelog · Oct 16 · score 0.143_

You can now use the generally available Xcode 27 runner image to build and test your Apple applications in GitHub Actions. Previously in public preview, this GitHub-hosted image runs on&#8230; The post Xcode 27 runner image generally available appeared first on The GitHub Blog .

`github` `github actions` `runner` `apple`

### 64. [By Default, Insecure: Apache Airflow Disables SSH Host Key Verification](https://www.ox.security/blog/by-default-insecure-apache-airflow-disables-ssh-host-key-verification/)
_OX Security · Oct 16 · score 0.137 · CVE-2026-94134, CVE-2026-94135_

Vulnerability Details CVE-2026-94134 &#8211; SSH hook default, both providers CVE-2026-94135 &#8211; Async SFTP path Severity: High &#8211; CVSS 8.1 (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N) CWE: CWE-322 (Key Exchange without Entity Authentication) Affected packages: apache-airflow-providers-ss…

`ssh` `cve-` `cvss`

### 65. [Top 8 Application Security Platforms: Ranked for 2026 | Endor Labs](https://www.endorlabs.com/learn/best-application-security-platforms)
_Endor Labs · Oct 16 · score 0.136_

Application security platforms combine SAST, SCA, container scanning, and secrets detection into one workflow. See the top 8 platforms ranked for 2026.

`container`

### 66. [SBOM vs. SBOM: Comparing SBOMs from Different Tools and Lifecycle Stages | Endor Labs](https://www.endorlabs.com/learn/sbom-vs-sbom-comparing-sboms-from-different-tools-and-lifecycle-stages)
_Endor Labs · Oct 16 · score 0.127_

Software vendors active in certain verticals will soon be required to provide customers with SBOMs for their products. But how and when should an SBOM for a given piece of software be produced?

`sbom`

### 67. [Employees using personal ChatGPT at work? Here's what IT admins need to do](https://www.bleepingcomputer.com/news/security/employees-using-personal-chatgpt-at-work-heres-what-it-admins-need-to-do/)
_BleepingComputer · Oct 16 · score 0.084_

Employees using personal ChatGPT accounts at work can expose sensitive company data, even when their organization provides an approved Enterprise workspace. NordLayer explains how IT teams can investigate unauthorized AI use and block sensitive information before it reaches personal accounts. [...]

`teams`

### 68. [Multi-repository support and other improvements for GitHub in Slack and Teams](https://github.blog/changelog/2026-10-15-copilot-in-slack-and-teams-adds-model-and-repository-updates)
_GitHub Changelog · Oct 16 · score 0.037_

@GitHub in Slack and Teams now supports working across multiple repositories in a single conversation. Whether you&#8217;re creating issues, opening pull requests, or investigating bugs, you can work across repositories&#8230; The post Multi-repository support and other improvements for GitHub in Sl…

`github` `slack` `teams`

### 69. [Open source license compliance generally available](https://github.blog/changelog/2026-10-16-open-source-license-compliance-generally-available)
_GitHub Changelog · Oct 16 · score 0.028_

Enterprises can now manage their dependencies&#8217; licenses at scale with sophisticated, ruleset-based checks that enforce a centralized policy. Open source license compliance is now generally available for GitHub Enterprise Cloud&#8230; The post Open source license compliance generally available …

`github`

### 70. [Deno Goes the Way of the Dinosaur](https://socket.dev/blog/deno-acquisition?utm_medium=feed)
_Socket Blog · Oct 16 · score 0.010_

Cloudflare is acquiring Deno’s team, which will provide another year of bug fixes and security updates before ending support for the runtime.

`cloudflare`

### 71. [Best SBOM Tools in 2026, Compared | Endor Labs](https://www.endorlabs.com/learn/best-sbom-tools-in-2026-compared)
_Endor Labs · Oct 16 · score 0.008_

Best SBOM Tools in 2026, Compared

`sbom`

### 72. [What is CI/CD Security and What Tools Do You Need to Do it? | Endor Labs](https://www.endorlabs.com/learn/what-is-ci-cd-security-and-what-tools-do-you-need-to-do-it)
_Endor Labs · Oct 16 · score 0.008_

Learn what CI/CD security is, why it’s important, and discover the key tools Endor Labs offers to help you secure your CI/CD pipelines.

`ci/cd`

### 73. [Key Questions for Your SBOM Program | Endor Labs](https://www.endorlabs.com/learn/sbom-vex-security-program-operations)
_Endor Labs · Oct 16 · score 0.008_

All the questions (and some of the answers) you need before kicking off your SBOM program.

`sbom`

### 74. [Microsoft: October Windows update may break Smart App Control](https://www.bleepingcomputer.com/news/microsoft/kb5127648-windows-security-update-may-break-smart-app-control/)
_BleepingComputer · Oct 16 · score 0.006_

Microsoft says some users may have trouble turning on Smart App Control after installing this month's KB5127648 Windows 11 security update. [...]

`windows`

### 75. [SFTPGo source-side file-pattern filter bypass during copy operations](https://github.com/advisories/GHSA-wwv9-g5x4-966q)
_GHSA — go · Oct 15 · score 1.037 · **MEDIUM 6.5** · ×2 reports · CVE-2026-103028, CVE-2026-77375_

Affected: github.com/drakkan/sftpgo/v2. ### Summary File pattern filters (`denied_patterns` / `allowed_patterns`) were evaluated on the destination of a copy only. A user holding the copy permission could copy a file denied by the filters to a permitted name and then read it. A recursive directory c…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-q7pc-356p-hggc)_

### 76. [GitHub CLI allows attestation verification bypass through unescaped regex metacharacters](https://github.com/advisories/GHSA-mm27-mwq9-fr5g)
_GHSA — go · Oct 15 · score 0.677 · **LOW 3.3** · ×3 reports · CVE-2026-64652, CVE-2026-64653, CVE-2026-64655_

Affected: github.com/cli/cli/v2. ### Summary A security vulnerability has been identified in GitHub CLI that could allow attestation verification bypass when using `gh attestation verify` with `--signer-repo` or `--signer-workflow` flags. GitHub CLI builds the certificate matcher from these flag val…

`github` `certificate`

_also: [GHSA — go](https://github.com/advisories/GHSA-4fjg-2h4q-fwg3), [GHSA — go](https://github.com/advisories/GHSA-cg6r-mpgc-h9mm)_

### 77. [Python Social Auth: Login CSRF in LINE backend (LineOAuth2) — missing OAuth state validation (incomplete fix of 5.0.0 campaign)](https://github.com/advisories/GHSA-526j-582w-7fm9)
_GHSA — pip · Oct 15 · score 0.424 · **MEDIUM 6.5** · CVE-2026-62322_

Affected: social-auth-core. ### Impact Applications using the LINE Login backend are vulnerable to login CSRF / forced authentication. An attacker can start a LINE authorization flow for an account they control and trick a victim into visiting the callback URL with the attacker’s authorization code.…

`python` `oauth` `csrf`

### 78. [Terragrunt catalog predictable temp symlink clobber](https://github.com/advisories/GHSA-wv6g-x823-wx9m)
_GHSA — go · Oct 15 · score 0.351 · **MEDIUM** · CVE-2026-64672_

Affected: github.com/gruntwork-io/terragrunt. ### Summary Terragrunt's `terragrunt catalog` command clones each repository referenced in your catalog configuration into a temporary working directory. In affected versions, the clone path it derived was deterministic and sat under the shared system te…

`github`

### 79. [Pipecat: Public exposure of Pipecat’s development runner can allow unauthenticated bot session creation](https://github.com/advisories/GHSA-hqm2-cfx2-2vgh)
_GHSA — pip · Oct 15 · score 0.332 · **MEDIUM 5.6** · CVE-2026-102682_

Affected: pipecat-ai. Pipecat’s built-in development runner exposes endpoints that create bot sessions and, for the Daily transport, paid Daily rooms. These development endpoints intentionally do not authenticate callers. The runner binds to localhost by default and is designed exclusively for local…

`runner` `session`

### 80. [unstructured: Stored XSS via unescaped HTML generation](https://github.com/advisories/GHSA-v5mq-3xhg-98m9)
_GHSA — pip · Oct 15 · score 0.275 · **MEDIUM 6.1** · CVE-2026-104250_

Affected: unstructured. ### Summary When `unstructured` parses an untrusted document and outputs the result as HTML, malicious markup contained in the document (e.g. `<img src=x onerror=...>`) is left in the output HTML without escaping. When that output is displayed in a browser, the script embedde…

`xss`
