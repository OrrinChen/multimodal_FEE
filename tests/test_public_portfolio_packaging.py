from pathlib import Path


PUBLIC_TEXT_PATHS = (
    Path("README.md"),
    Path("ROADMAP.md"),
    Path("TASK_MEMORY.md"),
    Path("docs/interview_story.md"),
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
