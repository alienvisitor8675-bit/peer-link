# Launch review — October 2, 2026

**Production is on hold.** Peer Link is the working name. Peer Adapters is the
recommended public name because [Peer Link already identifies a P2P crypto
product](https://github.com/peer-link/peer-link). No three-user testing gate applies.

## Gap assessment and completed work

| Area | Finding and implementation | Remaining release gate |
| --- | --- | --- |
| Repository | Canonical workspace migration preserved Git history, uncommitted work and linked worktrees. Rebrand and contract v2 are prepared in a separate launch branch. | GitHub transfer to `zkp2p/peer-link` is verified by stable repository ID. Publish the reviewed branch and enforce protections. |
| Private adoption | Original public candidate mapping makes precision, identity provenance and unauthenticated source status explicit. Private Peer code and signing fields stay private. | Each bank still needs its own private-service review and production approval. |
| Verifier | The previous components were not a deployable end-to-end manual service. Runtime execution, owner client, exact-version receipts, minimization and controller admission are now connected. | Independent rebuild and hardware validation of the final release candidate; approved source policy, signing identity and owner-consented live test. |
| Deployment | Dedicated VPC, least-privilege roles, immutable worker launch settings, durable budget/lease and external cleanup were exercised on AWS. | Enforce GitHub branch/environment protection, publish a pinned controller version and configure an invoke-only OIDC role. These are not established by YAML alone. |
| Incentives | A 500 USDC sponsor deposit is confirmed. Proposed awards total $175, each bank capped at $50. | Verify project allocation and payout eligibility before announcing funded assignments or replacing old terms. |
| Docs and copy | One docs page is in [draft PR #2037](https://github.com/zkp2p/zkp2p-clients/pull/2037); Shoku provided review-only copy/video. | Final links/name/terms, checks on the final commit and explicit production approval. |
| Landing hosting | The current landing project is linked to Sachin's personal Vercel scope. The local rebrand preview builds and renders. | Verify hosting access and the current production rollback deployment before a Peer-hosted promotion; no hosting transfer or production deploy has occurred. |

## Concrete security findings

- **A 100× amount mismatch was corrected before release.** Native minor units
  cannot be copied directly into Peer's current two-decimal settlement input.
  The original bridge would have passed 25,000 VND as 25,000 settlement units.
  It now produces 2,500,000, retains source precision and rejects rounding or
  integer overflow. This change is original contract mapping; no private parser
  implementation or fixture was copied.

- **Live bank access is not approved.** The checked-in source policy and release
  remain disabled. The synthetic test's disposable signer and approved fixture
  policy are not production credentials or bank evidence. Being logged in to a
  bank is not client consent.
- **GitHub privilege protection is an external dependency.** The manual workflow
  contains no checkout or bank secrets. Contributor code cannot supply deployment
  inputs. It must remain disabled until actual repository/environment controls
  and the exact AWS OIDC policy are verified after transfer.
- **Private evidence needed tighter handling.** The trusted reader now validates
  duplicate selection before minimizing the selected record. The guest receives
  necessary payment identifiers, not credentials, names, balances, memos or other
  transactions. Guest strings never appear in the public receipt. Required
  identifiers are still sensitive while inside the enclave.
- **Company Mercury data warrants a narrower read surface.** The existing web
  history operation can retrieve up to 100 records inside the enclave. The client
  now discloses that scope. Mercury documents a [read-only token tier](https://docs.mercury.com/docs/getting-started)
  and [single-transaction endpoint](https://docs.mercury.com/reference/gettransaction).
  Review that surface's field semantics and a separately scoped API adapter before
  preferring it over a company browser session. No company session was accessed
  during these tests; do not infer API/web schema equivalence.
- **Same-account separation has limits.** The dedicated VPC has no peering or
  inbound rules. Worker roles cannot read production secrets, use KMS or assume
  roles; the manual worker could read only its pinned synthetic bundle version.
  Account administrators, AWS control plane, quotas and billing remain shared.
- **Resource guards are bounded controls, not a billing guarantee.** Atomic
  admission reserved $2 per worker against a $50 infrastructure limit, including
  previous reservations; concurrency is one. Host shutdown and an independent
  expiry Lambda limit lifetime. Billing lag, service failure or administrator
  overrides remain risks. Actual billing has not yet been reconciled.
- **Monitoring is not unattended yet.** Cleanup results and CloudTrail were
  inspected directly, and expiry errors have a CloudWatch alarm. An end-to-end
  notification route still needs a real delivery test before unattended use.
- **The trusted computing base remains substantial.** AWS attestation, the
  owner client, release approver, Python, Wasmtime and the enclave kernel are
  trusted. Memory is not guaranteed zeroized; timing/outcome channels and software
  vulnerabilities remain. A report does not establish recipient credit or final
  settlement, and never authorizes payout or a production attestation.

See the [architecture diagram and attack paths](architecture.md).

## Validation evidence

The current local candidate passes `npm run check`: 77 TypeScript tests, 165
Python tests, types, lint, coverage, fixture/report validation, privacy scanning
and the landing build. The later operator CLI and settlement mapping changes
have local coverage; the hardware record below names the earlier source it
actually tested. It is not hardware evidence for the final candidate.

The [synthetic hardware record](../verification/infra/evidence/2026-10-02-synthetic-e2e.json)
identifies the source commit, Wasm hash, EIF hash, measured PCRs and receipt digest.
It records real AWS attestation, client encryption, enclave-terminated HTTPS,
compiled guest execution, independent oracle comparison and receipt verification.
Wrong nonce/policy/measurement, replay and an invalid source credential were
rejected. AWS tests rejected unapproved/overridden requests, a concurrent worker,
consumed approvals and paused admission. Both test workers terminated, both
encrypted disks were deleted, and the active lease was cleared. The test fixture
and worker artifacts are disposable; no production release is implied.

## Release and rollback proposal

The reviewed docs preview currently corresponds to commit
`2a02990968ac0d933f48d42106db75dfab6713a4`, deployment
`dpl_BVMWUrgbDcJgeRYS9FtbU9x8yaQa`; [CI run 9525](https://github.com/zkp2p/zkp2p-clients/actions/runs/36987404971)
and all four Vercel preview builds passed. The [docs preview](https://docs-igi4o7mp0-zkp2p.vercel.app/developer/peer-link)
was checked in the browser, including the source-to-settlement unit example. The previous
docs production coordinate is commit `39918abc349f0e0e9142230738c7f8850c964d41`,
deployment `dpl_BzUq3XgEVqWyFS5AGh1nedpJSue7`. Re-read these immediately before
approval/promotion because other releases can advance them. No production
verifier exists to roll back to; disabling admission is its safe baseline.

1. The repository transfer to `zkp2p/peer-link` is complete. Publish the reviewed launch branch. Verify
   required CI, CODEOWNERS enforcement, main protection and protected manual
   environment settings. Keep ordinary PR CI free of AWS/signing/bank credentials.
2. Confirm the Merit project allocation, recheck claims, publish exact bank scopes
   and smaller amounts, then reply to Vietcombank and Monobank. Preserve earned
   obligations. Funding receipts do not themselves activate an award.
3. Freeze the verifier candidate; obtain independent matching builds, isolated
   signer/operator authority and an approved bank source policy. Repeat hardware
   negative tests and complete one owner's explicit local-client consent test.
   No bank session belongs in a chat, workflow, issue or AI prompt.
4. Present the exact commits, image/adapter digests, protection evidence, live-test
   result, cost ledger and previous deployment identifiers for Sachin's production
   approval. Do not enable public bank sessions with the synthetic manifest.
5. After approval, merge through main and fast-forward `releases/docs/prod` only
   when it has no unique commits. Verify the resulting Vercel SHA at docs.peer.xyz.
   Deploy the landing page explicitly, and enable only the approved manual
   verifier release. Social copy/video remain review-only until approved.

Rollback starts by disabling dispatch and pausing admission, then revoking the
release manifest and terminating exact owned workers. Verify termination, disk
deletion and lease clearance before removing infrastructure. Retain cost/audit
records and never refund uncertain reservations automatically. Restore docs or
landing content with a reviewed revert through normal release history; do not
force a production branch or reactivate an old signing authority.
