# feedrank — 2026-10-31

_80 items, 5d window._

### 1. [Ivanti Connect Secure: Ivanti Connect Secure Missing Authentication for Critical Function Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111357)
_CISA KEV · Oct 31 · score 1.610 · **CRITICAL 9.5** · ×2 reports · CVE-2026-111357_

Ivanti Connect Secure contains a missing authentication for critical function vulnerability that could allow a local authenticated attacker to escalate their privileges. This vulnerability can be chained with CVE-2026-104935 and CVE-2026-118527. Required action: Apply mitigations in accordance with …

`ivanti` `cve-`

_also: [The Hacker News](https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html)_

### 2. [Trojanized Claude Code Extension Delivered Persistent SSH Backdoor to Developer Machines](https://www.stepsecurity.io/blog/claude-code-extension-trojanized)
_StepSecurity · Oct 31 · score 0.456 · **HIGH 8.5**_

On October 29, 2026, a trojanized version (2.1.313) of the official Claude Code VS Code extension was published to Cursor's extension marketplace, reaching up to 5,000 Cursor users during an 11-hour window. Sandbox and registry analysis confirmed that on load it planted an attacker SSH key, set up p…

`ssh` `backdoor`

### 3. [imgproxy has integer overflow in imgproxy ICO loader that causes denial of service and may permit remote code execution](https://github.com/advisories/GHSA-hff9-5pqw-6w9f)
_GHSA — go · Oct 30 · score 1.102 · **CRITICAL 9.8** · ×3 reports_

Affected: github.com/imgproxy/imgproxy/v3, github.com/imgproxy/imgproxy/v2, github.com/imgproxy/imgproxy. ## Summary The ICO loader allocates `data_size + BMP_FILE_HEADER_LEN` bytes after reading a 32-bit attacker-controlled `data_size`. For `data_size > UINT32_MAX - BMP_FILE_HEADER_LEN`, the additi…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-494m-4556-wf5p), [GHSA — go](https://github.com/advisories/GHSA-mmq5-xm89-9pfg)_

### 4. [GitLab Community Edition and Enterprise Edition: GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-97229)
_CISA KEV · Oct 30 · score 0.876 · **CRITICAL 9.5** · ×3 reports · CVE-2026-97229_

GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression v…

`gitlab` `ci/cd`

