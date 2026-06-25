# Project Review Notes

Repository: `ecs-fargate-terraform-github-actions`

## What I cleaned or improved

- Rebuilt the main README with a career-progression story.
- Added your requested animated footer/contact section.
- Checked the uploaded source for screenshots. No existing screenshots/images were found for this project.
- Added `docs/screenshots/README.md` with safe screenshot names to add after running the project.
- Updated the Terraform code so the project actually uses ECS Fargate instead of EC2 launch type.
- Added ALB, target group, ECS task execution role, CloudWatch log group, ECR repository, ECS cluster, task definition, and ECS service.
- Removed the hard-coded Terraform backend bucket from the source to avoid deployment errors in another AWS account.
- Updated GitHub Actions workflows to use the `main` branch and commit SHA based Docker image tags.
- Kept `.env`, secrets, Terraform state, kubeconfigs, and token files blocked in `.gitignore`.
- Added cleanup/cost-control commands in README.

## Review before making public

- Run local Docker build before pushing.
- Run `terraform -chdir=terraform fmt` before committing.
- Add your own screenshots after running the project.
- Replace placeholder GitHub repository secrets with your own AWS lab values.
- Do not commit real cloud credentials, tokens, kubeconfigs, private keys, `.env`, or Terraform state.
