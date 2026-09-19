# feedrank — 2026-09-19

_80 items, 5d window._

### 1. [Linux Kernel: Linux Kernel Improper Check for Unusual or Exceptional Conditions Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-39682)
_CISA KEV · Sep 19 · score 1.471 · **CRITICAL 9.0** · ×2 reports · CVE-2025-39682_

Linux Kernel contains an improper check for unusual or exceptional conditions vulnerability in the TLS receive path which allows a zero-length record retrieved from the rx_list to bypass the intended recvmsg() record-type handling, potentially causing subsequent TLS records to be processed using inc…

`linux` `kernel` `tls`

_also: [The Hacker News](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)_

### 2. [Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild](https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html)
_The Hacker News · Sep 19 · score 1.365 · **CRITICAL 9.5** · CVE-2026-58138_

A critical vulnerability impacting Orkes Conductor is being actively exploited in the wild, according to Fortinet. The vulnerability in question is CVE-2026-58138 (CVSS v3.1 score: 9.8/CVSS v4 score: 9.3), which relates to a case of unauthenticated remote code execution. "Orkes Conductor 3.21.21 bef…

`fortinet` `rce` `actively exploited` `in the wild` `cve-`

### 3. [SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html)
_The Hacker News · Sep 19 · score 0.616 · **CRITICAL 9.0** · CVE-2026-28326_

SolarWinds has released security updates to address a high-severity flaw in Access Rights Manager (ARM) that, if successfully exploited, could lead to an unauthenticated remote code execution vulnerability. The vulnerability, tracked as CVE-2026-28326, is rated 8.8 out of 10.0 on the CVSS scoring sy…

`rce` `cve-` `cvss`

### 4. [CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories](https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html)
_The Hacker News · Sep 19 · score 0.803 · **HIGH 8.5**_

An attacker copied about 170 of CrowdSec's private GitHub repositories on May 22 using the account of an employee who had just left, CrowdSec&nbsp;said on September 18. The French security company had kept his GitHub access open. CrowdSec says his laptop was compromised in May's&nbsp;supply chain at…

`npm` `github` `supply chain`

### 5. [Mnemosyne has JWT signature verification bypass sync server that allows authentication bypass](https://github.com/advisories/GHSA-xcw4-53cc-hv32)
_GHSA — pip · Sep 18 · score 1.310 · **CRITICAL 9.1** · CVE-2026-59163_

Affected: mnemosyne-memory. ### Summary The Mnemosyne sync server's authentication check decoded JWT bearer tokens but never verified their HMAC-SHA256 signatures. Any well-formed token was accepted, allowing an unauthenticated attacker to impersonate any user and read or modify their sync data. **S…

`jwt` `token` `authentication bypass` `cvss`

### 6. [LMDeploy has an SSRF bypass](https://github.com/advisories/GHSA-39wr-7q6h-cf68)
_GHSA — pip · Sep 18 · score 0.940 · **CRITICAL 9.8** · ×4 reports · CVE-2025-59953, CVE-2025-66455, CVE-2026-33625_

Affected: lmdeploy. ### Summary The URL checking logic in lmdeploy has a logical flaw that could be bypassed by attackers, leading to SSRF attacks. ### Details The current lmdeploy project uses `_is_safe_url` to validate the input URL. The main logic is to perform security checks on the host portion…

`github` `ssrf`

