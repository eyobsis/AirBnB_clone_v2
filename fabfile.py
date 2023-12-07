from fabric import task

@task
def do_deploy(c, archive_path):
    # Your deployment logic here
    print(f"Deploying {archive_path}...")
    # Example: Run a command
    c.run(f"ls -l {archive_path}")

