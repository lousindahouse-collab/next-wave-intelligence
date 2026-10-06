# Reddit Data Use — Next Wave Prototype

Next Wave is a locally hosted research prototype that uses approved, read-only Reddit API access to identify aggregate patterns in public discussions, such as recurring product problems, unmet needs, user frustrations, requests for alternatives, and commercial-intent signals.

## Intended Reddit access

- Public posts and comments only.
- Read-only access.
- No posting, voting, messaging, moderation actions, or account interaction.
- No private messages or private communities.

## Data minimisation

The Reddit collector is designed to derive aggregate metrics rather than build a corpus of Reddit content. The application does not intentionally retain Reddit usernames, full post bodies, or full comment bodies in its long-term analytics tables. Derived outputs include topic/problem frequency, pain score, commercial-intent score, subreddit breadth, engagement aggregates, and historical trend snapshots.

Limited source references may be retained for verification and debugging, subject to configured retention controls.

## User profiling

Next Wave is not intended to create individual user profiles, infer sensitive personal attributes, identify users across services, or make decisions about individual Redditors.

## AI/model use

Reddit content is not intended to be used to train a general-purpose AI model. The collector performs deterministic and aggregate classification/scoring for the Next Wave opportunity-intelligence prototype.

## Status

This repository is a development-stage local prototype. Reddit collection remains disabled by default and must only be enabled with approved Reddit API credentials and in accordance with Reddit's applicable developer terms and policies.