_also: [GHSA — pip](https://github.com/advisories/GHSA-3hmm-rh5q-gwwr), [GHSA — pip](https://github.com/advisories/GHSA-2vh9-42vm-xmv2), [GHSA — pip](https://github.com/advisories/GHSA-5h8j-6crg-7rmw)_

### 7. [Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)
_The Hacker News · Sep 18 · score 0.778 · **CRITICAL 9.5** · CVE-2026-85889_

Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required. The vulnerability, tracked as CVE-2026-85889, carries a CVSS score of 10.0. "Missing authentication for critical function in …

`azure` `privilege escalation` `cve-` `cvss`

### 8. [Linux Kernel: Linux Kernel Race Condition Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-39964)
_CISA KEV · Sep 18 · score 0.666 · **CRITICAL 9.0** · CVE-2025-39964_

Linux Kernel contains a race condition vulnerability which allows concurrent writes to the same AF_ALG socket causing data to be unpredictably interleaved and creating inconsistencies in the socket's internal state. Required action: Apply mitigations in accordance with vendor instructions, ensuring …

`linux` `kernel`

### 9. [Linux Kernel: Linux Kernel Out-of-Bounds Write Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-53266)
_CISA KEV · Sep 18 · score 0.601 · **CRITICAL 9.0** · CVE-2026-53266_

Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of…

`linux` `kernel`

### 10. [kcp front-proxy does not strip inbound X-Remote-* identity headers, allowing any authenticated client to inject groups/warrants and impersonate system:masters in any workspace](https://github.com/advisories/GHSA-c8w2-fgvx-vhv4)
_GHSA — go · Sep 18 · score 0.351 · **CRITICAL 9.9** · CVE-2026-61682_

Affected: github.com/kcp-dev/kcp, github.com/kcp-dev/kcp. # Summary The kcp front-proxy fails to strip client-supplied identity headers before forwarding requests to shards. Any authenticated tenant can inject their own `X-Remote-Group` and `X-Remote-Extra-*` headers, which the shard trusts as a ver…

`github`

### 11. [AnyIO run_process/open_process ignores extra_groups and can retain parent supplementary groups](https://github.com/advisories/GHSA-3w57-8xmc-8v26)
_GHSA — pip · Sep 18 · score 0.319 · **CRITICAL** · ×2 reports · CVE-2026-63349, CVE-2026-63374_

Affected: anyio. AnyIO 4.14.0 accepts the POSIX extra_groups argument on anyio.run_process() and anyio.open_process(), but open_process() forwards the wrong variable to the backend: when extra_groups is not None, it assigns kwargs["extra_groups"] = group instead of extra_groups. As a result, callers…

`python` `container` `linux`

_also: [GHSA — pip](https://github.com/advisories/GHSA-82r6-8w77-94w6)_

### 12. [Obot: Server-Side Request Forgery via remote MCP server URL](https://github.com/advisories/GHSA-jgh3-fggc-mcpm)
_GHSA — go · Sep 18 · score 0.924 · **HIGH 8.8** · ×3 reports_

Affected: github.com/obot-platform/obot. ## Summary In affected versions, the URL of a remote MCP server is attacker-controlled at registration and is fetched server-side with no validation of the destination. There is no guard against loopback, link-local, RFC1918 private ranges, or the cloud metad…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-pr6h-vr44-xq8j), [GHSA — go](https://github.com/advisories/GHSA-xwmw-prc4-v3cr)_

### 13. [Capsule: hostnameRegexHandler.OnUpdate validates stale (old) Tenant regex, allowing invalid AllowedHostnames regex to bypass webhook validation](https://github.com/advisories/GHSA-f94q-w3w8-cj67)
_GHSA — go · Sep 18 · score 0.727 · **HIGH 7.1** · ×3 reports · CVE-2026-61672, CVE-2026-61794, CVE-2026-61795_

Affected: github.com/projectcapsule/capsule. ### Summary A parameter order bug in `internal/webhook/tenant/validation/hostname_regex.go` causes the `hostnameRegexHandler.OnUpdate` webhook to validate the **old** Tenant object's `AllowedHostnames.Regex` instead of the **new** one being submitted. Thi…

`go ` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-gjw4-3v3v-rqxg), [GHSA — go](https://github.com/advisories/GHSA-gxjc-74v5-3vx3)_

### 14. [ToolHive: containerized MCP servers can reach host services via host.docker.internal, enabling lateral movement](https://github.com/advisories/GHSA-qg2g-g9w3-m5h8)
_GHSA — go · Sep 18 · score 0.544 · **HIGH 8.8** · CVE-2026-58197_

Affected: github.com/stacklok/toolhive. ## Summary A containerized MCP server running with the default `network` permission profile (`insecure_allow_all: true`) can reach host-local services via `host.docker.internal`. This includes the ToolHive API itself, other ToolHive-managed MCP server proxies,…

`github` `container` `docker`

### 15. [zot: Bearer authentication maps DELETE to push scope, allowing unauthorized deletion](https://github.com/advisories/GHSA-qg67-7m6v-qg25)
_GHSA — go · Sep 18 · score 0.537 · **HIGH 8.1** · CVE-2026-61833_

Affected: zotregistry.dev/zot/v2. ### Summary A bearer token with only `pull` and `push` scopes can successfully delete manifests and blobs from a zot registry. The bearer authentication handler maps all non-GET/HEAD HTTP methods, including DELETE, to the `"push"` action, and the `DistSpecAuthzHandl…

`github` `docker` `token`

### 16. [Happy Birthday, Shai-Hulud](https://socket.dev/blog/happy-birthday-shai-hulud?utm_medium=feed)
_Socket Blog · Sep 18 · score 0.495 · **HIGH 8.5** · ×2 reports_

It has been one year since Shai-Hulud made its first appearance on npm.

`npm` `shai-hulud`

_also: [The Hacker News](https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html)_

### 17. [Semantic MediaWiki'a missing authorization in the smwtask API module allows unauthenticated access to admin-only maintenance tasks](https://github.com/advisories/GHSA-jr78-w6w5-m8f8)
_GHSA — composer · Sep 18 · score 0.464 · **HIGH 8.6** · ×8 reports · CVE-2025-10354, CVE-2025-61682, CVE-2026-77606_

Affected: mediawiki/semantic-media-wiki. ### Summary The `api.php?action=smwtask` API module performs no authorization check. The equivalent maintenance interface in the web UI (`Special:SMWAdmin`) requires the `smw-admin` right, but the API module that backs several of the same operations enforces …

`php`

_also: [GHSA — composer](https://github.com/advisories/GHSA-9rcc-pmj8-ffhr), [GHSA — composer](https://github.com/advisories/GHSA-cx86-7xwp-w9wf), [GHSA — composer](https://github.com/advisories/GHSA-q5fm-9mx6-44f4), [GHSA — composer](https://github.com/advisories/GHSA-7xv3-gf2g-498h), [GHSA — composer](https://github.com/advisories/GHSA-59xw-qv23-j3rc)_

### 18. [File Viewer: DOM XSS via unsafe hyperlink schemes in the legacy DOC renderer](https://github.com/advisories/GHSA-3753-m2x2-q623)
_GHSA — npm · Sep 18 · score 0.427 · **HIGH 8.2** · CVE-2026-91127_

Affected: @file-viewer/doc, msdoc-viewer. ### Summary Before 2.3.1, the legacy `.doc` renderer emitted document hyperlink targets after HTML escaping but without a URL-scheme allowlist. A crafted `.doc` could therefore render a live `javascript:`, `vbscript:`, `data:`, or similarly unsafe link. Scri…

`javascript` `xss`

### 19. [Perses's unvalidated project parameter enables filesystem path traversal](https://github.com/advisories/GHSA-vr5f-w35q-98jp)
_GHSA — go · Sep 18 · score 0.373 · **HIGH** · ×3 reports · CVE-2026-63199, CVE-2026-63445, CVE-2026-63458_

Affected: github.com/perses/perses. ### Impact When Perses is using the file system database, on the list endpoints, the project value is bound from the request into the resource `Query` struct and is never validated against directory-traversal characters (validation/Flatten only runs for Create/Upd…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-4227-9989-jrhx), [GHSA — go](https://github.com/advisories/GHSA-cjgj-2fwf-4c2w)_

### 20. [adm-zip: Uncontrolled memory allocation via the declared uncompressed size (DoS)](https://github.com/advisories/GHSA-7q85-xj36-vmfc)
_GHSA — npm · Sep 18 · score 0.331 · **HIGH 7.5** · CVE-2026-77301_

Affected: adm-zip. ### Summary adm-zip allocates an entry's output buffer from the declared uncompressed size (central-directory `size` field) before validating it against the actual data. A tiny crafted ZIP that declares a huge uncompressed size forces a multi-gigabyte allocation from a few bytes. …

`node`

### 21. [Opencast: Stored XSS in Paella player via WebVTT/DFXP caption cue text](https://github.com/advisories/GHSA-m6c8-jcw2-5r25)
_GHSA — npm · Sep 18 · score 0.240 · **HIGH 8.7** · CVE-2026-77615_

Affected: org.opencastproject:opencast-engage-paella-player-7, org.opencastproject:opencast-engage-paella-player-7, paella-core. ## Summary The Opencast Paella player renders caption cue text into `innerHTML` without escaping. The captions canvas clears `_captionsContainer.innerHTML` and then append…

`xss`

### 22. [Convoy: Cross-Tenant Source IDOR Leaks Plaintext Message Broker Credentials](https://github.com/advisories/GHSA-p5vg-v7mj-f6q4)
_GHSA — go · Sep 18 · score 0.239 · **HIGH** · CVE-2026-81505_

Affected: github.com/frain-dev/convoy. ## Summary frain-dev/convoy (all versions up to and including v26.6.2, no patch available) lets any authenticated caller who is authorized on at least one project read ANY OTHER project's "Source" record by ID via GET /api/v1/projects/{projectID}/sources/{sourc…

`github` `kafka`

### 23. [Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2](https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html)
_The Hacker News · Sep 18 · score 0.190 · **HIGH 8.5**_

The Pakistan-aligned threat group tracked as Transparent Tribe (aka APT36 and Earth Karkaddan) has been attributed to a fresh set of cyber attacks targeting government and defense entities in India and Afghanistan. The attacks, per Zscaler ThreatLabz, involve the use of previously undocumented tools…

`rust` `github` `backdoor`

### 24. [Grav CMS vulnerable to remote code execution via .zip file upload](https://github.com/advisories/GHSA-r94f-hx44-8jqf)
_GHSA — composer · Sep 17 · score 1.553 · **CRITICAL 9.1** · ×18 reports · CVE-2026-59193, CVE-2026-61449, CVE-2026-61453_

Affected: getgrav/grav. ### Summary A logged-in user can run any command on the server. A settings field can fill itself by calling one of Grav's built-in routines, and a safety check is supposed to allow only harmless ones. The check only recognises a routine when its name is written as one piece o…

`php`

_also: [GHSA — composer](https://github.com/advisories/GHSA-xhfv-7758-r9hx), [GHSA — composer](https://github.com/advisories/GHSA-q2j8-x8hf-63ch), [GHSA — composer](https://github.com/advisories/GHSA-f8wv-xp27-6gq7), [GHSA — composer](https://github.com/advisories/GHSA-vfmf-q6x9-cw96), [GHSA — composer](https://github.com/advisories/GHSA-4v9q-p283-qc2m)_

### 25. [Cisco Identity Services Engine: Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76460)
_CISA KEV · Sep 17 · score 1.049 · **CRITICAL 9.0** · ×2 reports · CVE-2026-76460_

Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface. R…

`cisco`

_also: [The Hacker News](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)_

### 26. [RabbitMQ amqp091-go: Denial of Service via Malicious Field Length in AMQP Client](https://github.com/advisories/GHSA-4v58-74mf-rjx3)
_GHSA — go · Sep 17 · score 0.901 · **CRITICAL** · ×9 reports · CVE-2026-77403, CVE-2026-77404, CVE-2026-77405_

Affected: github.com/rabbitmq/amqp091-go. **Summary** A vulnerability in the readField function allows a malicious or compromised AMQP server to trigger an unhandled runtime panic in the client application, leading to an immediate crash of the entire process. **Details** When parsing incoming AMQP f…

`go ` `github` `rabbitmq`

_also: [GHSA — go](https://github.com/advisories/GHSA-c5pq-fr2g-9jpf), [GHSA — go](https://github.com/advisories/GHSA-r9c8-gcjp-xfwh), [GHSA — go](https://github.com/advisories/GHSA-j497-x9hr-x34x), [GHSA — go](https://github.com/advisories/GHSA-27gv-rfvv-22mv), [GHSA — go](https://github.com/advisories/GHSA-rm6m-hrcw-jw33)_

### 27. [Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files](https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html)
_The Hacker News · Sep 17 · score 0.765 · **CRITICAL 9.5** · CVE-2026-77179_

Malicious code running inside a Docker Sandboxes virtual machine on macOS could escape the project directory shared into it and read or change files anywhere else on the host, Docker warns in a&nbsp;security announcement&nbsp;on September 15. The escape runs with the rights of the host account that …

`docker` `macos` `cve-`

### 28. [Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)
_The Hacker News · Sep 17 · score 0.511 · **CRITICAL 9.5** · CVE-2026-81642_

Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an&nbsp;advisory&nbsp;on Wednesday. An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution. …

`dns` `dnssec` `unbound` `rce` `cve-`

### 29. [Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html)
_The Hacker News · Sep 17 · score 0.411 · **CRITICAL 9.5**_

A critical vulnerability in Check Point's Security Management and Log Servers could allow an attacker without login credentials to run code as root on those servers over the network. The Security Management Server is the system that controls firewall policy and administrator access. Check Point has …

`firewall`

### 30. [CakePHP: Multiple methods in FunctionsBuilder vulnerable to SQL injection](https://github.com/advisories/GHSA-vjqc-q4mp-2rvf)
_GHSA — composer · Sep 17 · score 0.239 · **CRITICAL** · CVE-2026-79752_

Affected: cakephp/database, cakephp/database, cakephp/database, cakephp/database, cakephp/database. ### Impact The `FunctionsBuilder::cast($field, $dataType)`, `extract($part, $expr)`, `datePart($part, $expr)`, `dateAdd($expr, $value, $unit)` methods are vulnerable to SQL injection if user controlle…

`sql injection`

### 31. [djust: A template binding inherits a context safety grant it never earned (XSS)](https://github.com/advisories/GHSA-xjw9-38cr-6372)
_GHSA — pip · Sep 17 · score 0.571 · **HIGH 8.1** · ×8 reports · CVE-2026-61588, CVE-2026-61590, CVE-2026-61591_

Affected: djust. A context safety grant was inherited by a template **binding** that never earned it, so rebinding a name the view had marked safe left the mark attached to the new, attacker-controlled value. djust's context safety channel is keyed by **name**, not by value. Every bind copied the va…

`bind` `xss`

_also: [GHSA — pip](https://github.com/advisories/GHSA-9395-2g46-rj3f), [GHSA — pip](https://github.com/advisories/GHSA-pvg3-6q9j-mj3x), [GHSA — pip](https://github.com/advisories/GHSA-c67v-vqrp-m5wj), [GHSA — pip](https://github.com/advisories/GHSA-f795-p5jw-j6g2), [GHSA — pip](https://github.com/advisories/GHSA-4mf4-73j6-mvrw)_

### 32. [CoreDNS DoH/DoQ/gRPC bypass UPDATE rejection enforced on UDP/TCP](https://github.com/advisories/GHSA-9gm5-9rfh-m6vx)
_GHSA — go · Sep 17 · score 0.500 · **HIGH 7.5** · ×2 reports · CVE-2026-82399, CVE-2026-86003_

Affected: github.com/coredns/coredns. ### Summary CoreDNS accepted [RFC 2136](https://datatracker.ietf.org/doc/html/rfc2136) UPDATE messages over DoH, DoH3, DoQ, and DNS-over-gRPC, then allowed the `proxy`/`forward` plugin to send them unchanged to an upstream DNS server. UDP, TCP, and DoT rejected …

`github` `dns`

_also: [GHSA — go](https://github.com/advisories/GHSA-mrg3-qvqr-jw29)_

### 33. [Tina: [Broken Access Control] letting any TinaCloud user authorize against any self-hosted site](https://github.com/advisories/GHSA-g74q-6g2f-874x)
_GHSA — npm · Sep 17 · score 0.475 · **HIGH 8.8** · CVE-2026-63506_

Affected: @tinacms/auth, next-tinacms-azure. ## Summary `@tinacms/auth`'s `isAuthorized(req)` decides authorization by validating the caller's bearer token against `https://identity.tinajs.io/v2/apps/${req.query.clientID}/currentUser`, where the `clientID` comes from the request and is never compare…

`azure` `token`

### 34. [RMCP: Custom HTTP headers leak to cross-origin redirect targets](https://github.com/advisories/GHSA-9g45-5xwm-f3wc)
_GHSA — rust · Sep 17 · score 0.388 · **HIGH 8.2** · ×3 reports · CVE-2026-63127, CVE-2026-63128, CVE-2026-64684_

Affected: rmcp. ## Summary The `rmcp` crate's `StreamableHttpClientTransport` forwards caller-supplied custom HTTP headers (such as `X-API-Key`, `X-Auth-Token`, `Api-Key`) to cross-origin redirect targets. The `default_http_client()` function builds a `reqwest::Client` without a redirect policy over…

`token`

_also: [GHSA — rust](https://github.com/advisories/GHSA-9pj6-vhgr-3mwh), [GHSA — rust](https://github.com/advisories/GHSA-33f5-2c5q-wgwj)_

### 35. [Skipper has OPA body-authz bypass: truncated_body mitigation fails open on chunked/HTTP-2 (incomplete fix GHSA-8qqm-fp2q-v734)](https://github.com/advisories/GHSA-5gpm-rgj3-9q76)
_GHSA — go · Sep 17 · score 0.388 · **HIGH 7.5** · CVE-2026-86043_

Affected: github.com/zalando/skipper. - **Affected component:** `filters/openpolicyagent/openpolicyagent.go` → `ExtractHttpBodyOptionally`; combined with `github.com/open-policy-agent/opa-envoy-plugin` `envoyauth/request.go` → `getParsedBody` / `checkIfHTTPBodyTruncated`. Filter: `opaAuthorizeReques…

`github` `envoy` `cve-`

### 36. [ExifReader: DoS via Crafted HEIC/AVIF iloc Box - Memory Exhaustion](https://github.com/advisories/GHSA-pj96-35fp-cfcc)
_GHSA — npm · Sep 17 · score 0.324 · **HIGH 7.5** · CVE-2026-85715_

Affected: exifreader. ## Summary ExifReader 4.41.0 is vulnerable to denial of service through a crafted HEIC or AVIF file with a malicious `iloc` box. When `offsetSize`, `lengthSize`, and `baseOffsetSize` are set to zero in the iloc header, the extent-parsing loop allocates an unbounded number of Ja…

`npm` `node` `javascript`

### 37. [Vendure: Unauthenticated ReDoS via `regex` filter on SQLite backends](https://github.com/advisories/GHSA-jgm3-qmp2-c4p7)
_GHSA — npm · Sep 17 · score 0.322 · **HIGH 7.5** · CVE-2026-63460_

Affected: vendure/core. ### Summary > [!IMPORTANT] > Only instances running on the SQLite driver (better-sqlite3) are affected; SQLite is usually used in development/testing backend, so production deployments on PostgreSQL or MySQL/MariaDB are unaffected. The `StringOperators.regex` filter exposed o…

`node` `postgresql` `mysql` `mariadb` `sqlite`

### 38. [oras-go: Blind SSRF via unvalidated Link header URL in pagination allows internal network probing](https://github.com/advisories/GHSA-h7vf-4x9w-h99v)
_GHSA — go · Sep 17 · score 0.288 · **HIGH 8.8** · ×2 reports · CVE-2026-85731, CVE-2026-85732_

Affected: oras.land/oras-go/v2. ## Summary oras-go's pagination helper `parseLink()` in `registry/remote/utils.go` follows the `Link` response header from a registry without validating the URL's host or scheme. When a malicious registry returns a `Link` header containing an absolute URL pointing to …

`ssrf`

_also: [GHSA — go](https://github.com/advisories/GHSA-m37j-52j7-pjw7)_

### 39. [Vendure has stored XSS in the Admin Dashboard via unsafe HTML-stripping (innerHTML) of entity descriptions](https://github.com/advisories/GHSA-xhq9-whgq-49j5)
_GHSA — npm · Sep 17 · score 0.255 · **HIGH 8.7** · CVE-2026-63459_

Affected: @vendure/dashboard. # Stored XSS in the Admin Dashboard via unsafe HTML-stripping (`innerHTML`) of entity descriptions **Package:** @vendure/dashboard (vendure-ecommerce/vendure, latest master) · ## Summary The dashboard's `RichTextDescriptionCell` "strips HTML" from an entity's `descripti…

`node` `chromium` `firefox` `xss`

### 40. [Jupyter Server: 5xx request logging leaks token-bearing Referer header values](https://github.com/advisories/GHSA-c3mw-737p-c7g2)
_GHSA — pip · Sep 17 · score 0.220 · **HIGH 7.1** · CVE-2026-86049_

Affected: jupyter_server. ### Summary When a request returns a 500, `jupyter_server/log.py` logs a small JSON block of request headers. The Referer header was copied into it as-is, so a token in the Referer URL ended up in the logs in plain text. ### Impact Anyone who can read the server logs can pi…

`token`

### 41. [Iran-Linked Handala Hack Tied to HEAVYGRAM Telegram Backdoor That Can Steal Passwords](https://thehackernews.com/2026/09/iran-linked-handala-hack-tied-to.html)
_The Hacker News · Sep 17 · score 0.214 · **HIGH 8.5**_

The Iran-linked "hacktivist" persona known as Handala Hack has been attributed to a Telegram-based surveillance backdoor called HEAVYGRAM and a Delphi-based utility known as CRUDEEXCLUDE. "HEAVYGRAM offers builtin commands supporting remote command execution, system, network and process information …

`session` `backdoor` `exfiltration`

### 42. [libp2p: Gossipsub StrictSign accepts attacker-signed messages as a victim RSA peer ID](https://github.com/advisories/GHSA-c3gv-825q-fvmp)
_GHSA — npm · Sep 17 · score 0.195 · **HIGH 7.5** · CVE-2026-86038_

Affected: @libp2p/gossipsub. ### Summary `@libp2p/gossipsub` `StrictSign` validation does not bind a supplied message public key to the claimed `from` peer ID when `from` is an RSA-style peer ID that does not inline its public key. An attacker can set `from` to a victim RSA peer ID, sign the message…

`bind`

### 43. [China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America](https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html)
_The Hacker News · Sep 17 · score 0.186 · **HIGH 8.5**_

The China-aligned state-sponsored threat actor known as FamousSparrow has been observed deploying a previously unreported backdoor called SparroWocky in attacks targeting multiple countries in Latin America since at least August 2025. "SparroWocky is a modular, C++ backdoor," ESET security researche…

`backdoor`

### 44. [Pocketbase: Unhandled panic in worker goroutines](https://github.com/advisories/GHSA-84vh-m24q-wjjx)
_GHSA — go · Sep 17 · score 0.171 · **HIGH** · CVE-2026-82410_

Affected: github.com/pocketbase/pocketbase, github.com/pocketbase/pocketbase. PocketBase already has builtin panic-recover middleware for the regular requests handling but it doesn't cover panics in internal child/worker goroutines which in some situations could cause termination of the server proce…

`github`

### 45. [Brevo supply-chain attack injected ClickFix scripts on customer sites](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)
_BleepingComputer · Sep 17 · score 0.167 · **HIGH 8.5**_

Brevo confirmed that attackers stole a Cloudflare API key and used it to inject malicious ClickFix scripts into its websites and JavaScript files embedded on customer sites to distribute malware. [...]

`javascript` `cloudflare`

### 46. [@cyclonedx/cyclonedx-npm: Shell Injection via Unsanitized --workspace Argument on Windows](https://github.com/advisories/GHSA-q69g-4hcv-6jg4)
_GHSA — npm · Sep 17 · score 0.126 · **HIGH** · CVE-2026-71538_

Affected: @cyclonedx/cyclonedx-npm. ## Summary A **Windows-specific** command injection vulnerability exists in `@cyclonedx/cyclonedx-npm` when the CLI is invoked with the `--workspace <value>` option. User-supplied `--workspace` values can be passed to a shell command without proper neutralization …

`npm` `windows`

### 47. [BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS](https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html)
_The Hacker News · Sep 17 · score 0.094 · **HIGH 8.0**_

The Internet Systems Consortium (ISC) has released&nbsp;BIND 9.20.29 and 9.21.26&nbsp;to fix fourteen security flaws it&nbsp;disclosed&nbsp;on 16 September in BIND 9, its open-source DNS server software. One of them affects any BIND server that answers DNS-over-HTTPS (DoH). A sender with no credenti…

`dns` `bind`

### 48. [Active Exploitation Attempts Target WSO2 API Manager JWT Bypass With Forged Admin Tokens](https://thehackernews.com/2026/09/active-exploitation-attempts-target.html)
_The Hacker News · Sep 16 · score 0.548 · **CRITICAL 9.5** · CVE-2026-5430_

A critical security flaw in WSO2 API Manager has come under active exploitation in the wild, according to findings from watchTowr. The vulnerability, tracked as CVE-2026-5430 (CVSS score: 9.8/10.0), is a case of improper verification of a cryptographic signature that could result in account takeover…

`jwt` `in the wild` `cve-` `cvss`

### 49. [@zereight/mcp-gitlab: Unauthenticated arbitrary file read via `upload_markdown` enables PAT exfiltration and full account takeover](https://github.com/advisories/GHSA-cv3r-c5h8-f4g5)
_GHSA — npm · Sep 16 · score 0.465 · **CRITICAL 9.8** · ×4 reports · CVE-2026-61559, CVE-2026-61560, CVE-2026-61568_

Affected: @zereight/mcp-gitlab. ### Summary The SSE transport mode (`SSE=true`) exposes all MCP tools without any authentication. The `upload_markdown` tool reads arbitrary files from the server's local filesystem via an unsanitized `file_path` parameter and uploads them to a GitLab project. Combine…

`gitlab` `docker` `exfiltration`

_also: [GHSA — npm](https://github.com/advisories/GHSA-2h44-8472-frjj), [GHSA — npm](https://github.com/advisories/GHSA-vmp7-252j-cwp7), [GHSA — npm](https://github.com/advisories/GHSA-5648-rgj9-v224)_

### 50. [Acronis Backup: Acronis Backup Incorrect Default Permissions Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-87886)
_CISA KEV · Sep 16 · score 0.346 · **CRITICAL 9.0** · ×2 reports · CVE-2026-87886_

Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability that could allow for privilege escalation. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security…

`privilege escalation`

_also: [The Hacker News](https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html)_

### 51. [Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html)
_The Hacker News · Sep 16 · score 0.263 · **CRITICAL 9.5** · CVE-2026-89026_

A critical security flaw in Issabel Framework, a web-based framework for the open-source unified communications PBX software, has come under active exploitation. The vulnerability in question is CVE-2026-89026 (CVSS v3.1 score: 9.8/CVSS v4.0 score: 9.3), which can allow an unauthenticated remote att…

`exploit` `cve-` `cvss`

### 52. [Attackers Exploit WooCommerce Wholesale Lead Capture Flaw to Plant PHP Web Shells](https://thehackernews.com/2026/09/attackers-exploit-woocommerce-wholesale.html)
_The Hacker News · Sep 16 · score 0.226 · **CRITICAL 9.5**_

Threat actors are exploiting a critical security flaw in WooCommerce Wholesale Lead Capture, a premium WordPress plugin that has more than 6,000 active installs. "This vulnerability can be leveraged by unauthenticated attackers to upload arbitrary files, including PHP backdoors, and achieve remote c…

`php` `exploit`

### 53. [node-opcua: TCP Socket Leak (FIN-WAIT-2) via keepalive reconnection cycle - Resource Exhaustion](https://github.com/advisories/GHSA-r2pf-9cw4-5j65)
_GHSA — npm · Sep 16 · score 0.263 · **HIGH 7.0** · CVE-2026-68904_

Affected: node-opcua-transport, node-opcua-client, node-opcua. SUMMARY ------- A combination of bugs in node-opcua causes unlimited TCP socket accumulation (FIN-WAIT-2 state) during automatic reconnection, leading to memory exhaustion and eventual container/process crash (OOM kill). The issue is tri…

`node` `container` `podman` `linux`

### 54. [@nuxtjs/mdc's URL sanitizer misses SVG xlink:href and data:text/html, allowing XSS from untrusted markdown at the default configuration](https://github.com/advisories/GHSA-mxm6-v9r6-r94c)
_GHSA — npm · Sep 16 · score 0.194 · **HIGH 8.1** · CVE-2026-63671_

Affected: @nuxtjs/mdc. ## Summary `@nuxtjs/mdc` renders untrusted markdown (including raw HTML) to a Vue component tree. Across two prior advisories it added a URL/attribute sanitizer to block dangerous links in that HTML: `validateProps` / `validateProp` and an `unsafeLinkPrefix` deny-list (`dist/r…

`xss`

### 55. [Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation](https://thehackernews.com/2026/09/google-patches-pixel-modem-flaw-amid.html)
_The Hacker News · Sep 16 · score 0.168 · **HIGH 7.5** · CVE-2026-58704_

Google has disclosed that a high-severity security flaw in its Pixel Cellular Modem has come under exploitation in the wild. The vulnerability, tracked as CVE-2026-58704 (CVSS score: 8.0), is a privilege escalation flaw. "In Cellular Modem, there is a possible permission bypass due to a logic error …

`in the wild` `privilege escalation` `cve-` `cvss`

### 56. [Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution](https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html)
_The Hacker News · Sep 15 · score 0.452 · **CRITICAL 9.5** · CVE-2026-76461_

Cisco has warned that a new critical vulnerability impacting AsyncOS Software for Cisco Secure Email Gateway has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-76461, carries a CVSS score of 9.8 out of a maximum of 10.0. It has been described as a case of insuffic…

`cisco` `in the wild` `cve-` `cvss`

### 57. [China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE](https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html)
_The Hacker News · Sep 15 · score 0.265 · **CRITICAL 9.0**_

A Chinese threat actor has been attributed to a spear-phishing campaign that exploits recently patched security flaws in Google Chrome and Microsoft Windows to deliver a malicious JavaScript backdoor called GRIMWEDGE. Volexity, which is tracking the threat cluster under the moniker UTA0560, said the…

`javascript` `windows` `chrome` `zero-day` `exploit`

### 58. [LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server](https://thehackernews.com/2026/09/litespeed-enterprise-flaw-could-let-one.html)
_The Hacker News · Sep 15 · score 0.098 · **CRITICAL 9.5**_

A critical vulnerability in LiteSpeed Web Server Enterprise could let a low-privilege website user gain root access on a shared-hosting server, cPanel warned in an&nbsp;advisory published on September 14. On such servers, many customers' sites run on a single machine, and an attacker with one of tho…

`exploit`

### 59. [Human Attacker Exploits Marimo RCE, Reaches SSH Bastion in Eight Seconds](https://thehackernews.com/2026/09/human-attacker-exploits-marimo-rce.html)
_The Hacker News · Sep 15 · score 0.093 · **CRITICAL 9.0**_

With artificial intelligence (AI) shrinking the window between vulnerability discovery and exploitation and lowering the barrier to entry for bad actors, new findings from Sysdig show that skilled human operators can move just as swiftly after gaining initial access. In one instance highlighted by t…

`ssh` `rce`

### 60. [emp3r0r has an unauthenticated HTTP Polling DoS](https://github.com/advisories/GHSA-4595-rvpx-4q34)
_GHSA — go · Sep 15 · score 0.177 · **HIGH 7.5** · CVE-2026-61554_

Affected: github.com/jm33-m0/emp3r0r/core. ### Summary The `http_poll` C2 transport accepts attacker-controlled HTTP polling sessions before CBOR `MsgAuth` authentication is completed. A remote unauthenticated attacker can create arbitrary polling sessions and send request bodies that are forwarded …

`go ` `github`

### 61. [libp2p-quic: Remote panic via certificate expiry race during QUIC handshake](https://github.com/advisories/GHSA-5hq8-qhww-jm7q)
_GHSA — rust · Sep 15 · score 0.157 · **HIGH** · CVE-2026-61544_

Affected: libp2p-quic. ### Summary `libp2p-quic` can panic on an inbound QUIC handshake if a malicious peer presents a valid, short lived libp2p TLS certificate and delays the final TLS 1.3 handshake fragment until the certificate expires. This is remotely reachable by a network peer and can crash a…

`github` `tls` `certificate`

### 62. [ZITADEL: Improper Role Revocation on Granted Projects during Multiple Role Deletions](https://github.com/advisories/GHSA-v859-c572-qh5p)
_GHSA — go · Sep 14 · score 0.265 · **HIGH 8.1** · ×2 reports · CVE-2026-56668, CVE-2026-76081_

Affected: github.com/zitadel/zitadel. ### Summary A bug in how ZITADEL updates permissions when multiple project roles are deleted at the same time can cause some user permissions to be missed. This issue specifically affects **User Grants on Granted Projects** (projects shared between different org…

`github`

_also: [GHSA — go](https://github.com/advisories/GHSA-vrh8-c9cm-wh8v)_

### 63. [ShinyHunters hacks Clop leak site, threatens to extort ransomware gang](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)
_BleepingComputer · Sep 19 · score 0.682_

The ShinyHunters extortion gang breached the Clop (aka Cl0p) ransomware operation's data leak site, defacing the Tor site and allegedly stealing server data and the private keys for its onion service. [...]

`ransomware` `data leak`

### 64. [Identity Visibility in 2026: The Foundation of Identity Security](https://thehackernews.com/2026/09/identity-visibility-in-2026-foundation.html)
_The Hacker News · Sep 19 · score 0.435_

Identity visibility is a starting point for modern identity security, because stolen and misused credentials are among the most frequently reported initial access vectors in breach research, including Verizon's annual Data Breach Investigations Report. This article explains what identity visibility …

`iam` `breach`

### 65. [BragJack attacks hijack AI browser agents through malicious extensions](https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/)
_BleepingComputer · Sep 19 · score 0.082_

BragJack, a proof-of-concept attack from Forever Security's Gal Weizman, hijacks the AI assistants in Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome using one malicious extension. The Prompt Forcing technique earned over $20,000 in bounties and two CVEs. [...]

`chrome` `edge`

### 66. [AnyCable: Telemetry Subsystem Contains Hardcoded Authentication Token and Transmits CLI Arguments Including Secrets](https://github.com/advisories/GHSA-w72w-9qmj-c9qm)
_GHSA — go · Sep 18 · score 0.643 · **MEDIUM 5.9** · ×2 reports · CVE-2026-63405, CVE-2026-63406_

Affected: github.com/anycable/anycable. ### Summary The telemetry subsystem embeds a hardcoded auth token (`"secret"`) in the public source and transmits raw CLI arguments—including `--secret`, `--jwt_secret`, and `--http_rpc_secret` values—to a third-party telemetry endpoint. ### Details In `teleme…

`github` `token`

_also: [GHSA — go](https://github.com/advisories/GHSA-5p54-whvp-x327)_

### 67. [Paymenter has a credit-refund double-spend race condition in service downgrade (doUpgrade)](https://github.com/advisories/GHSA-5gmm-hjfj-8ff7)
_GHSA — composer · Sep 18 · score 0.519 · **MEDIUM 6.5** · CVE-2026-71537_

Affected: paymenter/paymenter. ### Summary The service downgrade implementation in `app/Livewire/Services/Upgrade.php::doUpgrade()` executes a proration calculation and a subsequent user credit refund without any transactional safety or database locks. The only concurrency check relies on an unisola…

`php`

### 68. [md-editor-v3: XSS via fenced-code language rendering bypass](https://github.com/advisories/GHSA-3rm2-h79c-8qw6)
_GHSA — npm · Sep 18 · score 0.369 · **MEDIUM 6.1** · CVE-2026-84992_

Affected: md-editor-v3. ### Summary `MdPreview` interpolates a fenced-code language into HTML attributes without escaping it. A crafted info string therefore executes JavaScript even when the shipped `XSSPlugin` is enabled. ### Details `useMarkdownIt()` (`packages/MdEditor/layouts/Content/compositio…

`javascript` `xss`

### 69. [Caddy: rewrite placeholder re-expansion, unbounded body buffer DoS, and fileHidden case-sensitivity bypass](https://github.com/advisories/GHSA-j8px-rmrx-76h9)
_GHSA — go · Sep 18 · score 0.313 · **MEDIUM 6.5** · CVE-2026-77281_

Affected: github.com/caddyserver/caddy/v2. # Caddy v2.11.3 — Three vulnerabilities in handler/placeholder layer **Tested against:** `caddy:2.11.3` (official Docker image, SHA verified at runtime) **Reproduction environment:** Docker Desktop 4.73.1 / Engine 29.4.3 on Windows 10 host, isolated contain…

`github` `docker` `windows`

### 70. [Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer](https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html)
_The Hacker News · Sep 18 · score 0.308_

A financially motivated threat actor has been linked to the development and distribution of a JavaScript (JS)-based information stealer known as PhantomRaven via the npm package registry. "The developer likely wrote the malware using a large language model (LLM), an assessment made with high confide…

`npm` `javascript` `token` `stealer`

### 71. [Process Compose: Browser DNS rebinding lets websites control local process-compose MCP tools](https://github.com/advisories/GHSA-5gm3-9crp-6g3v)
_GHSA — go · Sep 18 · score 0.273 · **MEDIUM** · CVE-2026-77339_

Affected: github.com/f1bonacc1/process-compose. ## Summary A malicious website can use DNS rebinding to control a developer's local process-compose MCP SSE listener when MCP SSE is enabled. The vulnerable path accepts browser-origin requests before any Host validation, Origin validation, or caller-s…

`github` `token` `dns`

### 72. [Attacker infrastructure, but vibe-coded: tracking the evolution of credential harvesting platforms](https://securitylabs.datadoghq.com/articles/attacker-infrastructure-but-vibe-coded/)
_Datadog Security Labs · Sep 18 · score 0.268_

In this post, we examine two vibe-coded credential harvesting platforms, Loot and UltraVault, and the Amazon Bedrock abuse used to validate stolen secrets.

`credential`

### 73. [WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage](https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html)
_The Hacker News · Sep 18 · score 0.266_

Cybersecurity researchers have discovered a cluster of 13 npm packages that have been found to deliver a previously undocumented JavaScript stealer codenamed WeaselBiscuit. The new malware family, per OpenSourceMalware, exhibits functional overlaps with two malware strains associated with the Democr…

`npm` `javascript` `chrome` `stealer`

### 74. [Gyazo server flaw exploited to steal 23.6 million user records](https://www.bleepingcomputer.com/news/security/gyazo-server-flaw-exploited-to-steal-236-million-user-records/)
_BleepingComputer · Sep 18 · score 0.240_

The Gyazo image-sharing platform has confirmed it suffered a data breach after hackers exploited a server vulnerability that allowed them to steal 23.6 million user records. [...]

`breach`

### 75. [An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.](https://thehackernews.com/2026/09/an-abandoned-cdn-domain-was-re.html)
_The Hacker News · Sep 18 · score 0.150_

In July 2025, someone registered a domain that used to belong to a content delivery network.&nbsp; The CDN had been wound down years earlier, and the domain it served assets from was allowed to expire. What it had not lost were its callers. Thousands of websites, code repositories, and documentation…

`cdn`

### 76. [Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root](https://thehackernews.com/2026/09/public-exploits-released-for-four-linux.html)
_The Hacker News · Sep 18 · score 0.146_

A security researcher has released working exploit code for four Linux kernel flaws that each let a local user gain root, the highest level of access on a machine. Kernel maintainers have fixed all four over the past few weeks, so a system running an up-to-date kernel is not affected. But the exploi…

`linux` `kernel` `exploit`

### 77. [Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer](https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/)
_BleepingComputer · Sep 18 · score 0.104_

An ongoing malware campaign uses SEO-optimized GitHub repositories to impersonate well-known software firms to push a previously undocumented information stealer called Rapuncel. [...]

`github` `lastpass` `stealer`

### 78. [Stage-only npm tokens for safer automation](https://github.blog/changelog/2026-09-18-stage-only-npm-tokens-for-safer-automation)
_GitHub Changelog · Sep 18 · score 0.087_

You can now select Read and write (stage only) when creating an npm granular access token. This lets your automated workflows stage package versions for review without giving the token&#8230; The post Stage-only npm tokens for safer automation appeared first on The GitHub Blog .

`npm` `github` `token`

### 79. [Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)
_The Hacker News · Sep 18 · score 0.068_

A flaw in four widely used AI coding agents lets someone who controls a plugin's code repository swap the plugin an agent installs for a malicious one, even when the agent locked that plugin to a specific reviewed version, security firm&nbsp;Air Security said on Thursday. The firm said Anthropic has…

`github`

### 80. [Copilot code review: An improved review experience](https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience)
_GitHub Changelog · Sep 18 · score 0.054_

Copilot code review now gives you a clearer view of how a review changes over time, more intelligently auto-resolves its own suggestions, and generates useful commit messages when you accept&#8230; The post Copilot code review: An improved review experience appeared first on The GitHub Blog .

`github`
