.PHONY: portfolio-demo

portfolio-demo:
	@python3 scripts/build_portfolio_screenshots.py
	@python3 scripts/smoke_cli_workflow.py
	@python3 scripts/smoke_interview_packaging.py
	@printf '%s\n' 'expected: screenshots=3 commands=6 verify_verdict=support docs=6 api_key_required=False'
