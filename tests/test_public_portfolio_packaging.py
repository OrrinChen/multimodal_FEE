from pathlib import Path


PUBLIC_TEXT_PATHS = (
    Path("PORTFOLIO.md"),
    Path("README.md"),
    Path("ROADMAP.md"),
    Path("TASK_MEMORY.md"),
    Path("docs/interview_story.md"),
    Path("docs/sixty_second_pitch.md"),
    Path("docs/resume_bullets.md"),
    Path("docs/system_design_notes.md"),
    Path("docs/failure_modes.md"),
    Path("docs/demo_script.md"),
    Path("reports/final_report.md"),
    Path("reports/resume_bullet.txt"),
)


def test_public_packaging_has_no_local_or_self_rating_leaks():
    combined = "\n".join(path.read_text(encoding="utf-8") for path in PUBLIC_TEXT_PATHS)

    forbidden_fragments = (
        "ashare-radar",
        "/Users/orynwilder",
        "New project 2",
        "S-level",
        "business-shock",
        "Business-shock",
    )
    for fragment in forbidden_fragments:
        assert fragment not in combined


def test_public_packaging_has_no_stale_unchecked_mvp_items():
    task_memory = Path("TASK_MEMORY.md").read_text(encoding="utf-8")

    stale_items = (
        "[ ] Implement FMP client module",
        "[ ] Store investor deck metadata",
        "[ ] Add deck PDF parsing",
        "[ ] Add chart extraction only after table/text pipeline works",
    )
    for item in stale_items:
        assert item not in task_memory

    assert "Original MVP checklist" in task_memory
    assert "Known out-of-scope items" in task_memory


def test_resume_bullets_avoid_overclaiming_optional_backends():
    generated_bullet = Path("reports/resume_bullet.txt").read_text(encoding="utf-8")
    doc_bullets = Path("docs/resume_bullets.md").read_text(encoding="utf-8")
    combined = generated_bullet + "\n" + doc_bullets

    assert "dense-proxy" in combined
    assert "validator-augmented retrieval" in combined
    assert "GraphRAG" not in generated_bullet
    assert "SEC/FMP data" not in generated_bullet
    assert "general chart" not in combined.lower()
    assert "trained neural" not in combined.lower()


def test_readme_has_portfolio_screenshots_and_pitch():
    readme = Path("README.md").read_text(encoding="utf-8")
    first_screen = readme[:2500]

    assert "PORTFOLIO.md" in first_screen
    assert "make portfolio-demo" in first_screen
    assert "docs/assets/killer_metrics.png" in first_screen
    assert "Full engine accuracy" in first_screen
    assert "docs/sixty_second_pitch.md" in readme

    asset_paths = (
        Path("docs/assets/claim_verification_demo.png"),
        Path("docs/assets/case_study_replay.png"),
        Path("docs/assets/memo_trace_demo.png"),
        Path("docs/assets/killer_metrics.png"),
    )
    for path in asset_paths:
        assert str(path) in readme
        assert path.exists(), path
        assert path.stat().st_size > 10_000


def test_portfolio_md_is_recruiter_entrypoint():
    portfolio = Path("PORTFOLIO.md").read_text(encoding="utf-8")

    assert "Claim-level financial evidence verification" in portfolio
    assert "docs/assets/claim_verification_demo.png" in portfolio
    assert "docs/assets/case_study_replay.png" in portfolio
    assert "docs/assets/memo_trace_demo.png" in portfolio
    assert "docs/assets/killer_metrics.png" in portfolio
    assert "30-minute reproduction" in portfolio
    assert "portfolio-v1" in portfolio
    assert "Ordinary RAG" in portfolio
    assert "claim decomposition" in portfolio
    assert "evidence graph" in portfolio
    assert "numeric reconciliation" in portfolio
    assert "validator gate" in portfolio
    assert "AI infra" in portfolio
    assert "Financial AI" in portfolio
    assert "RAG/eval" in portfolio


def test_makefile_exposes_short_portfolio_demo():
    makefile = Path("Makefile").read_text(encoding="utf-8")

    assert "portfolio-demo:" in makefile
    assert "python3 scripts/build_portfolio_screenshots.py" in makefile
    assert "python3 scripts/smoke_cli_workflow.py" in makefile
    assert "python3 scripts/smoke_interview_packaging.py" in makefile
    assert "screenshots=3" in makefile
    assert "commands=6" in makefile
    assert "verify_verdict=support" in makefile
    assert "docs=6" in makefile
    assert "api_key_required=False" in makefile