_also: [The Hacker News](https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html), [The Hacker News](https://thehackernews.com/2026/10/attacker-tried-to-exploit-alpine-linuxs.html)_

### 5. [Ivanti Connect Secure: Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-118527)
_CISA KEV · Oct 30 · score 0.624 · **CRITICAL 9.0** · CVE-2026-118527_

Ivanti Connect Secure contains a generation of predictable numbers or identifiers vulnerability that allows a remote authenticated attacker to upload files with attacker-controlled content to a known location on disk. This vulnerability can be chained with CVE-2026-104935 and CVE-2026-111357. Requir…

`ivanti` `cve-`

### 6. [Critical Linux kernel flaw allows remote root attacks on MPTCP servers](https://www.bleepingcomputer.com/news/security/critical-linux-kernel-flaw-allows-remote-root-attacks-on-mptcp-servers/)
_BleepingComputer · Oct 30 · score 0.497 · **CRITICAL 9.5**_

Security researchers at Anthropic have developed an exploit for a critical Linux kernel vulnerability that allows unauthenticated attackers to remotely execute commands as root on servers running Multipath TCP (MPTCP) listeners. [...]

`linux` `kernel` `exploit`

### 7. [WordPress RCE Flaw Draws Nearly 63,000 Attack Attempts in Just 24 Hours](https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html)
_The Hacker News · Oct 30 · score 0.426 · **CRITICAL 9.0**_

Threat actors have been observed attempting to exploit a high-severity security flaw in WordPress Core shortly after patches were released. The vulnerability, which does not have a CVE identifier, relates to a case of remote code execution impacting WordPress Core versions 4.7 through 7.1.3. It carr…

`rce` `exploit` `cvss`

### 8. [Drupal warns of critical Commerce Core flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/drupal-warns-of-critical-commerce-core-flaw-exploited-in-attacks/)
_BleepingComputer · Oct 30 · score 0.379 · **CRITICAL 9.5**_

Drupal warned admins to patch a critical access bypass vulnerability in the Commerce Core module that attackers are exploiting in the wild. [...]

`in the wild`

### 9. [Hackers Actively Exploit Highly Critical Drupal Commerce Core Authorization Bypass Flaw](https://thehackernews.com/2026/10/hackers-actively-exploit-highly.html)
_The Hacker News · Oct 30 · score 0.354 · **CRITICAL 9.5** · CVE-2026-118539_

Drupal has warned that threat actors are exploiting a "highly critical" security flaw in its Commerce Core component. The vulnerability, tracked as CVE-2026-118539 (CVSS score: N/A), is a case of missing authorization affecting Commerce Core versions from 0.0.0 to 2.41 and from 3.0.0 to 3.3.13. "Thi…

`exploit` `cve-` `cvss`

### 10. [signalk-server has SSRF via absolute signalk.appIcon URL in the app store icon fetcher](https://github.com/advisories/GHSA-7wpf-ch8f-5f4x)
_GHSA — npm · Oct 30 · score 0.349 · **CRITICAL 9.8** · ×2 reports_

Affected: signalk-server. ### Summary The app store icon code (`dist/appstore/icon-probe.js` around line 200 and `icon-bytes.js` around line 138) resolves a plugin's declared `signalk.appIcon`. Relative paths are pinned to the CDN, but an absolute http(s) URL is used as-is: the server fetches it, fo…

`docker` `cdn` `ssrf`

_also: [GHSA — npm](https://github.com/advisories/GHSA-4xm8-rg9h-jhq2)_

### 11. [Why Urgent Security Fixes Aren't Fixed. Observe, Prove, Act, Confirm Gets Them Moving](https://thehackernews.com/2026/10/why-urgent-security-fixes-arent-fixed.html)
_The Hacker News · Oct 30 · score 0.176 · **CRITICAL 9.5**_

The alert is critical. The fix is known. And the ticket sits in a queue for days. Security teams understand the risk, but the people who keep applications available need proof that the change won’t break anything.&nbsp; Their concerns are practical. An IPS protection could block legitimate traffic. …

`teams`

### 12. [AdminNeo SQLite: multi_query Incorrect Check of Function Return Value RCE](https://github.com/advisories/GHSA-p96f-p2p2-2g3h)
_GHSA — composer · Oct 30 · score 0.972 · **HIGH 8.1** · ×6 reports · CVE-2026-59978, CVE-2026-96629, CVE-2026-96630_

Affected: adminneo-org/adminneo. ### Summary This vulnerability is a patch bypass that exploits catastrophic backtracking in a regular expression used to filter ATTACH statements in AdminNeo's SQLite functionality. The original vulnerability (CVE-2021-43008) allowed authenticated users to create PHP…

`php` `github` `sqlite` `rce` `cve-`

_also: [GHSA — composer](https://github.com/advisories/GHSA-6vfx-w7q3-42gq), [GHSA — composer](https://github.com/advisories/GHSA-rx7m-wxwq-vxr9), [GHSA — composer](https://github.com/advisories/GHSA-q5mp-gfjf-cf2j), [GHSA — composer](https://github.com/advisories/GHSA-wm25-49w3-5qrg), [GHSA — composer](https://github.com/advisories/GHSA-jm85-8cpp-9cjc)_

### 13. [Forge: ASN.1 OID first arc truncation in asn1.oidToDer](https://github.com/advisories/GHSA-4642-5mcj-2rqw)
_GHSA — npm · Oct 30 · score 0.703 · **HIGH 7.5** · ×11 reports · CVE-2026-118775, CVE-2026-118777, CVE-2026-118778_

Affected: node-forge. ### Summary `asn1.oidToDer()` did not range-check the first two arcs of an OID string, so an OID such as `0.42.840.113549.1.1.1` or `4294977127.18.840.113549.1.1.1` was encoded as the DER of a different OID (here rsaEncryption, `1.2.840.113549.1.1.1`). This is an incomplete fix…

`node` `cve-`

_also: [GHSA — npm](https://github.com/advisories/GHSA-6wvx-3r32-xmcg), [GHSA — npm](https://github.com/advisories/GHSA-525v-9gp9-w22h), [GHSA — npm](https://github.com/advisories/GHSA-7wch-p9px-956x), [GHSA — npm](https://github.com/advisories/GHSA-h6cr-wjv9-3cpp), [GHSA — npm](https://github.com/advisories/GHSA-4487-j8r4-4g2f)_

### 14. [Kubeflow Pipelines: Pipeline archive upload allows decompression bomb to exhaust server memory](https://github.com/advisories/GHSA-8fmv-6rg5-5924)
_GHSA — go · Oct 30 · score 0.631 · **HIGH 7.5** · ×2 reports · CVE-2026-118759, CVE-2026-118761_

Affected: github.com/kubeflow/pipelines, github.com/kubeflow/pipelines. ## Summary The Kubeflow Pipelines API server decompresses uploaded pipeline archives without adequately bounding expanded data in affected versions. A small ZIP or gzip-compressed tar archive can consume disproportionately large…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-wg5q-x4j9-qm54)_

### 15. [pypdf has possible infinite loop when hitting EOF in standard xref table during trailer search](https://github.com/advisories/GHSA-5849-834g-hvw5)
_GHSA — pip · Oct 30 · score 0.567 · **HIGH** · ×7 reports · CVE-2026-119203, CVE-2026-119204, CVE-2026-119205_

Affected: pypdf. ### Impact An attacker who uses this vulnerability can craft a PDF which leads to an infinite loop. This requires opening an incomplete file without a `trailer`. ### Patches This has been fixed in [pypdf==6.21.4](https://github.com/py-pdf/pypdf/releases/tag/6.21.4). ### Workarounds …

`github`

_also: [GHSA — pip](https://github.com/advisories/GHSA-cggf-277g-3q54), [GHSA — pip](https://github.com/advisories/GHSA-mfr5-77xh-9j7h), [GHSA — pip](https://github.com/advisories/GHSA-42gh-23hr-vphw), [GHSA — pip](https://github.com/advisories/GHSA-4vqv-7265-gm2w), [GHSA — pip](https://github.com/advisories/GHSA-62m5-6wh8-28x7)_

### 16. [russh: Agent server never calls `Agent::confirm`, so keys added with the confirm constraint (`ssh-add -c`) sign without confirmation](https://github.com/advisories/GHSA-vp5q-ff62-jwqv)
_GHSA — rust · Oct 30 · score 0.500 · **HIGH 4.3** · ×3 reports · CVE-2026-116696, CVE-2026-116773, CVE-2026-116794_

Affected: russh. ### Summary The agent server in `russh::keys::agent::server` never calls `Agent::confirm` before signing with a key that was added with the confirm constraint. That constraint is `SSH_AGENT_CONSTRAIN_CONFIRM` (RFC 9987 §5.2.7.2), which is what `ssh-add -c` sends. The call was replac…

`ssh`

_also: [GHSA — rust](https://github.com/advisories/GHSA-9wfm-jcj8-jfv9), [GHSA — rust](https://github.com/advisories/GHSA-4p9f-7p9m-5vfg)_

### 17. [Authlib RFC 7592 examples omit registration-access-token client binding](https://github.com/advisories/GHSA-c73q-w75p-j82v)
_GHSA — pip · Oct 30 · score 0.453 · **HIGH 8.8** · CVE-2026-116672_

Affected: Authlib. ## Description ### Summary RFC 7592 (OAuth 2.0 Dynamic Client Registration Management Protocol) lets a previously registered client read, update, or delete its own registration, authenticated by a `registration_access_token` issued specifically to that client at registration time.…

`oauth` `token`

### 18. [pyasn1 has quadratic-complexity denial of service in binary REAL decoding](https://github.com/advisories/GHSA-mm57-4v3p-rchx)
_GHSA — pip · Oct 30 · score 0.452 · **HIGH 7.5** · ×2 reports · CVE-2026-119194, CVE-2026-119197_

Affected: pyasn1. ## Summary In pyasn1 0.6.4 and earlier, decoding a binary-encoded ASN.1 REAL with a large mantissa can consume CPU time quadratic in the mantissa length. The BER, CER, and DER decoders all use the affected `RealPayloadDecoder`. An application is exposed when it passes attacker-cont…

`github` `cve-`

_also: [GHSA — pip](https://github.com/advisories/GHSA-fm9c-5rcf-2q5p)_

### 19. [@sigstore/oci sends the registry Authorization header to a cross-host blob-upload Location](https://github.com/advisories/GHSA-j63v-mwhm-56jx)
_GHSA — npm · Oct 30 · score 0.353 · **HIGH 7.4** · CVE-2026-118763_

Affected: @sigstore/oci. ### Summary @sigstore/oci sends the registry Authorization header to a cross-host blob-upload Location ## Affected versions and vulnerable location - Confirmed on sigstore-js at `3a83271` (current HEAD). - File: `packages/oci/src/registry.ts`. - `signIn()` installs the crede…

`sigstore` `docker` `token` `credential`

### 20. [Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html)
_The Hacker News · Oct 30 · score 0.309 · **HIGH 8.5**_

Cybersecurity researchers have disclosed that a trojanized version of Anthropic's official Claude Code extension was distributed through the Cursor Marketplace as a legitimate update, attempting to install a persistent SSH backdoor on affected systems. The malicious update, version 2.1.313, was dist…

`ssh` `backdoor`

### 21. [GraphQL-core has denial of service via memory leak in aborted validations](https://github.com/advisories/GHSA-mpqx-q82w-9x46)
_GHSA — pip · Oct 30 · score 0.306 · **HIGH 7.5** · CVE-2026-119286_

Affected: graphql-core. ### Summary When a validation was aborted because the document contained more errors than allowed by `max_errors` (100 by default), `validate()` raised a single module-level `ValidationAbortedError` instance. Python appends the frames of every `raise` to the existing `__trace…

`python`

### 22. [follow-redirects: Cross-realm sensitiveHeaders arrays are discarded and custom credentials can follow redirects](https://github.com/advisories/GHSA-mrwp-f3q8-3g9p)
_GHSA — npm · Oct 30 · score 0.295 · **HIGH 5.9** · CVE-2026-116689_

Affected: follow-redirects. ### Summary follow-redirects 1.16.0 and 1.16.1 validate the documented sensitiveHeaders option with instanceof Array. An array created in another JavaScript realm is silently replaced with an empty list, so a caller-declared custom credential header can be forwarded to an…

`javascript` `credential`

### 23. [joi: quadratic-time split in `string().email({ multiple: true })` allows denial of service](https://github.com/advisories/GHSA-4528-x5fx-h6hg)
_GHSA — npm · Oct 30 · score 0.263 · **HIGH 7.5** · CVE-2026-118772_

Affected: joi, @hapi/joi, joi. ### Summary `Joi.string().email({ multiple: true })` takes quadratic time to split a value that contains a long run of whitespace. One request with 100 KB of spaces blocks the Node.js event loop for several seconds, which causes a denial of service. ### Details When th…

`node`

### 24. [@hapi/content: quadratic-time parsing of Content-Disposition parameters allows denial of service](https://github.com/advisories/GHSA-8494-f6mr-cjpv)
_GHSA — npm · Oct 30 · score 0.263 · **HIGH 7.5** · CVE-2026-119202_

Affected: @hapi/content, content. ### Summary `Content.disposition()` takes quadratic time when a `Content-Disposition` parameter contains a long token without `=`. One unauthenticated multipart request can block the Node.js event loop for several minutes. ### Details `Content.disposition()` reads t…

`node` `token`

### 25. [OAuthLib: Token grants can use attacker-supplied client_id for authorization after authenticating a different client](https://github.com/advisories/GHSA-7984-qgvg-3j9c)
_GHSA — pip · Oct 30 · score 0.237 · **HIGH** · CVE-2026-118669_

Affected: oauthlib. ## Summary OAuthlib's token grant handlers can authenticate one client while authorizing the grant type and requested scopes using a different, attacker-supplied `client_id` from the request body. In affected token grant flows, `authenticate_client(request)` sets `request.client`…

`token`

### 26. [Malicious Claude Code extension on Cursor planted SSH backdoors](https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/)
_BleepingComputer · Oct 30 · score 0.150 · **HIGH 8.5**_

A malicious version of Anthropic's Claude Code VS Code extension was distributed through Cursor's extension marketplace for approximately 11 hours on October 29, exposing up to 5,000 developers to malware designed to install persistent SSH backdoors. [...]

`ssh`

### 27. [Cisco Secure Firewall ASA Software and Cisco Secure FTD Software: Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76418)
_CISA KEV · Oct 29 · score 1.185 · **CRITICAL 9.5** · ×2 reports · CVE-2026-76418_

Cisco Secure Firewall ASA Software and Cisco Secure FTD Software contains an unchecked return value to NULL pointer dereference vulnerability that could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition. Required ac…

`cisco` `asa` `firewall`

_also: [The Hacker News](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html)_

### 28. [Broadcom VMware ESX: Broadcom VMWare ESX Insufficient Logging Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-41709)
_CISA KEV · Oct 29 · score 0.681 · **CRITICAL 9.0** · ×2 reports · CVE-2026-41709_

Broadcom VMWare ESX contains an insufficient logging vulnerability that could allow a malicious actor with admin access to perform certain operations without being logged. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizin…

`vmware`

_also: [The Hacker News](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html)_

### 29. [zip: legacy Shrink/Reduce/Implode decoder: denial of service from attacker-controlled ZIP64 uncompressed size](https://github.com/advisories/GHSA-9hj8-73fh-9963)
_GHSA — rust · Oct 29 · score 0.478 · **CRITICAL 7.5** · ×5 reports · CVE-2026-115905, CVE-2026-115906, CVE-2026-115907_

Affected: zip. ### Summary A malicious 149-byte ZIP archive can cause a denial of service in applications that enable `legacy-zip` and use `ZipArchive::extract()`. An attacker-controlled ZIP64 uncompressed size triggers a `capacity overflow` panic in the Shrink decoder in optimized builds, potential…

`rust`

_also: [GHSA — rust](https://github.com/advisories/GHSA-hjqx-j4rw-g7xv), [GHSA — rust](https://github.com/advisories/GHSA-8hxf-qr8p-62x4), [GHSA — rust](https://github.com/advisories/GHSA-q7v9-x93c-xqv3), [GHSA — rust](https://github.com/advisories/GHSA-m665-v7pm-7grj)_

### 30. [ThreatsDay: Critical Firewall Flaws, Banking Trojans Rented, Weaponized PDF, Token Theft + 26 More Stories](https://thehackernews.com/2026/10/threatsday-critical-firewall-flaws.html)
_The Hacker News · Oct 29 · score 0.454 · **CRITICAL 9.5**_

Some attacks take real skill. Others just need someone to leave a door open. This week has both. Exposed passwords, old bugs still getting exploited, and trusted software doing things it shouldn't. There's a strange mix of clever tricks and careless mistakes. Hackers are borrowing trust from familia…

`token` `firewall`

### 31. [Node2Shell: Reproducing CVE-2026-111497 in the Node.js Brotli decoder](https://securitylabs.datadoghq.com/articles/node2shell-cve-2026-111497-nodejs-brotli-decoder/)
_Datadog Security Labs · Oct 29 · score 0.360 · **CRITICAL 9.0** · ×3 reports · CVE-2026-111497_

We reproduced CVE-2026-111497, an out-of-bounds write in the Brotli decoder bundled with Node.js and other runtimes, and explain how to detect and remediate it.

`node` `cve-`

_also: [Sysdig](https://webflow.sysdig.com/blog/node2shell-cve-2026-111497-detecting-the-node-js-brotli-rce), [The Hacker News](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html)_

### 32. [Hackers Exploited Cisco SD-WAN Flaw to Plant Malware Built to Steal Encryption Keys](https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html)
_The Hacker News · Oct 29 · score 0.242 · **CRITICAL 9.5**_

Hackers exploited a critical Cisco Catalyst SD-WAN flaw, fixed in February, to plant custom malware inside the systems that control an organization's SD-WAN network. The malware, called KeyDrift, is designed to copy the keys that encrypt traffic between sites and store them for later use,&nbsp;Cisco…

`cisco`

### 33. [What the PHP Patch Scramble Reveals About Remediation](https://checkmarx.com/blog/what-the-php-patch-scramble-reveals-about-remediation/)
_Checkmarx Zero · Oct 29 · score 0.209 · **CRITICAL 9.5**_

When Nick Woodhead spoke with Business Insider on October 23, he had been awake for nearly 48 hours responding to critical PHP vulnerabilities. The CTO of Rothco and Compubox was helping his teams update systems, review logs for signs of compromise, and protect older installations while they waited …

`php` `teams`

### 34. [cert-manager: Direct ACME Challenge resources can bypass Issuer DNS01 solver policy and use ClusterIssuer DNS credentials](https://github.com/advisories/GHSA-8rvj-mm4h-c258)
_GHSA — go · Oct 29 · score 0.467 · **HIGH 7.3** · CVE-2026-62290_

Affected: github.com/cert-manager/cert-manager, github.com/cert-manager/cert-manager. ## Summary `Challenge` resources under `acme.cert-manager.io` can be created directly by namespace users. On create, cert-manager performs no admission validation tying the Challenge to an `Order`, an owner referen…

`github` `credential` `acme` `dns`

### 35. [PraisonAI vulnerable to Remote Code Execution via Broken AST Sandbox](https://github.com/advisories/GHSA-26mh-57q7-jfvr)
_GHSA — pip · Oct 29 · score 0.448 · **HIGH 7.3** · CVE-2026-61438_

Affected: praisonai. ### Summary JobWorkflowExecutor._exec_inline_python() is designed to safely execute inline Python expressions from YAML workflow script: steps using AST validation. The function claims to block dangerous operations by (a) checking all AST nodes against an allowlist, and (b) prov…

`python`

### 36. [Daptin: ParseAcceptLanguage `_` separator bypass enables >250x CPU amplification via Accept-Language header in LanguageMiddleware](https://github.com/advisories/GHSA-rhj7-vh3v-mcq6)
_GHSA — go · Oct 29 · score 0.389 · **HIGH** · CVE-2026-62160_

Affected: github.com/daptin/daptin. ### Summary Daptin's `LanguageMiddleware` (registered as a global gin middleware) calls `golang.org/x/text/language.ParseAcceptLanguage` on the raw `Accept-Language` header of every HTTP request without imposing any size or shape filter. The underlying parser has …

`golang` `github` `cve-`

### 37. [Twisted: Unauthenticated Remote Denial of Service in the Twisted HTTP/2 Server via Rapid Stream Reset](https://github.com/advisories/GHSA-vpp8-g58w-m8mp)
_GHSA — pip · Oct 29 · score 0.332 · **HIGH 7.5** · CVE-2023-44487_

Affected: Twisted. ## Summary An uncontrolled-resource-consumption vulnerability (CWE-400) in the Twisted HTTP/2 server lets any unauthenticated remote client exhaust server CPU over a single connection. A client that sends a request header block with `END_STREAM` and then immediately resets the str…

`cve-`

### 38. [@eeacms/volto-chatbot has Unauthenticated Danswer API Confused Deputy Proxy](https://github.com/advisories/GHSA-w9x9-j56r-h98r)
_GHSA — npm · Oct 29 · score 0.227 · **HIGH 8.2**_

Affected: @eeacms/volto-chatbot. ## Unauthenticated Danswer API Confused Deputy Proxy in @eeacms/volto-chatbot ### Summary `@eeacms/volto-chatbot` exposes an Express middleware route (`**/_v1_da/**`) that accepts unauthenticated HTTP requests from any network client and proxies them to the configure…

`session`

### 39. [decode-uri-component vulnerable to denial of service via quadratic replacement of percent-encoded runs](https://github.com/advisories/GHSA-qr28-fpjm-wq7f)
_GHSA — npm · Oct 29 · score 0.206 · **HIGH** · CVE-2026-118664_

Affected: decode-uri-component. ### Summary `decodeUriComponent()` takes quadratic time on malformed input that has many distinct percent-encoded runs. A single unauthenticated request of about 224 KB can block the Node.js event loop for about 20 seconds. Version 0.5.0, the release that fixed CVE-20…

`node` `cve-`

### 40. [@sylphx/pdf-reader-mcp: HTTP transport accepts unauthenticated requests despite a configured MCP_API_KEY](https://github.com/advisories/GHSA-q344-5v34-gm84)
_GHSA — npm · Oct 29 · score 0.163 · **HIGH 7.5** · CVE-2026-62264_

Affected: @sylphx/pdf-reader-mcp. ### Impact When `@sylphx/pdf-reader-mcp` is run as an HTTP server (`MCP_TRANSPORT=http`), it reads the `MCP_API_KEY` environment variable and logs `API key authentication enabled (X-API-Key header)` at startup, but it never validated the `X-API-Key` header on incomi…

`bind`

### 41. [PHP2Shell (CVE-2026-109618 and CVE-2026-109619): Detecting unauthenticated remote code execution in PHP core](https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core)
_Sysdig · Oct 28 · score 0.922 · **CRITICAL 9.5** · ×2 reports · CVE-2026-109618, CVE-2026-109619_

PHP2Shell (CVE-2026-109618 and CVE-2026-109619) lets an unauthenticated attacker run code on a PHP server with HTTP requests alone. The Sysdig Threat Research Team analyzed the exploitation and outlines affected versions, mitigations, and how to detect post-exploitation activity at runtime with Sysd…

`php` `cve-`

_also: [OX Security](https://www.ox.security/blog/php2shell-day-5-the-panic-hasnt-turned-into-patching/)_

### 42. [Volt Typhoon Used Covert Silent Train Network in Four Zero-Day Exploitation Campaigns](https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html)
_The Hacker News · Oct 28 · score 0.433 · **CRITICAL 9.0**_

The China-nexus cyber espionage group known as Volt Typhoon has been attributed to a now-disrupted covert access network dubbed Silent Train that has been put to use for zero-day exploitation and strategic access. "First identified in late 2023, Silent Train uses rotating chains of compromised SOHO,…

`zero-day`

### 43. [Linux Kernel: Linux Kernel Missing Initialization of a Variable Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)
_CISA KEV · Oct 28 · score 0.417 · **CRITICAL 9.0** · CVE-2026-46300_

Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. Thi…

`php` `linux` `kernel` `cve-`

### 44. [Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch](https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html)
_The Hacker News · Oct 28 · score 0.296 · **CRITICAL 9.5** · CVE-2026-101767_

Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber. The vulnerability in question is CVE-2026-101767 (CVSS score: 9.8) , a case of improper authentication in the Oracle Application Obje…

`rce` `cve-` `cvss`

### 45. [ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html)
_The Hacker News · Oct 28 · score 0.285 · **CRITICAL 9.5** · CVE-2026-35273_

The critical Oracle PeopleSoft bug that ShinyHunters has exploited since May is not one flaw but three chained together, the researchers who reported it said this week. Oracle patched all three under a single identifier,&nbsp;CVE-2026-35273, in June. Its root is a server-side request forgery (SSRF) …

`zero-day` `ssrf` `cve-`

### 46. [Adobe Fixes 8 Critical Campaign Classic Flaws Allowing Code Execution and Security Bypass](https://thehackernews.com/2026/10/adobe-fixes-8-critical-campaign-classic.html)
_The Hacker News · Oct 28 · score 0.268 · **CRITICAL 9.5** · CVE-2026-104351_

Adobe has released patches to address multiple critical security flaws in Campaign Classic that, if successfully exploited, could result in arbitrary code execution, security feature bypass, and privilege escalation. The list of eight vulnerabilities is as follows - CVE-2026-104351 (CVSS score: 9.9)…

`privilege escalation` `cve-` `cvss`

### 47. [Electrum: Malicious server can replace a just-broadcast tx and try to trick user into RBF-ing it](https://github.com/advisories/GHSA-6jp4-8v48-cc5v)
_GHSA — pip · Oct 28 · score 0.129 · **CRITICAL 7.5** · CVE-2026-117601_

Affected: electrum. ### Summary The main Electrum server the client connects to is trusted with mempool ("unconfirmed") transactions. This is documented [design](https://electrum.readthedocs.io/en/latest/faq.html#does-electrum-trust-servers). [0] However now someone figured out a way to practically …

`exploit`

### 48. [Echo: HTTPS Redirect and HSTS Bypass via Unconditional Trust of Forwarded Scheme Headers](https://github.com/advisories/GHSA-2ffq-g2xg-c22p)
_GHSA — go · Oct 28 · score 0.789 · **HIGH 7.5** · ×10 reports · CVE-2026-118266, CVE-2026-118650, CVE-2026-118651_

Affected: github.com/labstack/echo/v5, github.com/labstack/echo/v4. ## Description `Context.Scheme()` unconditionally trusts four client-controlled HTTP headers to determine the request scheme, with no mechanism to configure trusted sources. This allows a remote unauthenticated attacker to bypass HT…

`github` `ssl`

_also: [GHSA — go](https://github.com/advisories/GHSA-3pmx-cf9f-34xr), [GHSA — go](https://github.com/advisories/GHSA-xwq5-6cqp-vx96), [GHSA — go](https://github.com/advisories/GHSA-v753-g4cw-jm48), [GHSA — go](https://github.com/advisories/GHSA-23wf-92cp-8pcj), [GHSA — go](https://github.com/advisories/GHSA-375p-5qhx-8wq4)_

### 49. [Vue I18n: `escapeParameter` does not escape named values when the same call also passes a list](https://github.com/advisories/GHSA-8rc2-428q-7ww3)
_GHSA — npm · Oct 28 · score 0.737 · **HIGH 7.2** · ×2 reports · CVE-2026-118256, CVE-2026-118257_

Affected: vue-i18n, vue-i18n, @intlify/core, @intlify/core, @intlify/core-base. ### Summary When `escapeParameter` is enabled (`escapeParameterHtml` in the Legacy API), Vue I18n escapes the interpolation parameters before formatting a message. `escapeParams()` escapes either the list values or the n…

`github`

_also: [GHSA — npm](https://github.com/advisories/GHSA-83rm-6c8r-g728)_

### 50. [Go JOSE: Panics in JSON parsing](https://github.com/advisories/GHSA-vvm8-gf78-28g4)
_GHSA — go · Oct 28 · score 0.471 · **HIGH 7.5** · ×3 reports · CVE-2026-116585, CVE-2026-116586, CVE-2026-116587_

Affected: github.com/go-jose/go-jose/v4, github.com/go-jose/go-jose/v3. ### Summary Parsing deeply nested JSON structures can hit Go's stack limit, causing the application to crash. Note: this advisory is the same as https://github.com/go-jose/go-jose/security/advisories/GHSA-6mp9-8xrw-74r4. ### Imp…

`go ` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-4w3g-jfj2-cw2q), [GHSA — go](https://github.com/advisories/GHSA-mgcc-cww5-fp2q)_

### 51. [GraphQL Tools: Per-request connection parameters persist into later users' WebSocket authentications](https://github.com/advisories/GHSA-434m-5hcj-pxf3)
_GHSA — npm · Oct 28 · score 0.416 · **HIGH** · CVE-2026-118665_

Affected: @graphql-tools/executor-legacy-ws. # Stale authentication state in `@graphql-tools/executor-legacy-ws`: per-request `extensions.connectionParams` persist in executor closure state and are replayed in a later caller's `connection_init` ## Report metadata | Field | Value | | --- | --- | | Pa…

`npm` `github` `credential`

### 52. [vLLM: Permissive default CORS origins allow cross-origin requests to the vLLM HTTP server](https://github.com/advisories/GHSA-vvpg-rrww-wpmh)
_GHSA — pip · Oct 28 · score 0.382 · **HIGH 8.1** · ×4 reports · CVE-2026-115914, CVE-2026-115915, CVE-2026-115916_

Affected: vllm. ### Summary The OpenAI-compatible server registers Starlette `CORSMiddleware` with `allowed_origins` defaulting to `["*"]`, and performs no authentication unless `--api-key` (or `VLLM_API_KEY`) is configured. A web page on any origin can send requests to a vLLM server that the victim…

`vpn`

_also: [GHSA — pip](https://github.com/advisories/GHSA-gq5q-89c7-vhvx), [GHSA — pip](https://github.com/advisories/GHSA-h3rc-j82p-2c3h), [GHSA — pip](https://github.com/advisories/GHSA-q97c-p368-75c4)_

### 53. [systeminformation vulnerable to Windows command injection in services() through Unicode quotation marks](https://github.com/advisories/GHSA-3f7j-7jwc-fxfj)
_GHSA — npm · Oct 28 · score 0.337 · **HIGH 7.8** · ×3 reports · CVE-2026-116576, CVE-2026-116673, CVE-2026-116674_

Affected: systeminformation. ### Summary On Windows, `systeminformation@5.33.15` builds a PowerShell command using the value passed to `services()`. The default sanitizer removes ASCII quotes but keeps Unicode curly quotes, spaces, and parentheses. A crafted service name can use those characters to …

`node` `windows`

_also: [GHSA — npm](https://github.com/advisories/GHSA-4vjg-vx72-qq4g), [GHSA — npm](https://github.com/advisories/GHSA-7648-jmwf-vw7j)_

### 54. [American Organizations Under Attack: Skyw4lker Device Code Phishing Campaign Exposed](https://thehackernews.com/2026/10/american-organizations-under-attack.html)
_The Hacker News · Oct 28 · score 0.316 · **HIGH 8.5**_

Modern phishing campaigns can compromise American businesses without relying on traditional credential theft. Attackers can abuse legitimate cloud services, authentication mechanisms, and trusted business workflows to gain access to corporate accounts while leaving fewer obvious signs behind. ANY.RU…

`credential`

### 55. [Happy DOM: SSRF via iframe and link stylesheet when parsing untrusted HTML](https://github.com/advisories/GHSA-c8p4-j97h-3vg8)
_GHSA — npm · Oct 28 · score 0.296 · **HIGH 8.6** · ×2 reports · CVE-2026-118660, CVE-2026-118661_

Affected: happy-dom. ## Summary happy-dom v20.8.9 makes real server-side HTTP requests to arbitrary URLs when parsing HTML containing `<iframe>` or `<link rel="stylesheet">` elements. This behavior is enabled by default (`disableIframePageLoading: false`, `disableCSSFileLoading: false`). When an app…

`ssrf`

_also: [GHSA — npm](https://github.com/advisories/GHSA-5fpq-26gf-qwcr)_

### 56. [Seroval: fromJSON deserializer trusts node-supplied array length and sequence doneAt (unauthenticated event-loop DoS)](https://github.com/advisories/GHSA-97r2-qh9m-474h)
_GHSA — npm · Oct 28 · score 0.233 · **HIGH 7.5** · ×3 reports · CVE-2026-116580, CVE-2026-116581, CVE-2026-116584_

Affected: seroval. ### Summary `fromJSON` and `fromCrossJSON` used two node fields without checking them. - An array node's element list was not checked to be an array. A small payload could set the length the decoder looped over. This part is also tracked in GHSA-wp97-x4hv-qvhp. - A sequence node's…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-wp97-x4hv-qvhp), [GHSA — npm](https://github.com/advisories/GHSA-7rv5-mrxv-xcr9)_

### 57. [graphql-scalars PhoneNumber scalar is vulnerable to regular expression denial of service](https://github.com/advisories/GHSA-x8rm-f576-gq67)
_GHSA — npm · Oct 28 · score 0.188 · **HIGH 7.5** · CVE-2026-115887_

Affected: graphql-scalars. ## Summary The regular expression behind `GraphQLPhoneNumber` since 1.24.1 backtracks exponentially. A string made of a run of digits followed by one character that makes the match fail (for example `"1".repeat(30) + "x"`) blocks the JavaScript thread for seconds, and ever…

`javascript`

### 58. [LangGraph JavaScript custom authentication may permit cross-user Store access](https://github.com/advisories/GHSA-4hm6-w6qq-w73v)
_GHSA — pip · Oct 28 · score 0.180 · **HIGH** · CVE-2026-118668_

Affected: langgraph-api. ## Summary LangGraph deployments using JavaScript or TypeScript custom authentication may fail to apply Store authorization changes returned by an authorization handler. In affected deployments, an authenticated user may be able to access Store data outside their authorized …

`javascript` `typescript`

### 59. [Apple Backports Fix for Exploited CoreGraphics Flaw to Older iPhones and iPads](https://thehackernews.com/2026/10/apple-backports-fix-for-exploited.html)
_The Hacker News · Oct 27 · score 0.250 · **CRITICAL 9.0** · CVE-2026-86950_

Apple on Monday backported fixes for a high-severity security flaw that was exploited in real-world cyber attacks to older devices. The vulnerability, tracked as CVE-2026-86950 (CVSS score: 8.8), is an out-of-bounds write affecting CoreGraphics that could result in arbitrary code execution when proc…

`apple` `cve-` `cvss`

### 60. [RUSTSEC-2026-0412: Vulnerability in cargo-nextest](https://rustsec.org/advisories/RUSTSEC-2026-0412.html)
_RustSec · Oct 27 · score 0.151 · **CRITICAL 9.0**_

Arbitrary code execution when rerunning tests from a portable recording

`cargo`

### 61. [Adobe Commerce and Magento: Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48356)
_CISA KEV · Oct 27 · score 0.151 · **CRITICAL 9.0** · CVE-2026-48356_

Adobe Commerce and Magento contain an unrestricted upload of file with dangerous type vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim's account or session. Required action: Apply mitigation…

`session`

### 62. [PhpSpreadsheet: SSRF whitelist bypass via unre-validated HTTP redirect in Drawing::setPath external image loading](https://github.com/advisories/GHSA-2phh-27fw-q4gc)
_GHSA — composer · Oct 27 · score 0.358 · **HIGH 6.4** · ×3 reports · CVE-2026-108357, CVE-2026-108358, CVE-2026-108360_

Affected: phpoffice/phpspreadsheet, phpoffice/phpspreadsheet, phpoffice/phpspreadsheet, phpoffice/phpspreadsheet, phpoffice/phpspreadsheet. ## Summary PhpSpreadsheet's `Worksheet\Drawing::setPath()` validates an external-image URL against an operator-supplied `isWhitelisted` callback **once**, on th…

`php` `ssrf`

_also: [GHSA — composer](https://github.com/advisories/GHSA-3x94-m842-937c), [GHSA — composer](https://github.com/advisories/GHSA-rxj4-h86g-25gc)_

### 63. [FileBrowser: Symlink following escapes user scope allowing arbitrary file read outside the served directory](https://github.com/advisories/GHSA-mgqf-5mf5-prfj)
_GHSA — go · Oct 27 · score 0.268 · **HIGH 8.6** · CVE-2026-116682_

Affected: github.com/gtsteffaniak/filebrowser/backend. ## Summary File read paths resolve symbolic links with `filepath.EvalSymlinks` and then operate on the resolved target without re-checking that the target still lies inside the user's source/scope. A symlink located inside a user's accessible di…

`github` `container` `ssh`

### 64. [Wails: wildcardPatternToRegex allows Origin bypass via suffix match in BindingsAllowedOrigins](https://github.com/advisories/GHSA-47hv-j4px-h3c9)
_GHSA — go · Oct 27 · score 0.223 · **HIGH** · CVE-2026-34157_

Affected: github.com/wailsapp/wails/v2. # Security Vulnerability Report: Wails v2 — Origin Validator Bypass via Wildcard Pattern | | | |---|---| | **Product** | wailsapp/wails (v2) | | **Affected File** | `v2/internal/frontend/originvalidator/originValidator.go` | | **Affected Versions** | All versi…

`github` `linux` `windows` `macos` `cvss`

### 65. [CTFer.io's CTFd Terraform Provider allows a local or remote attacker to read team passwords in state as non sensitive values](https://github.com/advisories/GHSA-vg84-c5mg-76xh)
_GHSA — go · Oct 27 · score 0.184 · **HIGH** · CVE-2026-116683_

Affected: github.com/ctfer-io/terraform-provider-ctfd, github.com/ctfer-io/terraform-provider-ctfd/v2. ### Impact CTFer.io's CTFd Terraform Provider stores `ctfd_team.password` as non-sensitive values (CWE-522). A local or remote attacker, who can have access to the Terraform state, can read team pa…

`github` `terraform`

### 66. [Atlantis: OS command injection through PR-controlled Terraform workspace enables RCE during plan](https://github.com/advisories/GHSA-rjh2-4xgw-p2hj)
_GHSA — go · Oct 27 · score 0.161 · **HIGH 8.8** · CVE-2026-116676_

Affected: github.com/runatlantis/atlantis. ### Summary Atlantis passes the Terraform `workspace` value from a pull request's `atlantis.yaml` into a shell command without quoting or escaping it. A contributor whose pull request is eligible for an Atlantis plan can include shell metacharacters in the …

`github` `terraform` `rce`

### 67. [Dolibarr has SQL Injection in societe/class/societe.class.php via localtax1_value parameter](https://github.com/advisories/GHSA-v5fq-cf5m-vwv7)
_GHSA — composer · Oct 27 · score 0.161 · **HIGH 8.8** · CVE-2026-33944_

Affected: dolibarr/dolibarr. ### Summary A SQL Injection vulnerability exists in the Third Party (Company) update functionality of Dolibarr ERP/CRM. The `localtax1_value` parameter (`lt1`) is concatenated directly into an SQL UPDATE statement in `societe/class/societe.class.php` at line 1672 without…

`php` `sql injection`

### 68. [TinyMCE Cross-Site Scripting (XSS) vulnerability using media plugin `data-mce-object` serialization](https://github.com/advisories/GHSA-mf2p-h6hf-fcwm)
_GHSA — composer · Oct 27 · score 0.137 · **HIGH** · CVE-2026-116675_

Affected: tinymce, TinyMCE, tinymce/tinymce, tinymce, TinyMCE. ### Impact Stored XSS vulnerability in the media plugin. Attackers can inject malicious scripts via elements crafted through the data-mce-object attribute, which are created and executed before sanitization. Impacts users of TinyMCE with…

`xss`

### 69. [compress zstd: Panic on two-block frames](https://github.com/advisories/GHSA-fpmh-frq8-7rj8)
_GHSA — go · Oct 27 · score 0.137 · **HIGH** · CVE-2026-116591_

Affected: github.com/klauspost/compress/zstd. ### Summary A crafted ~27 KB two-block zstd frame makes DecodeAll and the streaming decoder panic with an out-of-range slice index instead of returning a decode error. The same bytes decode fine with the reference zstd. Any program that decompresses untr…

`github`

### 70. [Symfony: ReDoS in HeaderUtils::split() Reachable Through the Cache-Control Request Header](https://github.com/advisories/GHSA-r925-mgvr-h9cc)
_GHSA — composer · Oct 27 · score 0.126 · **HIGH** · CVE-2026-108082_

Affected: symfony/http-foundation, symfony/http-foundation, symfony/http-foundation, symfony/symfony, symfony/symfony. ### Description `HeaderUtils::split()` parsed header values with a pattern whose token alternative also matched whitespace, followed by a `(?<!\s)` lookbehind. A run of whitespace p…

`token`

### 71. [Symfony: Unbounded Recursion in the YAML Inline Lexer Lets a Single Document Crash the Process](https://github.com/advisories/GHSA-2v3c-qxhr-7vpv)
_GHSA — composer · Oct 27 · score 0.106 · **HIGH** · CVE-2026-109413_

Affected: symfony/symfony, symfony/symfony, symfony/symfony, symfony/symfony, symfony/yaml. ### Description `Yaml\Parser::lexInlineStructure()` recursed through `lexInlineMapping()` and `lexInlineSequence()` for every `{` and `[` of an inline collection, without entering the nesting level that the r…

`php`

### 72. [litellm 1.107.0 Compromised on PyPI and Docker: Credential Stealer and Hourly Remote Code Loader](https://www.stepsecurity.io/blog/litellm-1-107-0-compromised-pypi-backdoored-wheels-credential-stealer)
_StepSecurity · Oct 26 · score 0.936 · **CRITICAL 9.0**_

litellm 1.107.0 PyPI wheels and Docker images shipped a .pth credential stealer and an hourly remote code loader that exfiltrate to litellm.dev. Analysis, IOCs, and how to respond.

`pypi` `docker` `credential` `stealer`

### 73. [Chainalysis Confirms Intrusion Into Internal Tools and Exposure of Customer Identity Data](https://thehackernews.com/2026/10/chainalysis-confirms-intrusion-into.html)
_The Hacker News · Oct 31 · score 0.393_

American blockchain analysis firm Chainalysis said it was the target of a cybersecurity incident in which an external actor accessed non-sensitive customer data. However, the company noted that the breach did not result in unauthorized access to its investigation content, authentication credentials,…

`session` `breach`

### 74. [Cloudflare Reports 18.2 Million Network-Layer DDoS Attacks in Q3, Up 38%](https://thehackernews.com/2026/10/cloudflare-reports-182-million-network.html)
_The Hacker News · Oct 31 · score 0.187_

Threat actors are launching about 8,226 network-layer distributed denial-of-service (DDoS) attacks per hour, Cloudflare revealed Thursday. The web infrastructure and security company said it autonomously mitigated 18.2 million network-layer (L3) DDoS attacks and 14.4 trillion HTTP DDoS requests in t…

`cloudflare`

### 75. [A Shared ChatGPT Link Could Run Attacker Code in Your Session and Read Private Chats](https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html)
_The Hacker News · Oct 31 · score 0.105_

A malicious ChatGPT share link could run an attacker's code in the logged-in session of anyone who opened it, allowing them to read their private conversations, researchers at&nbsp;the security firm Parameter&nbsp;showed. The researchers reported the flaw through&nbsp;OpenAI's bug bounty program&nbs…

`session`

### 76. [Nuxt: Dot segments in the request path bypass `server/middleware` path checks and server route rules on page routes](https://github.com/advisories/GHSA-9v7c-q64q-vv33)
_GHSA — npm · Oct 30 · score 0.390 · **MEDIUM 6.5** · CVE-2026-119200_

Affected: nuxt, @nuxt/nitro-server. ### Summary Since `4.6.0`, Nuxt resolves `.` and `..` segments in the request path, including percent-encoded forms such as `%2e`, before rendering a page. Nitro's routing, Nitro's route rules and `server/middleware` see the path with those segments still in place…

`node`

### 77. [PHPUnit vulnerable to code execution by other local users via shared temporary directory in PHPT code coverage handling](https://github.com/advisories/GHSA-9vw2-f4vp-x7gf)
_GHSA — composer · Oct 30 · score 0.345 · **MEDIUM** · CVE-2026-119193_

Affected: phpunit/phpunit. ### Summary When PHPT tests are run with code coverage, PHPUnit 13.4.0 to 13.4.3 writes the code of each PHPT test to a directory with a fixed name below the operating system's path used for temporary files, for instance `/tmp/phpunit-phpt` on Linux, and executes it from t…

`linux`

### 78. [Billions stolen in Binance hack](https://risky.biz/RBNEWS627/)
_Risky Business News · Oct 30 · score 0.323_

Billions stolen from Binance in a crypto hack, Last week’s PHP2Shell bugs are being exploited to hack Palo Alto Networks firewalls, The Brotli bugs also get a run, Belarusian state hackers carry out a wiper attack, and a hacker leaks the data of 41,000 DHS employees.

`palo alto`

### 79. [CISA says max severity GitLab flaw now exploited in the wild](https://www.bleepingcomputer.com/news/security/hackers-now-exploiting-max-severity-gitlab-flaw-in-attacks/)
_BleepingComputer · Oct 30 · score 0.310_

Attackers have started exploiting a maximum-severity GitLab vulnerability patched earlier this month, according to the US Cybersecurity and Infrastructure Security Agency (CISA). [...]

`gitlab` `in the wild`

### 80. [Compromised Claude Code Extension (2.1.313) in Cursor Marketplace Plants Attacker SSH Key and Persistence](https://www.ox.security/blog/malicious-claude-code-extension-cursor-ssh-backdoor/)
_OX Security · Oct 30 · score 0.283_

A modified build of Anthropic&#8217;s Claude Code extension was available in the Cursor Extension Marketplace for about 11 hours on October 29, 2026. The malicious extension added an attacker-controlled SSH key, installed persistence, and attempted to open a reverse SSH tunnel. Overview On October 2…

`ssh`
