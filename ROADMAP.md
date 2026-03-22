# Code Challenge Roadmap

## Phase 1: Core Engine (Months 1-3)
- [RC] Sandboxed execution engine — gVisor containers, resource limits (256MB, 5s)
- [RC] Monaco editor frontend — syntax highlighting, autocomplete, themes
- [RC] Python + JavaScript runtime support
- [RC] Problem format spec — JSON schema for problems, tests, solutions
- [RC] 100 curated problems (Easy: 40, Medium: 40, Hard: 20)
- [RC] Basic test runner — visible + hidden test cases
- [RC] User auth — GitHub OAuth + email/password
- [RC] PostgreSQL schema — users, submissions, problem stats
- **Milestone**: Alpha launch with 100 problems, 2 languages

## Phase 2: AI + Competition (Months 4-6)
- [RC] Rust + Go runtime support
- [RC] AI problem generator — local inference, skill-calibrated
- [RC] Glicko-2 rating system
- [RC] Global leaderboard with weekly/monthly/all-time views
- [RC] Weekly contest system — 90-minute timed events
- [RC] Skill profiling — mastery map across 40+ categories
- [RC] Progressive hint system
- [RC] Solution analysis — complexity detection, optimal comparison
- [RC] 300 more curated problems (total: 400)
- **Milestone**: Public beta, weekly contests, AI adaptation

## Phase 3: Teams + Education (Months 7-9)
- [RC] Team creation + private leaderboards
- [RC] Team analytics dashboard
- [RC] LTI 1.3 integration for LMS
- [RC] Custom problem set builder
- [RC] SSO (SAML/OIDC) for institutions
- [RC] Video explanations (Manim-generated)
- [RC] Community discussion system
- [RC] 100 more curated problems (total: 500)
- [RC] Java + C++ language support
- **Milestone**: Teams tier launch, 3 institutional pilots

## Phase 4: Scale (Months 10-12)
- [RC] TypeScript + C# language support
- [RC] Mobile-optimized experience
- [RC] Pair programming mode
- [RC] Interview prep tracks
- [RC] Exportable skill profiles
- [RC] Daily challenge system
- [RC] Achievement badges + gamification
- [RC] API for third-party embedding
- **Milestone**: 10K active users, 8 languages

## Phase 5: Growth (Year 2)
- [RC] Problem marketplace — community-created challenges
- [RC] Corporate hiring integration — skill-verified profiles
- [RC] Bootcamp partnership program
- [RC] Advanced AI — multi-step problem chains, project-based challenges
- [RC] Real-time multiplayer contests (head-to-head)
- [RC] Offline mode for workshops/events
- **Milestone**: 50K users, revenue-positive

## Revenue Targets
| Quarter | Free Users | Pro MRR | Teams MRR | Total ARR |
|---------|-----------|---------|-----------|-----------|
| Q1 Y1   | 500       | $2K     | —         | $24K      |
| Q2 Y1   | 2,000     | $15K    | $5K       | $240K     |
| Q3 Y1   | 5,000     | $40K    | $20K      | $720K     |
| Q4 Y1   | 10,000    | $75K    | $50K      | $1.5M     |
| Q4 Y2   | 50,000    | $200K   | $150K     | $4.2M     |
